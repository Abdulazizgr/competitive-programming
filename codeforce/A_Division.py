x = int(input())

for i in range(x):
    y = int(input())

    if 1900 <= y:
        print("Division 1")
    elif 1600 <= y <= 1899:
        print("Division 2")
    elif 1400 <= y <= 1599:
        print("Division 3")
    elif y <= 1399:
        print("Division 4")

    
#     For Division 1: 1900≤rating
# For Division 2: 1600≤rating≤1899
# For Division 3: 1400≤rating≤1599
# For Division 4: rating≤1399
    