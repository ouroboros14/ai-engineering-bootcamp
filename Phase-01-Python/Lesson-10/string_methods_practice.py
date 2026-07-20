sentence = input("Enter a sentence of your choice: ")

print()
original_sentence = print(f"Original sentence: {sentence}")
uppercase_sentence = print(f"Uppercase sentence: {sentence.upper()}")
lowercase_sentence = print(f"Lowercase sentence: {sentence.lower()}")
original_sentence_again = print(f"Original sentence again: {sentence}")
processed_sentence = print(f"Processed sentence: {sentence.upper().lower().upper()}")
print(sentence == uppercase_sentence)

print()
lowercase_without_lower = print(f"Lowercase sentence without lower(): {sentence.replace('A', 'a').replace('B', 'b').replace('C', 'c').replace('D', 'd').replace('E', 'e').replace('F', 'f').replace('G', 'g').replace('H', 'h').replace('I', 'i').replace('J', 'j').replace('K', 'k').replace('L', 'l').replace('M', 'm').replace('N', 'n').replace('O', 'o').replace('P', 'p').replace('Q', 'q').replace('R', 'r').replace('S', 's').replace('T', 't').replace('U', 'u').replace('V', 'v').replace('W', 'w').replace('X', 'x').replace('Y', 'y').replace('Z', 'z')}")