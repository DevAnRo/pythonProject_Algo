'''Exercices d'entraînement par l'utilisateur Antony Rocher via leetcode'''


def parseToRoman(number):
    decimal = [1000, 500, 100, 50, 10, 5, 1]
    roman = ["M", "D", "C", "L", "X", "V", "I"]
    longueur_decimal = len(decimal)
    roman_num = ""
    i = 0

    while number > 0:
        for _ in range(number // decimal[i]):
            roman_num = roman_num + roman[i]
            number = number - decimal[i]
        i = i + 1
    return (roman_num)


# Exemple d'utilisation
number = 300
resultat = parseToRoman(number)
print(resultat)


########################################################################################################################

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


# Exemple : Convertir 354 en chiffres romains
nombre = 354
resultat = int_to_roman(nombre)
print(resultat)


########################################################################################################################

def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            # Vérifie si le caractère est une lettre
            shift = 13  # Décalage ROT13
            if char.islower():
                # Si le caractère est en minuscule
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                # Si le caractère est en majuscule
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            # Si le caractère n'est pas une lettre, le laisse inchangé
            result += char
    return result


# Exemple d'utilisation
texte_original = "Hello, World!"
texte_chiffre = rot13(texte_original)

print(f"Texte d'origine: {texte_original}")
print(f"Texte chiffré ROT13: {texte_chiffre}")


########################################################################################################################

def reverse(text):
    # Retourne le mot à l'envers
    result = ''
    longeur_text = len(text) - 1

    for char in text:
        result = result + text[longeur_text]
        longeur_text = longeur_text - 1

    return result


# Exemple d'utilisation
texte = "bonjour antony"
print(reverse(texte))


########################################################################################################################
def est_palindrome(nombre):
    # Vérifie que l'entrée est un entier
    if not isinstance(nombre, int):
        raise ValueError("L'entrée doit être un entier")

    # Convertit le nombre en chaîne de caractères pour faciliter la comparaison
    str_nombre = str(nombre)
    # Vérifie si la chaîne est égale à sa version inversée
    if str_nombre == str_nombre[::-1]:

        return True
    else:
        return False


# Exemple d'utilisation
nombre = 15555551
print(est_palindrome(nombre))


########################################################################################################################

def fibionnacci(number):
    # Version Recursive compplixité importante niveau mémoire dépilage
    total_fib = 0
    if number <= 1:
        return 1
    else:
        total_fib = fibionnacci(number - 1) + fibionnacci(number - 2)
    return (total_fib)


# Exemple d'utilisation
nombre = 10
print(fibionnacci(nombre))


def fibonnacci_iterative(n):
    # Version itération compléxité meilleure
    premier_terme = 0
    deuxième_terme = 1
    troisième_terme = 0

    for i in range(n):
        troisième_terme = premier_terme + deuxième_terme
        premier_terme = deuxième_terme
        deuxième_terme = troisième_terme
    return (troisième_terme)


# Exemple d'utilisation
nombre = 10
print(fibionnacci(nombre))
########################################################################################################################
