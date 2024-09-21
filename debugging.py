import random
import logging

DEBUG_STEP = 0
logging.basicConfig(level=logging.INFO)

def generate_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]

def find_max(numbers):
    if not numbers:
        return None
    
    max_num = numbers[0]
    if DEBUG_STEP >= 1:
        # TODO: Use print statements to debug this function
        # HINT: Print the current max_num and the number being compared in each iteration
        for num in numbers[1:]:
            if num > max_num:
                max_num = num
                # ... IMPLEMENT
    
    return max_num

def sort_list(numbers):
    n = len(numbers)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if DEBUG_STEP >= 2:
                # TODO: Set a breakpoint on the line below and use stepping to debug
                comparisons += 1
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    swaps += 1
    logging.info(f"Sort completed with {comparisons} comparisons and {swaps} swaps.")
    return numbers

def calculate_average(numbers):
    if not numbers:
        return 0
    
    if DEBUG_STEP >= 3:
        # TODO: Use variable inspection to debug this function
        # HINT: Inspect 'total' and 'count' variables as you step through the code
        # ... IMPLEMENT
        return 0  # Remove this line when implementing the function
    
    return 0  # Remove this line when implementing the function

def debug_console_example():
    if DEBUG_STEP >= 4:
        # TODO: Use the debug console to evaluate the expressions below
        # HINT: Try typing these in the debug console and observe the results
        numbers = [1, 2, 3, 4, 5]
        # ... IMPLEMENT
        logging.info("Debug console step completed")

def main():
    numbers = generate_random_list(10)
    print("Original list:", numbers)

    max_num = find_max(numbers)
    print("Maximum number:", max_num)

    sorted_numbers = sort_list(numbers.copy())
    print("Sorted list:", sorted_numbers)

    average = calculate_average(numbers)
    print("Average:", average)

    debug_console_example()

if __name__ == "__main__":
    main()