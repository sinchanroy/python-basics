from module import parse

def inFunc():
    print("in Function")
    flag = parse.parser()
    print("returned from parser")
    print(flag)
    return True

if __name__ == '__main__':
    print("in main")
    flag = inFunc()
    if flag is True:
        print("everything went well")
    else:
        print("there is problem")





