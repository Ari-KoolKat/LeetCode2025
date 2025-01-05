class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        # If the brute force comes close to 32 test cases solved 
        # out of 39 we ll try to sum up the directions and 
        # apply that shifting changes at the end
        array_for_shift=[0]*(len(s)+1)
        for start,end,direction in shifts:
            if direction==1:
                array_for_shift[start]+=1
                array_for_shift[end+1]-=1
            else:
                array_for_shift[start]-=1
                array_for_shift[end+1]+=1
                
        shift_cumulat=0
        for i in range(len(s)):
            shift_cumulat+=array_for_shift[i]
            array_for_shift[i]=shift_cumulat

        resulted=[]

        for i in range(len(s)):
            new_char=chr((ord(s[i])-ord('a')+array_for_shift[i])%26+ord('a'))
            resulted.append(new_char)
        
        return ''.join(resulted)
