user_sentence = input("Enter a sentence: ")

clean_sentence = user_sentence.strip()
print(f"Cleaned sentence: {clean_sentence}")

print(f"Character count: {len(clean_sentence)}")

number_of_spaces = clean_sentence.count(" ")
print(f"Number of spaces: {number_of_spaces}")

letter_a_count = clean_sentence.count("a") + clean_sentence.count("A")
print(f"Number of 'a' letters: {letter_a_count}")

replaced_sentence = clean_sentence.replace("Python", "AI")
print(f"Replaced sentence: {replaced_sentence}")

find_AI_in_sentence = clean_sentence.find("AI")
print(f"Index of 'AI': {find_AI_in_sentence}")

if clean_sentence.find("developer") != -1:
    print("The word 'developer' is present in the sentence.")
else:
    print("The word 'developer' is not present in the sentence.")

spaces_count = clean_sentence.count(" ")
words_count = spaces_count + 1
print(f"Number of words: {words_count}")