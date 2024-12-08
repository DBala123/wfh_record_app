import time
from wfh_functions import every_nth2
import re

date = time.strftime("%a %b %d %Y")

days_input = input(f"For the week ending {date}, which days did you work from home this week?")
days_input = days_input.split(" ")
hrs_worked = 7.5 * len(days_input)
print(f"Hrs worked this week: {hrs_worked}")
more_hrs = input("Did you want to add more hrs? Please state 'no' or no. of hrs.")
if more_hrs == "no":
    print(f"Hrs worked this week: {hrs_worked}")
else:
    more_hrs_day = input("Which day did you want to add to?")
    total_hrs = hrs_worked + float(more_hrs)
    print(f"Hrs worked this week: {total_hrs}")

hrs_dict = {}
# hrs_dict["date"] = date

for day in days_input:
    hrs_dict[day] = 7.5
    try:
        if day == more_hrs_day:
            hrs_dict[day] = hrs_dict[day] + float(more_hrs)
    except NameError:
        continue

# Add total hrs to dictionary
if more_hrs == "no":
    hrs_dict["total"] = hrs_worked
else:
    hrs_dict["total"] = total_hrs

# Convert dictionary to a string
dict_str = ""
for key, value in hrs_dict.items():
    dict_str = dict_str + f"{key}: {value} "

# Input date & hrs into text file, delete any empty lines that may appear initially.
with open("hrs_record.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    if content.strip() == "":
        file.seek(0)
        file.truncate()
        file.write(f"{date}\n{dict_str}\n")
    else:
        file.write(f"{date}\n{dict_str}\n")


# Obtain running total of hrs worked
with open("hrs_record.txt", "r") as file:
    record = file.readlines()


if len(record) >= 2:
    record2 = every_nth2(record, 2)

    runtotal_list = []
    for string in record2:
        match = re.search(r"total: (.+)", string)
        if match:
            runtotal_list.append(float(match.group(1)))
    runtotal = sum(runtotal_list)
    print(f"Running total of hrs worked: {runtotal}")
else:
    print("Running total is 0.")




