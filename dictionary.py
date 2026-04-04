userDetails = {'ID' : 1, 'userName' : 'Just_me'}
print(type(userDetails))
print(userDetails)

location = dict(s = 'Samtse', t = 'Thimphu', p = 'Paro')
print(location)

print(userDetails['userName'])
print(location.get('t'))

userDetails['email'] = 'justme@example.com' #adding new key-value pair to dictionary
print(userDetails)
userDetails['userName'] = 'just_me_updated' #updating the existing value
print(userDetails)

del location['p'] #deleting a ley_value pair from the dictionary
print(location)

deleted_value = userDetails.pop('email') #removing a key-value pair and storing the removed value in variable
print(deleted_value)

del_key, del_value = userDetails.popitem() #removing tge last inserted key-value pair and storing the removed key and value in seprated variable
print(f'the deleted key is {del_key} and the deleted value is {del_value}')
location.clear() #removing all key_value pairs from the dictionary
print(location)