numbers = [3,9,4,7,5,0,1,2,6,8]

def quick_sort(numbers):
    N = len(numbers)
    if N <= 1:
        return numbers
    else:
        pivot = numbers[0] # 우선 첫번째 값을 둠
        left, right = [], [] # 빈 리트를 만들어줌
        # 지금 numbers[0]인 3보다 작은애들은 left에, 큰 애들은 right에 넣어줌.

        for idx in range(1,N): # numbers[0]이 피봇의 자리니까.
            if numbers[idx] > pivot:
                right.append(numbers[idx])
            else:
                left.append(numbers[idx])
        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)
        # 지금은 [0,1,2] 3 [4,5,6,7]
        #           L   Pivot    R
        # 그냥 이렇게만 있음.

        return [*sorted_left, pivot, *sorted_right]
        # *는 언팩킹임.

print(numbers)
print(quick_sort(numbers))
