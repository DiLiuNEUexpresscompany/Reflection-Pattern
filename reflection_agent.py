import openai
import os
from dotenv import load_dotenv
from typing import List, Dict

# Load environment variables from .env file
load_dotenv()

class ReflectionAgent:
    def __init__(self, model: str = "gpt-4"):
        # Get the API key from environment variable
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.model = model

    def generate(self, chat_history: List[Dict]) -> str:
        """Generates initial content or revisions based on chat history."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=chat_history,
            timeout=20
        )
        return response['choices'][0]['message']['content']

    def reflect(self, content: str, chat_history: List[Dict]) -> str:
        """Provides critique and suggestions for improving content."""
        reflection_history = [
            {"role": "system", "content": "Provide feedback for improving the content."},
            {"role": "user", "content": content}
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=reflection_history
        )
        return response['choices'][0]['message']['content']

    def run(self, user_msg: str, generation_system_prompt: str, reflection_system_prompt: str, n_steps: int = 3, verbose: int = 1) -> str:
        generation_history = [{"role": "system", "content": generation_system_prompt}, {"role": "user", "content": user_msg}]
        
        try:
            for step in range(n_steps):
                # Generate
                content = self.generate(generation_history)
                
                # Reflect
                critique = self.reflect(content, generation_history)
                
                # Update history with assistant's content and user critique
                generation_history.extend([
                    {"role": "assistant", "content": content},
                    {"role": "user", "content": critique}
                ])
                
                if verbose:
                    print(f"Step {step+1}/{n_steps}")
                    print(f"Content: {content}\n")
                    print(f"Critique: {critique}\n")
                    
        except KeyboardInterrupt:
            print("\nProcess interrupted by user.")
            return "Process interrupted."
        
        return content