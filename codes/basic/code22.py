def PrimeCheck(n):
    if n>1:
        count=0
        for i in range(2,int(n/2)+1):
            if n%i==0:
                count+=1
                break;
        if count==0:
            print(f"{n} is a Prime Number!!!")
        else:
            print(f"{n} is not a Prime Number")
    else:
        pass

n=(int)(input("Enter a number to check if it is Prime number or not? :"))
PrimeCheck(n)
