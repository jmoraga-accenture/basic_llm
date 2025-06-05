#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Test script for the primary test case: land productivity boost"""

from app import ConfigManager, HOI4AIGenerator

def test_primary_case():
    """Test the primary specification requirement."""
    try:
        config_manager = ConfigManager()
        generator = HOI4AIGenerator(config_manager)
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        print("Please ensure config/config.json exists with valid OpenAI API key")
        return
    
    # Primary test case from specifications
    request = "Create code to increment all the user's land productivity by 10%"
    
    print("=" * 60)
    print("TESTING PRIMARY TEST CASE")
    print("=" * 60)
    print(f"Request: {request}")
    print("-" * 60)
    
    result = generator.generate_code(request)
    
    if result['success']:
        print("✅ SUCCESS: Code generated successfully!")
        print("-" * 60)
        print("Generated Code:")
        print("-" * 60)
        print(result['code'])
        print("-" * 60)
        print(f"Script Type: {result.get('type', 'unknown')}")
        print("✅ Primary test case PASSED!")
    else:
        print("❌ FAILED: Could not generate code")
        print(f"Error: {result.get('error', 'Unknown error')}")
        print("❌ Primary test case FAILED!")
    
    print("=" * 60)

def test_additional_cases():
    """Test additional supported cases."""
    try:
        config_manager = ConfigManager()
        generator = HOI4AIGenerator(config_manager)
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return
    
    test_cases = [
        "Create an event that gives the player 100 political power",
        "Make a national focus that unlocks advanced tank technology",
        "Create a decision to improve relations with all neighbors by 25",
        "Generate code for a national spirit that increases factory output by 15%",
        "Create an event that triggers when Germany declares war on Poland"
    ]
    
    print("\nTESTING ADDITIONAL CASES")
    print("=" * 60)
    
    for i, request in enumerate(test_cases, 1):
        print(f"\nTest {i}: {request}")
        print("-" * 40)
        
        result = generator.generate_code(request)
        
        if result['success']:
            print("✅ SUCCESS")
            print(f"Type: {result.get('type', 'unknown')}")
            # Show first 200 characters of generated code
            code_preview = result['code'][:200] + "..." if len(result['code']) > 200 else result['code']
            print(f"Preview: {code_preview}")
        else:
            print("❌ FAILED")
            print(f"Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    test_primary_case()
    test_additional_cases()
    print("\n🎮 Test complete! You can now run 'python app.py' to start the web server.") 