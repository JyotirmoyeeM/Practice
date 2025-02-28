#WAP to convert decimal to binary
N=int(input())
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
    """
    The logic used here is that whenever we try to convert an integer (+ve) integer to decimal, we divide it by 2 until we can reduce the integer to 1 or 0. Then we cumulate the remainder every time we divide and find our result. 
    """
