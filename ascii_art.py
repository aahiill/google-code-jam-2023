# Test 1: PASS - 9 points
# Test 2: TLE - time limit exceeded

def find_nth_character(N):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alphabet)
    total_repeats = 0
    letter_index = 0
    repeat_count = 1
    
    # Calculate the number of times each letter is repeated
    while N > total_repeats:
        total_repeats += repeat_count
        letter_index = (letter_index + 1) % n
        if letter_index == 0:
            repeat_count += 1
    
    # Determine the N-th printed character
    letter_index = (letter_index + n - 1) % n
    return alphabet[letter_index]

# Read number of test cases
T = int(input())

# Loop through each test case
for t in range(1, T+1):
    N = int(input())
    result = find_nth_character(N)
    print("Case #{}: {}".format(t, result))
