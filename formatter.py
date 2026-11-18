first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
year = input("Enter event year: ").strip()
month = input("Enter event month: ").strip()
day = input("Enter event day: ").strip()

full_name = (first_name + " " + last_name).title()
event_date = month + "/" + day + "/" + year

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name.upper())
print("Section:", section.upper())
print("Event:", event_name.title())
print("Event Date:", event_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: None yet")
print("Registration record created successfully."
