l = int(input())
s = input()
ans = 0
for i in range(l):
    ans+=(ord(s[i])-96)*31**i%1234567891
print(ans%1234567891)
