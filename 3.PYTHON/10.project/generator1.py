import random
import uuid

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_id():
    return str(uuid.uuid4())

def generate_name():
    return random.choice(names)

def generate_birthdate():
    year = random.randint(1970, 2005)
    month = random.randint(1, 12)
    # month_str = ""
    # if month < 10:
    #     month_str = '0'
    # month_str += str(month)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

def generate_gender():
    return random.choice(['Male', 'Female'])

def generate_address():
    city = random.choice(cities)
    street = random.randint(1, 100)
    return f"{street} {city}"

data = []
for _ in range(10):
    id = generate_id()
    name = generate_name()
    birthdate = generate_birthdate()
    gender = generate_gender()
    address = generate_address()
    
    a_user = (id, name, birthdate, gender, address)
    data.append(a_user)

for d in data:
    print(d)
