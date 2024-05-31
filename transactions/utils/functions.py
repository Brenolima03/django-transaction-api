def validate_credit_card(number):
    """
    Validate a credit card number using the Luhn algorithm.
    
    Args:
    number (str): The credit card number as a string.
    
    Returns:
    bool: True if the credit card number is valid, False otherwise.
    """
    # Remove any spaces from the input
    number = number.replace(" ", "")
    if not number.isdigit() or len(number) != 16:
        return False

    total = 0
    reverse_digits = number[::-1]

    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0
