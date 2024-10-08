# Step 1: Extract the core part of the message "gnirtS PLIO"
encoded_message = "&&&**$gnirtS PLIO!!@1234"
core_message = encoded_message[6:16]  # Extract "gnirtS PLIO"

# Step 2: Reverse the first word "gnirtS" -> "String"
words = core_message.split()
first_word_reversed = words[0][::-1]  # Reverse the first word "gnirtS" -> "String"

# Step 3: Replace shifted vowels in the second word
# "PLIO": Replace I->E and O->U to get "PLEU"
second_word = words[1]
decoded_second_word = second_word.replace('I', 'E').replace('O', 'U')

# Step 4: Combine the decoded words
decoded_message = f"{first_word_reversed} {decoded_second_word}"

# Print the final decoded message
print("Decoded Message:", decoded_message)
