import math
import sys

class Lisp:
    @staticmethod
    def parse(s: str) -> int:
        stack = []
        num = ""
        for c in s:
            if c in "1234567890":
                num += c
            elif num:
                stack.append(int(num))
                num = ""
            if c in "+-*":
                stack.append(c)
            elif c == ")":
                print(stack)
                nums = []
                while stack[-1] not in ["+","-", "*"]:
                    nums.append(stack.pop())
                opp = stack.pop()
                if opp == "+":
                    stack.append(sum(nums))
                elif opp == "-":
                    nums = [n * -1 for n in nums]
                    nums[-1] *= -1
                    stack.append(sum(nums))
                elif opp == "*":
                    stack.append(math.prod(nums))
        return stack.pop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Lisp().parse(sys.argv[1]))


