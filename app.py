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
    try:
        cursor = collection.insert_one(doc)
        print(cursor)
    except Exception as e:
        print(e)

def create_Many_documents(doc, collection):
    """Insert a multiple document into the collection."""
    try:
        cursor = collection.insert_many(doc)
        print(cursor)
    except Exception as e:
        print(e)
        
def read_all_documents(collection):
    """Fetch and print all documents."""
    try:
        cursor = collection.find({})
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def read_one_document(collection):
    """Fetch and print one documents."""
    try:
        cursor=collection.find_one()
        print(cursor)
    except Exception as e:
        print(e)
    
def read_document_by_id(id, collection):
    """Fetch and print document by id."""
    try:
        cursor = collection.find({"_id": id})
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)
        
def read_document_by_condition(field, value):
    """Fetch and print document by condition."""
    try:
        cursor=collection.find({ field : value })
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def deleteOne( doc, collection):
    """Delete one document that matches the condition."""
    try:
        cursor=collection.delete_one(doc)
        print(cursor)
    except Exception as e:
        print(e)

def deleteMany( doc, collection):
    """Delete many document that matches the condition."""
    try:
        cursor=collection.delete_many(doc)
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

def updateOne(doc, collection, toUpdate):
    """Updates one document that matches the condition."""
    try:
        cursor=collection.update_one(doc, {"$set" : toUpdate})
        print(cursor)
    except Exception as e:
        print(e)

def updateMany(doc, collection, toUpdate):
    """Update many document that matches the condition."""
    try:
        cursor=collection.update_many(doc, {"$set" : toUpdate})
        for docs in cursor:
            print(docs)
    except Exception as e:
        print(e)

#__________________________________________________________________________________________________

"""Logical, Comparison and Element nstrictions"""


def notOperator(collection, condition, field):
    """Compute the not operator"""
    try:
        cursor = collection.find({field: {"$not": condition}})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def andOperator(collection, condition1, condition2):
    """Compute the and operator"""
    try:
        cursor = collection.find({"$and": [condition1, condition2]})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def orOperator(collection, condition1, condition2):
    """Compute the or operator"""
    try:
        cursor = collection.find({"$or": [condition1, condition2]})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def greaterThanOperator(collection, field, value):
    """Compute the greater than operator"""
    try:
        cursor = collection.find({field: {"$gt": value}})
        docs = []
        for doc in cursor:
            
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def lessThanOperator(collection, field, value):
    """Compute the less than operator"""
    try:
        cursor = collection.find({field: {"$lt": value}})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def inOperator(collection, field, array):
    """Compute the in operator"""
    try:
        cursor = collection.find({field: {"$in": array}})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)

def existOperator(collection, field, bool):
    """compute the exist operator"""
    try:
        cursor = collection.find({field: {"$exists": bool}})
        docs = []
        for doc in cursor:
            docs.append(doc)
        return docs
    except Exception as e:
        print(e)
#__________________________________________________________________________________________________
######Arrays######

def Push(field,value,collection):
    """Add a new item to an array."""
    try:
        cursor = collection.update_one({ "_id": 1 },{ "$push": { field: value } })
        print(cursor)
    except Exception as e:
        print(e)

def Pull(field,value,collection):
    """Remove an item from an array."""
    cursor = collection.update_one({ "_id": 1 },{ "$pull": { field: value } })
    try:
        cursor = collection.update_one({ "_id": 1 },{ "$pull": { field: value } })
        print(cursor)
    except Exception as e:
        print(e)

def find_all_in(array,collection):
    """find documents based on contents."""
    try:
        cursor = collection.find({ "name": { "$all":array} } )
        for nam in cursor:
            print(nam)
       
    except Exception as e:
        print(e)


def find_by_size(field,size,collection):    
    """find documents based on size."""
    try:
        cursor = db.students.find( { field: { "$size": size } } )
        for doc in cursor:
            print(doc)

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
        print("11. Total Students in the Course")
        print("12. Top 10 Students in the Course")
        print("13. Push element")
        print("14. Pull element")
        print("15. find documents using $all")
        print("16. find documents by size")
        print("17. Perform not logical operations")
        print("18. Perform and logical operations")
        print("19. Perform or logical operations")
        print("20. Perfrom greater than comparison operations")
        print("21. Perform less than comparison operations")
        print("22. Perform in element operations")
        print("23. Perform exist element operations")

        
        print("24. Exit")

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
   ######################################################################################################################         
    
