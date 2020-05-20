#https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        
        def partition(left,right,pivot_index):
            # 1. get pivot value 
            pivot=nums[pivot_index]
            
            # 2. move pivot to end
            nums[pivot_index],nums[right]=nums[right],nums[pivot_index]
            
            # 3. move all smaller elements to the left
            # all values left to temp_i will be smaller 
            temp_i=left
            for i in range(left,right):
                if nums[i]<pivot:
                    nums[temp_i],nums[i]=nums[i],nums[temp_i]
                    temp_i+=1
                    
            # 4. move pivot to its final place
            nums[temp_i],nums[right]=nums[right],nums[temp_i]
            
            # 5. return index of pivot in it's sorted position
            return temp_i
            
            
            
        n= len(nums)
        
        #edge cases
        if not nums:
            return -1
        if n==1:
            return nums[0]
        
        left=0
        right=n-1 
      
        # m = index of "n-kth" smallest element
        m=n-k
        
        #using left element as pivot
        pivot_index=left
        
        #return index of the pivot in it's sorted position
        sorted_index=partition(left,right,pivot_index)
        
        #iterate until mth smallest element is at it's sorted position
        while  sorted_index != m: 
            # index of mth smallest element is greater than pivots sorted index - go right
            if m>sorted_index:
                left=sorted_index+1   
            else:
            # go left
                right=sorted_index-1
            pivot_index=left
            sorted_index=partition(left,right,pivot_index)   
        return nums[m]
