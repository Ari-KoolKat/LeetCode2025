class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0] * (2 * n - 1)  # Initialize the result list
        used = [False] * (n + 1)     # To track used numbers

        def backtrack(index):
            if index == len(result):
                return True  # Successfully filled the sequence

            if result[index] != 0:
                return backtrack(index + 1)  # Skip if already filled

            # Try to place numbers from n down to 1
            for num in range(n, 0, -1):
                if not used[num]:
                    if num == 1:
                        result[index] = num
                        used[num] = True
                    else:
                        next_index = index + num  # The position for the second occurrence
                        if next_index < len(result) and result[next_index] == 0:
                            # Place the number
                            result[index] = num
                            result[next_index] = num
                            used[num] = True
                        else:
                            continue  # Skip if cannot place the second occurrence

                    # Recur to fill the next position
                    if backtrack(index + 1):
                        return True  # Found a valid sequence

                    # Backtrack
                    result[index] = 0
                    if num == 1:
                        used[num] = False
                    else:
                        result[next_index] = 0
                        used[num] = False

            return False  # No valid placement found

        backtrack(0)  # Start backtracking from index 0
        return result