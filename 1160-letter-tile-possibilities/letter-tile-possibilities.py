class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        from collections import Counter
        
        # Count the frequency of each letter
        letter_count = Counter(tiles)
        unique_sequences = set()
        
        def backtrack(current_sequence):
            # Add the current sequence to the set if it's not empty
            if current_sequence:
                unique_sequences.add(current_sequence)
            
            # Try to add each letter to the current sequence
            for letter in letter_count:
                if letter_count[letter] > 0:  # If the letter is available
                    # Choose the letter
                    letter_count[letter] -= 1
                    # Recur with the updated sequence
                    backtrack(current_sequence + letter)
                    # Backtrack: un-choose the letter
                    letter_count[letter] += 1
        
        # Start backtracking with an empty sequence
        backtrack("")
        
        # Return the number of unique sequences
        return len(unique_sequences)