#####Here prints out the total number of students in the course by course code###########
        elif choice == "11":
            name = input("Enter course_code(e.g. EOW379): ")
            totalStudents_per_course(name)

    #####Here prints out the top 10 students in the course by course code###########
        elif choice == "12":
            name = input("Enter course_code(e.g. EOW379): ")
            top10Students_per_course(name)
##############################################################################################################################            
   ##### ARRAYS QUERIES ###########
          """Push elements to an array"""
        elif choice == "13":
            field = input("Enter field (advisors) or (enrolled_courses): ")
            if field == "advisors":
                num_advisors=int(input("Enter number of advisors: "))
                advisors=[]
                for n in range(num_advisors):
                    advisor_id=input("Enter id of advisor: ")
                    advisors.append(advisor_id)   
                Push( "advisors",advisors, collection)
        elif field == "enrolled_courses":
            courses = []
            course_num = int(input("Enter the number of courses you do: "))
            for i in range(course_num):
                course_id =  ObjectId()
                course_code = input("Enter course_code: ")
                semester = input("Enter the semester: ")
                grade = input("Enter your grade: ")
                status = input("Enter the status(Complete OR Enrolled): ")
                courses.append({"course_id ": course_id, "course_code": course_code, "semester":semester, "grade":grade, "status":status})
            Push( "enrolled_courses",courses, collection)    

         

          
            """Pull elements to an array"""
        elif choice == "14":
            field = input("Enter field (advisors) or (enrolled_courses): ")
            if field == "advisors":
                num_advisors=int(input("Enter number of advisors: "))
                advisors=[]
                for n in range(num_advisors):
                    advisor_id=input("Enter id of advisor: ")
                    advisors.append(advisor_id)   
                Pull( "advisors",advisors, collection)
        elif field == "enrolled_courses":
            courses = []
            course_num = int(input("Enter the number of courses you do: "))
            for i in range(course_num):
                course_id =  ObjectId()
                course_code = input("Enter course_code: ")
                semester = input("Enter the semester: ")
                grade = input("Enter your grade: ")
                status = input("Enter the status(Complete OR Enrolled): ")
                courses.append({"course_id ": course_id, "course_code": course_code, "semester":semester, "grade":grade, "status":status})
            Pull( "enrolled_courses",courses, collection)


            """find documents using all operator"""
        elif choice == "15":
            courses = []
            course_num = int(input("Enter the number of names to search: "))
            if course_num ==1:
                 name = input("Enter name: ")
                 find_all_in( [name], collection)
            else:  
                for i in range(course_num):
                    name = input("Enter name: ")
                    courses.append(name)
                for nam in courses:
                    find_all_in( [nam], collection)  


            """find documents by size"""
        elif choice == "16":
            field = input("Enter field (advisors) or (enrolled_courses): ")
            size = int(input("Enter size: "))
            find_by_size(field,size, collection)
        ##################################################################### ################

        elif choice == "17":
            #field = input("enter field: ")
            value = input("enter value: ")
            
            condition = {"$ne":value}
            notOperator(collection, condition, field)
            

        elif choice == "18":
            
            field1 = input("enter first field: ")
            value1 = input("enter the first value: ")
           
            condition1 = {field1: value1}

            field2 = input("enter second field: ")
            value2 = input("enter the value you want to change: ")
            
            condition2 = {field2: value2}
    
            andOperator(collection, condition1, condition2)
            
        
        elif choice == "19":
            field1 = input("enter first field: ")
            value1 = input("enter the first value: ")
            condition1 = {field1: value1}

            field2 = input("enter second field: ")
            value2 = input("enter the value you want to change: ")
            condition2 = {field2: value2} 

            orOperator(collection, condition1, condition2)

        elif choice == "20":
            field = input("enter field: ")
            value = input("enter value: ")

            greaterThanOperator(collection, field, value)

        elif choice == "21":
            field = input("enter field: ")
            value = input("enter value: ")

            lessThanOperator(collection, field, value)

        elif choice == "22":
            array = []
            field = input("enter field: ")
            numElements = int(input("enter number of elements to check in: "))
            for _ in range(numElements):
                element = input("enter each element: ")
                array.append(element)
            
            result = inOperator(collection, field, array)
            
            print(result)

        elif choice == "23":
            field = input("enter field: ")
            bool = input("enter boolean value True or False: ")

            existOperator(collection, field, bool)





        

    #####THIS CONDITION IS FOR EXITING###########
        elif choice == "24":
            print("Exiting...")
            quit()

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
