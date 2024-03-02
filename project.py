import openai

# Set your OpenAI API key here
openai.api_key = "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"

def generate_recipe(ingredients):
    prompt = f"Generate a cooking recipe that includes {', '.join(ingredients)}. Provide detailed instructions and list all necessary ingredients."

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # You may need to adjust the engine based on the latest models
        prompt=prompt,
        max_tokens=300  # Adjust as needed
    )

    return response.choices[0].text.strip()

def main():
    print("Welcome to the Recipe Generator!")

    while True:
        ingredients_str = input("Enter ingredients (comma-separated): ")
        ingredients = [ingredient.strip() for ingredient in ingredients_str.split(",")]

        if not ingredients:
            print("Please enter at least one ingredient.")
            continue

        # Generate recipe
        recipe = generate_recipe(ingredients)

        # Display the generated recipe
        print("\nGenerated Recipe:")
        print(recipe)

        # Ask if the user wants to generate another recipe
        another_recipe = input("\nGenerate another recipe? (yes/no): ").lower()
        if another_recipe != 'yes':
            print("Thank you for using the Recipe Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
