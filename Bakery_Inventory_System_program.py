print("Bakery Inventory System - Sweet Surrender Bakery")

           



name = input("Enter your name: ")
phone = int(input("Enter ID number: "))
password = input("Enter your password: ") 
try:
    number = int(input("Enter PIN number for ingredient management system: "))
    result = 10 / number
    if number <= 0:
        raise ValueError("Error. Invalid PIN. Must be numbers")
    
except ValueError as ve:
    print(ve)
    print(f"Access Granted, PIN is: {result} ")
except ValueError:
    print("Error. Invalid PIN. Must be a number.")
except ZeroDivisionError:
    print("Error: Can not repeat / minus PIN by 0")
else:
    print("Input was user PIN")
finally:
    print("Will execute all bakery management system")
    print("--- Available Cakes List---:")
    print("1. Cola cake")
    print("2. Fanta cake")
    print("3. Eclairs")
    print("4. Doughnuts and brioches")
    print("5. Cherry Pie")
    
def add_nrs(a,b):
    result = a+b
    print("The username I.D.", result)
    return result
def sub_nos(a,b):
    results = a+b
    print("The diff", results)
    return results
x = 53396
y = 10232
a = 5
b = 10333
sum_2nrs = add_nrs(x,y)
print("User gateway I.D. ",sum_2nrs)
print("Email: alteo0987654321@yohaa.org")

ingredients = {}  # Dictionary to store ingredient data
def add_ingredient():
    try:
        ing_id = input("Enter ingredient ID: ").strip()
        if ing_id in ingredients:
            print("Error: ingredient ID already exists!")
            return
        
        name = input("Enter Name: ").strip()
        quantity = int(input("Enter quantity: ").strip())  # Convert to integer
        category = input("Enter category: ").strip()
        calories = float(input("Enter calories: ").strip())  # Convert to float

        ingredients[ing_id] = (name, quantity, category, calories)
        print("ingredient added successfully!")
    
    except ValueError:
        print("Error: Invalid input! quantity must be an integer and calories must be a number.")
def view_ingredients():
    if not ingredients:
        print("No ingredients found!")
        return
    
    print("\ningredient List:")
    print("ID\tName\tquantity\tcategory\tcalories")
    print("-" * 50)
    
    for ing_id, details in ingredients.items():
        print(f"{ing_id}\t{details[0]}\t{details[1]}\t{details[2]}\t{details[3]}")
def search_ingredient():
            try:
                ing_id = input("Enter ingredient ID to search: ").strip()
                if ing_id in ingredients:
                    details = ingredients[ing_id]
                    print(f"\ningredient Found:\nID: {ing_id}\nName: {details[0]}\nquantity: {details[1]}\ncategory: {details[2]}\ncalories: {details[3]}")
                else:
                        print("Error: ingredient not found!")
                        print("try another ingredient!")
            except TheIngredientWasNotFound as e:
                print(f"Still was a problem finding the ingredient!!! {e}")
def update_ingredient():
    ing_id = input("Enter ingredient ID to update: ").strip()
    
    if ing_id in ingredients:
        name, quantity, category, calories = ingredients[ing_id]
        
        print("Leave blank to keep current value.")
        new_name = input(f"Enter new Name ({name}): ").strip() or name
        new_quantity = input(f"Enter new quantity ({quantity}): ").strip()
        new_category = input(f"Enter new category ({category}): ").strip() or category
        new_calories = input(f"Enter new calories ({calories}): ").strip()
        
        # Convert types if input is not empty
        quantity = int(new_quantity) if new_quantity else quantity
        calories = float(new_calories) if new_calories else calories

        ingredients[ing_id] = (new_name, quantity, new_category, calories)
        print("ingredient details updated successfully!")
    
    else:
        print("Error: ingredient not found!")
def delete_ingredient():
        try:
            ing_id = input("Enter ingredient ID to delete: ").strip()
    
            if ing_id in ingredients:
                del ingredients[ing_id]
                print("ingredient deleted successfully!")
            else:
                print("Error: ingredient not found!")
        except TheIngredientWasNotFound as e:
                print(f"Still was a problem finding the ingredient!!! {e}")
def ingredients_by_category():
    try:
            category = set(emp[2] for emp in ingredients.values())  # Extracting category names
    
            if not category:
                print("No ingredients in/with any categories found!")
                return

                for cat in category:
                    print(f"\ncategory: {cat}")
                    print("ID\tName\tquantity\tcalories")
                    print("-" * 40)
        
                for ing_id, details in ingredients.items():
                    if details[2] == cat:
                        print(f"{ing_id}\t{details[0]}\t{details[1]}\t{details[3]}")
                        
    except TheIngredientCategoryWasNotFound as e:
                print(f"Still was a problem finding the ingredient by category!!! {e}")
def average_calories():
    try:
                if not ingredients:
                        print("No ingredients found to calculate calories for!")
                return

                total_calories = sum(emp[3] for emp in ingredients.values())  # Summing salaries
                avg_calories = total_calories / len(ingredients)
    
                print(f"\naverage calories: {avg_calories:.2f}")
    except TheAverageCaloriesCouldNotBeRetrieved as e:
                print(f"Still was a problem finding the average calories!!! {e}")
while True:
        print("\ningredient management System")
        print("1. Add ingredient")
        print("2. View ingredients")
        print("3. Search ingredient")
        print("4. Update ingredient")
        print("5. Delete ingredient")
        print("6. ingredients by category")
        print("7. average calories Calculator")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_ingredient()
        elif choice == "2":
            view_ingredients()
        elif choice == "3":
            search_ingredient()
        elif choice == "4":
            update_ingredient()
        elif choice == "5":
            delete_ingredient()
        elif choice == "6":
            ingredients_by_category()
        elif choice == "7":
            average_calories()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")
        

