# Reflection Pattern Project

This project implements a **Reflection Pattern** using OpenAI's API. The Reflection Pattern involves generating, critiquing, and refining content iteratively to achieve higher quality. This method is useful for tasks like code generation, content creation, and complex decision-making, where initial output quality needs iterative improvement.

## Table of Contents
- [Background](#background)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Testing](#testing)
- [Example Output](#example-output)
- [License](#license)

## Background

The Reflection Pattern implemented in this project follows an iterative loop of:
1. **Generate**: Producing initial content based on a prompt.
2. **Reflect**: Critiquing the generated content and suggesting improvements.
3. **Revise**: Updating the content based on feedback and repeating the loop.

This approach is implemented in the `ReflectionAgent` class, which uses OpenAI's API to perform each of these steps with a large language model.

## Project Structure

```plaintext
Reflection-Pattern/
├── reflection_agent.py          # Core class implementing the Reflection Pattern
├── example.py                   # Example usage of the ReflectionAgent
├── test_reflection_pattern.py    # Unit tests for the ReflectionAgent class
├── requirements.txt             # List of dependencies
└── .env                         # Environment file storing API key (not included in version control)
```

### Files
- **reflection_agent.py**: Defines the `ReflectionAgent` class, which carries out the generate-reflect-revise loop.
- **example.py**: Demonstrates how to use the `ReflectionAgent` to generate and refine content.
- **test_reflection_pattern.py**: Contains unit tests to ensure that each method in the `ReflectionAgent` class works as expected.
- **requirements.txt**: Lists required libraries for running the project.
- **.env**: Stores sensitive information like the OpenAI API key (not included in the repository; add it locally).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Reflection-Pattern.git
   cd Reflection-Pattern
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Environment Setup

To use OpenAI's API, you'll need an API key.

1. **Create a `.env` file** in the project root and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   ```

2. **Ensure `python-dotenv` is installed** to load environment variables from `.env` files automatically.

## Usage

### Running an Example

The `example.py` file demonstrates how to use the `ReflectionAgent` to perform iterative content generation and refinement.

Run the example with:

```bash
python example.py
```

This example generates a Python implementation for merge sort, critiques it, and refines it iteratively, displaying the results at each step.

### Key Components

The `ReflectionAgent` class has three main methods:
- **`generate`**: Generates content based on the conversation history.
- **`reflect`**: Critiques the generated content, providing feedback for improvement.
- **`run`**: Orchestrates the reflection loop, iteratively generating and refining content.

## Testing

Run the unit tests to verify that the `ReflectionAgent` behaves as expected:

```bash
pytest test_reflection_pattern.py
```

### Test Cases
- **`test_generation`**: Ensures the `generate` method produces non-empty content.
- **`test_reflection`**: Verifies that the `reflect` method returns feedback containing improvement-related keywords.
- **`test_full_loop`**: Checks that the `run` method completes the reflection loop without errors.

## Example Output

After running `example.py`, you might see output like this:

```plaintext
Step 1/3
Content: "def merge_sort(arr): # Initial implementation ..."
Critique: "Consider adding comments and handling edge cases..."

Step 2/3
Content: "def merge_sort(arr): # Improved with comments and edge cases ..."
Critique: "Optimize the algorithm for performance..."

Step 3/3
Content: "def merge_sort(arr): # Final optimized version with comments..."
Final Result: "def merge_sort(arr): # Fully refined version with comments..."
```

## License

This project is licensed under the MIT License.
