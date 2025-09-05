"""
Explanation of the Corrected Code for String Compression
Let's go through the corrected code step-by-step to understand how it compresses a string by counting consecutive characters.

Problem Statement:
Given a string like "aaabbccdsa", we want to compress it such that consecutive duplicate characters are replaced by the character followed by its count. If a character appears only once consecutively, we just keep the character without the count.

Example:

Input: "aaabbccdsa"

Output: "a3b2c2dsa" (because: 'a' appears 3 times, 'b' appears 2 times, 'c' appears 2 times, 'd' appears once, and 's' and 'a' appear once each).

Step-by-Step Explanation of the Code:
1. Initial Checks:
python
if not input:
    return ""
If the input string is empty (""), we immediately return an empty string since there's nothing to compress.

2. Initialize Variables:
python
compressed = []
count = 1
compressed: This list will store the parts of the compressed string as we build it.

count: This keeps track of how many times the current character has appeared consecutively. We start with count = 1 because the first character has appeared at least once.

3. Loop Through the String:
python
for i in range(1, len(input)):
We start the loop from i = 1 (second character) because we compare the current character with the previous one (input[i-1]).

4. Compare Current and Previous Characters:
python
if input[i] == input[i-1]:
    count += 1
else:
    compressed.append(input[i-1])
    if count > 1:
        compressed.append(str(count))
    count = 1
If the current character (input[i]) is the same as the previous one (input[i-1]), we increment count.

If the current character is different:

We append the previous character (input[i-1]) to compressed.

If count > 1, we also append the count to compressed.

Reset count to 1 for the new character.

5. Handle the Last Character:
python
compressed.append(input[-1])
if count > 1:
    compressed.append(str(count))
After the loop ends, we need to handle the last character(s) in the string because the loop stops at the second last character.

We append the last character (input[-1]) to compressed.

If count > 1, we append the count as well.

6. Return the Compressed String:
python
return ''.join(compressed)
We join all the elements in compressed into a single string and return it.


"""


def compress_string(input):
    if input == "":
        return ""
        
    compressed = []
    count = 1
    for i in range(1, len(input)):
        if input[i] == input[i-1]:
            count += 1
        else:
            compressed.append(input[i-1])
            if count > 1:
                compressed.append(str(count))
            count = 1
            
    #the whole above loop was for string input index 0 to input[-2]
    
    #so for last input
    compressed.append(input[-1])
    if count > 1:
        compressed.append(str(count))
        
    return "".join(compressed)
    
input = "aaaabbbbbccddefghiiiij"

compressed_output = compress_string(input)

print(f"\nThe compressed output for {input} is {compressed_output}.")
