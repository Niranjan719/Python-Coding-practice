"""
PROMPT ENGINEERING FOR AI/ML INTERVIEWS
⭐⭐ Medium to Hard difficulty questions

These questions test:
- Prompt template design
- Few-shot learning
- Prompt optimization
- Error handling and retries
- Structured output generation
- Multi-turn conversations
"""

# ============================================================================
# Q1: BASIC PROMPT TEMPLATE - Template Variables
# ============================================================================
# Question: Create reusable prompt templates

class PromptTemplate:
    """
    ⭐ Easy
    Basic prompt template with variable substitution
    
    Example:
    template = PromptTemplate(
        "Answer the following question about {topic}: {question}"
    )
    
    prompt = template.format(topic="AI", question="What is RAG?")
    # Output: "Answer the following question about AI: What is RAG?"
    
    Methods:
    - format(): Substitute variables
    - validate(): Check all variables provided
    """
    
    def __init__(self, template_str):
        """Initialize with template string"""
        pass
    
    def format(self, **kwargs):
        """Substitute template variables and return prompt"""
        pass
    
    def validate(self, **kwargs):
        """Check if all required variables are provided"""
        pass


# ============================================================================
# Q2: CHAT TEMPLATE - Multi-turn Conversations
# ============================================================================
# Question: Build multi-turn conversation prompts

class ChatTemplate:
    """
    ⭐⭐ Medium
    Format messages for chat-based models (ChatGPT, Claude)
    
    Message structure:
    [
        {"role": "system", "content": "You are an AI expert..."},
        {"role": "user", "content": "What is RAG?"},
        {"role": "assistant", "content": "RAG is..."},
        {"role": "user", "content": "How does it work?"}
    ]
    
    Methods:
    - add_system_message()
    - add_user_message()
    - add_assistant_message()
    - get_messages()
    
    Example:
    template = ChatTemplate()
    template.add_system_message("You are a Python expert.")
    template.add_user_message("Write a function to reverse a list.")
    messages = template.get_messages()
    """
    
    def __init__(self):
        """Initialize empty message list"""
        pass
    
    def add_system_message(self, content):
        """Add system message (sets behavior)"""
        pass
    
    def add_user_message(self, content):
        """Add user message"""
        pass
    
    def add_assistant_message(self, content):
        """Add assistant response (for context)"""
        pass
    
    def get_messages(self):
        """Return formatted messages list"""
        pass


# ============================================================================
# Q3: FEW-SHOT LEARNING - Examples in Prompts
# ============================================================================
# Question: Add examples to improve model performance

def create_few_shot_prompt(task, examples, query):
    """
    ⭐⭐ Medium
    Build few-shot learning prompt with examples
    
    Few-shot improves accuracy by showing examples
    
    Input:
    task = "Classify sentiment"
    examples = [
        {"input": "I love this!", "output": "positive"},
        {"input": "This is terrible", "output": "negative"},
        {"input": "It's okay", "output": "neutral"}
    ]
    query = "Amazing product!"
    
    Output: Formatted prompt with task, examples, and query
    
    Typical structure:
    ```
    Task: Classify sentiment
    
    Examples:
    Input: I love this!
    Output: positive
    
    Input: This is terrible
    Output: negative
    
    Input: It's okay
    Output: neutral
    
    Now classify:
    Input: Amazing product!
    Output:
    ```
    
    Why it works:
    - Models learn from examples in context
    - More efficient than fine-tuning
    - Can customize for domain
    """
    pass


# ============================================================================
# Q4: CHAIN-OF-THOUGHT PROMPTING - Step-by-Step Reasoning
# ============================================================================
# Question: Improve reasoning with step-by-step prompts

def chain_of_thought_prompt(question, task_steps=None):
    """
    ⭐⭐ Medium
    Add "think step-by-step" to improve reasoning
    
    Simple version:
    Question + "Let's think step by step."
    
    Guided version:
    Provide explicit steps to follow
    
    Input:
    question = "If John has 5 apples and gives 2 to Mary, how many does he have?"
    
    task_steps = [
        "Identify the initial quantity",
        "Identify the change",
        "Calculate the final result"
    ]
    
    Output: Prompt that guides reasoning
    
    Typical prompt:
    ```
    Solve this step by step:
    
    Step 1: Identify the initial quantity
    John has 5 apples
    
    Step 2: Identify the change
    He gives 2 apples to Mary
    
    Step 3: Calculate the final result
    5 - 2 = 3
    
    Answer: John has 3 apples
    ```
    
    Result: Better accuracy, especially for math and logic
    """
    pass


