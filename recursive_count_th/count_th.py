'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, i=None, k=None, count=None):

    # TBC
    if i is None:
        i = 0
        k = i + 2
        count = 0
    if i != len(word):
        print('')
        print(word)
        print(word[i:k])
        if word[i:k] == 'th':
            count += 1
            i += 1
            k += 1
            return count_th(word, i, k, count)
        else:
            i += 1
            k += 1
            return count_th(word, i, k, count)
    return count
