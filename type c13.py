import random
import statistics

start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

p = random.randrange(start, stop, step)
q = random.randrange(start, stop, step)
r = random.randrange(start, stop, step)
s = random.randrange(start, stop, step)
t = random.randrange(start, stop, step)
u = random.randrange(start, stop, step)

print("Generated Numbers:")
print(p,q,r,s,t,u)

seq = (p,q,r,s,t,u)

mean = statistics.mean(seq)
median = statistics.median(seq)
mode = statistics.mode(seq)

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
