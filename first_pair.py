
arr = [-4, -3, -2, 0, 1, 2, 5]

def find_sum_zero_pair(arr):
    
    left, right = 0, len(arr) - 1

    while left < right:

        if arr[left] + arr[right] == 0:
            print(arr[left], arr[right])
            break

        elif arr[left] + arr[right] < 0:
            left += 1
        
        elif arr[left] + arr[right] > 0:
            right -= 1

        else:
            print("No possible pairs")