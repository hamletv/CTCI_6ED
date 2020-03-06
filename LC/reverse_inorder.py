'''Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.'''

input = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverse_inorder(string):
    new_string = ''
    for word in string.split():
        new_string += word[::-1] + ' '
    return new_string.strip()

print(reverse_inorder(input))
