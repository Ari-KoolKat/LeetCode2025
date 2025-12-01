class Solution(object):
    def maxRunTime(self, num_computers, batteries):
        """
        :type num_computers: int
        :type batteries: List[int]
        :rtype: int
        """
        batteries.sort()

        surplus = sum(batteries[:-num_computers])

        active_batteries = batteries[-num_computers:]
        for i in range(num_computers - 1):
            desired_runtime = surplus // (i + 1)
            if desired_runtime < active_batteries[i + 1] - active_batteries[i]:
                return active_batteries[i] + desired_runtime
            
            surplus -= (i + 1) * (active_batteries[i + 1] - active_batteries[i])

        return active_batteries[-1] + surplus // num_computers        