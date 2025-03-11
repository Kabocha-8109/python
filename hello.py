def square(z):
	print("{}的平方是{},三次方是{}". format(z,z*z,z**3))


x = int(input("請輸入一個正整數："))
print("您輸入的值",x)

if (x<0):
	print("您輸入的質小於0")
elif (x==0):
	print("您輸入的質等於0")

else:
	for i in range(1,x+1):
		square(i)