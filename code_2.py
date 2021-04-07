hidden_code = "377426415375"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
date_DD = int(input("Date your birthday is on? (1-31): "))
date_MM = int(input("Birthday month? (1-12): "))
print(days[((date_DD-int(hidden_code[date_MM-1]))%7)-1])

