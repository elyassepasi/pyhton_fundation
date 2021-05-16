# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]

# x[1][0]=15
# print(x)

# students[0]['last_name']='Brynat'
# print(students)

# sports_directory['soccer'][0]='Andres'
# print(sports_directory)

# z[0]['y']=30
# print(z)



students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
# there are some power moves here
# find all the logic you understand, look up what you don't
# ask if you don't quite get it
# def iterate_dictionary(some_list):
#     for curr_dict in some_list:
#         display_str = ''
#     for curr_key in curr_dict.keys():
#         display_str += f"{curr_key} - {curr_dict[curr_key]}, "
#     # remove comma and extra space from display_str
#         display_str = display_str[:len(display_str) - 2]
#         print(display_str)

# iterate_dictionary(students)



# def iterate_dictionary2(key, some_list):
#     for curr_dict in some_list:
#         print(curr_dict[key])

# iterate_dictionary2('first_name', students)
# iterate_dictionary2('last_name', students)

# dojo = {
#     'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#     'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def print_info(some_dict):
#     for key in some_dict.keys():
#         print(f"{len(some_dict[key])} {key.upper()}")
#     for item in some_dict[key]:
#         print(item)
#     # this prints a new line
#     print('\n')

# print_info(dojo)












x = [ [5,2,3], [10,8,9] ] 
student = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
#print(x)
student[0]['last_name']='Byren'
#print(student)
sports_directory['soccer'][0]='elyas'
#print(sports_directory)
z[0]['y']=40
#print(z)



def iterateDictionary(listname):
    for names in listname:
        for keys in names:
            print(keys,'-',str(names[keys]))
        
    
iterateDictionary(students)



def iterateDictionary2(key_name='',list_name=''):
    #print(key_name,list_name)
    for name in list_name:
        for keyname in name:
            if keyname==key_name:
                print(keyname,'-',name[keyname])

iterateDictionary2(key_name="last_name",list_name=student)




dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    
    for x,y in some_dict.items():
        leg=len(y)
        print(leg,x)
        for i in y:
            print(i)
    

printInfo(dojo)