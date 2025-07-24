#create a list
my_list = [ None, None, None,  None,  None,  None, None, None, None]

#creae a hash function 
def hash_function(value):
    sum_of_chars=0
    for char in value:
        sum_of_chars += ord(char)
#ord this is a unicode print 
        return sum_of_chars % 10

def add(name):
    index = hash_function(name)
    my_list[index] = name

add("Bob")
add('Pete')
add('Jones')
add('Lisa')
add('Siri')

def contains(name):
    index = hash_function(name)
    return my_list[index] == name

print("Pete is in the hash Table", contains("Pete"))
print("'Bob has hash code:", hash_function('Bob'))

