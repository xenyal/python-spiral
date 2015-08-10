import check
import math

def password_check(password):
    # Determine the number of digits, lowercase characters, uppercase characters
    # in password (the remaining characters are 'special')
    num_digits = len(list(filter(lambda s: s.isdigit(), password)))
    num_lower  = len(list(filter(lambda s: s.islower(), password)))
    num_upper  = len(list(filter(lambda s: s.isupper(), password)))
    length     = len(password)
    num_other  = length - num_digits - num_lower - num_upper
    passed     = ((num_digits * num_lower * num_upper) > 0)
    
    if not passed:
        print ('The password ("{0}") failed a basic test'.format(password))
        return passed
    else: 
        # Start from 0
        score = 0 
        # Deduct or add points based on string length
        if length < 5:
            score -= 10
        elif length > 8:
            score += 15
        # Add 10 points for each 'special' character, other than the first 'special'
            if num_other > 1:
                score += 10 * (num_other - 1)
            # Return the result
            if score > 40:
                return str(score)+":"+"strong"
            elif score >= 20:
                return str(score)+":"+"medium"
            else:
                return str(score)+":"+"weak"