
if __name__ == "__main__":
    num = int(input())

    print("+-+")
    for i in range(num):
        for _ in range(i):
            print("  ", end = "")
        print("| |")
        
        for _ in range(i):
            print("  ", end = "")
            
        if num-1 == i: 
            print("+-+")
        else:
            print("+-+-+")        

