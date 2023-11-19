def solution(A, B):
    n = len(A)
    total_fair_indexes = 0

    # Calculate prefix sums for arrays A and B
    prefix_sum_A = [0] * (n + 1)
    prefix_sum_B = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum_A[i] = prefix_sum_A[i - 1] + A[i - 1]
        prefix_sum_B[i] = prefix_sum_B[i - 1] + B[i - 1]

    # Iterate through each index K
    for k in range(1, n):
        sum_left_A = prefix_sum_A[k]
        sum_right_A = prefix_sum_A[n] - prefix_sum_A[k]

        sum_left_B = prefix_sum_B[k]
        sum_right_B = prefix_sum_B[n] - prefix_sum_B[k]

        # Check if the conditions for fairness are met
        if sum_left_A == sum_right_A and sum_left_B == sum_right_B:
            total_fair_indexes += 1

    return total_fair_indexes

# Test cases
print(solution([0, 4, -1, 0, 3], [0, -2, 5, 0, 3]))  # Output: 2
print(solution([2, -2, -3, 3], [0, 0, 4, -4]))       # Output: 1
print(solution([4, -1, 0, 3], [-2, 6, 0, 4]))         # Output: 0
print(solution([3, 2, 6], [4, 1, 6]))                 # Output: 0
print(solution([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))  # Output: 2
