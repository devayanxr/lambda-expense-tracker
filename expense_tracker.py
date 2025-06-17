from datetime import datetime
from functools import reduce

def add_expense(expenses, amount, category, description=""):
    """Add an expense with timestamp"""
    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expenses.append(expense)
    return expenses

def print_expenses(expenses):
    """Print expenses using lambda for formatting"""
    if not expenses:
        print("No expenses found.")
        return
    
    # Lambda to format each expense
    format_expense = lambda exp: f"${exp['amount']:.2f} | {exp['category']} | {exp['date']} | {exp['description']}"
    
    print("-" * 80)
    print(f"{'Amount':<10} | {'Category':<15} | {'Date':<16} | {'Description'}")
    print("-" * 80)
    
    # Using map with lambda to format all expenses
    formatted_expenses = list(map(format_expense, expenses))
    for expense in formatted_expenses:
        print(expense)

def total_expenses(expenses):
    """Calculate total using lambda with reduce"""
    if not expenses:
        return 0
    return reduce(lambda total, expense: total + expense['amount'], expenses, 0)

def filter_expenses_by_category(expenses, category):
    """Filter expenses by category using lambda"""
    return list(filter(lambda expense: expense['category'].lower() == category.lower(), expenses))

def filter_expenses_by_amount(expenses, min_amount=0, max_amount=float('inf')):
    """Filter expenses by amount range using lambda"""
    return list(filter(lambda expense: min_amount <= expense['amount'] <= max_amount, expenses))

def get_expense_statistics(expenses):
    """Get statistics using various lambda functions"""
    if not expenses:
        return "No expenses to analyze."
    
    # Lambda functions for statistics
    get_amount = lambda expense: expense['amount']
    amounts = list(map(get_amount, expenses))
    
    stats = {
        'total': total_expenses(expenses),
        'average': sum(amounts) / len(amounts),
        'minimum': min(amounts),
        'maximum': max(amounts),
        'count': len(expenses)
    }
    
    return stats

def get_category_summary(expenses):
    """Summarize expenses by category using lambda functions"""
    if not expenses:
        return {}
    
    # Get unique categories
    categories = list(set(map(lambda expense: expense['category'], expenses)))
    
    # Create summary for each category
    summary = {}
    for category in categories:
        category_expenses = filter_expenses_by_category(expenses, category)
        summary[category] = {
            'total': sum(map(lambda exp: exp['amount'], category_expenses)),
            'count': len(category_expenses),
            'average': sum(map(lambda exp: exp['amount'], category_expenses)) / len(category_expenses)
        }
    
    return summary

def sort_expenses(expenses, key='amount', reverse=False):
    """Sort expenses using lambda functions"""
    sort_keys = {
        'amount': lambda exp: exp['amount'],
        'category': lambda exp: exp['category'].lower(),
        'date': lambda exp: exp['date'],
        'description': lambda exp: exp['description'].lower()
    }
    
    if key in sort_keys:
        return sorted(expenses, key=sort_keys[key], reverse=reverse)
    else:
        return expenses

def search_expenses(expenses, search_term):
    """Search expenses using lambda"""
    search_term = search_term.lower()
    return list(filter(
        lambda expense: search_term in expense['category'].lower() or 
                       search_term in expense['description'].lower(),
        expenses
    ))

