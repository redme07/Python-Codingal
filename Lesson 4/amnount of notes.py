amnount = int(input("Enter a amnount of money:"))

note1 = amnount // 100
note2 = (amnount%100)//50
note3 = ((amnount%100)%50)//10

print("The amnount of 100 ruppee notes are", note1)
print("\nThe amnount of 50 ruppee notes are", note2)
print("\nThe amnount of 10 ruppee notes are", note3)