class Calculator:

    def __init__(self, numlist):
        self.numlist = numlist
    
    def sum(self):
        sum = 0
        for num in self.numlist:
            sum += num
        return sum
    
    def avg(self):
        return self.sum() / len(self.numlist)
    
if __name__ == '__main__':
    cal1 = Calculator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())
    cal2 = Calculator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())

