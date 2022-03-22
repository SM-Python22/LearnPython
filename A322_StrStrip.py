Email1 = "abc.aaa.123@gmail.com"
Email2 = "abc_aaa@yahoo.co.in"
Email3 = "abc_______123@testing.in"
content1 = "Dear User1, welcome to the program"
content2 = "Dear SuperUser2, welcome to the program"
print(content1[content1.find(' ')+1: content1.find(',')])
print(content2[content2.find(' ')+1: content2.find(',')])
print(Email1[Email1.find('@')+1: ])
print(Email2[Email2.find('@')+1: ])
print(Email3[Email3.find('@')+1: ])
