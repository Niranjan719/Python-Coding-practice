# AI/ML Interview Preparation - Study Plan & Tips

## Overview
This folder contains **70+ coding questions** specifically designed for:
1. **Gen AI/Agentic AI** interviews (Python, RAG, Prompt Engineering)
2. **AI/ML Engineer** interviews (AWS Bedrock, Python, System Design)

---

## Study Plan (4-6 Weeks)

### Week 1-2: Foundation (20-25 hours)
**Focus**: Python fundamentals and basic data structures

Files to study:
- `01_python_fundamentals.py` (10 questions)
  - Solve all 10 questions
  - Understand each solution
  - Practice variations
  
- `02_data_structures_algorithms.py` (10 questions)
  - Implement all algorithms from scratch
  - Understand time/space complexity
  - Practice on LeetCode similar problems

**Daily Practice**: 2-3 hours
- 1 hour: Theory and solutions
- 1-2 hours: Implementation and testing

**Assessment**: Can you solve each without looking at solutions?

---

### Week 2-3: NLP & LLM Concepts (15-20 hours)
**Focus**: Understanding LLM fundamentals

Files to study:
- `03_nlp_llm_fundamentals.py` (10 questions)
  - Implement text preprocessing
  - Understand embeddings and similarity
  - Learn about attention mechanism

**Practice**:
- Implement tokenizer from scratch
- Calculate TF-IDF manually on sample data
- Implement cosine similarity
- Understand how transformers work

**Resources**:
- Read: "Attention is All You Need" paper
- Watch: 3Blue1Brown - Neural Networks videos
- Study: HuggingFace documentation

---

### Week 3-4: RAG & Retrieval (15-20 hours)
**Focus**: Retrieval Augmented Generation concepts

Files to study:
- `04_rag_vector_database.py` (10 questions)
  - Document chunking strategies
  - Vector similarity search
  - Reranking and hybrid search
  - RAG evaluation metrics

**Practice**:
- Build simple RAG pipeline
- Implement document chunking
- Calculate retrieval metrics
- Optimize context windows

**Tools to explore**:
- Pinecone (vector database)
- Weaviate
- ChromaDB
- LangChain RAG examples

---

### Week 4-5: APIs & Integration (15-20 hours)
**Focus**: System integration and API design

Files to study:
- `05_api_integration.py` (10 questions)
  - REST API client implementation
  - Error handling and retries
  - Rate limiting
  - Async operations

**Practice**:
- Call OpenAI API
- Implement retry logic
- Build rate limiter
- Handle errors gracefully

**AWS Focus** (for Job 2):
- AWS Bedrock API
- AWS SDK (boto3)
- Error handling patterns

---

### Week 5-6: Prompt Engineering & Multi-Agent (15-20 hours)
**Focus**: Advanced prompt techniques and agent systems

Files to study:
- `06_prompt_engineering.py` (10 questions)
  - Prompt templates
  - Few-shot learning
  - Chain-of-thought
  - Output formatting

- `07_multi_agent_systems.py` (10 questions)
  - Agent architecture
  - Multi-agent coordination
  - Workflow orchestration
  - System design

**Practice**:
- Optimize prompts using iterative approach
- Build simple agent with LLM
- Implement multi-agent workflow
- Design scalable system

**Frameworks to learn**:
- LangChain
- LlamaIndex
- CrewAI
- LangGraph

---

## Interview Question Categories

### For Job 1: Gen AI/Agentic AI

**Must Know** (Priority: Critical):
- [ ] Prompt engineering (Q6)
- [ ] RAG concepts (Q4)
- [ ] Multi-agent systems (Q7)
- [ ] LLM fundamentals (Q3)
- [ ] Data structures basics (Q2)

**Should Know** (Priority: High):
- [ ] Python fundamentals (Q1)
- [ ] API integration (Q5)
- [ ] System design
- [ ] Error handling

**Nice to Know** (Priority: Medium):
- [ ] Advanced prompt optimization
- [ ] LangChain/CrewAI internals
- [ ] Fine-tuning strategies

---

### For Job 2: AI/ML Engineer (AWS Bedrock)

**Must Know** (Priority: Critical):
- [ ] Python fundamentals (Q1)
- [ ] Data structures (Q2)
- [ ] API integration (Q5)
- [ ] NLP basics (Q3)
- [ ] Multi-agent workflows (Q7)

**Should Know** (Priority: High):
- [ ] AWS Bedrock fundamentals
- [ ] REST API design
- [ ] Error handling and retries
- [ ] System design

**Nice to Know** (Priority: Medium):
- [ ] RAG concepts (Q4)
- [ ] Prompt engineering (Q6)
- [ ] AWS optimization

---

## Interview Tips

### Before Interview
1. **Practice out loud**: Explain your solutions while coding
2. **Time yourself**: Complete questions in 20-30 minutes
3. **Know tradeoffs**: Understand time vs space complexity
4. **Test edge cases**: Empty input, large input, errors
5. **Prepare examples**: Have real examples ready

### During Interview
1. **Clarify requirements**: Ask questions before coding
2. **Explain approach**: "I'll use X because..."
3. **Write testable code**: Classes, functions, error handling
4. **Consider scalability**: "What if we had 1M items?"
5. **Discuss tradeoffs**: Different approaches and their pros/cons

### Example Interview Flow

**Q: "How would you implement RAG for a knowledge base?"**

