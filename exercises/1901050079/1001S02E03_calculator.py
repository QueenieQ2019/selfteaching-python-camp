print('输入数字开始进行计算')
a=int(input(''))
print('请选择：\n+\n-\n*\n/')
c=input('')
print('请继续输入数字')
b=int(input(''))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print('输入错误')