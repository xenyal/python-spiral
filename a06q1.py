import check
import math

## Question 1 

## password_check(password) produces False and prints a message if password
## violates one of the basic password rules; it produces a score and the 
## strenght of the password as a string if password does not violate one 
## of the basic rules.
## Effects: Prints a message if password violates a rule.
## password_check: Str -> (Anyof False Str)
## Examples:
## * password_check("") => False and the following is printed:
## The password ("") failed a basic test
## * password_check("Aaaa123") => "0:weak"

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

# Test examples given on the assignment
check.expect("password_check: Xy 37 1-0", password_check("Xy 37 1-0"), "35:medium")