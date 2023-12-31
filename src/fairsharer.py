def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration, each instance of the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iterations:
    Integer to set the number of iterations
    """
    for _ in range(num_iterations):


        highest_value = max(values)
        value_share = highest_value * share
        # Creating a copy of values for simultaneous updates
        values_new = values.copy()

        # Handling all instances of the highest value
        for index, value in enumerate(values):
            if value == highest_value:
                left_index = (index - 1) % len(values)
                right_index = (index + 1) % len(values)

                values_new[index] -= value_share * 2
                values_new[left_index] += value_share
                values_new[right_index] += value_share

        values = values_new

    return values

# Test the function
print(fair_sharer([0, 1000, 800, 0], 2))

    
print(fair_sharer([800, 0, 800, 0], 1))

