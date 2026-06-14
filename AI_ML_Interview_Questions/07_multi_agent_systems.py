"""
MULTI-AGENT SYSTEMS & SYSTEM DESIGN FOR AI/ML INTERVIEWS
⭐⭐⭐ Hard difficulty questions

These questions test:
- Agent architecture and communication
- Workflow orchestration
- Task delegation and coordination
- State management
- Tool/Action execution
- System design and scalability
"""

# ============================================================================
# Q1: BASIC AGENT ARCHITECTURE - Agent Class
# ============================================================================
# Question: Design a basic AI agent

class Agent:
    """
    ⭐⭐⭐ Hard
    Basic agent that can think, plan, and act
    
    Components:
    1. State: Agent's current context/knowledge
    2. Tools: Available functions agent can use
    3. Memory: Past interactions and decisions
    4. Reasoning: LLM that decides next action
    
    Example:
    agent = Agent(
        name="ResearchAgent",
        role="Research documents and summarize",
        tools=[search_tool, summarize_tool]
    )
    
    response = agent.run("Find info about RAG")
    
    Frameworks: LangChain Agents, CrewAI, AutoGPT
    """
    
    def __init__(self, name, role, tools=None):
        """Initialize agent with name, role, and available tools"""
        self.name = name
        self.role = role
        self.tools = tools or {}
        self.memory = []
        self.state = {}
    
    def think(self, task):
        """Use LLM to decide what to do next"""
        pass
    
    def act(self, action, parameters):
        """Execute action/tool call"""
        pass
    
    def run(self, task):
        """Execute task: think -> act -> observe loop"""
        pass
    
    def save_to_memory(self, interaction):
        """Save interaction for future reference"""
        pass


# ============================================================================
# Q2: MULTI-AGENT COLLABORATION - Agent Communication
# ============================================================================
# Question: Coordinate multiple agents

class MultiAgentSystem:
    """
    ⭐⭐⭐ Hard
    Coordinate multiple specialized agents
    
    Architecture:
    - Manager Agent: Delegates tasks, coordinates
    - Worker Agents: Specialize in specific tasks
    - Communication: Agents send messages
    
    Example workflow:
    Manager: "I need research on AI ethics and coding best practices"
    |
    +-> Research Agent: "Finding AI ethics papers..."
    +-> Code Agent: "Finding coding standards..."
    |
    Both agents complete, return results
    Manager: Combines and summarizes
    
    Frameworks: CrewAI, LangGraph, Multi-agent Instruct
    
    Benefits:
    - Specialization: Each agent expert in domain
    - Parallelization: Agents work simultaneously
    - Robustness: If one fails, others continue
    - Scalability: Easy to add more agents
    """
    
    def __init__(self):
        """Initialize system with empty agent list"""
        self.agents = {}
        self.message_queue = []
    
    def register_agent(self, name, agent):
        """Register an agent in the system"""
        pass
    
    def send_message(self, from_agent, to_agent, message):
        """Send message between agents"""
        pass
    
    def orchestrate_task(self, task, manager_agent):
        """Coordinator delegates task to agents and combines results"""
        pass


# ============================================================================
# Q3: TOOL/ACTION EXECUTION - Agent Toolbox
# ============================================================================
# Question: Implement agent tools

class Tool:
    """
    ⭐⭐ Medium
    Tool that an agent can call
    
    Example tools:
    - SearchTool: Query search engine
    - CalculatorTool: Perform math
    - PythonTool: Execute code
    - APICaller: Call external APIs
    - FileReader: Read files
    - DatabaseQuery: Query databases
    
    Structure:
    - Name: What the tool does
    - Description: When to use it
    - Parameters: What inputs it needs
    - Execute: Run the tool
    
    Example:
    search_tool = Tool(
        name="WebSearch",
        description="Search the web for information",
        parameters=["query", "num_results"],
        execute=google_search
    )
    """
    
    def __init__(self, name, description, parameters, execute_func):
        self.name = name
        self.description = description
        self.parameters = parameters
        self.execute = execute_func
    
    def call(self, **kwargs):
        """Call the tool with parameters"""
        pass
    
    def validate_parameters(self, **kwargs):
        """Check if required parameters provided"""
        pass


# ============================================================================
# Q4: WORKFLOW ORCHESTRATION - DAG Execution
# ============================================================================
# Question: Execute workflow with dependencies

