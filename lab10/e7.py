studentId = input("Inserire id studente: ")

courses = []

with open("./e7/classes.txt", "r") as coursesFile:
    line = coursesFile.readline()
    while line != "":
        courses.append(line.strip())
        line = coursesFile.readline()

for course in courses:
    with open('./e7/' + course + ".txt", 'r') as courseFile:
        line = courseFile.readline()
        while line != "":
            if line.strip().startswith(studentId):
                print(course, line.strip().split(" ")[1])
                break
            line = courseFile.readline()