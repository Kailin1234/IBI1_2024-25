# if the input number is n
# another variable is m
# when m not equals to 0, it can enter a loop
# n+m=n, which updates the n value
# m = m-1, which update the m value
# if the updated m value still conforms to line 3, it will enter a loop again.
# if the updated m value doesn't conform, it will stop and output the result

for n in range(1,11):
    m = n-1
    while m != 0:
        n = n+m
        m -= 1
        if m == 0:
            break
    print(n)

# Result: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55