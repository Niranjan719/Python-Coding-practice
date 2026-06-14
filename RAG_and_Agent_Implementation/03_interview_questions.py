"""
LANGCHAIN & LANGGRAPH INTERVIEW QUESTIONS
Expected questions and answers for AI/ML interviews

These are common questions asked by companies using LangChain/LangGraph
(Anthropic, OpenAI partners, startup AI companies, etc.)
"""

# ============================================================================
# SECTION 1: LANGCHAIN FUNDAMENTALS
# ============================================================================

LANGCHAIN_QUESTIONS = [
    {
        "id": "LC1",
        "difficulty": "⭐ Easy",
        "question": "What is LangChain and why is it important?",
        "answer": """
LangChain is a framework for developing applications powered by language models.

Key components:
1. LLMs: Interface to language models (OpenAI, Claude, etc.)
2. Chains: Sequences of LLM calls and actions
3. Agents: LLMs making decisions about which tools to use
4. Memory: Maintaining conversation history
5. Tools: Functions agents can call

Why important:
- Simplifies LLM application development
- Provides abstractions for common patterns
- Handles API complexity
- Supports multiple LLM providers
- Built-in error handling and retries

Example:
```python
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4")
template = "What is {topic}?"
prompt = PromptTemplate(template=template, input_variables=["topic"])
chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(topic="RAG")
```
        """,
    },
    {
        "id": "LC2",
        "difficulty": "⭐ Easy",
        "question": "What is the difference between a Chain and an Agent?",
        "answer": """
Chain:
- Predetermined sequence of steps
- Each step knows what comes next
- No decision-making
- Predictable and reliable
- Good for fixed workflows

Example:
Prompt -> LLM -> Output -> Format -> Return

Agent:
- Dynamic sequence based on LLM decisions
- LLM decides which tool to use
- Can adapt to different inputs
- More flexible but less predictable
- Good for complex tasks

Example:
Think -> LLM decides action -> Execute tool -> Observe -> Repeat

Analogy:
- Chain: Following a recipe exactly
- Agent: A chef deciding what to cook based on available ingredients

When to use:
- Use Chain for: RAG, question answering, text transformation
- Use Agent for: Research tasks, complex problem solving, dynamic workflows
        """,
    },
    {
        "id": "LC3",
        "difficulty": "⭐⭐ Medium",
        "question": "How does LangChain's memory system work? What types of memory exist?",
        "answer": """
LangChain Memory Types:

1. ConversationBuffer:
   - Stores all messages in conversation
   - Simplest, but uses lots of tokens
   - Good for short conversations
   
   ```python
   from langchain.memory import ConversationBufferMemory
   memory = ConversationBufferMemory()
   ```

2. ConversationSummaryMemory:
   - Summarizes old messages
   - Reduces token usage
   - LLM creates summary
   
   ```python
   memory = ConversationSummaryMemory(llm=llm)
   ```

3. ConversationKGMemory:
   - Builds knowledge graph of entities
   - Extracts relationships
   - More structured

4. ConversationEntityMemory:
   - Tracks entities and their attributes
   - Updates entity information

5. VectorStoreRetrieverMemory:
   - Uses vector DB for semantic search
   - Retrieves relevant past messages
   - Best for long conversations

Best Practices:
- Use appropriate memory for conversation length
- Summarize periodically to reduce tokens
- Consider cost vs. quality tradeoff
- Monitor token usage
- Implement cleanup for old conversations
        """,
    },
    {
        "id": "LC4",
        "difficulty": "⭐⭐ Medium",
        "question": "Explain the ReACT (Reasoning + Acting) pattern used in agents.",
        "answer": """
ReACT is the core pattern in LangChain agents:

Steps:
1. Thought: LLM thinks about what to do
   - Analyze the problem
   - Identify relevant information needed
   - Plan approach

2. Action: LLM decides which tool to use
   - Select appropriate tool from available options
   - Prepare inputs for tool

3. Observation: Observe result of action
   - Tool executes and returns result
   - Result becomes new context

4. Repeat: Continue loop until done
   - "Final Answer" terminates loop
   - Max iterations prevents infinite loops

Example:
Thought: I need to find current stock price
Action: GetStockPrice
Action Input: {"symbol": "AAPL"}
Observation: AAPL is at $150
Thought: I found the price, I can answer now
Final Answer: Apple stock is at $150

Benefits:
- Interpretable reasoning trace
- Can correct mistakes mid-execution
- Works with large action spaces
- Easy to debug

Comparison with other patterns:
- Chain of Thought: Only reasoning, no actions
- Tree of Thought: Multiple reasoning paths
- ReACT: Reasoning + Acting in loop

Production Considerations:
- Reduce number of actions (API costs)
- Parallelize independent actions
- Cache frequently used results
- Monitor action patterns
        """,
    },
    {
        "id": "LC5",
        "difficulty": "⭐⭐⭐ Hard",
        "question": "Design a production-ready LangChain RAG system with error handling.",
        "answer": """
Production RAG System Design:

Components:
1. Document Ingestion Pipeline
2. Vector Store Management
3. Retriever with Filtering
4. LLM Integration
5. Error Handling
6. Monitoring
7. Caching

```python
from langchain.chains import RetrievalQA
from langchain.callbacks import StdOutCallbackHandler
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import logging

class ProductionRAG:
    def __init__(self, model="gpt-4", retrieval_k=3):
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(embedding_function=self.embeddings)
        self.llm = ChatOpenAI(model=model, temperature=0)
        self.retrieval_k = retrieval_k
        self.memory = ConversationSummaryMemory(llm=self.llm)
        
    def build_chain(self):
        retriever = self.vector_store.as_retriever(
            search_kwargs={"k": self.retrieval_k}
        )
        
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            callbacks=[StdOutCallbackHandler()],
            memory=self.memory
        )
        return chain
    
    def query_with_retry(self, question, max_retries=3):
        for attempt in range(max_retries):
            try:
                chain = self.build_chain()
                result = chain({"query": question})
                return {
                    "answer": result["result"],
                    "sources": result["source_documents"]
                }
            except Exception as e:
                logging.error(f"Attempt {attempt+1} failed: {str(e)}")
                if attempt == max_retries - 1:
                    raise
        
        return {"answer": "Unable to answer", "sources": []}

# Usage
rag = ProductionRAG()
result = rag.query_with_retry("What is RAG?")
```

Error Handling Patterns:
- Retry with exponential backoff
- Fallback to simpler models
- Cache for common queries
- Graceful degradation

Monitoring:
- Log all queries and responses
- Track API costs
- Monitor latency
- Measure accuracy with human feedback
- Alert on anomalies

Optimization:
- Batch queries when possible
- Use streaming for long responses
- Implement query caching
- Optimize embeddings model choice
- Tune retrieval parameters
        """,
    },
    {
        "id": "LC6",
        "difficulty": "⭐⭐ Medium",
        "question": "What are Tools in LangChain and how do you create them?",
        "answer": """
Tools allow agents to interact with external systems.

Creating Tools:

1. Simple Function Tool:
```python
from langchain.tools import tool

@tool
def get_stock_price(symbol: str) -> str:
    \"\"\"Get current stock price\"\"\"
    return f"Price of {symbol}: $100"

# Tool automatically created with name and description
```

2. Structured Tool:
```python
from langchain.tools import Tool
from pydantic import BaseModel, Field

class StockInput(BaseModel):
    symbol: str = Field(description="Stock symbol")

tool = Tool(
    name="GetStockPrice",
    func=get_stock_price,
    description="Get current stock price",
    args_schema=StockInput
)
```

3. Custom Tool Class:
```python
from langchain.tools import BaseTool
from typing import Optional

class StockPriceTool(BaseTool):
    name: str = "GetStockPrice"
    description: str = "Get current stock price"
    
    def _run(self, symbol: str):
        return f"Price of {symbol}: $100"
    
    def _arun(self, symbol: str):
        # Async version
        return await self._run(symbol)

tool = StockPriceTool()
```

Best Practices:
- Clear, concise descriptions
- Handle errors gracefully
- Validate inputs
- Document parameters
- Support async operations
- Consider tool combinations

Agent with Tools:
```python
from langchain.agents import create_react_agent

tools = [get_stock_price, calculate_profit]
agent = create_react_agent(llm, tools, prompt)
```
        """,
    },
    {
        "id": "LC7",
        "difficulty": "⭐⭐ Medium",
        "question": "How do you handle token limits in LangChain?",
        "answer": """
Token Limit Management:

1. Monitor Token Usage:
```python
from langchain.callbacks import get_openai_callback

with get_openai_callback() as cb:
    response = chain.run(query)
    print(f"Tokens used: {cb.total_tokens}")
```

2. Reduce Context Size:
- Use document summarization
- Retrieve fewer documents (k=3 instead of k=10)
- Implement semantic chunking
- Use query expansion carefully

3. Memory Optimization:
```python
# Use summarization memory instead of buffer
memory = ConversationSummaryMemory(llm=llm)

# Implement sliding window
memory = ConversationBufferWindowMemory(k=5)  # Keep last 5 messages
```

4. Prompt Optimization:
- Reduce prompt size
- Use instruction following instead of examples
- Dynamic prompt templates

5. Model Selection:
- Use cheaper models for non-critical tasks
- GPT-3.5-turbo for simple tasks
- GPT-4 for complex reasoning

6. Batch Processing:
```python
# Process multiple queries together
batch_results = chain.batch([query1, query2, query3])
```

7. Caching:
```python
from langchain.cache import InMemoryCache
import langchain
langchain.llm_cache = InMemoryCache()
```

Cost Calculation:
- Input tokens: fewer is better
- Output tokens: model choice matters
- Tool calls: can add overhead
- Monitor and optimize continuously

Best Practices:
- Always check token limits before deployment
- Use callbacks to track usage
- Implement monitoring and alerting
- Test with real data
- Have fallback strategies
        """,
    },
]

