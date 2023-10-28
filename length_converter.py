#Unit Converter - Length Converter

#Initialization
global proceed
proceed : bool
rpt = 'y'

#User Choice
mainchc = input("Meter -> Feet Conversion : Press 1\nFeet -> Meter Conversion : Press 2\n")
if mainchc == 1 or mainchc == '1':
  
  #Try Catch block
  while rpt == 'y':
    try:
      #User Input
      userin = float(input("Enter the length in meters : \n"))
      proceed = True
      break

    except ValueError:
      #Incase of Error
      print("Enter a valid integer/floating point number.\n")
      rpt = input("Enter again? (y/n): \n")

      if rpt == 'n':
        #Ending the program
        proceed = False
        print("The program is ending...\n")
        break

  if proceed:
    #Starting the program
    print("Conversion of Meter to Feet :- ")
    print(f"Your entered value {userin} meter(s)")
    print(f"The converted value is approximately {round((userin * 3.28),3)} feet")

if mainchc == 2 or mainchc == '2':

    #Try Catch block
  while rpt == 'y':
    try:
      #User Input
      userin = float(input("Enter the length in feet : \n"))
      proceed = True
      break

    except ValueError:
      #Incase of Error      
      print("Enter a valid integer/floating point number.\n")
      rpt = input("Enter again? (y/n): \n")

      if rpt == 'n':
        #Ending the program
        proceed = False
        print("The program is ending...\n")
        break

  if proceed:
    #Starting the program
    print("Conversion of Feet to Meter :- ")
    print(f"Your entered value {userin} Feet")
    print(f"The converted value is approximately {round((userin / 3.28),3)} meter(s)")

else:
  #Incase invalid choice is provoked
  print("Enter valid choice")
