from datetime import date

# 1. 💰 Calculadora de propina  
def calculatePropina(count, percentage):
    return int(count * (percentage / 100))
print(calculatePropina(1500,20))

# 2. 📏 Conversor de unidades  
def metersKm(meters):
    return float(meters/1000)
print(metersKm(100))

# 3. ✉️ Generador de email empresarial 
def generateEmail(name, lastName, domain='empresa.com'):
    return f"{name.lower()}.{lastName.lower()}@{domain}"
print(generateEmail("Daniel","Gonzalez","gmail.com"))

# 4. 🧾 Precio con impuestos  
def taxPrice(priceBase, taxRate= 0.21):
    return float(priceBase * (taxRate) + priceBase)
print(taxPrice(10000))


# 5. 🔐 Simulador de login  
def login(user, password, userReal, passwordTrue):
    return user == userReal and password == passwordTrue

# 6. 🧑‍💻 Generador de nombre de usuario  
def generateUser(name, lastName, birthday):
    return f"{name.lower()}{lastName.lower()}{str(birthday)}"

# 7. ✨ Formateador de nombres  
def formatNames(nameComplete):
    return nameComplete.title()
print(formatNames("Juan Perez"))

# 8. 🎂 Calculadora de edad  
def calculateAges(birthday):
    hoy = date.today()
    edad = hoy.year - birthday.year - ((hoy.month, hoy.day) < (birthday.month, birthday.day))
    return edad
# 9. 📞 Validación de número telefónico  
def validarTelefono(numero):
    return numero.startswith('+') and numero[1:].isdigit() and 10 <= len(numero[1:]) <= 15


# 10. 🧠 Notas de estudiantes  
def promedioNotas(lista_notas):
    if not lista_notas:
        return 0
    return round(sum(lista_notas) / len(lista_notas), 2)

