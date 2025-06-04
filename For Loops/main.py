import time #ignore this
#For Loop Just repeats ( does a loop ) for a limited number of times
# rather than while loop that does for unlimited times
#For Loop - Limited Times
#While Loop - Unlimited
for i in range(10):
    print(i)
#Result will Be Numbers From 0 to 9 ( cuz for computers it startes from 0 )
# If need to count from 1 TO 10 just add (+1) with i or inside range with 10

#For Between 2 number
print()
print("For numbers between 50 to 100")
time.sleep(5)  #yep ignore it to add a gap between two results
for e in range(50,100):
    print(e)
print("Here same 50 is Inclusive , 100 is exclusive soo write 100+1 to give result upto 100") 
    
    # Example
print()
time.sleep(3)
for h in range(50,100+1):
# or print(f=1)
 print(h)
 
time.sleep(3)
print()
print(" Now for skipping a number in count-down or count-up we use a thrid argument in range with a comma :")
for a in range(1,40,2):
     #here we wrote 2 after 40 as a thrid argument , so it will skip a number in counting 
     print(a)

print("here it skipped counting by providing result as 1-3-5...... ")   

