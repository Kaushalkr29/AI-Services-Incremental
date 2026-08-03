import json
from pathlib import Path
import sys
from agent.script import run_marketpulse



def main():
    print("=" * 50)
    print("      Welcome to AI Incremental Agent CLI")
    print("=" * 50)

    try:
        question = input("\nAsk Agent: ").strip()
        if not question:
            print("Error: Question cannot be empty.")
            sys.exit(1)

        raw_path = input("Image path (press Enter to skip): ").strip()
        image_path = raw_path if raw_path else None

        print("\n[Processing request...]")
        
        # Execute the agent workflow
        result = run_marketpulse(
        question=question,
        image_path=image_path or None
    )


        # Print structured JSON response
        print("\n--- Agent Response ---")
        print(json.dumps(result, indent=2))

    except Exception as e:
        print(f"\nExecution Error: {e}")


if __name__ == "__main__":
    main()


 