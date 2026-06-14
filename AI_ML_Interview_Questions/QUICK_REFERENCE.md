# Quick Reference Guide

## How to Use This Folder

### 1. Start with README.md
Understand the folder structure and which files matter for your target role.

### 2. Follow STUDY_PLAN.md
- Week 1-2: Python fundamentals + DSA
- Week 3-4: NLP/LLM + RAG
- Week 5-6: APIs + Prompt Engineering + Multi-agent
- Total: 4-6 weeks, 80-120 hours

### 3. Study Each File in Order

**File 1: 01_python_fundamentals.py**
- 10 beginner-friendly questions
- Topics: strings, lists, dicts, comprehensions, generators
- Difficulty: ⭐ Easy
- Time to complete: 3-5 hours
- Expected after: Can write clean, Pythonic code

**File 2: 02_data_structures_algorithms.py**
- 10 core algorithm questions
- Topics: binary search, sorting, graphs, DP
- Difficulty: ⭐⭐ Medium
- Time to complete: 8-12 hours
- Expected after: Can solve LeetCode medium problems

**File 3: 03_nlp_llm_fundamentals.py**
- 10 NLP/LLM specific questions
- Topics: tokenization, embeddings, attention, TF-IDF
- Difficulty: ⭐⭐ Medium
- Time to complete: 6-10 hours
- Expected after: Understand how LLMs work

**File 4: 04_rag_vector_database.py**
- 10 RAG architecture questions
- Topics: chunking, similarity search, reranking, evaluation
- Difficulty: ⭐⭐ Medium
- Time to complete: 6-10 hours
- Expected after: Can design RAG systems

**File 5: 05_api_integration.py**
- 10 API/integration questions
- Topics: REST, retries, rate limiting, async
- Difficulty: ⭐⭐ Medium
- Time to complete: 6-10 hours
- Expected after: Can build production APIs

**File 6: 06_prompt_engineering.py**
- 10 prompt engineering questions
- Topics: templates, few-shot, chain-of-thought, optimization
- Difficulty: ⭐⭐ Medium
- Time to complete: 5-8 hours
- Expected after: Can write effective prompts

**File 7: 07_multi_agent_systems.py**
- 10 system design questions
- Topics: agents, orchestration, workflows, scaling
- Difficulty: ⭐⭐⭐ Hard
- Time to complete: 10-15 hours
- Expected after: Can design complex agent systems

---

## By Target Role

### For Job 1: Gen AI/Agentic AI - Python, RAG, Prompt Engineering

**Must Study** (Priority 1):
1. File 6: Prompt Engineering (10 hours)
2. File 4: RAG & Vector Database (10 hours)
3. File 7: Multi-Agent Systems (15 hours)
4. File 3: NLP & LLM Fundamentals (8 hours)

**Should Study** (Priority 2):
1. File 1: Python Fundamentals (5 hours)
2. File 5: API Integration (8 hours)

Total: ~60 hours = ~2 weeks focused study

### For Job 2: AI/ML Engineer - AWS Bedrock, Python

**Must Study** (Priority 1):
1. File 1: Python Fundamentals (5 hours)
2. File 2: Data Structures & Algorithms (10 hours)
3. File 5: API Integration (10 hours)
4. File 3: NLP & LLM Fundamentals (8 hours)
5. File 7: Multi-Agent Systems (12 hours)

**Should Study** (Priority 2):
1. File 4: RAG & Vector Database (8 hours)
2. File 6: Prompt Engineering (6 hours)

Total: ~70 hours = ~2.5 weeks focused study

---

## How to Solve Each Question

### Step 1: Understand the Problem
- Read the question carefully
- Understand the input and expected output
- Look at examples
- Ask clarifying questions mentally

### Step 2: Think of Approach
- Write pseudocode
- Consider tradeoffs (time vs space)
- Think of edge cases
- Discuss approach (as if in interview)

### Step 3: Implement
- Write clean, readable code
- Use meaningful variable names
- Add comments
- Handle errors

### Step 4: Test
- Test with given examples
- Test edge cases (empty, large, invalid)
- Check time/space complexity
- Optimize if needed

### Step 5: Explain
- Can you explain it to someone else?
- Why this approach over alternatives?
- What are tradeoffs?
- How would you scale it?

