ai_companies = ("OpenAI", "DeepMind", "Anthropic", "Cohere", "MetaAI")

print(f"List of AI companies: {ai_companies}")
print(f"First AI company: {ai_companies[0]}")
print(f"Last AI company: {ai_companies[-1]}")
print(f"Total number of AI companies: {len(ai_companies)}")

ai_companies[1] = "Google DeepMind"  # This will raise a TypeError because tuples are immutable.

numbers = (67, 69, 420)
print(f"The sum of the numbers in the tuple is: {numbers[0] + numbers[1] + numbers[2]}")

# A programmer should choose a tuple over a list when they want to ensure that the data cannot be modified after creation since, tuples are immutable.