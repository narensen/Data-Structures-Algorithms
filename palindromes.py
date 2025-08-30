import re
word = "A man, a plan, a canal: Panama"

def palindrome_checker(word):

    word = word.replace(" ","")
    word_cleaned = re.sub(r'[^A-Za-z0-9 _-]', '', word).lower()
    print(word_cleaned)

    left, right = 0, len(word_cleaned) - 1

    while left < right:

        if word_cleaned[left] == word_cleaned[right]:
            left += 1
            right -=1

        else:
            return "Not a palindrome"
            break
    
    return "is palindrome"

print(palindrome_checker(word))