# ============================================================================
# Q5: PROMPT OPTIMIZATION - Iterative Improvement
# ============================================================================
# Question: Refine prompts based on results

def optimize_prompt_iteratively(base_prompt, test_cases, llm_func, iterations=3):
    """
    ⭐⭐ Medium
    Iteratively improve prompt based on test results
    
    Process:
    1. Start with base prompt
    2. Test on examples
    3. Identify failures
    4. Adjust prompt
    5. Repeat
    
    Input:
    base_prompt = "Classify text as spam or not spam: {text}"
    test_cases = [
        {"text": "Win free money!", "expected": "spam"},
        {"text": "Meeting at 3pm", "expected": "not spam"}
    ]
    llm_func = model.generate
    iterations = 3
    
    Output: Optimized prompt with improved accuracy
    
    Used for: Finding best phrasing, structure, examples
    """
    pass


# ============================================================================
# Q6: OUTPUT PARSING - Structured Responses
# ============================================================================
# Question: Get structured output from LLM

def create_structured_output_prompt(task, output_format, query):
    """
    ⭐⭐ Medium
    Force LLM to output in specific format
    
    Output formats:
    - JSON
    - CSV
    - Markdown table
    - Key-value pairs
    
    Input:
    task = "Extract information"
    output_format = {
        "name": "string",
        "age": "integer",
        "role": "string"
    }
    query = "John is 30 years old and is a software engineer"
    
    Prompt should be:
    ```
    Extract information from: John is 30 years old and is a software engineer
    
    Return as JSON in this format:
    {
        "name": "string",
        "age": "integer",
        "role": "string"
    }
    
    Answer:
    ```
    
    Expected output:
    {
        "name": "John",
        "age": 30,
        "role": "software engineer"
    }
    
    Tip: Ask for JSON explicitly to ensure parseable output
    """
    pass


# ============================================================================
# Q7: ROLE-BASED PROMPTING - Setting Context
# ============================================================================
# Question: Set role/persona in prompt

def create_role_based_prompt(role, context, query):
    """
    ⭐ Easy
    Set role/persona for better domain-specific responses
    
    Roles help models:
    - Use appropriate terminology
    - Focus on relevant aspects
    - Adopt correct tone
    
    Input:
    role = "Python Expert"
    context = "Function implementation"
    query = "How to optimize a loop?"
    
    Output: Prompt with role context
    
    Typical structure:
    ```
    You are a Python Expert specializing in Function implementation.
    
    Question: How to optimize a loop?
    
    Provide:
    - Correct Python syntax
    - Performance considerations
    - Best practices
    ```
    
    Roles to try:
    - "ML Engineer"
    - "Software Architect"
    - "Data Scientist"
    - "DevOps Engineer"
    """
    pass


# ============================================================================
# Q8: ERROR RECOVERY - Handling Bad Responses
# ============================================================================
# Question: Handle and recover from LLM errors

def prompt_with_error_recovery(prompt, llm_func, max_retries=3):
    """
    ⭐⭐ Medium
    Call LLM with error recovery for invalid responses
    
    Common issues:
    - Hallucinations (making up facts)
    - Format errors (wrong output format)
    - Off-topic responses
    
    Input:
    prompt = "Classify sentiment: Excellent product!"
    llm_func = model.generate
    max_retries = 3
    
    Process:
    1. Call LLM
    2. Validate response
    3. If invalid:
       - Adjust prompt with more specific instructions
       - Retry up to max_retries
    4. If still invalid, raise exception
    
    Validation checks:
    - Response matches expected format
    - Response contains keywords
    - Response length within bounds
    
    Example:
    ```
    If response doesn't match expected format:
    "Please respond with exactly one word: positive, negative, or neutral"
    ```
    """
    pass


# ============================================================================
# Q9: SYSTEM PROMPT DESIGN - Best Practices
# ============================================================================
# Question: Create effective system prompts

