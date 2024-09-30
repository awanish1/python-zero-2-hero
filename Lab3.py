#For Loop Example
fruits= ["Apple","Banana","Orange"]
print("For Loop Example")
for i in fruits:
    print(i,end=" ")
print("\n")


#While Loop Example
i=1
print("While Loop Example")
while i<5:
    
    print(i,end=" ")
    #print("\n")
    i+=1
print("\n")

'''
1. Lists:
Lists are ordered collections of data elements of different data types.
Lists are mutable meaning a list can be modified anytime.
Elements can be accessed using indices.
They are defined using square bracket '[]'.
'''

#Example1 
fruits=["Apple","Banana","Orange"]
print("List Example")
print("Fruits are",fruits)

#modify lis
fruits.append("orange")
print("Modified Lists are :",fruits)

#Calculate sum of of Numbers in list
nummbers=[1,2,3,5,6,7]
sum=sum(nummbers)
print("Sum of Numbers is :",sum)

'''
2. Tuples
Tuples are also ordered collections of data elements of different data types, similar to Lists.
Elements can be accessed using indices.
Tuples are immutable meaning Tuples can't be modified once created.
They are defined using open bracket '()'.
'''

# Create a Tuple
print("Example of Tuple")
point=(6,7)
x,y=point
print(x,y)
tuple_ = ('apple', 'banana', 'cherry', 'orange')  
tuple_2= ('Mango','banana')
print(tuple_,tuple_2)

'''
3. Sets
Sets are unordered collections of immutable data elements of different data types.
Sets are mutable.
Elements can't be accessed using indices.
Sets do not contain duplicate elements.
They are defined using curly braces '{}'
'''

#Example of sets

set1={1,2,3,4,5}
print("Sets are: ",set1)
