def generate_full_half_fifth_values(base_value: int) -> tuple:
    '''Given a value generate a tuple with its
    title, full_value, half_value and fifth value.
    '''
    results_tuple = (
        base_value,
        base_value // 2,
        base_value // 5
    )
    return results_tuple
