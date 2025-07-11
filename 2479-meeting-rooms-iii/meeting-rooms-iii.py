class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        busy = []
        free = []

        meetings.sort()

        use_count = [0 for _ in range(n)]

        free = [i for i in range(n)]

        for m in meetings:

            start, end = m[0], m[1]

            # Take all the free rooms out
            while len(busy) > 0 and busy[0][0] <= start:
                heapq.heappush(free, heapq.heappop(busy)[1])

            # Determine which room the next meeting is added to
            if len(free) == 0:
                available, room = heapq.heappop(busy)
                heapq.heappush(busy, [available + end - start, room])
            else:
                room = heapq.heappop(free)
                heapq.heappush(busy, [end, room])

            use_count[room] += 1

        maxidx = 0
        max_use = use_count[0]

        for i in range(n):
            if use_count[i] > max_use:
                maxidx = i
                max_use = use_count[i]

        return maxidx