Your approach:
1. **Clarify**: Ask about data size, latency requirements, accuracy needs
2. **Explain**: "I'd use a two-stage approach: BM25 + vector search"
3. **Design**: Sketch architecture on whiteboard/screen
4. **Code**: Implement key components (chunking, search)
5. **Discuss**: "For scaling, we could use..."
6. **Optimize**: "To improve recall, we could..."

---

## Common Interview Questions

### Python Fundamentals
- "Implement a LRU cache" → Q1
- "Reverse a list in-place" → Q2
- "Find duplicate in array" → Q2

### LLM/NLP
- "How does attention work?" → Q3
- "Explain word embeddings" → Q3
- "What's the difference between TF-IDF and embeddings?" → Q3

### RAG
- "Design a RAG system" → Q4, Q7
- "How to chunk documents?" → Q4
- "How to rank documents?" → Q4
- "What metrics evaluate retrieval?" → Q4

### APIs
- "Design an API for LLM calls" → Q5, Q7
- "Handle rate limiting" → Q5
- "Retry logic for transient errors" → Q5

### Prompt Engineering
- "How to improve model accuracy?" → Q6
- "Design system prompt" → Q6
- "Few-shot vs zero-shot" → Q6

### Multi-Agent
- "Design multi-agent system" → Q7
- "How agents communicate?" → Q7
- "Workflow orchestration" → Q7

---

## Resources for Deeper Learning

### Reading
- [ ] LangChain Documentation
- [ ] CrewAI GitHub
- [ ] LlamaIndex Concepts
- [ ] LangGraph Examples
- [ ] AWS Bedrock API Docs

### Videos
- [ ] LangChain Tutorials (YouTube)
- [ ] RAG Implementation (Multiple sources)
- [ ] Prompt Engineering Best Practices
- [ ] Multi-agent Architectures
- [ ] System Design (CS75, Grokking)

### Practice Platforms
- [ ] LeetCode (DSA problems)
- [ ] HackerRank (Python)
- [ ] LangChain Cook Book
- [ ] GitHub: Awesome LLM
- [ ] Kaggle: RAG Competitions

### Projects to Build
1. **Simple RAG**: Document search + LLM answer
2. **Multi-agent**: Agents collaborating on task
3. **RAG Evaluator**: Implement Q4 metrics
4. **API Server**: Flask/FastAPI with LLM
5. **Prompt Optimizer**: Iteratively improve prompts (Q6)

---

## Quick Reference: Question Difficulty

### Easy (6 questions)
- Q1: String tokenization
- Q1: Word frequency
- Q4: Text cleaning
- Q6: Stop words
- Q6: Sentiment analysis
- Q10: Log API call

### Medium (45+ questions)
- Most questions in all files
- Focus on implementation and understanding
- These are typical interview questions

### Hard (15+ questions)
- Q2: Edit distance (DP)
- Q2: Longest substring (DP)
- Q3: BPE tokenization
- Q4: Optimal context window
- Q5: Async API calls
- Q6: Prompt optimization
- Q7: Multi-agent system
- Q7: Workflow orchestration
- Q7: Reasoning loop

---

## Success Criteria

### Week 1-2
- [ ] Can solve all Q1 & Q2 without looking at solutions
- [ ] Understand time/space complexity for each
- [ ] Can optimize basic algorithms

### Week 3-4
- [ ] Can explain attention mechanism
- [ ] Can implement TF-IDF
- [ ] Understand RAG pipeline
- [ ] Can evaluate retrieval quality

### Week 5-6
- [ ] Can design multi-agent system
- [ ] Can optimize prompts effectively
- [ ] Can handle errors and scale
- [ ] Can explain system design tradeoffs

### Interview Ready
- [ ] Can solve any Q1-Q2 in 20 mins
- [ ] Can design RAG system in 30 mins
- [ ] Can discuss Q7 deeply
- [ ] Can answer system design questions
- [ ] Can explain your solutions clearly

---

## Common Mistakes to Avoid

❌ **Don't**:
- Write code without understanding it
- Skip edge cases or error handling
- Ignore time/space complexity
- Over-complicate solutions
- Forget to test your code

✅ **Do**:
- Understand why each solution works
- Handle errors gracefully
- Optimize for scalability
- Keep solutions simple first
- Test thoroughly

---

## Interview Companies Using These Questions

**Startups**:
- Anthropic, Cohere, Hugging Face
- OpenAI, MidJourney, Stability AI
- Replicate, Together AI

**Tech Giants**:
- Google (AI research, TensorFlow)
- Meta (LLAMA, AI research)
- Microsoft (Azure AI, Copilot)
- AWS (Bedrock, SageMaker)
- OpenAI (GPT models)

**Enterprise AI**:
- Databricks, Databend
- Weaviate, Milvus
- Pinecone (vector DB)

---

## Final Checklist

Week 1-2:
- [ ] Study Q1 & Q2 thoroughly
- [ ] Implement all solutions
- [ ] Practice on similar problems

Week 3-4:
- [ ] Study Q3 & Q4
- [ ] Build simple RAG
- [ ] Understand transformers

Week 5-6:
- [ ] Study Q5, Q6, Q7
- [ ] Design multi-agent system
- [ ] Practice system design questions

Before Interview:
- [ ] Review all Q1 & Q2 (quick)
- [ ] Deep dive: Relevant Q for role
- [ ] Practice explaining solutions
- [ ] Prepare real examples
- [ ] Get good sleep!

---

**Good luck with your interviews!** 🚀

Last updated: June 12, 2026
