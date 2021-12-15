from open_text import open_text

text_dict = open_text('flowers.txt')

name = str(input('Please enter your first and last separated by a space: ')).title()

first = name[0]

letter = first[0]

# print the desired output
print('Your first name is: {}\nYour flower name is: {}'.format(first,text_dict[letter]))
