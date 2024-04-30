

def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def printPrimes(bottom, top):
    nums = [i for i in range(bottom, top)]
    primes = filter(is_prime, nums)
    
    for i in primes:
        print(i)



def reverseStr(str):
    ret = " "
    for i in range(len(str) -1, -1, -1):
        ret += str[i]
    return ret

def is_palindrome(str):
    return str == reverseStr(str)


def getLongestWord(sentense):
    words = sentense.split(' ')
    maxLen = 0
    maxWord = " "
    for word in words:
        if len(word) > maxLen:
            maxLen = len(word)
            maxWord = word
    return maxWord

def checkPassword(password):
    
    score = 5 

    if len(password) < 8:
        score -= 1
    
    if not any(char.isupper() for char in password):
        score -= 1
    
    if not any(char.islower() for char in password):
        score -= 1

    if not any(char.isdigit() for char in password):
        score -= 1
    
    special_characters = "!@#$%^&*()-_+=~`[]{}|;:,.<>?/"
    if not any(char in special_characters for char in password):
        score -= 1
    
    if score < 3:
        print("weak password")
    elif score < 5:
        print('medium password')
    else:
        print('strong password')
        
        
print(reverseStr("hello world"))
printPrimes(1,100)

