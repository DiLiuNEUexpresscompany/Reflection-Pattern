from reflection_agent import ReflectionAgent

def test_generation():
    agent = ReflectionAgent()  # No need for api_key argument
    test_history = [{"role": "user", "content": "Generate a simple Python script"}]
    result = agent.generate(test_history)
    assert result is not None
    assert isinstance(result, str)

def test_reflection():
    agent = ReflectionAgent() 
    test_content = "Sample Python code that needs review."
    test_history = [{"role": "user", "content": test_content}]
    critique = agent.reflect(test_content, test_history)
    
    # Check for more general terms related to feedback
    assert any(word in critique.lower() for word in ["improvement", "feedback", "suggestions"]), \
        f"Unexpected critique response: {critique}"

def test_full_loop():
    agent = ReflectionAgent()  
    result = agent.run(
        user_msg="Test prompt",
        generation_system_prompt="Test generation",
        reflection_system_prompt="Test reflection",
        n_steps=2
    )
    assert result is not None
