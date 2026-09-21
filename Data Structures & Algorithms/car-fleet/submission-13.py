class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if (len(stack) > 0 and stack[len(stack) - 1] >= time):
                pass
            else:
                stack.append(time)
        
        return len(stack)




        