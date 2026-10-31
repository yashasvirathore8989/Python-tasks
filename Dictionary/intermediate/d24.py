# Given a nested dictionary of students and their subject marks, calculate each student's total marks and find the topper.

students={
    'Ankit': {'Math': 90, 'Science': 85, 'English': 80},
    'Yashasvi': {'Math': 95, 'Science': 92, 'English': 88},
    'Anvi': {'Math': 98, 'Science': 100, 'English': 98}
}
topper_name=""
max_total=0
for name, subject in students.items():
    total=0
    for marks in subject.values():
        total+=marks
    print("Name :",name,",","Marks :",total)
    if total>max_total:
        max_total=total
        topper_name=name
print("Topper is",topper_name,"with",max_total,"marks...")