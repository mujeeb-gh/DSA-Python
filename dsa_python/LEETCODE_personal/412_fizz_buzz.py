from typing import List

# Time Complexity --> O(n)
# Space Complexity --> O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.result = []
        for i in range(1, n+1):
            if i%3 == 0 and i%5 ==0:
                self.result.append('FizzBuzz')
            elif i%3 == 0:
                self.result.append('Fizz')
            elif i%5 == 0:
                self.result.append('Buzz')
            else:
                self.result.append(str(i))
        return self.result
      

# print(fizzBuzz(15))