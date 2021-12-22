numList = []

def dupNum(num):
    if len(num) != 10:
        print("false")
    else:
        for i in range(10):
            if num[i] not in numList:
                numList.append(num[i])
            else:
                print("false")
                return
            print("true")
            return

dupNum('0123456789')
dupNum('01234')
dupNum('01234567890')
dupNum('6789012345')
dupNum('012322456789')