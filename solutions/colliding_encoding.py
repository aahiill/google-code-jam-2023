# Test 1: PASS - 4 points
# Test 2: PASS - 10 points

def has_collisions(mapping, words):
    unique_encodings = set()
    for word in words:
        encoded_word = ''.join(str(mapping[letter]) for letter in word)
        if encoded_word in unique_encodings:
            return True
        unique_encodings.add(encoded_word)
    return False

# Read number of test cases
T = int(input())

# Process each test case
for t in range(1, T+1):
    mapping = {}
    digits = input().strip().split()  # Read encoding values as a list of integers
    for i in range(26):
        mapping[chr(ord('A')+i)] = digits[i]
    N = int(input())
    words = [input().strip() for _ in range(N)]
    if has_collisions(mapping, words):
        print("Case #{}: YES".format(t))
    else:
        print("Case #{}: NO".format(t))
