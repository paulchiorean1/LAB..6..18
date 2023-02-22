# Paul Chiorean ID 2272166

password = input()

out = ''

for p in password:

    if p == 'i':
        out += "!"

    elif p == 'a':
        out += "@"

    elif p == 'm':
        out += "M"

    elif p == 'B':
        out += "8"

    elif p == 'o':
        out += '.'

    else:
        out += p

out = out + "q*s"

print(out)
