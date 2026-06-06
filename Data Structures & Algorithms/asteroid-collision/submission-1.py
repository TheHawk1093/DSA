class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0:

                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()

                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    alive = False
                    break

                else:
                    alive = False
                    break

            if alive:
                stack.append(asteroid)

        return stack
        """

        state = []

        for asteroid in asteroids:
            alive = True 
            while state and state[-1] > 0 and asteroid < 0:

                if abs(state[-1]) > abs(asteroid):
                    alive = False
                    break
                
                elif abs(state[-1]) == abs(asteroid):
                    alive = False
                    state.pop()
                    break
                
                else:
                    state.pop()
                    alive = True
            
            if alive:
                state.append(asteroid)
        return state





