class Solution:

    def encode(self, strs: list[str]) -> str:
        # Appends [length] + [#] + [word] for every string
        encoded_str = ""
        for word in strs:
            encoded_str += f"{len(word)}#{word}"
        return encoded_str

    def decode(self, s: str) -> list[str]:
        decoded = []
        i = 0
        
        # A while loop is required to manually control the pointer index
        while i < len(s):
            # Find the position of the delimiter starting from pointer i
            j = s.find("#", i)
            
            # Extract the full length (handles 1-digit, 2-digit, etc.)
            length = int(s[i:j])
            
            # Slide the pointer right past the '#' to grab the actual word
            word_start = j + 1
            word_end = word_start + length
            decoded.append(s[word_start:word_end])
            
            # Move the pointer to the start of the next encoded block
            i = word_end
            
        return decoded
