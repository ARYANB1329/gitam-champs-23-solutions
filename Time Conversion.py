hr = int(input())
mint = input()
part = input()
if hr==12 and part=='AM':
    hr = '00'
elif hr==12 and part=='PM':
    hr = 12
elif part=='PM':
    hr += 12
print(str(hr)+":"+str(mint))
