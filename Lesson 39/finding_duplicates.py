tour = ["new york city","london","toronto","rome","london","moscow","bangkok"]
target = "london"

def linear(tour,target):
    matches = []

    for i in range(len(tour)):
        if tour[i] == target:
            matches.append(i)

    if not matches:
        ValueError(f"{target} not in list")
    else:
        return matches
    
print(linear(tour,target))