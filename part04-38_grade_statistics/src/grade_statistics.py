

# final function to print grades 
def printing_grades(grade_printing_list:list):
  grades = [ [0,14] , [15,17] , [18,20] , [21,23], [24,27], [28,30] ]
  print("Grade distribution:")

  for i in list(range(5,-1,-1)):
    print(f"  {i}: ",end="")
    # finding the total numbers which come below a range of specific index
    for total_score in grade_printing_list:
      if total_score >= grades[i][0] and total_score <= grades[i][-1]:
          print("*",end="")
    print()

# function to compute exam and exercise points
def compute_points(exam_points_list:list,exercise_points_list:list):

  total_points_list = [ num + exercise_points_list[i] for i,num in enumerate(exam_points_list)  ]
  
  total_points_avg = sum(total_points_list) / len(total_points_list)
    
  no_of_passing_scores = [ num for i,num in enumerate(total_points_list) if exam_points_list[i] >= 10 and num > 14 ]
  
  pass_percentage = ( len(no_of_passing_scores) / len(total_points_list) ) * 100

  print(f"Points average: {total_points_avg:.1f}")
  print(f"Pass percentage: {pass_percentage:.1f}")

  grade_printing_list = [ num if ( exam_points_list[i] >= 10 and num > 14 ) else 0 for ( i,num ) in enumerate(total_points_list) ]
  printing_grades(grade_printing_list)

# function to start the loop of the program 
def main():
  exercise_points_list = []
  exam_points_list = []

  while True:
    student_input = input("Exam points and exercises completed:")
 
    if student_input == "":
      if exam_points_list == [] and exercise_points_list == []:
        break
      print("Statistics:")
      compute_points(exam_points_list,exercise_points_list)
      break
 
    exam_points,exercises_completed = student_input.split(" ") 
 
    exam_points_provided = int(exam_points)
    exercises_completed = int(exercises_completed)
  
    exercise_points_calculated = int(( exercises_completed / 100 ) * 100 * 0.1)

    exam_points_list.append(exam_points_provided)
    exercise_points_list.append(exercise_points_calculated) 

main()