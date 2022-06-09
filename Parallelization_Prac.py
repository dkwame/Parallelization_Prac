print('Beginning Program...')

import random
import numpy
import time
import multiprocessing
from multiprocessing import get_context
import matplotlib.pyplot as plt

print('—————————————————————————Summation of two numbers——————————————————————————')
print("Hello World")
sum=0

print('Summation function running...')

def summation(enter):
  if enter=='yes':
    a=input('Provide input for 1st number:')
    a=int(a)
    b=input('Provide input for 2nd nunmber:')
    b=int(b)
    sum=a+b
    print('Final Sum =',sum)


summation('yes')
input("Press Enter to continue...")

print('——————————————————————————Parallelization of Quadratic Expression x^2 + 100x + log(x)——————————————————————————')
#Select 20 random values of x between 1 and 200,000
i= 0
x_values = []
for n in range(0,20):
  i=random.randint(1,200000)
  x_values.append(i)
start_time=time.time()
print("20 random variables between [1,200k] were selected as x:")
print("Inputs", x_values)
output_values=[]
for x in x_values:
  t=0
  t = x**2 + 100*x + numpy.log(x) + 1000
  output_values.append(t)
print("Outputs", output_values)


#Define function with which x values will pass through for future parallelization
output_values=[]
def quad(x_values):
  for x in x_values:
    output_values=[]
    t=0
    t = x**2 + 100*x + numpy.log(x) + 1000
    output_values.append(t)
print("Let's parallelize this problem using N processors and compare computation times")
input("Press Enter to continue...")
#Parallelize N processors to run above calculations and compare execution times
time_values=[]
for N in [1,2,3,4,5,6,7,8]:
  pool = multiprocessing.get_context("fork").Pool(N)
  start_time = time.time()
  pool.map(quad,(x_values,))
  pool.close()

  print(N,"Processors")
  final_time=((time.time()-start_time)*1000)
  time_values.append(final_time)
  print('Run Time:',final_time, "Milliseconds")

#Visualization of execution times as N number of processors increases
plt.xlabel('Processors')
plt.ylabel('Time in Milliseconds')
plt.bar([1,2,3,4,5,6,7,8],time_values)
plt.show()
input("Press Enter to continue...")



print('——————————————————————————Trapezoidal Approximation of 14.3x^5——————————————————————————')
#Initialize bounds and partitions for trapezoidal approximation
equation=[]
a=input('Provide an lower limit: ')
a=int(a)
b=input('Provide an upper limit: ')
b=int(b)
n=input('How many trapezoids would you like? ')
n=int(n)
bounds_n_partition=numpy.linspace(a,b,n+1)
#Run & time initial trapezoidal approximation w/o parallelization
for x in bounds_n_partition:
  f=14.3*x**5
  equation.append(f)
  q=0
  for i in equation[+1:-1]:
    q+=i
  h=(b-a)/n
  Trapsum=(h/2)*(equation[0]+equation[-1]+2*q)
print(equation)
print('Trapezoidal Summation:',Trapsum)

#Set up trapezoidal approximation for paraellelization
input('Press Enter to continue to parallelization...')
def TrapezoidalSum(enter):
  start_time=time.time()
  for x in bounds_n_partition:
    f=14.3*x**5
    equation.append(f)
  q=0
  for i in equation[+1:-1]:
    q+=i
  h=(b-a)/n
  Trapsum=(h/2)*(equation[0]+equation[-1]+2*q)

TrapezoidalSum('enter')
#Set n processors to work separate calculations simulataneously
time_values=[]
Processors = [1,2,3,4,5,6,7,8]
for N in Processors:
  pool = multiprocessing.get_context("fork").Pool(N)
  start_time = time.time()
  pool.map(TrapezoidalSum,(bounds_n_partition,))
  pool.close()
#Notice how parallelization works best with higher computations
#Compare between computation times three and three thousand trapezoids
  print(N,"Processors")
  final_time=((time.time()-start_time)*1000)
  time_values.append(final_time)
  print('Run Time:',final_time, "Milliseconds")

#Visualization of parallelization
plt.xlabel('Processors')
plt.ylabel('Time in Milliseconds')
plt.bar(Processors,time_values)
plt.show()