# ============================================================================
# SECTION 2: LANGGRAPH QUESTIONS
# ============================================================================

LANGGRAPH_QUESTIONS = [
    {
        "id": "LG1",
        "difficulty": "⭐ Easy",
        "question": "What is LangGraph and how is it different from LangChain?",
        "answer": """
LangGraph:
- Graph-based state management for agents
- Built on top of LangChain
- Provides deterministic execution patterns
- Visual representation of workflows

LangChain:
- Framework for building LLM applications
- Linear chains and agents
- More flexible but less structured

Key Differences:

LangChain:
- Sequential processing
- Implicit state management
- Harder to debug complex flows
- Less explicit control

LangGraph:
- Graph-based state machines
- Explicit state transitions
- Visual debugging
- Conditional branching
- Cycle handling
- Better for complex workflows

When to use:
- LangChain: Simple RAG, basic agents
- LangGraph: Complex workflows, conditional logic, state machines

Example:
LangChain: prompt -> LLM -> output
LangGraph: [START] -> decide -> [search] -> [summarize] -> [END]
                          |
                        [direct_answer]

Benefits of LangGraph:
- Explicit state management
- Conditional edges
- Visualizable workflows
- Better error handling
- Easier testing
- Production-ready patterns
        """,
    },
    {
        "id": "LG2",
        "difficulty": "⭐⭐ Medium",
        "question": "Explain the StateGraph concept and how to build an agent with it.",
        "answer": """
StateGraph is the core of LangGraph:

Concept:
- Directed graph of processing nodes
- Each node receives and modifies state
- Edges define transitions between nodes
- State is passed through entire graph

Building an Agent:

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# Define state
class AgentState(TypedDict):
    task: str
    steps: Annotated[list, operator.add]  # Accumulate steps
    result: str

# Create graph
graph = StateGraph(AgentState)

# Define nodes
def think_node(state: AgentState) -> AgentState:
    # LLM generates thoughts
    thought = llm.generate_thought(state["task"])
    return {"steps": [f"Thought: {thought}"]}

def act_node(state: AgentState) -> AgentState:
    # Execute action
    action = llm.decide_action(state["steps"])
    result = execute_tool(action)
    return {"steps": [f"Action: {action}"]}

def decide_node(state: AgentState) -> str:
    # Conditional routing
    if is_complete(state):
        return END
    return "act"

# Add nodes
graph.add_node("think", think_node)
graph.add_node("act", act_node)

# Add edges
graph.add_edge("START", "think")
graph.add_conditional_edges(
    "think",
    decide_node,
    {
        "act": "act",
        END: END
    }
)
graph.add_edge("act", "think")

# Compile
agent = graph.compile()

# Run
result = agent.invoke({"task": "Research RAG"})
```

Key Concepts:
- State: Shared data structure
- Nodes: Processing functions
- Edges: Transitions between nodes
- Conditional edges: Dynamic routing

Advantages:
- Visual representation
- Explicit state transitions
- Easy to debug
- Composable
- Type-safe (with TypedDict)
        """,
    },
    {
        "id": "LG3",
        "difficulty": "⭐⭐⭐ Hard",
        "question": "Design a multi-agent system using LangGraph with sub-graphs.",
        "answer": """
Multi-Agent System with Sub-graphs:

Architecture:
- Main coordinator graph
- Specialized agent sub-graphs
- State synchronization
- Result aggregation

```python
from langgraph.graph import StateGraph, END, Graph
from typing import TypedDict

# Global state
class GlobalState(TypedDict):
    query: str
    research_result: str
    analysis_result: str
    final_answer: str

# Research agent sub-graph
def create_research_agent():
    graph = StateGraph(GlobalState)
    
    def search(state):
        results = search_tool(state["query"])
        return {"research_result": results}
    
    def summarize(state):
        summary = summarize_tool(state["research_result"])
        return {"research_result": summary}
    
    graph.add_node("search", search)
    graph.add_node("summarize", summarize)
    graph.add_edge("START", "search")
    graph.add_edge("search", "summarize")
    graph.add_edge("summarize", END)
    
    return graph.compile()

# Analysis agent sub-graph
def create_analysis_agent():
    graph = StateGraph(GlobalState)
    
    def analyze(state):
        analysis = analyze_tool(state["research_result"])
        return {"analysis_result": analysis}
    
    graph.add_node("analyze", analyze)
    graph.add_edge("START", "analyze")
    graph.add_edge("analyze", END)
    
    return graph.compile()

# Coordinator graph
def create_coordinator():
    graph = StateGraph(GlobalState)
    
    research_agent = create_research_agent()
    analysis_agent = create_analysis_agent()
    
    def run_research(state):
        result = research_agent.invoke(state)
        return result
    
    def run_analysis(state):
        result = analysis_agent.invoke(state)
        return result
    
    def combine_results(state):
        combined = f"Research: {state['research_result']}\nAnalysis: {state['analysis_result']}"
        return {"final_answer": combined}
    
    graph.add_node("research", run_research)
    graph.add_node("analysis", run_analysis)
    graph.add_node("combine", combine_results)
    
    graph.add_edge("START", "research")
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "combine")
    graph.add_edge("combine", END)
    
    return graph.compile()

coordinator = create_coordinator()
result = coordinator.invoke({"query": "Research AI ethics"})
```

Benefits:
- Agent specialization
- Parallel execution possible
- Clear separation of concerns
- Reusable components
- Easy to extend

Considerations:
- State synchronization
- Error propagation
- Performance optimization
- Timeout handling
- Resource management
        """,
    },
    {
        "id": "LG4",
        "difficulty": "⭐⭐ Medium",
        "question": "How do you handle cycles and loops in LangGraph?",
        "answer": """
Handling Cycles:

Problem:
- Agents need to loop (think -> act -> observe -> think)
- Need to prevent infinite loops
- Need clear exit conditions

Solutions:

1. Conditional Edges with Exit:
```python
graph.add_conditional_edges(
    "think",
    decide_next,
    {
        "act": "act",
        "end": END,
        "rethink": "think"  # Loop back
    }
)

def decide_next(state):
    if state["is_complete"]:
        return "end"
    elif state["needs_rethinking"]:
        return "rethink"
    return "act"
```

2. Iteration Counter:
```python
class AgentState(TypedDict):
    task: str
    iterations: int
    max_iterations: int
    result: str

def should_continue(state):
    if state["iterations"] >= state["max_iterations"]:
        return "end"
    return "act"
```

3. Success Condition:
```python
def should_continue(state):
    if "Final Answer" in state.get("last_output", ""):
        return "end"
    return "continue"
```

Best Practices:
- Always have max iteration limit
- Implement early stopping criteria
- Log iteration progress
- Monitor for patterns (repeated states)
- Implement timeout
- Have explicit exit conditions

Example with Loop:
```python
graph.add_edge("START", "think")
graph.add_conditional_edges(
    "think",
    lambda state: "act" if not is_done(state) else "end"
)
graph.add_edge("act", "observe")
graph.add_edge("observe", "think")  # Loop back
graph.add_edge("end", END)
```

Debugging Loops:
- Print state at each iteration
- Visualize graph (LangGraph.draw_ascii())
- Track state changes
- Use breakpoints
- Monitor memory usage
        """,
    },
    {
        "id": "LG5",
        "difficulty": "⭐⭐⭐ Hard",
        "question": "Compare different agent architectures: Plan-Execute, ReACT, and Tool Use.",
        "answer": """
Agent Architecture Comparison:

1. Plan-Execute:
   Structure:
   - Plan: Break task into steps
   - Execute: Follow plan sequentially
   
   Advantages:
   - Explainable (clear plan)
   - Efficient (no replanning)
   - Good for structured tasks
   
   Disadvantages:
   - Inflexible (can't adapt)
   - Fails if plan is wrong
   
   Best for: Well-defined tasks, workflows

2. ReACT (Reason + Act):
   Structure:
   - Thought: Why take action?
   - Action: Which tool to use?
   - Observation: What happened?
   - (Repeat)
   
   Advantages:
   - Flexible (adapts to results)
   - Interpretable (shows reasoning)
   - Robust (corrects mistakes)
   
   Disadvantages:
   - More API calls
   - Slower than Plan-Execute
   - Can hallucinate actions
   
   Best for: Complex problems, exploration

3. Tool Use:
   Structure:
   - Decide tool and input
   - Execute tool
   - Get result
   - Repeat if needed
   
   Advantages:
   - Simple and direct
   - Efficient
   - Works well with structured tools
   
   Disadvantages:
   - Limited reasoning visibility
   - Hard to debug
   
   Best for: Tool-heavy tasks, APIs

When to Use:
- Research/exploration -> ReACT
- Task automation -> Plan-Execute
- API integration -> Tool Use
- Complex reasoning -> ReACT
- Speed critical -> Plan-Execute

Hybrid Approach (Best):
```
Plan (top-level strategy)
  -> ReACT loop (detailed reasoning + tool use)
  -> Observe results
  -> Adapt plan if needed
```

Implementation:
```python
# Plan phase
plan = llm.generate_plan(task)

# Execute phase (ReACT loop)
for step in plan:
    thought = llm.think(step)
    tool, input = llm.select_tool(thought)
    result = tool(input)
    # Observe and potentially adjust
```

Trade-offs:
- Explainability vs Efficiency
- Flexibility vs Predictability
- Reasoning vs Speed
        """,
    },
]

