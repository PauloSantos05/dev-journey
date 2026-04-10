# For loop examples

# range(start, end, step) =  generates a sequence of numbers from start to end with a specified step. The start parameter is inclusive, while the end parameter is exclusive. The step parameter determines the increment between each number in the sequence. If the step is not provided, it defaults to 1.

import time

for i in range(10, 30 + 1, 5):    
    print('i: ', i)
    
print('---')

#Print the characters of a string using a for loop
for i in "Neo The Matrix":
    print(i)
    
print('---')

for seconds in range(10, 0, -1):
    print('seconds: ', seconds)
    time.sleep(1)  # pause for 1 second between iterations