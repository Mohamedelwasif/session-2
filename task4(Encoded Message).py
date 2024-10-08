class MessageDecoder:
    def __init__(self, encoded_message):
        # Initialize the encoded message and extract the core part
        self.encoded_message = encoded_message
        self.core_message = self.extract_core_message()
    
    def extract_core_message(self):
        # Step 1: Extract the core part of the message: "yalpstcejorp EPUVT"
        return self.encoded_message[7:24]  # Extract the substring from the 7th to the 24th position
    
    def reverse_first_word(self):
        # Step 2: Reverse the first word: "yalpstcejorp" becomes "projectplay"
        words = self.core_message.split()
        first_word_reversed = words[0][::-1]
        return first_word_reversed
    
    def decode_second_word(self):
        # Step 3: Replace shifted vowels in the second word
        # "EPUVT": Replace E->A and U->O to get "APOVT"
        words = self.core_message.split()
        second_word = words[1]
        decoded_second_word = second_word.replace('E', 'A').replace('U', 'O')
        return decoded_second_word
    
    def get_decoded_message(self):
        # Step 4: Combine the decoded words
        first_word = self.reverse_first_word()
        second_word = self.decode_second_word()
        return f"{first_word} {second_word}"

# Instantiate the decoder with the encoded message
decoder = MessageDecoder("##$$$@!yalpstcejorp EPUVT****9887")

# Get the final decoded message
decoded_message = decoder.get_decoded_message()

# Print the final decoded message
print("Decoded Message:", decoded_message)
