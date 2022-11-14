# from time import sleep
# import psutil

# while True:
#     print(
#         f"RAM Usage (%): {psutil.virtual_memory().percent}",
#         f"CPU Usage (%): {psutil.cpu_percent()}",
#         f"Processes (Count): {len(psutil.pids())}",

#     )
#     net_conns = psutil.net_connections()
#     for each_conn in net_conns:
#         print(each_conn)
#     sleep(0.5)

company_list = [
    "KFC",
    "Nissan",
    "Monde",
    "Gardenia",
    "HSBC",
    "Toyota",
    "Dole",
    "Microsoft",
    "San Miguel",
    "Del Monte",
    "Canonical",
    "Ayala",
    "Udenna",
    "Magnolia",
    "ZTE",
    "BPI",
    "Atlassian",
    "Nestle",
    "Jollibee",
    "Lenovo",
    "Selecta",
    "IBM",
]

print("\nprint list of companies:\n")
print(company_list)

print("\nprint each element in the list of companies:\n")
for each_company in company_list:
    print(each_company)

print("\nsort the list of companies then print:\n")
print(sorted(company_list))

print("\nlist of companies to tuple:\n")
company_tuple = tuple(company_list)
print(company_tuple)

print("\nadd company to tuple:\n")
company_set = set(company_list)
print(company_set)
