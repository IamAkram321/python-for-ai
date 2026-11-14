
"""Conditional Statement: It is used to make certain decisions based on whether the condition is True of False."""
age = 18
if age >= 18:
    print("You can vote")

signal = "red"
if signal == "red":
    print("You can't go")
else:
    print("You can go")

citizen = "Nepali"
if age >= 18 and citizen=="Nepali":
    print("You can vote in Nepal")
else:
    print("You can't vote in Nepal")


is_raining = True
if is_raining:
    print("Take Umbrella")
else:
    print("Don't take Umbrella")

marks = 69
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B+")
elif marks >=60:
    print("B")
else:
    print("C")


has_id = True
has_uniform = True

if has_id:
    if has_uniform:
        print("You are an obedient student")

has_id = True
has_uniform = False

if has_id and has_uniform:
    print("You are an obedient student")

if has_id or has_uniform:
    print("This time you can enter the school but not next time.")
