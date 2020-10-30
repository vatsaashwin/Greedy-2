# // Time Complexity : O(n)
# // Space Complexity : O(n), can be reduced to O(1) if we specify hashmap of length 26 instead of defaultdict
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# By observation, Eg: 3A 2B 1C, n=2
# 1. We need to put As in place and then cooldown period in between and other letters can fit in anywahere accordingly. The max one matters. 
# 2. How to know the number of partitions? (eg.: A__A__A, here max partitions are 2)
# 3. partitions = MaxFreq-1, here: 3-1= 2
# 4. empty = n*partitions = 2*2 =4
# 5. pending(how many processes do I need to complete?) = length-MaxFreq*maxCount = 3
# 6. idle(spaces when all processes are placed and needing to cooldown) = max(0, empty - pending) = 1, as this can be negative if no idle spaces are there.
# 7. return idle+length
# Edge case? 3A 3B 2C, partitions: 2: AB_AB_AB, empty: 4 (incorrect as only two empty spaces are there. hence empty = (n-maxCount-1)*partitions= 2)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hmap = defaultdict(int)
        maxCount, maxFreq = 0,float('-inf')
        
        #calculate maxFrequency
        for ch in tasks:
            hmap[ch] += 1
            maxFreq = max(maxFreq, hmap[ch])

        #calculate maxCount
        for k,val in hmap.items():
            if hmap[k] == maxFreq:
                maxCount +=1
        
        #calculate partition, empty, pending, idle
        partition = maxFreq -1
        empty = (n-(maxCount-1))*partition
        pending = len(tasks)- maxFreq*maxCount
        idle = max(0, empty-pending)
        
        return (idle+len(tasks))
        