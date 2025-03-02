class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        id_value_map = {}

        # Process nums1
        for id_val in nums1:
            id_value_map[id_val[0]] = id_value_map.get(id_val[0], 0) + id_val[1]

        # Process nums2
        for id_val in nums2:
            id_value_map[id_val[0]] = id_value_map.get(id_val[0], 0) + id_val[1]

        # Convert the dictionary to a list of lists
        result = [[id_, value] for id_, value in id_value_map.items()]

        # Sort the result based on the id
        result.sort(key=lambda x: x[0])

        return result