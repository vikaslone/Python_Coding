# Given a sentence, return a sentence with the words reverse


def str_reverse(str1):
    list1 = str1.split()
    print(list1)
    list2 = []
    cnt = len(list1)
    print(cnt)
    while cnt > 0:
        print(cnt)
        list2.append(list1[cnt-1])
        print(list2)
        cnt = cnt-1
    return ' '.join(list2)


print(str_reverse('Hello world how are you'))

# Alternate and less coding method

def str_reverse_1(str1):
    return ' '.join(str1.split()[::-1])


print(str_reverse_1('Hello world how are you'))
