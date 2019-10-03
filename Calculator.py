"""Hausaufgabe eigener Taschenrechner"""

print("Willkommen bei Deinem persönlichen Taschenrechner.")
print("Du kannst so viele Berechnungen durchführungen wie Du willst")
print("Wenn Du das Programm beenden willst, bestätige eine leere Eingabe mit ENTER.")


while True:
    try:

# Verhalten bei diverser Eingabe

        number1 = (input("Erste Zahl eingeben: "))

        if number1 == "":
            break
        else:
            number1= int(number1)
            number2=(input("Zweite Zahl eingeben: "))

            if number2 == "":
                break
            else:
                number2= int(number2)
                operator= input("Lege einen Operator fest (+,-,*,/): ")

                if operator == "":
                    break
                else:

# Berechnung

                    if operator == "+":
                        result = number1 + number2
                        print("Ergebnis: " + str(result))
                    elif operator == "-":
                        result = number1 - number2
                        print("Ergebnis: " + str(result))
                    elif operator == "*":
                        result = number1 * number2
                        print("Ergebnis: " + str(result))
                    elif operator == "/":
                        if number1 % number2 != 0:
                            print("Ergebnis: " + str(int(number1/number2)) + " Rest " + str(number1%number2))
                        else:
                            result = number1 / number2
                            print("Ergebnis: " + str(result))
                    else:
                        print("Bitte einen der angegebenen Operatoren eingeben!")

    except Exception as e:
        print()
        print("Error:")
        print(e)
        print("Bitte erneut versuchen")
        print()

print("Programm beendet!")