# ============================================================================
# SECTION 3: SYSTEM DESIGN QUESTIONS FOR AI/ML
# ============================================================================

SYSTEM_DESIGN_QUESTIONS = [
    {
        "id": "SD1",
        "difficulty": "⭐⭐⭐ Hard",
        "question": "Design a large-scale RAG system for customer support (1M+ queries/day)",
        "answer": """
Requirements:
- Handle 1M+ queries per day
- Sub-second response time
- 99.9% uptime
- Multiple knowledge base updates
- Cost-effective

Architecture:

```
Users
  |
  v
[Load Balancer]
  |
  +---> [API Gateway]
            |
            +---> [Query Router]
                    |
                    +---> [Cache Layer] (Redis) - 80% hit rate
                    |
                    +---> [Retrieval Service]
                            |
                            +---> [Vector DB] (Pinecone/Milvus)
                            +---> [Embedding Service]
                            +---> [Reranker Service]
                    |
                    +---> [LLM Service]
                            |
                            +---> [LLM Pool] (GPT-4, GPT-3.5)
                            +---> [Response Cache]
                    |
                    +---> [Response Formatter]
                    |
                    +---> [Logging & Monitoring]
```

Components:

1. API Gateway:
   - Rate limiting
   - Authentication
   - Request validation
   - Load distribution

2. Query Router:
   - Route to cache or compute
   - Query classification
   - Priority handling

3. Cache Layer:
   - Query response cache
   - Embedding cache
   - TTL management

4. Retrieval Service:
   - Parallel retrieval:
     * BM25 search (100ms)
     * Vector search (50ms)
   - Hybrid ranking
   - Metadata filtering

5. Embedding Service:
   - Batch encoding
   - Caching
   - Different models for different doc types

6. Reranking Service:
   - Cross-encoder model
   - Top-k filtering
   - Score calibration

7. LLM Service:
   - Load balancing across models
   - Prompt caching
   - Streaming responses
   - Fallback strategies

8. Storage:
   - PostgreSQL: Metadata
   - Vector DB: Embeddings
   - Redis: Cache
   - S3: Documents and logs

Optimization:

1. Latency:
   - Parallel retrieval
   - Response streaming
   - Async processing
   - Connection pooling

2. Cost:
   - Use cheaper model for simple queries
   - Batch processing
   - Cache frequently asked
   - Optimize token usage

3. Scalability:
   - Horizontal scaling
   - Database sharding
   - Vector DB clustering
   - Load balancing

Data Flow:
1. User query comes in
2. Check cache (hit: return response)
3. Router classifies query
4. Parallel retrieve: BM25 + Vector
5. Rerank results
6. Check LLM cache
7. Generate with LLM
8. Cache response
9. Return to user

Monitoring:
- Query latency percentiles
- Cache hit rate
- LLM API usage
- Error rates
- User satisfaction

Scaling considerations:
- At 1M queries/day: ~11 QPS average, spiky
- Need auto-scaling
- Regional deployment for latency
- Multi-region for redundancy

Cost estimate:
- Embeddings: 1M queries * $0.0001 = $100/day
- LLM: 1M queries * $0.01 (avg) = $10k/day
- Infra: $5k/day
- Total: ~$15k/day or $5.5M/year
        """,
    },
    {
        "id": "SD2",
        "difficulty": "⭐⭐⭐ Hard",
        "question": "Design a multi-agent system for complex task automation",
        "answer": """
Scenario: Financial analysis and report generation

Requirements:
- Handle complex multi-step financial analysis
- Coordinate multiple specialized agents
- 30-minute turnaround time
- High accuracy (financial reports)
- Audit trail for compliance

Agent Architecture:

```
Orchestrator Agent
  |
  +---> [Data Collection Agent]
  |       - Fetch stock data
  |       - Get financial reports
  |       - Retrieve news
  |
  +---> [Analysis Agent]
  |       - Technical analysis
  |       - Fundamental analysis
  |       - Sentiment analysis
  |
  +---> [Comparison Agent]
  |       - Peer comparison
  |       - Industry trends
  |       - Historical comparison
  |
  +---> [Report Generation Agent]
  |       - Format findings
  |       - Create visualizations
  |       - Generate recommendations
  |
  +---> [Validation Agent]
         - Check accuracy
         - Verify sources
         - Flag concerns
```

Agent Specifications:

1. Orchestrator:
   - Breaks complex task into sub-tasks
   - Assigns to specialized agents
   - Aggregates results
   - Handles errors
   - Manages dependencies

2. Data Collection:
   - Tools: Market API, SEC EDGAR, News API
   - Parallel data fetching
   - Error handling for missing data

3. Analysis:
   - Technical indicators (RSI, MACD)
   - P/E ratio, debt analysis
   - Sentiment from news articles

4. Comparison:
   - Compare against peers
   - Calculate relative metrics
   - Identify outliers

5. Report Generation:
   - Template-based formatting
   - Add visualizations
   - Executive summary

6. Validation:
   - Cross-check calculations
   - Verify data consistency
   - Flag anomalies

Communication:

```python
class MessageBus:
    def send(self, from_agent, to_agent, message):
        # Route message
        # Store in queue
        # Deliver to agent
    
    def broadcast(self, from_agent, message):
        # Send to all agents
        # Update shared state
```

State Management:

```python
class SharedState:
    def __init__(self):
        self.raw_data = {}
        self.analysis_results = {}
        self.final_report = {}
        self.errors = []
        self.audit_log = []
    
    def update(self, agent_id, key, value):
        self.audit_log.append({
            "timestamp": time.time(),
            "agent": agent_id,
            "action": "update",
            "key": key,
            "value": value
        })
        self[key] = value
```

Coordination Pattern:

1. Orchestrator receives task
2. Creates work items for each agent
3. Agents work in parallel:
   - Data collection (10 min)
   - Analysis (10 min in parallel)
   - Comparison (5 min)
4. Report generation (5 min)
5. Validation (5 min)
6. Return complete report

Error Handling:

- Retry failed data fetches
- Skip optional agents
- Use cached data if available
- Alert on critical failures
- Generate partial report if needed

Monitoring:

- Agent execution time
- Error rates per agent
- Resource utilization
- Report quality metrics

Scaling:

- Process multiple reports in parallel
- Distribute agents across machines
- Use message queues (RabbitMQ)
- Implement worker pools

Cost Optimization:

- Cache frequently accessed data
- Batch API calls
- Use cheaper models for non-critical steps
- Implement caching layer
        """,
    },
    {
        "id": "SD3",
        "difficulty": "⭐⭐ Medium",
        "question": "Design the prompt engineering strategy for a production LLM application",
        "answer": """
Strategy for Effective Prompts:

1. Prompt Structure:

```
System Message:
- Define role
- Constraints
- Output format
- Tone

Context:
- Relevant information
- Examples (few-shot)
- Background

User Query:
- Clear question
- Required information
```

2. Prompt Engineering Techniques:

a) Role-Based:
"You are a financial analyst. Analyze this stock..."

b) Few-Shot:
"Examples:
Q: What is apple stock?
A: Apple Inc. stock is..."

c) Chain-of-Thought:
"Think step by step: First identify...then analyze...finally..."

d) Instruction Following:
"Do NOT include stock prices from before 2024
Include only confirmed news
Format as bullet points"

3. Optimization Process:

```
Version 1: Basic prompt
  -> Test on 100 examples
  -> Measure accuracy (e.g., 70%)
  -> Identify failure cases
  -> Adjust prompt

Version 2: Refined prompt
  -> Add constraints
  -> Better examples
  -> Test again (80%)
  
Version 3: Advanced
  -> Add chain-of-thought
  -> Multi-turn reasoning
  -> Test (85%)

Version 4: Production
  -> Optimize for cost
  -> Add caching
  -> Monitor quality
```

4. Quality Metrics:

- Accuracy: Does it answer correctly?
- Relevance: Is response on-topic?
- Consistency: Same query -> similar response?
- Efficiency: Minimal tokens used?
- Safety: No harmful content?

5. Prompt Template System:

```python
class PromptManager:
    def __init__(self):
        self.templates = {}
        self.version_history = {}
    
    def register_prompt(self, name, template, version):
        self.templates[name] = {
            "template": template,
            "version": version,
            "created_at": time.time()
        }
    
    def get_prompt(self, name):
        return self.templates[name]
    
    def a_b_test(self, name, version_a, version_b, samples):
        # Test both versions on samples
        # Calculate metrics
        # Return winner
```

6. Template Structure:

```
System:
{role_definition}
{constraints}
{output_format}

Context:
{background_info}
{examples}

User Query:
{query}

Answer:
```

7. Advanced Techniques:

- Dynamic prompts based on query type
- Multi-stage prompting (plan -> execute)
- Prompt caching for common questions
- Monitoring prompt effectiveness
- A/B testing new prompts

8. Deployment Strategy:

- Start with tested version
- Gradually roll out new versions
- Monitor quality metrics
- Have rollback plan
- Version all prompts
- Document rationale

9. Cost Optimization:

- Reuse prompts when possible
- Cache expensive prompts
- Use cheaper models for simple tasks
- Optimize prompt length
- Batch similar queries

10. Monitoring:

- Track prompt performance
- Monitor user satisfaction
- Flag degradation
- Update underperforming prompts
- A/B test improvements
        """,
    },
]

