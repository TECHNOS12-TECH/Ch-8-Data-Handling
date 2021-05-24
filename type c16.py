import random
import statistics
a=random.random()
b=random.random()
c=random.random()
d=random.random()
e=random.random()
f=random.random()
print("Genrated numbers:\n",a,b,c,d,e,f)
print() # For adding space
series=a,b,c,d,e,f
mean=statistics.mean(series)
mode=statistics.mode(series)
median=statistics.median(series)
print("The Mean of Generated numbers:\n",mean)
print() 
print("The Mode of Generated numbers:\n",mode)
print()
print("The Median of Genrated numbers:\n",median)