---

## Success Indicators

### After Week 1-2
- [ ] Can write Pythonic code
- [ ] Understand all data structures
- [ ] Can solve File 1 & 2 from memory
- [ ] Know time/space complexity

### After Week 3-4
- [ ] Can explain attention mechanism
- [ ] Understand RAG architecture
- [ ] Can implement basic RAG
- [ ] Know NLP concepts

### After Week 5-6
- [ ] Can design multi-agent system
- [ ] Can optimize prompts
- [ ] Can handle API errors
- [ ] Can discuss system design

### Interview Ready
- [ ] File 1 & 2: Can solve any in 20 minutes
- [ ] File 3 & 4: Can design system in 30 minutes
- [ ] File 5: Can explain APIs and error handling
- [ ] File 6 & 7: Can discuss advanced topics deeply

---

## Important Notes

### Don't Just Copy Solutions
- Understand why each line works
- Write from scratch multiple times
- Explain out loud while coding
- Challenge yourself with variations

### Focus on Understanding
- Understand the "why" not just "how"
- Know tradeoffs and alternatives
- Be able to optimize
- Explain to others

### Practice Real-World Scenarios
- "How would you scale this?"
- "What if data was 100x larger?"
- "How to handle failures?"
- "What about security?"

### Test Your Code
- Run all examples
- Test edge cases
- Check error handling
- Verify complexity

---

## Tips for Interview Success

### Before Interview
✓ Solve all questions without looking at solutions
✓ Practice explaining solutions
✓ Know your complexity analysis
✓ Prepare project examples
✓ Get good sleep!

### During Interview
✓ Clarify requirements before coding
✓ Explain your approach first
✓ Write clean, testable code
✓ Test your code
✓ Discuss tradeoffs and scaling

### Common Traps
✗ Don't code without thinking
✗ Don't ignore edge cases
✗ Don't forget to test
✗ Don't over-complicate
✗ Don't rush

---

## Resources

### For Deeper Learning
- LangChain Documentation: https://python.langchain.com/
- CrewAI: https://github.com/joaomdmoura/crewAI
- LlamaIndex: https://gpt-index.readthedocs.io/
- AWS Bedrock: https://aws.amazon.com/bedrock/
- Hugging Face: https://huggingface.co/

### Practice Platforms
- LeetCode (DSA)
- HackerRank (Python)
- GitHub (Open source projects)
- Kaggle (Competitions)

### Videos & Articles
- 3Blue1Brown - Neural Networks
- Jeremy Howard - Fast.ai
- Andrej Karpathy - LLM courses
- Research papers on Arxiv

---

## Folder Structure

```
AI_ML_Interview_Questions/
├── README.md                          # Overview and structure
├── STUDY_PLAN.md                      # 4-6 week study plan
├── QUICK_REFERENCE.md                 # This file
├── 01_python_fundamentals.py          # 10 Q - Basics
├── 02_data_structures_algorithms.py   # 10 Q - DSA
├── 03_nlp_llm_fundamentals.py         # 10 Q - NLP
├── 04_rag_vector_database.py          # 10 Q - RAG
├── 05_api_integration.py              # 10 Q - APIs
├── 06_prompt_engineering.py           # 10 Q - Prompts
└── 07_multi_agent_systems.py          # 10 Q - Agents
```

---

## Getting Started

1. **Pick your target role**
   - Gen AI/Agentic AI? → Focus on Files 3, 4, 6, 7
   - AI/ML Engineer? → Focus on Files 1, 2, 3, 5, 7

2. **Read STUDY_PLAN.md**
   - Understand the timeline
   - Commit to the schedule

3. **Start with File 1**
   - Read each question
   - Implement solutions
   - Test thoroughly

4. **Progress systematically**
   - One file per week
   - Complete all 10 questions
   - Don't move to next until comfortable

5. **Practice explaining**
   - Say solutions out loud
   - Record yourself
   - Get feedback

---

## Good Luck! 🚀

You have everything you need to ace these interviews. 

**Remember**: 
- Consistency beats intensity
- Understanding beats memorization
- Practice beats watching tutorials
- Small steps lead to big results

Start with File 1 today!

---

**Need help?** Check each file's README section or STUDY_PLAN.md

Last updated: June 12, 2026
