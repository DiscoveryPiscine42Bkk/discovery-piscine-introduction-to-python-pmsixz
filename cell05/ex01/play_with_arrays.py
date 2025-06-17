def play_with_arrays():
    """
    defines an original array, calculates a new array by adding 2 to each element, and prints both arrays.
    """
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    new_array = [x + 2 for x in original_array]

    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

if __name__ == "__main__":
    play_with_arrays()