class WorkflowDAG:
    """
    ⭐⭐⭐ Hard
    Execute tasks in Directed Acyclic Graph (DAG)
    
    Used for: Complex workflows with dependencies
    
    Example workflow:
    ```
    FetchData -> ProcessData -> AnalyzeData -> GenerateReport
         |
         +-> (ProcessData depends on FetchData)
         +-> (AnalyzeData depends on ProcessData)
         +-> (GenerateReport depends on AnalyzeData)
    ```
    
    Benefits:
    - Parallelization: Independent tasks run concurrently
    - Dependency tracking: Automatic ordering
    - Error handling: Skip dependent tasks if parent fails
    - Monitoring: Track progress
    
    Frameworks: Apache Airflow, Prefect, Dagster
    """
    
    def __init__(self):
        """Initialize empty DAG"""
        self.tasks = {}
        self.dependencies = {}
    
    def add_task(self, task_name, task_func):
        """Add task to DAG"""
        pass
    
    def add_dependency(self, dependent_task, prerequisite_task):
        """task A depends on task B"""
        pass
    
    def execute(self):
        """Execute all tasks respecting dependencies"""
        pass
    
    def get_execution_order(self):
        """Return topologically sorted execution order"""
        pass


# ============================================================================
# Q5: STATE MANAGEMENT - Agent Context
# ============================================================================
# Question: Manage agent state and context

class AgentState:
    """
    ⭐⭐ Medium
    Manage agent's current state, context, and history
    
    Contains:
    - Current task
    - Intermediate results
    - Tool outputs
    - Decision history
    - Error tracking
    
    Example:
    state = AgentState()
    state.set("current_task", "Research AI")
    state.add_result("search_results", [...])
    state.add_error("Tool failed: API rate limit")
    
    history = state.get_history()
    """
    
    def __init__(self):
        """Initialize empty state"""
        self.state = {}
        self.history = []
        self.errors = []
    
    def set(self, key, value):
        """Set state variable"""
        pass
    
    def get(self, key):
        """Get state variable"""
        pass
    
    def add_result(self, step, result):
        """Add result from a step"""
        pass
    
    def add_error(self, error_message):
        """Track error"""
        pass
    
    def get_history(self):
        """Get execution history"""
        pass


# ============================================================================
# Q6: DECISION TREE - Conditional Agent Routing
# ============================================================================
# Question: Route tasks based on conditions

def build_decision_tree(task, conditions):
    """
    ⭐⭐ Medium
    Route task to appropriate agent based on conditions
    
    Example:
    task = "Extract data from PDF"
    
    Decision tree:
    if file_type == "PDF":
        -> PDFExtractor
    elif file_type == "CSV":
        -> CSVExtractor
    else:
        -> ManualAgent
    
    Input:
    task = "Extract data from report.pdf"
    conditions = [
        (lambda t: t.endswith('.pdf'), 'PDFExtractor'),
        (lambda t: t.endswith('.csv'), 'CSVExtractor'),
        (lambda t: t.endswith('.json'), 'JSONExtractor'),
    ]
    
    Output: Best agent to handle task
    
    Used for: Smart routing, task classification
    """
    pass


# ============================================================================
# Q7: REASONING LOOP - Iterative Task Solving
# ============================================================================
# Question: Implement agent reasoning loop

def agent_reasoning_loop(task, llm_func, max_iterations=10):
    """
    ⭐⭐⭐ Hard
    Core agent loop: Think -> Act -> Observe -> Repeat
    
    Loop:
    1. Observation: Current state
    2. Thought: What to do next
    3. Action: Execute tool/action
    4. Result: Tool output
    5. Repeat until done
    
    Input:
    task = "What's the population of Tokyo and its growth rate?"
    llm_func = model.generate
    max_iterations = 10
    
    Example execution:
    Observation: Task requires finding population and growth rate
    Thought: Need to search for Tokyo population data
    Action: search_tool("Tokyo population 2024")
    Result: Tokyo population is 37.4 million
    
    Observation: Found population, still need growth rate
    Thought: Need additional search for growth rate
    Action: search_tool("Tokyo population growth rate")
    Result: Annual growth rate is 0.5%
    
    Final Answer: Tokyo has 37.4M people with 0.5% annual growth
    
    Stop conditions:
    - Max iterations reached
    - Agent says "Final Answer"
    - Error occurred
    """
    pass


# ============================================================================
# Q8: ERROR HANDLING IN AGENTS - Recovery Strategies
# ============================================================================
# Question: Handle failures gracefully

