from reflection_agent import ReflectionAgent

# Initialize the agent (API key is loaded from .env automatically)
agent = ReflectionAgent()

# Define prompts
generation_prompt = "You are a Python programmer tasked with generating high-quality Python code."
reflection_prompt = "You are an experienced code reviewer. Provide feedback to improve the code."

# Define user message
user_msg = "Generate a Python implementation of merge sort"

# Run the reflection loop
result = agent.run(
    user_msg=user_msg,
    generation_system_prompt=generation_prompt,
    reflection_system_prompt=reflection_prompt,
    n_steps=2
)

print("Final Result:", result)
