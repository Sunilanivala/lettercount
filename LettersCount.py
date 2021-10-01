import pprint
def letterCount(message):
    count = {}
    for i in message:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return  count
msg = input("Write Something !!! : ")
pprint.pprint(letterCount(msg))
