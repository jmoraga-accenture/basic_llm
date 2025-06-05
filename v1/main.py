from src.openai_client import OpenAIClient

def main():
    try:
        # Initialize the client
        client = OpenAIClient()
        
        # Test prompt
        test_prompt = "What is the capital of France? Please provide a one-sentence answer."
        
        print("Sending test query to OpenAI API...")
        print(f"Prompt: {test_prompt}\n")
        
        # Get the response
        response = client.query(test_prompt)
        
        print("Response received:")
        print("-" * 50)
        print(response)
        print("-" * 50)
        
    except FileNotFoundError as e:
        print(f"Configuration Error: {str(e)}")
        print("\nPlease make sure to:")
        print("1. Copy config/config.json.template to config/config.json")
        print("2. Add your OpenAI API key to the config.json file")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 