def dictionary(d):
    s = ""
    for key,value in d.items():
        s += key+ '=' +value+ ';'
    string = s[:-1]
    return string
n = input("Enter the number of keys: ")
print'Enter the keys and values: '
d = dict(raw_input().split() for x in range(n))
result = dictionary(d)
print result
