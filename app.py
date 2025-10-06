from pymongo import MongoClient
from bson import ObjectId
import pprint

# -------------------------
# Database connection
# -------------------------
client = MongoClient("mongodb+srv://thabiso:BASOTHO@basotho.g73eyoe.mongodb.net/?retryWrites=true&w=majority&appName=BASOTHO")  # adjust if using Atlas
db = client["university_db"]      # replace with your chosen DB name
collection = db["students"]    # example collection

pp = pprint.PrettyPrinter(indent=2)


# -------------------------
# CRUD Function Templates
# -------------------------

def create_One_document(doc, collection):
    """Insert a single document into the collection."""
    try:
        cursor = collection.insert_one(doc)
        print(cursor)
    except Exception as e:
        print(e)

def create_Many_documents(doc, collection):
    """Insert a multiple document into the collection."""
    cursor = collection.insert_many(doc)
    try:
       print(cursor)
    except Exception as e:
        print(e)
        
def read_all_documents(collection):
    """Fetch and print all documents."""
    
    cursor = collection.find({})
    try:
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def read_one_document(collection):
    """Fetch and print one documents."""
    cursor=collection.find_one()
    try:
        print(cursor)
    except Exception as e:
        print(e)
    
def read_document_by_id(id, collection):
    """Fetch and print document by id."""
    cursor = collection.find({"_id": id})
    try:
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)
        
def read_document_by_condition(field, value):
    """Fetch and print document by condition."""
    cursor=collection.find({ field : value })
    try:
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def deleteOne( doc, collection):
    """Delete one document that matches the condition."""
    cursor=collection.delete_one(doc)
    try:
        print(cursor)
    except Exception as e:
        print(e)

def deleteMany( doc, collection):
    """Delete many document that matches the condition."""
    cursor=collection.delete_many(doc)
    try:
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def updateOne(doc, collection, toUpdate):
    """Updates one document that matches the condition."""
    cursor=collection.update_one(doc, {"$set" : toUpdate})
    try:
      print(cursor)
    except Exception as e:
        print(e)

def updateMany(doc, collection, toUpdate):
    """Update many document that matches the condition."""
    cursor=collection.update_many(doc, {"$set" : toUpdate})
    try:
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

#__________________________________________________________________________________________________
######Aggregation pipelines######

def totalStudents_per_course(courseCode):
    try:
        cursor = collection.aggregate( [{ "$unwind": "$enrolled_courses" }, { "$match": { "enrolled_courses.course_code" : courseCode}}  , { "$project": { "enrolled_courses.course_code":1, "_id": 0 }},  {"$count" : "Total Students In The Course"}])
        documents = []
        for doc in cursor:
            documents.append(doc)
        print(documents)
    except Exception as e:
        print("Error occured!!")

def top10Students_per_course(courseCode):
    try:
        cursor = collection.aggregate( [{ "$unwind": "$enrolled_courses" },{"$sort": {"grade": 1, "name": 1}}, { "$match": { "enrolled_courses.course_code" : courseCode}}  , { "$project": { "name": 1, "_id": 0 }},  {"$limit": 10} ])
        documents = []
        for doc in cursor:
            documents.append(doc)
        print(documents)
    except Exception as e:
        print("Error occured!!")

#__________________________________________________________________________________________________


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
        print("11. Perform logical instructions")
        print("12. Perform comparison and Element instructions")
        print("13. Total Students in the Course")
        print("14. Top 10 Students in the Course")
        print("15. Exit")

        choice = input("Enter choice: ")

        #####THIS CONDITION CHECKS FOR CREATING ONE DOCUMENT###########
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
            
            
            
            
          #####THIS CONDITION CHECKS FOR CREATING MANY DOCUMENTS###########
 
        elif choice == "2":
            num = int(input("Enter the number of students you would like to add: "))
            students=[]
            for i in range(num):
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
                students.append({"_id":ObjectId(), "name":name, "student_id":student_id,"contact_info":contact_info, "enrolled_courses": courses, "advisors":advisors})
                
            create_Many_documents(students, collection)
            
         #####THIS CONDITION CHECKS FOR READING ALL DOCUMENTS###########

        elif choice == "3":
            read_all_documents(collection)
        
        #####THIS CONDITION CHECKS FOR READING FIRST DOCUMENTS###########
        
        elif choice == "4":
            read_one_document(collection)
            
        #####THIS CONDITION CHECKS FOR READING A DOCUMENT BY _ID###########
        elif choice == "5":
            id = input("Enter object _id: ")
            read_document_by_id(ObjectId(id))


        #####THIS CONDITION CHECKS FOR READING A DOCUMENT BY CONDITION###########
        elif choice == "6":
            field = input("Enter field: ")
            value = input("Enter value: ")
            read_document_by_condition(field, value)
            
            
        #####THIS CONDITION UPDATES ONE DOCUMENT###########

        elif choice == "7":
            field = input("Enter field: ")
            oldValue = input("Enter value: ")
            newValue = input("Enter new value: ")
            updateOne({field : oldValue}, collection , {field : newValue})
            
        #####THIS CONDITION UPDATES MANY DOCUMENTS###########
        
        elif choice == "8":
            field = input("Enter field: ")
            oldValue = input("Enter value: ")
            newValue = input("Enter new value: ")
            updateMany( { field : oldValue}, collection , {field : newValue})



     #####THIS CONDITION IS FOR DELETING ONE DOCUMENT###########
        elif choice == "9":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteOne({field : value} , collection)
     
     
     #####THIS CONDITION IS FOR DELETING MANY DOCUMENTS###########
        elif choice == "10":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteMany({field : value} , collection)
            
        elif choice == "11":
            #conditions, operator, field
            operator = input("enter operator to compute($and, $or, and $not): ")
            if operator == "$not":
                field = input("enter field to compute on: ")
            conditions = input("enter conditions (must be an array with lists as elements): ")
            
            doc = logicalOpe(collection, operator, conditions, field)
            for docs in doc:
                print(docs)
            
            
        elif choice == "12":
            field = input("enter field to compute on: ")
            value = input("enter value to compute logic on: ")
            operator = input("enter the main operator like ($gt, $lt, $in, and $exists): ")
            
            doc = {field: {operator: value}}
            
            comparisonAndElemnt(doc, collection)
            
            result = comparisonAndElemnt(doc, collection)
            for resu in result:
                print(resu)

#####Here prints out the total number of students in the course by course code###########
        elif choice == "13":
            name = input("Enter course_code(e.g. EOW379): ")
            totalStudents_per_course(name)

    #####Here prints out the top 10 students in the course by course code###########
        elif choice == "14":
            name = input("Enter course_code(e.g. EOW379): ")
            top10Students_per_course(name)
        
    #####THIS CONDITION IS FOR EXITING###########
        elif choice == "15":
            print("Exiting...")
            quit()

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
