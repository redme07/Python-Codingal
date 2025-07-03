actual_cost = float(input("Enter the actual cost of the item"))
selling_cost = float(input("Enter the cost at which it is being sold at"))

if(actual_cost<selling_cost):
    profit = selling_cost - actual_cost
    #The .format is a used to print a variable using indexation. The variable should go in brackets
    #after the .format
    print("The profit that the seller is earning is {0}".format(profit))

else:
    loss = actual_cost - selling_cost
    #The f string method is also a way of printing a variable 
    print(f"The loss that the seller is getting per sale of item is {loss}")
