
# 1. Library Book Tracker
# Lista vacía para guardar los libros
books = []

# Función para añadir un libro
def add_book(title, author, pages):
    new_book = {
        "title": title,
        "author": author,
        "pages": pages
    }
    books.append(new_book)

# Función para buscar libros por título
def find_book(title):
    found = []
    for book in books:
        if book["title"].lower() == title.lower():
            found.append(book)
    return found

# Función para mostrar todos los libros
def show_books():
    return books


# 2. Student Grade Manager
# Diccionario para guardar estudiantes y sus calificaciones
students = {}

# Añadir un nuevo estudiante (sin calificaciones aún)
def add_student(name):
    if name not in students:
        students[name] = []
    # Si ya existe, no hacemos nada

# Agregar una calificación a un estudiante
def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
    else:
        print(f"El estudiante '{name}' no existe.")

# Calcular el promedio de calificaciones de un estudiante
def get_average(name):
    if name in students and students[name]:
        grades = students[name]
        return sum(grades) / len(grades)

# 3. Restaurant Menu Editor
# Diccionario para guardar platos
menu = {}

def add_dish(name, price, available=True):
    menu[name] = {"price": price, "available": available}

def change_availability(name, available):
    if name in menu:
        menu[name]["available"] = available

def total_available_price():
    total = 0
    for dish in menu.values():
        if dish["available"]:
            total += dish["price"]
    return total

# 4. Warehouse Box Counter
# Diccionario de cajas: nombre → cantidad
boxes = {}

def add_box(name, quantity):
    boxes[name] = quantity

def update_quantity(name, quantity):
    if name in boxes:
        boxes[name] += quantity

def has_enough(name, required):
    return boxes.get(name, 0) >= required

# 5. Movie Rating System
# Diccionario de películas: nombre → lista de calificaciones
movies = {}

def add_movie(title):
    movies[title] = []

def rate_movie(title, rating):
    if title in movies and 1 <= rating <= 5:
        movies[title].append(rating)

def average_rating(title):
    if title in movies and movies[title]:
        return sum(movies[title]) / len(movies[title])
    return 0


# 6. Online Course Tracker
# Diccionario: título → {"duración": horas, "inscritos": cantidad}
courses = {}

def add_course(title, hours, enrolled):
    courses[title] = {"hours": hours, "enrolled": enrolled}

def update_enrollment(title, new_enrolled):
    if title in courses:
        courses[title]["enrolled"] = new_enrolled

def filter_by_hours(min_hours):
    result = []
    for title, data in courses.items():
        if data["hours"] >= min_hours:
            result.append(title)
    return result

# 7. To-Do List Organizer
# Lista de tareas
tasks = []

def add_task(title, priority):
    tasks.append({"title": title, "priority": priority, "done": False})

def complete_task(title):
    for task in tasks:
        if task["title"] == title:
            task["done"] = True

def filter_tasks(priority=None, done=None):
    result = []
    for task in tasks:
        if (priority is None or task["priority"] == priority) and \
           (done is None or task["done"] == done):
            result.append(task)
    return result


# 8. Digital Wallet
# Lista de gastos
expenses = []

def add_expense(category, amount):
    expenses.append({"category": category, "amount": amount})

def total_spent():
    return sum(item["amount"] for item in expenses)

def expense_percentages():
    total = total_spent()
    per_category = {}
    for item in expenses:
        cat = item["category"]
        per_category[cat] = per_category.get(cat, 0) + item["amount"]
    for cat in per_category:
        per_category[cat] = round((per_category[cat] / total) * 100, 2)
    return per_category

# 9. Pet Adoption Center
# Lista de mascotas
pets = []

def add_pet(name, species, age):
    pets.append({"name": name, "species": species, "age": age})

def find_by_species(species):
    return [pet for pet in pets if pet["species"].lower() == species.lower()]

def older_than(age):
    return [pet for pet in pets if pet["age"] > age]

# 10. Gym Membership System
# Diccionario: nombre → {"plan": string, "paid": bool}
members = {}

def register_member(name, plan):
    members[name] = {"plan": plan, "paid": True}

def change_plan(name, new_plan):
    if name in members:
        members[name]["plan"] = new_plan

def unpaid_members():
    return [name for name, info in members.items() if not info["paid"]]
