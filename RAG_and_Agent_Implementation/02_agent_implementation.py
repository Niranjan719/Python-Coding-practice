"""
AGENT IMPLEMENTATION USING LANGCHAIN & LANGGRAPH
Production-ready code for interviews

LangChain: Framework for building LLM applications
LangGraph: Graph-based state management for agents

Time to write in interview: 40-60 minutes
Frameworks: langchain, langgraph, langchain-openai
"""

from typing import List, Dict, Any, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
import json


# ============================================================================
# PART 1: TOOL DEFINITIONS (What agent can do)
# ============================================================================

@dataclass
class Tool:
    """Tool that agent can use"""
    name: str
    description: str
    parameters: Dict[str, str]  # parameter_name: parameter_type
    execute_func: Any = None
    
    def __call__(self, **kwargs) -> str:
        """Execute tool"""
        if self.execute_func:
            return str(self.execute_func(**kwargs))
        return f"Executed {self.name} with {kwargs}"


class ToolRegistry:
    """Registry of available tools"""
    
    def __init__(self):
        self.tools: Dict[str, Tool] = {}
    
    def register(self, tool: Tool):
        """Register a tool"""
        self.tools[tool.name] = tool
    
    def get_tool(self, name: str) -> Optional[Tool]:
        """Get tool by name"""
        return self.tools.get(name)
    
    def get_tool_descriptions(self) -> str:
        """Get all tool descriptions for LLM"""
        descriptions = "Available Tools:\n"
        for name, tool in self.tools.items():
            descriptions += f"\n- {tool.name}: {tool.description}\n"
            descriptions += f"  Parameters: {json.dumps(tool.parameters, indent=2)}\n"
        return descriptions


# ============================================================================
# PART 2: AGENT STATE MANAGEMENT
# ============================================================================

@dataclass
class AgentState:
    """State maintained throughout agent execution"""
    
    # Input
    task: str
    
    # Processing
    thoughts: List[str] = field(default_factory=list)
    actions: List[Dict[str, str]] = field(default_factory=list)
    observations: List[str] = field(default_factory=list)
    
    # Output
    final_answer: Optional[str] = None
    
    # Metadata
    iteration: int = 0
    max_iterations: int = 10
    is_complete: bool = False
    
    def add_thought(self, thought: str):
        """Add agent thought"""
        self.thoughts.append(thought)
    
    def add_action(self, action: str, tool_name: str, tool_input: Dict):
        """Record action"""
        self.actions.append({
            "action": action,
            "tool": tool_name,
            "input": tool_input
        })
    
    def add_observation(self, observation: str):
        """Add observation from action"""
        self.observations.append(observation)
    
    def to_dict(self) -> Dict:
        """Convert state to dict for LLM prompt"""
        return {
            "task": self.task,
            "thoughts": self.thoughts,
            "actions": self.actions,
            "observations": self.observations,
            "iteration": self.iteration
        }


# ============================================================================
# PART 3: SIMPLE AGENT (No LangChain)
# ============================================================================

class SimpleAgent:
    """
    Basic agent that executes Think -> Act -> Observe loop
    Good for understanding agent fundamentals
    """
    
    def __init__(self, tools: ToolRegistry):
        self.tools = tools
        self.state: Optional[AgentState] = None
    
    def format_prompt(self, state: AgentState) -> str:
        """Format state into prompt for reasoning"""
        
        history = ""
        for i, (thought, action, observation) in enumerate(
            zip(state.thoughts, state.actions, state.observations)
        ):
            history += f"\nStep {i+1}:\n"
            history += f"Thought: {thought}\n"
            history += f"Action: {action['tool']}({json.dumps(action['input'])})\n"
            history += f"Observation: {observation}\n"
        
        prompt = f"""You are an AI agent. Your task is to: {state.task}

{self.tools.get_tool_descriptions()}

Use the following format for responses:

Thought: <what you should do>
Action: <tool_name>
Action Input: {{"parameter": "value"}}
Observation: <result of action>
... (repeat Thought/Action/Observation as needed)
Final Answer: <your final response>

{f"Previous steps:{history}" if history else ""}

Now continue:
Thought:"""
        
        return prompt
    
    def parse_response(self, response: str) -> Tuple[str, str, Dict]:
        """
        Parse LLM response to extract thought, action, input
        
        Returns:
            (thought, tool_name, tool_input)
        """
        # Simple parsing (real version would be more robust)
        lines = response.split('\n')
        
        thought = ""
        action = ""
        action_input = {}
        
        for line in lines:
            if line.startswith("Thought:"):
                thought = line.replace("Thought:", "").strip()
            elif line.startswith("Action:"):
                action = line.replace("Action:", "").strip()
            elif line.startswith("Action Input:"):
                try:
                    action_input = json.loads(line.replace("Action Input:", "").strip())
                except:
                    action_input = {}
        
        return thought, action, action_input
    
    def run(self, task: str, verbose: bool = True) -> str:
        """Execute agent loop"""
        
        self.state = AgentState(task=task)
        
        for iteration in range(self.state.max_iterations):
            self.state.iteration = iteration
            
            if verbose:
                print(f"\n--- Iteration {iteration + 1} ---")
            
            # Check if done
            if self.state.is_complete:
                break
            
            # Think
            prompt = self.format_prompt(self.state)
            response = self._llm_call(prompt)
            
            if verbose:
                print(f"LLM Response:\n{response}")
            
            # Parse response
            thought, action, action_input = self.parse_response(response)
            self.state.add_thought(thought)
            
            if verbose:
                print(f"Thought: {thought}")
            
            # Check if done
            if "final answer" in response.lower():
                self.state.final_answer = response
                self.state.is_complete = True
                break
            
            # Execute action
            if action and action in self.tools.tools:
                tool = self.tools.get_tool(action)
                observation = tool(**action_input)
                
                self.state.add_action(action, action, action_input)
                self.state.add_observation(observation)
                
                if verbose:
                    print(f"Action: {action}({action_input})")
                    print(f"Observation: {observation}")
            else:
                observation = f"Tool '{action}' not found. Available tools: {list(self.tools.tools.keys())}"
                self.state.add_action(action, action, action_input)
                self.state.add_observation(observation)
                
                if verbose:
                    print(f"Error: {observation}")
        
        return self.state.final_answer or "Task incomplete after max iterations"
    
    def _llm_call(self, prompt: str) -> str:
        """Simulate LLM call"""
        # In real: Use OpenAI API
        # response = client.chat.completions.create(
        #     model="gpt-4",
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return response.choices[0].message.content
        
        # Demo response
        if "search" in prompt.lower():
            return """Thought: I need to search for information
Action: search
Action Input: {"query": "example"}
Observation: Found relevant information
Final Answer: Based on the search results, the answer is..."""
        
        return "Final Answer: Task completed successfully"


