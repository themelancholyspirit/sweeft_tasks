
def lex_ord(word):
    arr = list(word)
    i = len(arr) - 1
    
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    
    if i <= 0:
        return 'no answer'

    j = len(arr) - 1

    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    arr[i:] = arr[len(arr)-1: i-1: -1]

    return ''.join(arr)

input_output = {
    'ab': 'ba',
    'bb': 'no answer',
    'hefg': 'hegf',
    'dhck': 'dhkc',
    'dkhc': 'hcdk'
}

for input in input_output:
    assert lex_ord(input) == input_output[input]