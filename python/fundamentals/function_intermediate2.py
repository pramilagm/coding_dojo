x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] =15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops
#  through each dictionary
#  in the list and prints each key and the associated value. For example, given the following list:

def iterateDictionary(some_list):
    for i in range(0,len(some_list)-1):
        for key,val in some_list[i].items():
            print(key,'-',val)
        return "don't rpint it"

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
        ]
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key
#  name, the function prints the value stored in that key for each dictionary. For example, 
#  iterateDictionary2('first_name',students) should output:

print("-----------------------------------")
def iterateDictionary2(key_name,some_list):
    for i in some_list:
        for k,v in i.items():
            if key_name==k:
                print(v)
            
iterateDictionary2("first_name",students)
print('_________________________________________')






# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, 
# prints the name of each key along with the size of its list, and then prints the associated values
#  within each key's list. For example:
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
dojo = {
   'LOCATION': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'INSTRUCTOR': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key, value in dojo.items():
        print(key)
        for i in range(len(value)):
            print(value[i])


printInfo(dojo)