import os
from pymongo import MongoClient
from faker import Faker
import random
from bson.objectid import ObjectId

# --- MongoDB Connection ---
# Students, insert your MongoDB connection URI here
# For example: "mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority"

MONGO_URI ="mongodb+srv://Tshephang:BASOTHO@basotho.g73eyoe.mongodb.net/?retryWrites=true&w=majority&appName=BASOTHO"#add your uri here for your cluster
DB_NAME = "university_db"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# --- Faker Initialization ---
fake = Faker('en_US')

# --- Configuration ---
NUM_STUDENTS = 150
NUM_PROFESSORS = 30
NUM_COURSES = 60
MIN_ENROLLED_COURSES = 3
MAX_ENROLLED_COURSES = 7

def generate_professors(num_professors):
    professors = []
    departments = ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology", "English", "History", "Fine Arts"]
    for i in range(num_professors):
        professor = {
            "_id": ObjectId(),
            "name": fake.name(),
            "employee_id": f"PROF{1000 + i}",
            "department": random.choice(departments),
            "contact_info": {
                "email": fake.unique.email(),
                "phone": fake.phone_number(),
            },
            "courses_taught": [],
            "research_interests": random.sample(fake.words(nb=5, unique=True), k=random.randint(1, 3))
        }
        professors.append(professor)
    print(f"Generated {len(professors)} professors.")
    return professors

def generate_courses(num_courses, professors_data):
    courses = []
    departments = [p["department"] for p in professors_data]
    departments = list(set(departments))
    
    for i in range(num_courses):
        course_code = f"{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))}{str(random.randint(100, 499))}"
        department = random.choice(departments)
        
        assigned_professors = random.sample([p["_id"] for p in professors_data if p["department"] == department], k=random.randint(1, 2)) if any(p["department"] == department for p in professors_data) else random.sample([p["_id"] for p in professors_data], k=1)

        course = {
            "_id": ObjectId(),
            "course_name": fake.catch_phrase(),
            "course_code": course_code,
            "department": department,
            "credits": random.randint(3, 5),
            "prerequisites": [],
            "assigned_professors": assigned_professors
        }
        courses.append(course)
    
    for course in courses:
        num_prereqs = random.randint(0, 2)
        if num_prereqs > 0 and len(courses) > 1:
            possible_prereqs = [c["course_code"] for c in courses if c["_id"] != course["_id"]]
            course["prerequisites"] = random.sample(possible_prereqs, k=min(num_prereqs, len(possible_prereqs)))

    print(f"Generated {len(courses)} courses.")
    return courses

def generate_students(num_students, courses_data, professors_data):
    students = []
    grades = ["A", "B+", "B", "C+", "C", "D", "F"]
    semesters = ["Fall 2023", "Spring 2024", "Fall 2024"]

    for i in range(num_students):
        student = {
            "_id": ObjectId(),
            "name": fake.name(),
            "student_id": f"S{10000 + i}",
            "contact_info": {
                "email": fake.unique.email(),
                "phone": fake.phone_number(),
            },
            "enrolled_courses": [],
            "advisors": []
        }

        num_enrolled = random.randint(MIN_ENROLLED_COURSES, MAX_ENROLLED_COURSES)
        selected_courses = random.sample(courses_data, k=min(num_enrolled, len(courses_data)))

        for course in selected_courses:
            enrollment = {
                "course_id": course["_id"],
                "course_code": course["course_code"],
                "semester": random.choice(semesters),
                "grade": random.choice(grades),
                "status": "Completed" if random.random() > 0.2 else "Enrolled",
            }
            student["enrolled_courses"].append(enrollment)
            
        student["advisors"] = random.sample([p["_id"] for p in professors_data], k=random.randint(1, 2))
        students.append(student)
    print(f"Generated {len(students)} students.")
    return students

def update_professor_courses_taught(professors_data, courses_data):
    for professor in professors_data:
        prof_courses_ids = [c["_id"] for c in courses_data if professor["_id"] in c["assigned_professors"]]
        db.professors.update_one({"_id": professor["_id"]}, {"$set": {"courses_taught": prof_courses_ids}})
    print("Updated professors' courses taught.")

def main():
    print(f"Connecting to MongoDB at {MONGO_URI}...")
    db.students.drop()
    db.courses.drop()
    db.professors.drop()
    print("Dropped existing collections.")

    professors_data = generate_professors(NUM_PROFESSORS)
    db.professors.insert_many(professors_data)

    courses_data = generate_courses(NUM_COURSES, professors_data)
    db.courses.insert_many(courses_data)

    update_professor_courses_taught(professors_data, courses_data)

    students_data = generate_students(NUM_STUDENTS, courses_data, professors_data)
    db.students.insert_many(students_data)

    print("\nDataset generation complete!")
    client.close()
    print("MongoDB connection closed.")

if __name__ == "__main__":
    main()