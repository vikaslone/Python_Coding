# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum
# exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds
# 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(int1, int2, int3):
    out_sum = sum((int1, int2, int3))
    if out_sum <= 21:
        return out_sum
    elif out_sum <= 31 and 11 in (int1, int2, int3):
        return out_sum-10
    else:
        return 'BUST'


print(blackjack(5, 6, 7))  # --> 18
print(blackjack(9, 9, 9))  # --> 'BUST'
print(blackjack(9, 9, 11))  # --> 19
