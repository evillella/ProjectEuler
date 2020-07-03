"""
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

factorial = {}
factorial[0] = 1
for i in range(1,10):
    factorial[i] = i*factorial[i-1]

def is_digit_factorial(num):
    if num < 3:
        return False
    total = 0
    for letter in str(num):
        total += factorial[int(letter)]
    return total == num

def get_sum_all():
    num_digits = 2
    final_answer = 0
    while int("1" + "0"*(num_digits - 1)) < num_digits*factorial[9]:
        print(num_digits,"digits")
        
        stage = [[i] for i in range(10) if factorial[i] < int("1"+"0"*num_digits)]
        for i in range(num_digits-1):
            new_stage = []
            for digits in stage:
                top = digits[-1]
                for i in range(top+1):
                    new_stage.append(digits.copy()+[i])
            stage = new_stage
        # stage is a collection of all relevant non-increasing lists of num_digits digits
#        print(stage)
        for digits in stage:
            tot = 0
            for d in digits:
                tot += factorial[d]
            if is_digit_factorial(tot):
                print(tot)
                final_answer += tot
        
        
        num_digits+=1
    return final_answer

    
if __name__ == "__main__":
    print(get_sum_all())