# ============================================================================
# PART 4: LANGGRAPH AGENT (Production Version)
# ============================================================================

class LangGraphAgent:
    """
    Production agent using LangGraph state management
    
    LangGraph Benefits:
    - State persistence across steps
    - Visual graph representation
    - Conditional branching
    - Automatic error handling
    
    Real implementation:
    
    from langgraph.graph import StateGraph, END
    from typing import Annotated
    import operator
    
    class AgentState(TypedDict):
        task: str
        steps: Annotated[list, operator.add]
        result: str
        is_complete: bool
    
    def create_agent_graph():
        graph = StateGraph(AgentState)
        
        # Add nodes
        graph.add_node("think", think_node)
        graph.add_node("act", act_node)
        graph.add_node("observe", observe_node)
        graph.add_node("end", end_node)
        
        # Add edges
        graph.add_edge("START", "think")
        graph.add_conditional_edges(
            "think",
            decide_next_step,
            {
                "act": "act",
                "end": "end"
            }
        )
        graph.add_edge("act", "observe")
        graph.add_edge("observe", "think")
        graph.add_edge("end", END)
        
        return graph.compile()
    
    def think_node(state: AgentState) -> AgentState:
        # LLM thinking step
        return state
    
    def act_node(state: AgentState) -> AgentState:
        # Execute tool
        return state
    
    def observe_node(state: AgentState) -> AgentState:
        # Process observations
        return state
    
    def end_node(state: AgentState) -> AgentState:
        # Finalize
        return state
    
    def decide_next_step(state: AgentState) -> str:
        # Conditional routing
        return "end" if state.is_complete else "act"
    """
    
    def __init__(self):
        """Initialize LangGraph agent"""
        self.graph = None
        self.state = {}
    
    def create_graph(self):
        """Create LangGraph graph"""
        # Real implementation would use langgraph.graph.StateGraph
        # This shows the structure
        
        graph_definition = {
            "nodes": [
                {"name": "think", "type": "processing"},
                {"name": "act", "type": "action"},
                {"name": "observe", "type": "processing"},
                {"name": "decide", "type": "routing"},
                {"name": "end", "type": "terminal"}
            ],
            "edges": [
                ("START", "think"),
                ("think", "decide"),
                ("decide", "act", {"condition": "not_complete"}),
                ("decide", "end", {"condition": "complete"}),
                ("act", "observe"),
                ("observe", "think")
            ]
        }
        
        return graph_definition
    
    def run(self, task: str) -> Dict:
        """Execute agent with graph"""
        self.state = {
            "task": task,
            "steps": [],
            "result": None,
            "is_complete": False
        }
        
        # In real: self.graph.invoke(self.state)
        
        return self.state


# ============================================================================
# PART 5: LANGCHAIN AGENT (Real Production Code)
# ============================================================================

