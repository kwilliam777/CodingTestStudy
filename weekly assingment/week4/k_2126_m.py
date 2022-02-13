class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        curr = mass
        for ast in asteroids:
            if ast <= curr: curr += ast
            else: return False
        return True
        