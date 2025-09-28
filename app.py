from pymongo import MongoClient
from bson import ObjectId
import pprint

# -------------------------
# Database connection
# -------------------------
client = MongoClient("mongodb+srv://group2:BASOTHO@basotho.g73eyoe.mongodb.net/?retryWrites=true&w=majority&appName=BASOTHO")  # adjust if using Atlas
db = client["university_db"]      # replace with your chosen DB name
collection = db["students"]    # example collection

pp = pprint.PrettyPrinter(indent=2)


# -------------------------
# CRUD Function Templates
# -------------------------

def create_One_document(doc, collection):
    """Insert a single document into the collection."""
    collection.insert_one(doc)

def create_Many_documents(doc, collection):
    """Insert a multiple document into the collection."""
    collection.insert_many(doc)

def read_all_documents(collection):
    """Fetch and print all documents."""
    collection.find({})


def read_one_document(collection):
    """Fetch and print one documents."""
    collection.find_one()

def read_document_by_id(id, collection):
    """Fetch and print document by id."""
    collection.find({"_id": id})

def read_document_by_condition(field, value):
    """Fetch and print document by condition."""
    collection.find({ field : value })

def deleteOne( doc, collection):
    """Delete one document that matches the condition."""
    collection.delete_one(doc)

def deleteMany( doc, collection):
    """Delete many document that matches the condition."""
    collection.delete_many(doc)

def updateOne(doc, collection, toUpdate):
    """Updates one document that matches the condition."""
    collection.update_one(doc, {"$set" : toUpdate})

def updateMany(doc, collection, toUpdate):
    """Update many document that matches the condition."""
    collection.update_many(doc, {"$set" : toUpdate})

# -------------------------
# Menu System
# -------------------------


def menu():
    while True:
        print("\n--- MongoDB Project Menu --- ")
        print("1. Create One Document ")
        print("2. Create Many Documents ")
        print("3. Read All Documents ")
        print("4. Read First Document ")
        print("5. Read Documents By ID ")
        print("6. Read Documents By Condition ")
        print("7. Updates one document")
        print("8. Update many documents")
        print("9. Deletes one document")
        print("10. Deletes many documents")
        print("11. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student_id: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            contact_info = {"email":email, "phone":phone}
            courses = []
            course_num = int(input("Enter the number of courses you do: "))
            for i in range(course_num):
                course_id =  ObjectId()
                course_code = input("Enter course_code: ")
                semester = input("Enter the semester: ")
                grade = input("Enter your grade: ")
                status = input("Enter the status(Complete OR Enrolled): ")
                courses.append({"course_id ": course_id, "course_code": course_code, "semester":semester, "grade":grade, "status":status})
            num_advisors=int(input("Enter number of advisors: "))
            advisors=[]
            for n in range(num_advisors):
                advisor_id=input("Enter id of advisor: ")
                advisors.append(advisor_id)
                
            create_One_document({"_id":ObjectId(), "name":name, "student_id":student_id,"contact_info":contact_info, "enrolled_courses": courses, "advisors":advisors}, collection)

        elif choice == "2":
            num = int(input("Enter the number of students you would like to add: "))
            students=[]
            for i in range(num):
                name = input("Enter student name: ")
                age = int(input("Enter age: "))
                students.append({"name": name, "age": age})
            create_Many_documents(students, collection)
#68d98e559a33206ced717614asdfghj
        elif choice == "3":
            read_all_documents()
            
        elif choice == "4":
            read_one_document()

        elif choice == "5":
            id = input("Enter object _id: ")
            read_document_by_id(ObjectId(id))

        elif choice == "6":
            field = input("Enter field: ")
            value = input("Enter value: ")
            read_document_by_condition(field, value)

        elif choice == "7":
            field = input("Enter field: ")
            oldValue = input("Enter value: ")
            newValue = input("Enter new value: ")
            updateOne({field : oldValue}, collection , {field : newValue})

        elif choice == "8":
            field = input("Enter field: ")
            oldValue = input("Enter value: ")
            newValue = input("Enter new value: ")
            updateMany( { field : oldValue}, collection , {field : newValue})

        elif choice == "9":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteOne({field : value} , collection)

        elif choice == "10":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteMany({field : value} , collection)

        elif choice == "11":
            print("Exiting...")
            quit()

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()