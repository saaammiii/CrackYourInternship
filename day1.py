# find dublicate no
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return nums[i]
            
#Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        st=set()
        unique_indx=0
        for i in range(len(nums)):
            if nums[i] not in st:
                st.add(nums[i])
                nums[unique_indx] = nums[i]
                unique_indx+=1
        return unique_indx
        

#  Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt=0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp=nums[i]
                nums[i]=nums[cnt]
                nums[cnt]=temp
                cnt+=1
            if nums[i]==0:
                pass
        return nums
        
