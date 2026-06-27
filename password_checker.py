password = input("Enter your password: ")

has_upper = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_number = True
    elif not char.isalnum():
        has_symbol = True

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1

if score <= 1:
    print("Weak Password")
elif score <= 3:
    print("Medium Password")
else:
    print("Strong Password")











