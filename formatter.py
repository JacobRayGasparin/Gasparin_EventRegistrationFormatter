import datetime

first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

full_name = (first_name + " " + last_name).title()
date_obj = datetime.date(year, month, day)
formatted_date = date_obj.strftime("%B") + " " + str(date_obj.day) + ", " + str(date_obj.year)

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Event:", event_name.title())
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")
