'''
* DAILY CODING CHALLENGE
*
* DATE: 11/20/19
*
* CHALLENGE: Given a number in the form of a list of digits, return all possible permutations.
*
*            E.G.: Given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
'''


def permutation(list):

    # If there are no elements, return an empty list.
    if len(list) == 0:
        return []

    # If there is one element, return a nested list containing
    # the single element.
    elif len(list) == 1:
        return [list]

    # There are more than one elements in the list.
    else:
        perm_list = []
        for i in range(len(list)):
            j = list[i]
            remaining = list[:i] + list[i+1:]
            for p in permutation(remaining):
                perm_list.append([j] + p)
        return perm_list


'''
TESTING

EXPECTED: ['1', '2', '3', '4']
          ['1', '2', '4', '3']
          ['1', '3', '2', '4']
          ['1', '3', '4', '2']
          ['1', '4', '2', '3']
          ['1', '4', '3', '2']
          ['2', '1', '3', '4']
          ['2', '1', '4', '3']
          ['2', '3', '1', '4']
          ['2', '3', '4', '1']
          ['2', '4', '1', '3']
          ['2', '4', '3', '1']
          ['3', '1', '2', '4']
          ['3', '1', '4', '2']
          ['3', '2', '1', '4']
          ['3', '2', '4', '1']
          ['3', '4', '1', '2']
          ['3', '4', '2', '1']
          ['4', '1', '2', '3']
          ['4', '1', '3', '2']
          ['4', '2', '1', '3']
          ['4', '2', '3', '1']
          ['4', '3', '1', '2']
          ['4', '3', '2', '1']
'''

data = list('1234')
for p in permutation(data):
    print(p)
