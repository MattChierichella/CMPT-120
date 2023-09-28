def main():
  
  #set this to any double
  doubleValue = 11.223
  
  #set this to any int
  intValue = 89
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  #populate this list
  myFriends = ["Conor", "Griffin", "Jake", "Corbin", "Charlie"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2:4])
  
  #populate this list with five numbers
  fiveNumbers = [34, 43, 194, 709, 799]
  print(fiveNumbers[0] + fiveNumbers[4])
  print(fiveNumbers[2] - fiveNumbers[0])
  print(fiveNumbers[1] * fiveNumbers[4])
  print(fiveNumbers[2] / fiveNumbers[3])
  #do each of the four equations with different numbers each time.
  
  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[2] = 32
  fiveNumbers[4] = 8
  print(fiveNumbers)
  #print out the list
  
  
main()
