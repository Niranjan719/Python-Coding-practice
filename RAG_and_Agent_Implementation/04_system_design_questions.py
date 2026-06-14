"""
SYSTEM DESIGN INTERVIEW QUESTIONS FOR RAG & AGENTS
Common questions asked in senior/architect-level interviews

Focus: Scalability, reliability, cost, and production deployment
"""

SYSTEM_DESIGN_SCENARIOS = [
    {
        "id": "RAG-001",
        "title": "Design a Real-time Document QA System",
        "difficulty": "⭐⭐⭐ Hard",
        "description": """
Design a system where users can upload documents and ask questions about them in real-time.

Constraints:
- Document size: 1MB to 1GB
- Concurrent users: 100-10,000
- Query response time: < 5 seconds
- Document indexing time: < 2 minutes for 1GB
- 99.5% uptime

Key Questions to Address:
1. How do you handle large documents?
2. What's your embedding strategy?
3. How do you manage concurrent uploads?
4. What about document updates?
5. How do you ensure security/privacy?
6. What's your cost model?
""",
        "solution": """
Architecture:

```
┌─────────────┐
│   Users     │
└──────┬──────┘
       │
┌──────▼──────────────────┐
│   API Gateway (REST)     │
│   - Auth                 │
│   - Rate limiting        │
│   - Request validation   │
└──────┬──────────────────┘
       │
   ┌───┴───┐
   │       │
┌──▼─┐  ┌──▼──────────────┐
│ │  │  │ Document Upload  │
│Cache ││ - File parsing   │
│ │  │  │ - Chunking       │
└──┬─┘  │ - Virus scan     │
   │    └────┬─────────────┘
   │         │
┌──▼─────────▼──────────────┐
│ Document Processing Queue   │
│ (Kafka/RabbitMQ)           │
│ - Embedding generation      │
│ - Indexing                  │
│ - Metadata extraction       │
└────────────┬────────────────┘
             │
      ┌──────┴──────┐
      │             │
 ┌────▼────┐  ┌────▼──────────────┐
 │ Vector   │  │ Full-text Index   │
 │ Database │  │ (Elasticsearch)   │
 │(Pinecone)│  └────┬──────────────┘
 └────┬─────┘       │
      │       ┌─────▼─────┐
      │       │ Query      │
      │       │ Processor  │
      │       │ - Rewrite  │
      │       │ - Expand   │
      │       └─────┬──────┘
      │             │
 ┌────┴─────────────┴─────┐
 │ Retrieval Service       │
 │ - Hybrid search         │
 │ - Reranking             │
 │ - Deduplication         │
 └────┬────────────────────┘
      │
 ┌────▼──────────────┐
 │ LLM Service        │
 │ - Prompt building  │
 │ - LLM call         │
 │ - Streaming        │
 └────┬───────────────┘
      │
 ┌────▼──────────────┐
 │ Response          │
 │ Formatter         │
 └────┬───────────────┘
      │
 ┌────▼──────────────┐
 │ User              │
 └───────────────────┘
```

Detailed Design:

1. Upload Phase (2 minutes max):
   ```
   User uploads 1GB PDF
   -> File stored in S3 with signed URL
   -> Metadata: user_id, doc_id, timestamp
   -> Job created in queue
   -> Return job_id to user
   
   Background processing:
   -> Download from S3
   -> Parse PDF (PyPDF2, pypdfium2)
   -> Split into 512-char chunks with 50-char overlap
   -> Generate embeddings (batch of 128)
   -> Store in vector DB
   -> Store metadata in PostgreSQL
   -> Mark complete
   ```

2. Query Phase (< 5 seconds):
   ```
   User: "What is in chapter 3?"
   
   a) Check cache (hash of query + doc_id)
   b) If cache miss:
      - Expand query (synonym replacement)
      - Generate embedding
      - Vector search (top 20)
      - BM25 search (top 20)
      - Rerank with cross-encoder (top 5)
      - Build context (max 4000 tokens)
      - Generate prompt
      - Stream response from LLM
   c) Cache response
   d) Return to user
   ```

3. Scalability Strategies:

   For 10K concurrent users:
   - Load balancer (round-robin, health-check)
   - Multiple API instances (auto-scaling)
   - Vector DB cluster (replicas)
   - Embedding service pool (batch processing)
   - Redis cluster for caching
   - Elasticsearch sharding

4. Cost Optimization:
   - Cache embeddings ($0 after first)
   - Use GPT-3.5-turbo for simple Q&A
   - Implement streaming (don't wait for full response)
   - Batch embedding generation
   - Pre-compute common queries

5. Reliability:
   - Retry with exponential backoff
   - Circuit breaker for LLM API
   - Fallback to cached responses
   - Document backups in S3
   - Monitoring and alerting

6. Security:
   - User can only access their documents
   - Encryption in transit and at rest
   - Document scanning for malware
   - Audit logging
   - Rate limiting

7. Monitoring:
   - Query latency: p50, p95, p99
   - Cache hit rate
   - Vector DB response time
   - LLM API usage and cost
   - Error rates per component
   - Storage usage

Cost Estimate (1000 users, 1M docs):
- Vector DB: Pinecone $0.10/1M vectors = ~$100/month
- LLM: $0.015 per 1K output tokens = ~$5K/month
- S3: $1/month per TB = $100/month
- Infrastructure: $5K/month
- Total: ~$10K/month
        """,
    },
    {
        "id": "RAG-002",
        "title": "Design a Knowledge Base Search System",
        "difficulty": "⭐⭐⭐ Hard",
        "description": """
Design a system where companies can build private knowledge bases and search them.

Requirements:
- 10K+ companies
- Each company: 100K-10M documents
- Query response: < 2 seconds
- Multi-language support
- Document versioning
- Search quality: High recall

Unique Challenges:
1. Multi-tenancy with strict data isolation
2. Handling diverse document types
3. Versioning and updates
4. Cost efficiency at scale
5. Personalization
""",
        "solution": """
Multi-Tenant Architecture:

```
┌─────────────────────────────────┐
│     Search API                  │
│ - Authentication                │
│ - Request routing               │
└──────────┬──────────────────────┘
           │
      ┌────┴────┐
      │          │
 ┌────▼────┐ ┌──▼─────────────┐
 │ Tenant   │ │ Document       │
 │Registry  │ │ Ingestion      │
 │ (Cache)  │ │ Pipeline       │
 └────┬─────┘ └──┬─────────────┘
      │          │
      │      ┌───▼────────────┐
      │      │ Job Queue      │
      │      │ (per tenant)   │
      │      └───┬────────────┘
      │          │
 ┌────▼──────────▼──────────┐
 │ Shared Infrastructure     │
 │ - Vector DB (multi-index) │
 │ - FTS (multi-index)       │
 │ - PostgreSQL (metadata)   │
 │ - Redis (cache)           │
 └────┬─────────────────────┘
      │
 ┌────▼──────────────────────┐
 │ Query Engine               │
 │ - Routing to tenant index  │
 │ - Hybrid search            │
 │ - Personalization          │
 └────┬──────────────────────┘
      │
 ┌────▼──────────────┐
 │ Response          │
 └───────────────────┘
```

Key Design Decisions:

1. Isolation Strategy:
   - Physical: Separate vector DB per tenant (expensive)
   - Logical: Shared vector DB with tenant prefix (cost-effective)
   - Hybrid: Shared for small tenants, physical for large
   
   Recommendation: Logical isolation with partition keys

2. Indexing:
   - Separate Elasticsearch index per tenant
   - Shared vector DB with namespacing
   - Metadata index for filtering

3. Query Processing:
   ```
   1. Tenant ID from JWT token
   2. Query expansion (synonyms, stemming)
   3. Multi-language support:
      - Language detection
      - Translate to English
      - Search in original + English
   4. Hybrid search:
      - Vector search on tenant namespace
      - BM25 search on tenant index
      - Combine results
   5. Personalization:
      - Weight documents by user interaction
      - Boost recent documents
      - Prefer high-rated documents
   6. Reranking:
      - Cross-encoder model
      - Diversify results
      - Re-order by relevance
   ```

4. Versioning:
   ```
   Documents can have versions:
   - v1: Original upload
   - v2: Update
   - v3: Another update
   
   Storage:
   - Keep all versions
   - Search latest by default
   - Allow filtering by version
   - Show version history
   ```

5. Cost Model:
   ```
   Tiered pricing:
   - Starter: 10K docs, 1K queries/month = $50
   - Pro: 100K docs, 100K queries/month = $500
   - Enterprise: Unlimited = Custom
   
   Cost per company = base + (queries * $0.01) + (docs * $0.001)
   ```

Challenges & Solutions:

1. Data Isolation:
   - Use tenant_id in all queries
   - Enforce at DB layer
   - Regular audit checks

2. Load Balancing:
   - Hash by tenant_id for affinity
   - Separate queues for large tenants
   - Priority queuing

3. Updates:
   - Queue update jobs
   - Atomic version updates
   - Rollback capability

4. Monitoring:
   - Per-tenant metrics
   - Cost tracking per tenant
   - Query quality feedback
        """,
    },
    {
        "id": "AGENT-001",
        "title": "Design an Enterprise Task Automation System",
        "difficulty": "⭐⭐⭐ Hard",
        "description": """
Design a system for automating complex business processes using agents.

Requirements:
- Support 100+ different workflows
- Handle long-running tasks (hours)
- Handle failures and retries
- Multi-step approval workflows
- Integration with 50+ external systems
- Audit trail for compliance

Example Workflows:
- Bug triaging (GitHub -> Jira -> Slack)
- Contract review (Doc -> Analysis -> Email)
- Financial reporting (Data -> Analysis -> Report)
""",
        "solution": """
Enterprise Automation Architecture:

```
┌──────────────────────┐
│ Workflow Definition  │
│ (DSL/UI)             │
└──────┬───────────────┘
       │
┌──────▼────────────────────┐
│ Workflow Orchestrator      │
│ - Parse workflow          │
│ - Validate dependencies   │
│ - Create execution plan   │
└──────┬────────────────────┘
       │
┌──────▼───────────────────┐
│ Execution Engine          │
│ - State management        │
│ - Error handling          │
│ - Retry logic             │
└──────┬──────────────────┘
       │
   ┌───┴──────┬──────────┬──────────┐
   │          │          │          │
┌──▼──┐  ┌───▼───┐  ┌──▼──┐  ┌───▼────┐
│Agent│  │Tool   │  │Human│  │External│
│Pool │  │Engine │  │Appr │  │Systems │
│     │  │       │  │oval │  │        │
└──┬──┘  └───┬───┘  └──┬──┘  └───┬────┘
   │         │        │         │
┌──▼─────────▼────────▼─────────▼──┐
│ Shared Services                   │
│ - Logging                         │
│ - Monitoring                      │
│ - Notifications                   │
│ - API integrations                │
└───────────────────────────────────┘
```

Workflow Definition Example:

```yaml
name: Bug Triage
trigger: github.issue.opened
steps:
  - name: parse_issue
    agent: parsing
    input: github_issue
    
  - name: analyze_severity
    agent: classification
    input: parsed_issue
    
  - name: route_to_team
    agent: routing
    input: severity
    decision:
      high: assign_p1_team
      medium: assign_p2_team
      low: assign_backlog
  
  - name: create_jira
    tool: jira.create_issue
    input: analyzed_issue
    
  - name: notify_team
    tool: slack.send_message
    input: team, jira_id
    
  - name: update_github
    tool: github.add_comment
    input: issue, status
```

Key Design Decisions:

1. State Management:
   ```
   Workflow State:
   - workflow_id
   - status: pending/running/completed/failed
   - steps: [{id, status, input, output, error}]
   - execution_time
   - context: shared data
   
   Stored in PostgreSQL with versioning
   ```

2. Agent Orchestration:
   ```
   - Agent pool (10-100 instances)
   - Work queue (RabbitMQ)
   - Lease-based (60 sec timeout)
   - Automatic reassignment on failure
   ```

3. Error Handling:
   ```
   For each step:
   - Retry with exponential backoff (max 3)
   - On final failure: alert or skip
   - Allow manual intervention
   - Detailed error logging
   ```

4. Integrations:
   ```
   - API adapter pattern
   - OAuth/API key management
   - Rate limiting per service
   - Circuit breaker pattern
   - Webhook handlers
   ```

5. Human Approval:
   ```
   - Pause at approval nodes
   - Send notifications
   - Set timeout (default 24h)
   - Allow rejection with reason
   ```

Cost & Performance:

- Processing time: 100ms per step
- For 5-step workflow: ~500ms
- Concurrent workflows: 1000+
- Cost: ~$0.01 per workflow execution

Monitoring:

- Success rate per workflow
- Average execution time
- Cost per workflow
- Most common failures
- Performance bottlenecks
        """,
    },
    {
        "id": "AGENT-002",
        "title": "Design a Personal AI Assistant (Like ChatGPT with Memory)",
        "difficulty": "⭐⭐⭐ Hard",
        "description": """
Design a conversational AI assistant with:
- Persistent memory of users
- Multi-turn conversations
- Tool usage
- Personalization
- Privacy

Challenges:
- 100M+ users
- Billions of conversations
- Long-term memory management
- Privacy and data retention
- Cost optimization
""",
        "solution": """
Personal AI Assistant Architecture:

```
┌──────────────┐
│ User Input   │
└──────┬───────┘
       │
┌──────▼──────────────────┐
│ Conversation Router      │
│ - User auth              │
│ - Session routing        │
└──────┬──────────────────┘
       │
┌──────▼──────────────────┐
│ Memory Retrieval Service │
│ - Short-term: Last 10   │
│ - Long-term: Semantic   │
│ - Preferences: User     │
└──────┬──────────────────┘
       │
┌──────▼──────────────┐
│ Context Builder      │
│ - Format message     │
│ - Add memory         │
│ - Inject tools       │
└──────┬───────────────┘
       │
┌──────▼──────────────┐
│ LLM Service          │
│ - Generate response  │
│ - Decide on tool use │
└──────┬───────────────┘
       │
    ┌──┴──┐
    │     │
┌───▼─┐ ┌─▼──────────────┐
│Tool │ │Save Memory      │
│Exec │ │- Conversation  │
│     │ │- Preferences   │
└───┬─┘ │- Facts about   │
    │   │  user          │
    │   └────┬───────────┘
    │        │
    └────┬───┘
         │
    ┌────▼──────────┐
    │ Response      │
    └───────────────┘
```

Memory System:

```python
class UserMemory:
    def __init__(self, user_id):
        self.user_id = user_id
    
    # Short-term: Last conversation
    short_term = ConversationBuffer(max_tokens=2000)
    
    # Medium-term: Summaries (1 week)
    medium_term = ConversationSummaryMemory(ttl=7*24*3600)
    
    # Long-term: Semantic search (1 year)
    long_term = VectorStoreRetrieverMemory(
        vector_store=chroma,
        retention=365*24*3600
    )
    
    # Preferences: User settings
    preferences = {
        'tone': 'formal',
        'language': 'en',
        'timezone': 'UTC',
        'interests': ['AI', 'Science']
    }
    
    # Facts: About the user
    facts = {
        'name': 'Alice',
        'job': 'Software Engineer',
        'company': 'Google'
    }
```

Privacy & Retention:

```
- User can delete any message (right to be forgotten)
- Memory retention: 1 year default (configurable)
- Encryption at rest
- No sharing with third parties
- GDPR compliant
- Audit logging
```

Cost Model:

- Per conversation tokens: ~0.001
- Memory storage: ~100B per user/year
- Infrastructure: $2/month per active user

Personalization:

1. Tone & Style:
   - Formal vs casual
   - Technical vs simple
   - Verbose vs concise

2. Knowledge:
   - Remember conversations
   - Extract facts about user
   - Suggest relevant topics

3. Tools:
   - Remember preferences
   - Calendar integration
   - Email summaries

Scaling:

- Millions of concurrent conversations
- Distributed conversation storage (Cassandra)
- Semantic search with FAISS
- Redis for session cache
        """,
    },
]

