print("Please input something")
user_input = input()
print(user_input[1:-1])
arr = []
for letter in user_input:
    arr.append(letter)


def is_palindrome(arr):
    if len(arr) > 1:
        return True
    else:
        if arr[0] == arr[-1]:
            return is_palindrome(arr[1:-1])
        else:
            return False


print(f'The array is "{arr}" ')

if(is_palindrome(arr) == True):
    print(f'{user_input} is a palindrome')
else:
    print(f'{user_input} is not a palindrome')
