from FEATURE import search_transaction_by_date,sort_transactions_by_amount,add_data,delete_data,sum_amount
 
transaction=[
{"date":"2021-10-18","amount":2000,"desc":"fruits"},
{"date":"2021-10-20","amount":3000,"desc":"vegetables"},
{"date":"2021-10-15","amount":4000,"desc":"groceries"},
{"date":"2021-10-28","amount":1500,"desc":"bills"},
{"date":"2021-10-19","amount":2000,"desc":"medicalexpenses"},
]

while True:
  print("Menu:")
  print("1. Display transactions")
  print("2. Search transaction by date")
  print("3. Sort transactions by amount")
  print("4. Add transaction")
  print("5. Delete transaction")
  print("6. Stop")
  print("7. Sum amount")

  choice = input("Enter your choice: ")

  if choice == '1':
    print(transaction)
  elif choice == '2':
    target_date = input("Enter the date to search for: ")
    result = search_transaction_by_date(transaction, target_date)
    if result:
      print("Transaction found:", result)
    else:
      print("Transaction not found for date:", target_date)
  elif choice == '3':
    sorted_transactions = sort_transactions_by_amount(transaction.copy())
    print("Sorted transactions:", sorted_transactions)
  elif choice == '4':
    transaction = add_data(transaction)
    print("Transaction added successfully.")
  elif choice == '5':
    transaction = delete_data(transaction)     
    print("Transaction deleted successfully.")
  elif choice == '6':
    transaction = stop_data(transaction)
    print("Transaction stop.")
  elif choice == '7':
    transcation = add_data(transaction)  
    print("sum of the given year.")
    break
  else:
    print("Invalid choice. Please try again.")
