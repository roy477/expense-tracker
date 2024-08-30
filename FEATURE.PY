def search_transaction_by_date(transactions, target_date):
  for i in range(len(transactions)):
    if transactions[i]['date'] == target_date:
      return transactions[i]
  return None

def sort_transactions_by_amount(transactions):
  for i in range(len(transactions) -1 ):
    for j in range(len(transactions)-i -1 ):
      if transactions[j]['amount'] > transactions[j + 1]['amount']:
        transactions[j], transactions[j + 1] = transactions[j + 1], transactions[j]
  return transactions

def add_data(transaction):
  date=input("Enter the date:")
  amount=int(input("Enter the amount:"))
  desc=input("Enter the description:")
  transaction.append({"date":date,"amount":amount,"desc":desc})
  return transaction

def delete_data(transaction):
  date=input("Enter the date to delete: ")
  for i in range(len(transaction)):
    if transaction[i]['date'] == date:
      del transaction[i]
      return transaction
  return transaction 


def sum_amount(transaction):
  sum=0
  year=input("Enter the year:")
  for transaction in transcations:
    if transcation["date"][0:4]==year:
        sum+=transaction['amount']
  return sum