class LangChainAgent:
    """
    Production agent using LangChain
    
    Real implementation:
    
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_openai import ChatOpenAI
    from langchain_core.tools import Tool as LangChainTool
    
    def create_langchain_agent():
        # Define tools
        tools = [
            LangChainTool(
                name="Search",
                func=google_search,
                description="Search the web for information"
            ),
            LangChainTool(
                name="Calculate",
                func=calculator,
                description="Perform mathematical calculations"
            )
        ]
        
        # Create LLM
        llm = ChatOpenAI(model="gpt-4", temperature=0)
        
        # Create agent
        agent = create_react_agent(llm, tools, prompt)
        
        # Create executor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=10,
            handle_parsing_errors=True
        )
        
        return agent_executor
    
    # Usage:
    agent = create_langchain_agent()
    result = agent.invoke({"input": "What is the capital of France?"})
    print(result["output"])
    """
    
    def __init__(self):
        self.agent = None
        self.tools = []
    
    def setup(self):
        """Setup LangChain agent"""
        print("In real project:")
        print("""
        from langchain.agents import create_react_agent
        from langchain_openai import ChatOpenAI
        from langchain.callbacks import StdOutCallbackHandler
        
        llm = ChatOpenAI(model="gpt-4", temperature=0)
        
        # Create agent with tools
        agent = create_react_agent(
            llm=llm,
            tools=self.tools,
            prompt=custom_prompt
        )
        
        # Add monitoring
        executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            callbacks=[StdOutCallbackHandler()],
            verbose=True
        )
        """)


# ============================================================================
# PART 6: EXAMPLE: RESEARCH AGENT
# ============================================================================

def create_research_agent() -> SimpleAgent:
    """Create example research agent"""
    
    # Create tools
    tools = ToolRegistry()
    
    # Search tool
    def search(query: str) -> str:
        """Simulate web search"""
        return f"Search results for '{query}': Found 5 relevant articles..."
    
    search_tool = Tool(
        name="search",
        description="Search the web for information",
        parameters={"query": "string"},
        execute_func=search
    )
    tools.register(search_tool)
    
    # Read tool
    def read_document(url: str) -> str:
        """Simulate reading document"""
        return f"Document content from {url}: Lorem ipsum dolor sit amet..."
    
    read_tool = Tool(
        name="read_document",
        description="Read a document from URL",
        parameters={"url": "string"},
        execute_func=read_document
    )
    tools.register(read_tool)
    
    # Summarize tool
    def summarize(text: str) -> str:
        """Summarize text"""
        return f"Summary: {text[:100]}..."
    
    summarize_tool = Tool(
        name="summarize",
        description="Summarize text",
        parameters={"text": "string"},
        execute_func=summarize
    )
    tools.register(summarize_tool)
    
    return SimpleAgent(tools)


# ============================================================================
# USAGE IN INTERVIEW
# ============================================================================

if __name__ == "__main__":
    """
    Interview Flow:
    
    1. Explain Agent concept (2 min)
       - Think step: LLM decides what to do
       - Act step: Execute tool
       - Observe step: Process result
       - Loop until answer found
    
    2. Show Tool Registry (5 min)
       - How agents access tools
       - Tool definition
       - Parameter validation
    
    3. Explain State Management (3 min)
       - Track thoughts, actions, observations
       - Maintain history
       - Check stopping conditions
    
    4. Code SimpleAgent (15 min)
       - Show loop structure
       - Parse LLM output
       - Execute tools
    
    5. Discuss LangGraph (3 min)
       - State management framework
       - Graph-based routing
       - Production ready
    
    6. Mention LangChain (2 min)
       - Built on top of these concepts
       - Production frameworks
    
    7. Run example (5 min)
       - Show agent in action
    
    Total: 35 minutes
    """
    
    print("=" * 60)
    print("AGENT IMPLEMENTATION - INTERVIEW DEMO")
    print("=" * 60)
    
    # Create research agent
    agent = create_research_agent()
    
    # Example task
    task = "Find information about Retrieval Augmented Generation and summarize it"
    
    print(f"\nTask: {task}\n")
    
    # Run agent
    result = agent.run(task, verbose=True)
    
    print("\n" + "=" * 60)
    print("KEY CONCEPTS TO MENTION")
    print("=" * 60)
    print("""
    1. Agent Loop:
       - Thought: What should I do?
       - Action: Use a tool
       - Observation: What happened?
       - Repeat until done
    
    2. ReACT (Reasoning + Acting):
       - Generate reasoning trace
       - Dynamically choose actions
       - Observe results
       - Form next action
    
    3. Tool Calling:
       - LLM decides which tool to use
       - Agent executes tool
       - Results fed back to LLM
    
    4. State Management:
       - Track all steps
       - Maintain conversation history
       - Decide when to stop
    
    5. Error Handling:
       - Invalid tool names
       - API errors
       - Max iteration limit
       - Malformed responses
    
    6. LangChain/LangGraph:
       - Pre-built agent patterns
       - State persistence
       - Tool integration
       - Monitoring and logging
    
    7. Production Considerations:
       - Cost optimization (fewer API calls)
       - Latency (parallel tool execution)
       - Reliability (error recovery)
       - Monitoring (track agent behavior)
       - Caching (reuse results)
    """)
