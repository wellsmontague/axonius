import csv
import random
import string

# Predefined lists of first and last names
first_names = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Hank", "Irene", "John", "Karen", "Leo", "Mona", "Nick", "Olive", "Paul", "Quincy", "Rose", "Sam", "Tina", "Uma", "Vince", "Wendy", "Xavier", "Yolanda", "Zane"] * 4
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter"] * 2
nouns = ["apple", "ball", "cat", "dog", "elephant", "fish", "giraffe", "hat", "ice", "jug", "kite", "lamp", "monkey", "nut", "orange", "penguin", "quilt", "rabbit", "snake", "turtle", "umbrella", "vase", "whale", "xylophone", "yacht", "zebra"]

def generate_random_id():
    return ''.join(random.choices(string.digits, k=8))

def generate_endpoint_name():
    return random.choice(nouns) + str(random.randint(100, 999))

def generate_data(num_rows):
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'firstname', 'id', 'lastname', 'mail', 'name', 'endpointname', 'username'])

        for _ in range(num_rows):
            firstname = random.choice(first_names)
            lastname = random.choice(last_names)
            domain = "ad.wellsmontague.net"  # Typical AD domain format
            id = generate_random_id()
            endpointname = generate_endpoint_name()
            mail = f"{firstname.lower()}.{lastname.lower()}@wellsmontague.net"
            username = f"{firstname[0].lower()}{lastname.lower()}"
            name = f"{firstname} {lastname}"

            writer.writerow([domain, firstname, id, lastname, mail, name, endpointname, username])

if __name__ == "__main__":
    num_rows = int(input("Enter the number of rows desired for the CSV file: "))
    generate_data(num_rows)
    print(f"CSV file with {num_rows} rows has been generated successfully.")

