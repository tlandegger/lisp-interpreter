import functools
import math
import sys

class Lisp:
    @staticmethod
    def parse(s: str) -> int:
        stack = []
        num = ""
        func = False
        for c in s:
            if c in "1234567890":
                num += c
            elif num:
                stack.append(int(num))
                num = ""
            if c == "(":
                func = True
            elif c == "-" and not func:
                num += c
            elif c in "+-*/":
                stack.append(c)
                func = False
            elif c == ")":
                nums = []
                while stack[-1] not in ["+","-", "*", "/"]:
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
                elif opp == "/":
                    stack.append(functools.reduce(lambda x, y: int(x) // int(y), nums[::-1]))
        return stack.pop() if stack else int(num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(Lisp().parse(sys.argv[1]))
    else:
        print("call main.py with a lisp expression as a string to parse it")



