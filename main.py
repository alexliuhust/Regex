# https://www.youtube.com/watch?v=K8L6KVGG-7o

import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
coreymsbcom
coreyms_com
    com
321055504321
321-555-4321
123.555.1234
123*555*1234
800-555-1234
934-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
dat
sat
bat
'''

sentence = 'Start a sentence and then ' \
           'bring it to an end'

pattern = re.compile(
    r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# matches = pattern.search(sentence)

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)



