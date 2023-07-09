# Write a class called Course that has the following:

# • A field name that is the name of the course, a field capacity that is the maximum number of students allowed in the course, and a list called student_IDs representing the students in the course by their ID numbers (stored as strings).

# • A constructor that takes the name of the course and capacity and sets those fields accordingly. The constructor should also initialize student_IDs list to an empty list, but it should not take a list as a parameter. It should only have the course name and capacity as parameters.

# • A method called is_full() that takes no arguments and returns True or False based on whether or not the course is full (i.e. if the number of students in the course is equal to or above the capacity).

# • A method called add_student() that takes a student ID number and adds the student to the course by putting their ID number into the list. If the student is already in the course, they must not be added to the list, and if the course is full, the student must not be added to the course. After adding a student, the capacity will be reduced

# • A method called remove_student() that takes a student ID number and removes the student from the course list. After removing a student, the capacity will be increased

# Test the class by creating a Course object, adding several students to the class, and calling the is_full() method. Print out the value of the student_IDs field to make sure everything comes out as expected.

# A method called isExist() that takes student ID number and returns True if the student exists and False otherwise

class Course:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.student_IDs = []

    def is_full(self):
        # if len(self.student_IDs) >= self.capacity:
        #     return True
        # return False
        if self.capacity:
            return False
        return True

    def add_student(self, student_id):
        if self.is_full() or student_id in self.student_IDs:
            return False
        else:
            self.student_IDs.append(student_id)
            self.capacity -= 1
            return True

    def remove_student(self, student_id):
        if student_id in self.student_IDs:
            self.student_IDs.remove(student_id)
            self.capacity += 1
            return True
        return False

    def isExist(self, student_id):
        return student_id in self.student_IDs

    def studentCount(self):
        return len(self.student_IDs)


course = Course('Python', 5)

capacity = 5
for id in range(capacity):
    print('Adding Student:', course.add_student('18-'+str(id)))

print('Adding Student:', course.add_student('18-100'))
print('Adding Student:', course.add_student('18-101'))

print('Removing Student:', course.remove_student('18-0'))
print('Checking Existence:', course.isExist('18-2'))
print('capacity: ', course.capacity)
print('All student IDs: ', course.student_IDs)
print('Is the course full?: ', course.is_full())
print("Number of students:", course.studentCount())
