def permutations(nums):
    result = []

    def backtrack(path, remaining):
        if len(path) == len(nums):
            result.append(path.copy())
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            backtrack(path, new_remaining)
            path.pop()

    backtrack([], nums)
    return result

print(permutations([1, 2, 3]))
print(permutations([1, 2]))

def combinations(nums, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(combinations([1,2,3,4], 2))
print(combinations([1,2,3], 2))

def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

print(subsets([1,2,3]))
print(subsets([1,2]))

def binary_strings(n):
    result = []

    def backtrack(path):

        # Base case
        if len(path) == n:
            result.append("".join(path))
            return

        for choice in ['0', '1']:
            path.append(choice)
            backtrack(path)
            path.pop()

    backtrack([])
    return result

print(binary_strings(3))
print(binary_strings(2))

def binary_strings(n):
    result = []

    def backtrack(path):
        if len(path) == n:
            result.append("".join(path))
            return

        for choice in ['0', '1']:
            path.append(choice)
            backtrack(path)
            path.pop()

    backtrack([])
    return result


# Test
print(binary_strings(3))
print(binary_strings(2))

def is_safe(board, row, col, n):

    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


def solve_n_queens_with_pruning(n):
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        if row == n:
            result.append(board.copy())
            counter.solutions += 1
            return

        for col in range(n):

            if is_safe(board, row, col, n):
                board.append(col)
                backtrack(row + 1)
                board.pop()

    backtrack(0)

    counter.report()
    return result

def is_valid_board(board):
    n = len(board)

    for row1 in range(n):
        for row2 in range(row1 + 1, n):
            col1 = board[row1]
            col2 = board[row2]
            if col1 == col2:
                return False
            if abs(row1 - row2) == abs(col1 - col2):
                return False

    return True

class Counter:

    def __init__(self):
        self.total_calls = 0
        self.solutions = 0

    def report(self):
        print("Tổng số lần gọi:", self.total_calls)
        print("Số lời giải:", self.solutions)


def solve_n_queens_no_pruning(n):
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        if row == n:
            if is_valid_board(board):
                result.append(board.copy())
                counter.solutions += 1
            return

        for col in range(n):
            board.append(col)
            backtrack(row + 1)
            board.pop()

    backtrack(0)

    counter.report()
    return result

def is_safe(board, row, col, n):

    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col:
            return False
        if abs(prev_row - row) == abs(prev_col - col):
            return False

    return True


def solve_n_queens_with_pruning(n):
    counter = Counter()
    result = []
    board = []

    def backtrack(row):
        counter.total_calls += 1

        if row == n:
            result.append(board.copy())
            counter.solutions += 1
            return

        for col in range(n):

            if is_safe(board, row, col, n):
                board.append(col)
                backtrack(row + 1)
                board.pop()

    backtrack(0)

    counter.report()
    return result

import time

def print_board(solution, n):

    for row in range(n):
        for col in range(n):
            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print()


def compare_n_queens(n):

    print("=" * 50)
    print(f"So sánh N={n}")
    print("=" * 50)
    print("\n[1] Không pruning")

    start = time.time()
    result1 = solve_n_queens_no_pruning(n)
    time1 = time.time() - start

    print("Thời gian:", time1)
    print("\n[2] Có pruning")

    start = time.time()
    result2 = solve_n_queens_with_pruning(n)
    time2 = time.time() - start

    print("Thời gian:", time2)

    if time1 > time2 and time2 > 0:
            print(f"Tốc độ tang {time1/time2:.2f}x")
    else:
        print("Tốc độ: gần như tức thời (≈ 0s)")
    if result2:
        print("\nMột lời giải:")
        print_board(result2[0], n)

compare_n_queens(4)
compare_n_queens(6)

def subset_sum_basic(nums, target):
    result = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(
                i + 1,
                path,
                current_sum + nums[i]
            )
            path.pop()

    backtrack(0, [], 0)

    return result

def subset_sum_pruning(nums, target):
    nums.sort()
    result = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path.copy())
            return

        if current_sum > target:
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            if current_sum + nums[i] > target:
                break
            remaining_sum = sum(nums[i:])
            if current_sum + remaining_sum < target:
                break

            path.append(nums[i])
            backtrack(
                i + 1,
                path,
                current_sum + nums[i]
            )
            path.pop()

    backtrack(0, [], 0)

    return result