def create_system_prompt(role, constraints, output_format):
    """
    ⭐ Easy
    Design comprehensive system prompt
    
    Good system prompt includes:
    1. Role/persona
    2. Specific constraints
    3. Output format requirements
    4. Tone/style guidance
    5. What NOT to do
    
    Input:
    role = "AI Code Reviewer"
    constraints = [
        "Focus on security issues",
        "Report performance problems",
        "Avoid style nitpicks"
    ]
    output_format = "JSON with fields: issues, severity, fix"
    
    Output: System prompt string
    
    Example system prompt:
    ```
    You are an AI Code Reviewer expert.
    
    When reviewing code:
    - Focus ONLY on security issues
    - Report performance problems
    - Avoid style nitpicks or formatting suggestions
    - Provide specific fixes
    
    Output Format:
    {
        "issues": [...],
        "severity": "high|medium|low",
        "fix": "..."
    }
    
    Remember:
    - Don't suggest unnecessary changes
    - Prioritize security
    - Be concise and specific
    ```
    """
    pass


# ============================================================================
# Q10: PROMPT COMPOSITION - Building Complex Prompts
# ============================================================================
# Question: Combine multiple techniques

def compose_advanced_prompt(role, context, examples, task, output_format, query):
    """
    ⭐⭐ Medium
    Combine multiple prompt engineering techniques
    
    Combines:
    - Role-based prompting
    - Few-shot examples
    - Structured output
    - Chain-of-thought
    
    Input:
    role = "Data Analyst"
    context = "Business metrics analysis"
    examples = [...]
    task = "Analyze revenue decline"
    output_format = {"trend": "...", "cause": "...", "recommendation": "..."}
    query = "Why did Q2 revenue drop 15%?"
    
    Output: Sophisticated prompt that combines techniques
    
    Typical structure:
    ```
    You are a Data Analyst specializing in Business metrics analysis.
    
    Examples of similar analyses:
    [examples...]
    
    Task: Analyze revenue decline
    
    When analyzing, think step by step:
    1. Identify the trend
    2. Find potential causes
    3. Recommend actions
    
    Respond in this format:
    {
        "trend": "...",
        "cause": "...",
        "recommendation": "..."
    }
    
    Question: Why did Q2 revenue drop 15%?
    ```
    """
    pass


# ============================================================================
# SOLUTION TEMPLATE
# ============================================================================

"""
SOLUTIONS:

# Q1: Prompt Template
class PromptTemplate:
    def __init__(self, template_str):
        self.template = template_str
        import re
        self.variables = re.findall(r'{(\w+)}', template_str)
    
    def format(self, **kwargs):
        return self.template.format(**kwargs)
    
    def validate(self, **kwargs):
        return all(v in kwargs for v in self.variables)

# Q2: Chat Template
class ChatTemplate:
    def __init__(self):
        self.messages = []
    
    def add_system_message(self, content):
        self.messages.append({"role": "system", "content": content})
    
    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})
    
    def add_assistant_message(self, content):
        self.messages.append({"role": "assistant", "content": content})
    
    def get_messages(self):
        return self.messages

# Q3: Few-shot Prompt
def create_few_shot_prompt(task, examples, query):
    prompt = f"Task: {task}\\n\\n"
    
    prompt += "Examples:\\n"
    for i, example in enumerate(examples, 1):
        prompt += f"Example {i}:\\n"
        prompt += f"Input: {example['input']}\\n"
        prompt += f"Output: {example['output']}\\n\\n"
    
    prompt += f"Now solve:\\n"
    prompt += f"Input: {query}\\n"
    prompt += f"Output:"
    
    return prompt

# Q4: Chain of Thought
def chain_of_thought_prompt(question, task_steps=None):
    prompt = question + "\\n\\n"
    
    if task_steps:
        prompt += "Think step by step:\\n"
        for i, step in enumerate(task_steps, 1):
            prompt += f"Step {i}: {step}\\n"
    else:
        prompt += "Let's think step by step:"
    
    return prompt

# Q6: Structured Output
def create_structured_output_prompt(task, output_format, query):
    import json
    
    prompt = f"Task: {task}\\n\\n"
    prompt += f"Query: {query}\\n\\n"
    prompt += f"Return as JSON in this format:\\n"
    prompt += json.dumps(output_format, indent=2)
    prompt += f"\\n\\nAnswer:"
    
    return prompt
"""


if __name__ == "__main__":
    print("Prompt Engineering Questions")
    print("=" * 50)
