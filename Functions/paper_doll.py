# Given a string, return a string where for every character in the original there are three characters

"""
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(str1):
    lst_out = []
    for i in list(str1):
        lst_out.append(3*i)
        # print(lst_out)
    return ''.join(lst_out)


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

# Alternate code


def paper_doll_1(str1):
    str_out = ''
    for i in str1:
        str_out += 3*i
    return str_out


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
