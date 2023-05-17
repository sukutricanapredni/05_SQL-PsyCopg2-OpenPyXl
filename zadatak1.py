import pandas as panda

# # l=[1,2,3,4]
# # print(l[0])
# s=panda.Series([1,2,3,4],index=['a','b','c','d'])
# print(s)
# print(s[0])
# print(s[:3])
# s1=panda.Series(['a','b','c'])
# print(s1)

# s2=panda.Series([3.5,1.6,3.14])
# print(s2)

# s3=panda.Series({'a':1,'b':2,'c':3,'d':4},index=['b','d','c','h','j'])
# print(s3)
# print(s3[:'h'])

# l=[1,2,3,4,5]
# print(l[-3:])

# print(s3[-3:])
# print(s3['c':])

# l=[1,2,3,4,5]
# l=[i+5 for i in l]

# print(l)

# s4=panda.Series([1,2,3,4,5])
# print(s4+5)

# l1=[1,2,3,4,5,6]
# l2=[1,2,3,4,5]

# l3=[2,4,6,8,10]

# s5=panda.Series(l1)
# s6=panda.Series(l2)
# print(s5+s6)

# s7=panda.Series(['QA 1.Grupa','Python','Napredni python','QA 2.Grupa'],index=['cas4','cas2','cas1','cas3'])
# print(list(s7.index))

# print(s7)

# s8=panda.Series(list(range(1,51)))
# print(s8)
# print(s8.head(10))
# print(s8.tail(15))
# print(s7['cas2'],s7['cas3'])
# print(s7.loc[['cas2','cas3']])
# print(s8.iloc[0:3])
# print(s7.sort_index(inplace=True))
# print(s7)
# print(s7.sort_values(ascending=False,inplace=True))
# print(s7)

# s=panda.Series(list(range(1,51)),index=list(range(1,51)))
# print(s)
# print(s.sum())
# print(s.product())
# print(s.mean())
# print(s.median())
# print(s.min())
# print(s.max())
# print(s.agg(['sum','product','mean','median','min','max']))

s3=panda.Series({'a':1,'b':2,'c':3,'d':4},index=['b','d','c','h','j'])
print(s3)
print(s3.dropna())
print(s3.fillna(0))

r={'Veljko':70000,'Nikola':80000,'Marijan':60000,'Ana':100000,'Milena':65000}

##1.Zadatak
##Pretvoriti recnik r u seriju (pandas.series)
s=panda.Series(r)
print(s)
##2.Zadatak
##Izvuci prosek plata svih radnika
print(s.mean())

##3.Zadatak
##izvuci medianu plata svih radnika
print(s.median())

##4.Zadatak
##Izvuci 3 radnika sa najvecim platama
print(s.sort_values().tail(3))
print(s.sort_values(ascending=False).head(3))
s.rename("Radnici",inplace=True)
print(s)
