string = list('12345')
slicy_chunk = len(string) + 1
double_string = 2 * string
string = double_string[1:slicy_chunk]
print(string)

string = list('12345')
slicy_chunk = len(string) - 1
double_string = 2 * string
string = double_string[slicy_chunk:-1]
print(string)