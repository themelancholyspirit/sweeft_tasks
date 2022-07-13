# The whole algorithm takes O(n) time, n being the number fed to the program by the user.
# For space, the worst-case scenario is O(n), but there might be cases where the program can take up merely O(1) space.
# Since Python 3.6, the dict data structure reserves the positions in which data was inputted, meaning we can rely upon it.


n = int(input().strip())
freq = {}

for _ in range(n):
    word = input().strip()
    freq[word] = freq.get(word, 0) + 1

print(len(freq))
print(' '.join(val for val in freq.values()))