def handle_agent_error(error, fallback_strategy="retry"):
    """
    ⭐⭐ Medium
    Handle errors in agent execution
    
    Error types:
    - Tool execution error (API down)
    - LLM error (rate limited, timeout)
    - Format error (invalid response)
    - Logic error (agent stuck in loop)
    
    Strategies:
    1. Retry: Try again after delay
    2. Fallback: Use alternative tool
    3. Escalate: Ask human for help
    4. Skip: Skip this step, continue
    
    Input:
    error = APIError("Rate limit exceeded")
    fallback_strategy = "retry"
    
    Output: Recovery action
    
    Example:
    try:
        result = agent.run(task)
    except Exception as e:
        if should_retry(e):
            result = handle_agent_error(e, "retry")
        else:
            result = handle_agent_error(e, "escalate")
    """
    pass


# ============================================================================
# Q9: AGENT MEMORY - Learning FROM Past
# ============================================================================
# Question: Implement agent memory and learning

class AgentMemory:
    """
    ⭐⭐ Medium
    Agent learns from past interactions
    
    Memory types:
    - Short-term: Current conversation
    - Long-term: All past interactions
    - Procedural: How to use tools
    - Semantic: Facts and knowledge
    
    Benefits:
    - Avoid repeating mistakes
    - Improve efficiency
    - Provide context
    - Learn patterns
    
    Example:
    memory = AgentMemory()
    memory.add("tool_use", "search_tool works best with specific keywords")
    memory.add("failure", "API returns 429 when more than 100 calls/min")
    memory.add("success", "Breaking complex tasks into smaller steps helps")
    
    If error occurs, check similar past errors for solutions
    """
    
    def __init__(self):
        """Initialize memory storage"""
        self.short_term = []
        self.long_term = []
        self.failures = []
        self.successes = []
    
    def add(self, memory_type, content):
        """Add memory"""
        pass
    
    def recall_similar(self, query):
        """Find similar past experiences"""
        pass
    
    def learn_from_failure(self, error, solution):
        """Store lesson from failure"""
        pass


# ============================================================================
# Q10: SYSTEM DESIGN - Scalable Agent Architecture
# ============================================================================
# Question: Design scalable multi-agent system

def design_scalable_agent_system():
    """
    ⭐⭐⭐ Hard
    Design architecture for many agents and many tasks
    
    Considerations:
    1. Scalability: Handle thousands of agents/tasks
    2. Communication: Efficient message passing
    3. Scheduling: Task distribution and load balancing
    4. Persistence: Save state, recover from failures
    5. Monitoring: Track performance and errors
    6. Cost: Minimize API and compute costs
    
    Architecture:
    ```
    User Requests
         |
         v
    Request Queue (Redis/RabbitMQ)
         |
         v
    Manager Agent (Dispatcher)
         |
    +----+----+----+
    |    |    |    |
    v    v    v    v
    Agent1 Agent2 Agent3 Agent4
    (Specialized Workers)
    
    Shared Resources:
    - Vector DB (for RAG)
    - LLM API (cached)
    - Tool API endpoints
    - Memory/Knowledge Base
    ```
    
    Components:
    1. Request Queue: Async task queue
    2. Dispatcher: Routes tasks to agents
    3. Worker Pool: Multiple agent instances
    4. Shared Cache: Reuse results
    5. Database: Persist state
    6. Monitoring: Track metrics
    
    Frameworks: CrewAI, LangGraph, Semantic Kernel
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q1: Agent thinking
def think(self, task):
    prompt = f"Given task: {task}, what should I do? Respond with action: ..."
    return self.llm(prompt)

# Q3: Tool call
def call(self, **kwargs):
    if not self.validate_parameters(**kwargs):
        raise ValueError("Missing parameters")
    return self.execute(**kwargs)

# Q7: Reasoning loop
def agent_reasoning_loop(task, llm_func, max_iterations=10):
    observations = []
    state = {"task": task, "status": "thinking"}
    
    for i in range(max_iterations):
        # Think
        thought_prompt = f"Current: {observations}. Task: {task}. What next?"
        thought = llm_func(thought_prompt)
        
        # Check if done
        if "final answer" in thought.lower():
            return thought
        
        # Act
        action = parse_action(thought)
        result = execute_action(action)
        
        # Observe
        observations.append(f"Action: {action}, Result: {result}")
    
    return "Max iterations reached"
"""


if __name__ == "__main__":
    print("Multi-Agent Systems & System Design Questions")
    print("=" * 50)
