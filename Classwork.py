#1
# Create constant variables
RATE = 5.0
INITIAL_BALANCE = 10000.0
TARGET = 3 * INITIAL_BALANCE

# Initialize variables used with the loop.
balance = INITIAL_BALANCE
year = 0

# Count the years required for the investment to double.
while balance < TARGET :
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

# Print the results
print("The investment tripled after", year, "years.")
'''
The investment tripled after 23 years.
'''
#2
# Create constant variables
RATE = 10.0
INITIAL_BALANCE = 10000.0
TARGET = 3 * INITIAL_BALANCE

# Initialize variables used with the loop.
balance = INITIAL_BALANCE
year = 0

# Count the years required for the investment to double.
while balance < TARGET :
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

# Print the results
print("The investment doubled after", year, "years.")
'''
The investment doubled after 12 years.
'''
#3
# Create constant variables
RATE = 5.0
INITIAL_BALANCE = 10000.0
TARGET = 2 * INITIAL_BALANCE

# Initialize variables used with the loop.
balance = INITIAL_BALANCE
year = 0

# Count the years required for the investment to double.
while balance < TARGET :
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest
    print(year)
    print(balance)
'''
 =========
1
10500.0
2
11025.0
3
11576.25
4
12155.0625
5
12762.815625
6
13400.95640625
7
14071.0042265625
8
14774.554437890625
9
15513.282159785156
10
16288.946267774414
11
17103.393581163135
12
17958.56326022129
13
18856.491423232354
14
19799.31599439397
15
20789.28179411367
'''



