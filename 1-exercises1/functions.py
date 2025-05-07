from datetime import date

# 1. 💰 Calculadora de propina  
def calculate_tip(count, percentage):
    return float(count * (percentage / 100))
print(calculate_tip(100,15))

# 2. 📏 Conversor de unidades  
def test_meters_to_kilometers(meters):
    return float(meters/1000)
print(test_meters_to_kilometers(1500))

# 3. ✉️ Generador de email empresarial 
def test_create_email(name, lastName, domain='empresa.com'):
    return f"{name.lower()}.{lastName.lower()}@{domain}"
print(test_create_email("Lucia","Gomez","empresa.com"))

# 4. 🧾 Precio con impuestos  
def test_final_price(priceBase, taxRate= 0.21):
    return float(priceBase * (taxRate) + priceBase)
print(test_final_price(100))


# 5. 🔐 Simulador de login  
def test_validate_login_success(user, password):
    return user == "admin" and password == "1234" is True


def test_validate_login_fail(user, password):
    return validate_login("user", "wrong") is False



# 6. 🧑‍💻 Generador de nombre de usuario  
def test_generate_username(name, lastName, birthday):
    return f"{name.lower()}{lastName.lower()}{str(birthday)}"

# 7. ✨ Formateador de nombres  
def test_format_name(nameComplete):
    return nameComplete.title("name complete")
print (test_format_name("juan perez"))


# 8. 🎂 Calculadora de edad  
def test_calculate_age(birthday):
    return date.today().year - birthday
# 9. 📞 Validación de número telefónico  
def test_validate_phone_valid(numero):
    return numero.startswith('+') and numero[1:].isdigit() and 10 <= len(numero[1:]) <= 15
def test_validate_phone_invalid():
    return

# 10. 🧠 Notas de estudiantes  
def test_student_average(nombre, nota1,nota2,nota3):
    if not lista_notas:
        return 0
    return round(sum(lista_notas) / len(lista_notas), 2)
print(test_student_average("Daniela",[8,9,7]))


