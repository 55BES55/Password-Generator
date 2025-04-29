import random
password = ""
l = [
    # Großbuchstaben
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

    # Kleinbuchstaben
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',

    # Zahlen
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Sonderzeichen (häufig erlaubt)
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]
#Ein loop jenachdem wie lang das passwort sein soll hier :16
#um die zufällige auswahl immer wieder zu wiederholen
while len(password) != 16:
    r = random.choice(l)


    password = password + r



print(password)


