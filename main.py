a = ['1','2','123456','1234567']
b = lambda a:[i for i in a if len(i)>5]
print(len(a[0]))