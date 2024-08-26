# cook your dish here
# Function to determine if Tom can catch Jerry
def can_tom_catch_jerry(test_cases):
    results = []
    for X, Y in test_cases:
        if Y > X:
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input handling
T = int(input())
test_cases = []
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

# Get results
results = can_tom_catch_jerry(test_cases)

# Output results
for result in results:
    print(result)
