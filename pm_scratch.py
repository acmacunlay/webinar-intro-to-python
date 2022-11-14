# addend1: float = float(input('Enter 1st number: '))
# addend2: float = float(input('Enter 2nd number: '))

# sample_string = f'''
# The sum of {addend1} and {addend2} is {addend1 + addend2}.
# '''
# print(sample_string)

# cond1 = 1
# cond2 = ""

# check1 = True if cond1 > 0 else False
# check2 = True if cond2 == None else False

# print(check1 or check2)
# print(not check1)

# input_str = input('Enter a random string: ')
# print(input_str, input_str.upper(), input_str.lower())
# input_bytes = input_str.encode()
# print(input_bytes, input_bytes.decode())

# if False and True:
#     print('Conditions were met. 👍')

# elif True:
#     print('2nd conditions were met. 👍')

# else:
#     print('Conditions were not met. 😢')

# print('Executing code after the statement.')

company_list = [
    "KFC",
    "Nissan",
    "Monde",
    "Gardenia",
    "ASUS",
    "HSBC",
    "Toyota",
    "Dole",
    "Microsoft",
    "San Miguel",
    "Del Monte",
    "Canonical",
    "AWS",
    "Ayala",
    "Udenna",
    "Riot Games",
    "Magnolia",
    "Tesla",
    "Duolingo",
    "ZTE",
    "BPI",
    "Atlassian",
    "Gigabyte",
    "Nestle",
    "Jollibee",
    "Lenovo",
    "Selecta",
    "IBM",
]

# for each_company in company_list:
#     if each_company == "BPI":
#         break
#     print(each_company)

# iter_counter = 0
# iter_limit = 10
# while iter_counter <= iter_limit:
#     print(iter_counter)
#     iter_counter += 1

# try:
#     print(1 / 0)

# except ZeroDivisionError as exc:
#     print(1 / (0 + 1))

# company_list.append('Rockstar Games')
# print(sorted(company_list))

# sample_tuple = ('lorem', 'ipsum', 'dolor')
# print(sample_tuple)
# word1, word2, word3 = sample_tuple
# print(word1)
# print(word2)
# print(word3)

# sample_set = {'lorem', 'ipsum', 'dolor'}
# sample_set.add('sit')
# sample_set.add('lorem')
# set1 = sample_set
# set2 = {'sit','amet','lorem'}
# print(set1.intersection(set2))

sample_dict = {
    'lorem':0,
    'ipsum':0,
    'dolor':2,
}
# print(sample_dict)
for key, value in sample_dict.items():
    print(f'{key} -> {value}')
