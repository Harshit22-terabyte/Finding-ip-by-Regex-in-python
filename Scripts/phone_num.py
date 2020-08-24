import re

file=open('C:/Users/harshmis/PycharmProjects/Python/Scripts/data.txt','rt')
data=file.read()
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
matches=pattern.findall(data)
phone_num=[]
for match in matches:
    phone_num.append(match)

for num in phone_num:
    print(num)