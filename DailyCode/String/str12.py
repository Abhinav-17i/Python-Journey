s = input("Enter a string: ")

freq = {}

for ch in s:
    if ch != " ":          # ignore spaces
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

max_char = ""
max_count = 0

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_char = key

print("Most frequent character:", max_char)
print("Frequency:", max_count)