def main():
    expenses = []
    
    # Sample data for demonstration
    sample_expenses = [
        {'amount': 50.00, 'category': 'Food', 'description': 'Groceries', 'date': '2024-01-15 10:30'},
        {'amount': 25.50, 'category': 'Transport', 'description': 'Gas', 'date': '2024-01-16 08:15'},
        {'amount': 120.00, 'category': 'Food', 'description': 'Restaurant dinner', 'date': '2024-01-16 19:45'},
        {'amount': 15.75, 'category': 'Entertainment', 'description': 'Movie ticket', 'date': '2024-01-17 20:00'}
    ]
    
    print("Welcome to the Enhanced Expense Tracker!")
    print("This tracker demonstrates various lambda function uses.")
    print("\nLoading sample data...")
    expenses.extend(sample_expenses)
    
    while True:
        print('\n' + '='*50)
        print('EXPENSE TRACKER - Lambda Functions Demo')
        print('='*50)
        print('1.  Add an expense')
        print('2.  List all expenses')
        print('3.  Show total expenses')
        print('4.  Filter expenses by category')
        print('5.  Filter expenses by amount range')
        print('6.  Show expense statistics')
        print('7.  Show category summary')
        print('8.  Sort expenses')
        print('9.  Search expenses')
        print('10. Clear all expenses')
        print('11. Exit')
        print('='*50)
       
        choice = input('Enter your choice (1-11): ').strip()

        if choice == '1':
            try:
                amount = float(input('Enter amount: $'))
                category = input('Enter category: ').strip()
                description = input('Enter description (optional): ').strip()
                add_expense(expenses, amount, category, description)
                print(f"✓ Added expense: ${amount:.2f} for {category}")
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == '2':
            print('\n📋 ALL EXPENSES:')
            print_expenses(expenses)
    
        elif choice == '3':
            total = total_expenses(expenses)
            print(f'\n💰 TOTAL EXPENSES: ${total:.2f}')
    
        elif choice == '4':
            category = input('Enter category to filter: ').strip()
            filtered = filter_expenses_by_category(expenses, category)
            print(f'\n📂 EXPENSES FOR "{category.upper()}":')
            print_expenses(filtered)
    
        elif choice == '5':
            try:
                min_amt = float(input('Enter minimum amount (or press Enter for 0): ') or '0')
                max_amt = float(input('Enter maximum amount (or press Enter for no limit): ') or 'inf')
                filtered = filter_expenses_by_amount(expenses, min_amt, max_amt)
                print(f'\n💵 EXPENSES BETWEEN ${min_amt:.2f} AND ${max_amt:.2f}:')
                print_expenses(filtered)
            except ValueError:
                print("❌ Invalid amount range.")
        
        elif choice == '6':
            stats = get_expense_statistics(expenses)
            if isinstance(stats, dict):
                print('\n📊 EXPENSE STATISTICS:')
                print(f"Total Expenses: ${stats['total']:.2f}")
                print(f"Average Expense: ${stats['average']:.2f}")
                print(f"Minimum Expense: ${stats['minimum']:.2f}")
                print(f"Maximum Expense: ${stats['maximum']:.2f}")
                print(f"Number of Expenses: {stats['count']}")
            else:
                print(stats)
        
        elif choice == '7':
            summary = get_category_summary(expenses)
            if summary:
                print('\n📈 CATEGORY SUMMARY:')
                print("-" * 60)
                print(f"{'Category':<15} | {'Total':<10} | {'Count':<7} | {'Average'}")
                print("-" * 60)
                for category, data in summary.items():
                    print(f"{category:<15} | ${data['total']:<9.2f} | {data['count']:<7} | ${data['average']:.2f}")
            else:
                print("No expenses to summarize.")
        
        elif choice == '8':
            print("\nSort by:")
            print("1. Amount")
            print("2. Category")
            print("3. Date")
            print("4. Description")
            
            sort_choice = input("Enter sort option (1-4): ").strip()
            reverse_order = input("Sort in descending order? (y/n): ").strip().lower() == 'y'
            
            sort_options = {'1': 'amount', '2': 'category', '3': 'date', '4': 'description'}
            if sort_choice in sort_options:
                sorted_expenses = sort_expenses(expenses, sort_options[sort_choice], reverse_order)
                print(f'\n🔄 EXPENSES SORTED BY {sort_options[sort_choice].upper()}:')
                print_expenses(sorted_expenses)
            else:
                print("❌ Invalid sort option.")
        
        elif choice == '9':
            search_term = input('Enter search term: ').strip()
            if search_term:
                found_expenses = search_expenses(expenses, search_term)
                print(f'\n🔍 SEARCH RESULTS FOR "{search_term}":')
                print_expenses(found_expenses)
            else:
                print("❌ Please enter a search term.")
        
        elif choice == '10':
            confirm = input('Are you sure you want to clear all expenses? (y/n): ').strip().lower()
            if confirm == 'y':
                expenses.clear()
                print("✓ All expenses cleared.")
            else:
                print("Operation cancelled.")
        
        elif choice == '11':
            print('👋 Thank you for using the Expense Tracker!')
            print('You\'ve seen lambda functions used for:')
            print('• Filtering and mapping data')
            print('• Sorting with custom keys')
            print('• Reducing data to statistics')
            print('• Formatting output')
            print('• Searching and data transformation')
            break
        
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 11.")

if __name__ == "__main__":
    main()
