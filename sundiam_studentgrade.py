Name = input('\nenter your name: ')
section = input('enter your section: ')



prelim = round(float(input('\nenter prelim grade: ')))
midterm = round(float(input("enter midterm grade: ")))
final = round(float(input('enter your final grade: ')))


if (prelim >= 40 and prelim <= 100) and (midterm >= 40 and midterm <= 100) and (final >= 40 and final <= 100):
    
    prelim = (33.33) * (prelim) / 100
    midterm = (33.33 * midterm) / 100
    final = (33.33 * final) / 100
    gpa = round((prelim + midterm + final))
    
    if (gpa >= 99 and gpa <= 100):
        grade_points = "1.00"
        description = "excellent"
    elif gpa >= 96:
        grade_points = "1.25"
        description = "outstanding"
    elif gpa >= 93:
        grade_points = "1.50"
        description = "superior"
    elif gpa >= 90:
        grade_points = "1.75"
        description = "very good"
    elif gpa >= 87:
        grade_points = "2.00"
        description = "good"
    elif gpa >= 84:
        grade_points = "2.25"
        description = "satisfactory"
    elif gpa >= 81:
        grade_points = "2.50"
        description = "fairly satisfactory"
    elif gpa >= 78:
        grade_points = "2.75"
        description = "fair"
    elif gpa >= 75:
        grade_points = "3.00"
        description = "passed"
    elif gpa < 75 :
        grade_points = "5.0"
        description = "failed"
    else:
        grade_points = "5.00"
        description = "failed"
    print(f'\n\n===== calculating the grade =====' +
          f'\nname: {Name}' +
          f'\nsection: {section}' +
          f'\nprelim: {prelim}%' +
          f'\nmidterm: {midterm}%' +
          f'\nfinalterm: {final}%' +
          f'\n\ngpa: {gpa}%' +
          f'\ngrade points: {grade_points}' +
          f'\ndescription: {description}')
else:
    print('invalid grade')
    
          
    
    
              
       
       
       
       