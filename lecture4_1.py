import sys
args = sys.argv

class lecture4_1:
    def __init__(self):
        super().__init__()

    def main(self, a, b):
        print(self.compareValue(a, b))
        otherClass = lecture4_1_2()
        print(otherClass.compareValue2(a, b))

    def compareValue(self, a, b):
        if a >= b:
            return a
        elif b > a:
            return b

tmpArgs1 = args[1]
tmpArgs2 = args[2]
lecture4_1Class = lecture4_1()
lecture4_1Class.main(tmpArgs1, tmpArgs2)