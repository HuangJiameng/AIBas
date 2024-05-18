import argparse

def print_employee_card(name, age):
    card_template = f"---------------------\n"
    card_template += f"Employee Name: {name}\n"
    card_template += f"Age: {age}\n"
    card_template += "---------------------\n"
    print(card_template)

def main():
    parser = argparse.ArgumentParser(description="Prints an employee card.")
    parser.add_argument("name", help="Employee's name")
    parser.add_argument("age", type=int, help="Employee's age")

    parser.add_argument("-n", action="store", help="Number of cards to print", type=int, default=1)
    
    args = parser.parse_args()
    
    for i in range(args.n):
        print_employee_card(args.name, args.age)

if __name__ == "__main__":
    main()