from module import showUsers, users
from camelcase import CamelCase


showUsers(users)

c = CamelCase()
s = "this sentence needs camelcase"

#import modules from internet using pip instal ****
#the best place to look for them is: https://pypi.org/

camelcased = c.hump(s)
print(camelcased)