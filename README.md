# 💰 Enhanced Expense Tracker with Lambda Functions

A Python-based expense tracking application that demonstrates the power and versatility of lambda functions in real-world scenarios.

## 🚀 Features

- ✅ Add expenses with categories and descriptions
- 📊 Comprehensive expense statistics
- 🔍 Advanced filtering and searching
- 📈 Category-wise summaries
- 🔄 Flexible sorting options
- 💾 Real-time data processing with lambda functions

## 🎯 Lambda Functions Demonstrated

This project showcases various lambda function use cases:

- **Data Filtering**: Filter expenses by category, amount range, and search terms
- **Data Mapping**: Transform and format expense data for display
- **Data Reduction**: Calculate totals and statistics using `reduce()`
- **Custom Sorting**: Sort expenses by different criteria
- **List Processing**: Efficient data manipulation and transformation

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.6 or higher

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/expense-tracker-lambda.git
   cd expense-tracker-lambda
   ```

2. Run the application:
   ```bash
   python expense_tracker.py
   ```

3. Follow the interactive menu to explore features!

## 📖 How to Use

### Main Menu Options:
1. **Add Expense**: Record new expenses with amount, category, and description
2. **List Expenses**: View all recorded expenses in a formatted table
3. **Show Statistics**: Get comprehensive expense analytics
4. **Filter by Category**: View expenses from specific categories
5. **Filter by Amount**: Find expenses within a price range
6. **Category Summary**: See totals and averages per category
7. **Sort Expenses**: Organize expenses by amount, date, category, or description
8. **Search**: Find expenses containing specific terms
9. **Clear Data**: Reset all expense data

### Sample Usage:
```
Enter your choice (1-11): 1
Enter amount: $45.50
Enter category: Food
Enter description (optional): Lunch at cafe
✓ Added expense: $45.50 for Food
```

## 🎓 Learning Outcomes

By studying this code, you'll learn:
- How to use lambda functions with `map()`, `filter()`, and `reduce()`
- Functional programming concepts in Python
- Data processing and transformation techniques
- Building interactive console applications
- Code organization and best practices

## 🔧 Technical Details

### Lambda Functions Used:
- **Formatting**: `lambda exp: f"${exp['amount']:.2f} | {exp['category']}..."`
- **Filtering**: `lambda expense: expense['category'].lower() == category.lower()`
- **Sorting**: `lambda exp: exp['amount']` for custom sort keys
- **Statistics**: `lambda total, expense: total + expense['amount']`
- **Search**: `lambda expense: search_term in expense['description'].lower()`

### Key Features:
- Timestamp tracking for all expenses
- Flexible filtering and sorting mechanisms
- Statistical analysis with min/max/average calculations
- Category-wise expense summaries
- Full-text search across categories and descriptions

## 📊 Sample Output

```
💰 TOTAL EXPENSES: $231.25

📊 EXPENSE STATISTICS:
Total Expenses: $231.25
Average Expense: $57.81
Minimum Expense: $15.75
Maximum Expense: $120.00
Number of Expenses: 4

📈 CATEGORY SUMMARY:
Category        | Total      | Count   | Average
Food            | $170.00    | 2       | $85.00
Transport       | $25.50     | 1       | $25.50
Entertainment   | $15.75     | 1       | $15.75
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new filtering options
- Implement data export features
- Add expense categories management
- Improve the user interface
- Add data visualization

## 📝 License

This project is open source and available under the [MIT License](LICENSE).



---

**Note**: This project was developed as a learning exercise to explore lambda functions in Python. The enhanced features were developed with AI assistance to demonstrate advanced functional programming concepts.
