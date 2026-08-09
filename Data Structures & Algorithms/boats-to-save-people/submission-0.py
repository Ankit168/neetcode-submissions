class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people)-1
        boat = 0
        people.sort()
        print(people)
        while i<=j:
            if (people[i]+people[j])<=limit:
                j -= 1
                i += 1
            else:
                j -= 1
            
            boat += 1
        return boat
        