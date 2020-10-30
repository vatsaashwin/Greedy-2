# // Time Complexity : O(2n)
# // Space Complexity : O(n), candies array
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Compare from left side and right side. Is current >left? and curr>right? 

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        if len(ratings)==0 or ratings == None:
            return 0
        
        candies = [1]*len(ratings)
        
        #curr>left
        for x in range(1, len(ratings)):
            if ratings[x]>ratings[x-1]:
                candies[x] = candies[x-1]+1
                
        #curr>right
        for x in range(len(ratings)-2, -1, -1):
            if ratings[x]>ratings[x+1]:
                candies[x] = max(candies[x],candies[x+1]+1)
                
        output =0
        for x in candies:
            output +=x
            
        return output
        
        