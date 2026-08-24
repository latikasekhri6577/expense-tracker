from logic import add_expense,search_expenses,calculate_total,category_wise_spending,load_expenses,save_expenses,show_menu

def main():
    expenses = load_expenses()   
    while True:
        show_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            search_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            category_wise_spending(expenses)
        elif choice == '5':
            save_expenses(expenses)
        elif choice == '6':
            save_expenses(expenses) # Auto-save on exit
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

        
