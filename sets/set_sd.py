morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

# shows symmetric difference - courses that are not
# repeated in any of the courses in the set
possible_courses = morning ^ afternoon
print(possible_courses)

# Using the method
possible_courses_1 = morning.symmetric_difference(afternoon)
print(possible_courses_1)