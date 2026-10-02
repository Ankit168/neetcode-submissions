class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        result = []
        
        for asteroid in asteroids:
            # Collision only occurs if the incoming asteroid is moving left (< 0)
            # and the top of the stack is moving right (> 0)
            while result and asteroid < 0 < result[-1]:
                if result[-1] < abs(asteroid):
                    result.pop()  # Top asteroid explodes, continue checking the next one
                    continue
                elif result[-1] == abs(asteroid):
                    result.pop()  # Both asteroids explode
                break            # Incoming asteroid explodes or ties, stop checking
            else:
                # Executes if the while loop finished without breaking (no collision occurred)
                result.append(asteroid)
                
        return result