# ==========================================
# Zadanie 3.4
# ==========================================
# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
# i wypisujący x oraz trzecią potęgę x.
# Zatrzymanie programu następuje po wpisaniu z klawiatury "stop".
# Jeżeli użytkownik wpisze napis zamiast liczby, to program
# ma wypisać komunikat o błędzie i kontynuować pracę.

print("=== Task 3.4 ===")

while True:
    user_input = input("Podaj liczbę rzeczywistą (lub 'stop' aby zakończyć): ")
    if user_input == "stop":
        print("Koniec programu.")
        break
    try:
        x = float(user_input)
        print(f"x = {x}, x^3 = {x ** 3}")
    except ValueError:
        print(f"Błąd: '{user_input}' nie jest liczbą rzeczywistą!")