FOLLOW_UP_QUESTIONS = [
    "How would you handle system failures mid-execution?",
    "What metrics would you monitor?",
    "How would you optimize costs?",
    "How would you ensure data security?",
    "How would you test this system?",
    "What trade-offs did you make and why?",
    "How would you scale to 10x load?",
    "How would you handle latency requirements?",
    "What are the failure modes?",
    "How would you handle concurrent requests?",
]

# ============================================================================
# INTERVIEW TIPS FOR SYSTEM DESIGN
# ============================================================================

INTERVIEW_TIPS = """
System Design Interview Framework:

1. CLARIFY REQUIREMENTS (5 minutes):
   ✓ Ask clarifying questions
   ✓ Understand scale (users, QPS, data)
   ✓ Define success metrics
   ✓ List constraints

2. HIGH-LEVEL DESIGN (5 minutes):
   ✓ Draw main components
   ✓ Show data flow
   ✓ Identify critical paths
   ✓ Mention trade-offs

3. DETAILED DESIGN (10 minutes):
   ✓ Pick one component to deep-dive
   ✓ Explain choices
   ✓ Address bottlenecks
   ✓ Discuss alternatives

4. BOTTLENECK ANALYSIS (5 minutes):
   ✓ Where might it fail?
   ✓ Where's the latency?
   ✓ Where's the cost?
   ✓ How to improve?

5. SCALE & OPTIMIZATION (5 minutes):
   ✓ Can it handle 10x load?
   ✓ How to reduce latency?
   ✓ How to reduce cost?
   ✓ What to cache?

Key Principles:

- Start simple, add complexity
- Justify each decision
- Think about tradeoffs
- Use real numbers/estimates
- Draw diagrams
- Discuss alternatives
- Consider failure modes
- Think about monitoring

Common Trade-offs:

Consistency vs Availability:
- Strong consistency: Slower but accurate
- Eventual consistency: Faster but stale data

Latency vs Cost:
- Cache everything: Fast but expensive
- Compute on demand: Slow but cheap

Simplicity vs Features:
- Start simple: Easy to build and understand
- Add features: More value but complex

Accuracy vs Speed:
- High accuracy: Better results but slower
- Quick answer: Good enough results faster
"""

if __name__ == "__main__":
    print("=" * 80)
    print("SYSTEM DESIGN INTERVIEW QUESTIONS FOR RAG & AGENTS")
    print("=" * 80)
    
    for scenario in SYSTEM_DESIGN_SCENARIOS:
        print(f"\n\n{scenario['id']}: {scenario['title']}")
        print(f"Difficulty: {scenario['difficulty']}")
        print(f"\nDescription:\n{scenario['description']}")
        print("-" * 80)
    
    print("\n\n" + "=" * 80)
    print("FOLLOW-UP QUESTIONS TO EXPECT")
    print("=" * 80)
    for q in FOLLOW_UP_QUESTIONS:
        print(f"- {q}")
    
    print("\n\n" + "=" * 80)
    print("INTERVIEW TIPS")
    print("=" * 80)
    print(INTERVIEW_TIPS)