# ============================================================================
# INTERVIEW PREPARATION
# ============================================================================

def print_questions_by_difficulty(questions, difficulty):
    """Filter and print questions by difficulty"""
    filtered = [q for q in questions if q["difficulty"] == difficulty]
    for q in filtered:
        print(f"\n{q['id']}: {q['question']}")
        print(f"Difficulty: {q['difficulty']}")

def get_question_by_id(all_questions, question_id):
    """Get specific question by ID"""
    for q in all_questions:
        if q["id"] == question_id:
            return q
    return None

# ============================================================================
# USAGE
# ============================================================================

if __name__ == "__main__":
    all_questions = LANGCHAIN_QUESTIONS + LANGGRAPH_QUESTIONS + SYSTEM_DESIGN_QUESTIONS
    
    print("=" * 70)
    print("LANGCHAIN & LANGGRAPH INTERVIEW QUESTIONS")
    print("=" * 70)
    
    print("\n\nLANGCHAIN QUESTIONS (7 questions)")
    print("-" * 70)
    for q in LANGCHAIN_QUESTIONS:
        print(f"\n{q['id']}: {q['question']}")
        print(f"Difficulty: {q['difficulty']}")
    
    print("\n\nLANGGRAPH QUESTIONS (5 questions)")
    print("-" * 70)
    for q in LANGGRAPH_QUESTIONS:
        print(f"\n{q['id']}: {q['question']}")
        print(f"Difficulty: {q['difficulty']}")
    
    print("\n\nSYSTEM DESIGN QUESTIONS (3 questions)")
    print("-" * 70)
    for q in SYSTEM_DESIGN_QUESTIONS:
        print(f"\n{q['id']}: {q['question']}")
        print(f"Difficulty: {q['difficulty']}")
    
    print("\n\n" + "=" * 70)
    print("INTERVIEW TIPS")
    print("=" * 70)
    print("""
    1. Understand concepts deeply, not just code
    2. Explain your reasoning as you code
    3. Consider edge cases and error handling
    4. Discuss tradeoffs: speed vs accuracy, cost vs quality
    5. Mention production considerations
    6. Ask clarifying questions
    7. Practice explaining code verbally
    8. Know the trade-offs between different approaches
    """)
