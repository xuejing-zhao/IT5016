score = int(input("Enter your score: "))
if score < 0  or score >100:
  print("Grade is invalid ")
elif score >= 90:
  print("Grade: A ")
elif score >= 80:
  print("Grade: B" ) 
elif score >=70:
  print("Grade C " )
else:
  print("Grade: F ")