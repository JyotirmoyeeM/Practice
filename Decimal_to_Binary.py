#WAP to convert decimal to binary
N=2
ans = " "
if N==0:
    print(0)
else:
    while N>0:
        if N%2==0:
            ans = "0" + ans
        else:
            ans = "1" + ans
        N//=2
    print(ans)
