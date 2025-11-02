class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string by spaces to extract words
        words = s.split()
        
        # Step 2: Reverse the list of words
        words.reverse()
        
        # Step 3: Join them back with a single space
        return ' '.join(words)
