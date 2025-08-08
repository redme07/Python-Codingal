total_amnount = float(input("Enter the total bill amnount"))
paid_amnount = float(input('Enter the paid amnount'))

def bill(total_amnount, paid_amnount):
    if total_amnount > paid_amnount:
        print("Payment is remaining of value", total_amnount-paid_amnount)
    elif total_amnount<paid_amnount:
        return(paid_amnount-total_amnount)
    else:
        print("Transaction completed")

print(bill(total_amnount, paid_amnount))

