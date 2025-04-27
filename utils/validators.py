# Function to validate if a number is positive
def validate_positive_number(value):
    try:
        value = float(value)
        if value <= 0:
            return False
        return True
    except ValueError:
        return False

# Function to validate product name (check if non-empty string)
def validate_non_empty_string(value):
    return bool(value and value.strip())

