age= int(input("Enter Age:"))
sex=input("Enter your gender(m/f):")
marital_status=input("Enter your marital status (y/n):")

if sex=='f':
 print("She will work only in urban areas")
else:
 if sex=='m' and (age>=20 and age<=40):
  print("He work anywhere")
 elif sex=='m' and (age>=40 and age<=60):
  print("He work in urban area only")
 else:
  print("ERROR")

 


