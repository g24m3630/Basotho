from pymongo import MongoClient
from bson import ObjectId
import pprint

# -------------------------
# Database connection
# -------------------------
client = MongoClient("mongodb+srv://Tshephang:BASOTHO@basotho.g73eyoe.mongodb.net/?retryWrites=true&w=majority&appName=BASOTHO")  # adjust if using Atlas
db = client["university_db"]      # replace with your chosen DB name
collection = db["students"]    # example collection

pp = pprint.PrettyPrinter(indent=2)


# -------------------------
# CRUD Function Templates
# -------------------------

def create_document(doc, collection):
    """Insert a single document into the collection."""
    print(collection.insert_one(doc))

def create_many_documents(doc, collection):
    print(collection.insert_many(doc)) 
    
def read_all_documents():
    """Fetch and print all documents."""
    print(collection.find({}))
    
def read_one_document():
    """Fetch and print one document."""
    print(collection.find_one())
    
def read_document_by_id(id,collection):
    """Fetch and print all documents with the provided id."""
    collection.find({ "_id":id})

        
    
def read_documents_by_condition(field,value):
    """Fetch and print all documents with provided field and value."""
    print(collection.find({field:value}))

def deleteOne(doc,collection):
    """Delete one document."""
    collection.delete_one(doc)

def deleteMany(doc,collection):
    """Delete many documents."""
    collection.delete_many(doc)
    
def updateOne(doc,collection,toUpdate):
    """Update one document ."""
    collection.update_one(doc, {"$set":toUpdate})
    
def updateMany(doc,collection,toUpdate):
    """update many documents."""
    collection.update_many(doc, {"$set":toUpdate})

# -------------------------
# Menu System
# -------------------------

def menu():
    while True:
        print("\n--- MongoDB Project Menu ---")
        print("1. Create One Document")
        print("2. Read All Documents")
        print("3. Create Many Documents")
        print("4. Read first Document")
        print("5. Read Document by _id")
        print("6. Read Document by User")
        print("7. Update one document")
        print("8. update many documents")
        print("9. Delete one document")
        print("10. Delete many documents")
        print("11. EXIT")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter age: "))
            create_document({"name": name, "age": age},collection)
        
      
        elif choice == "2":
            read_all_documents()
            
        elif choice == "3":
            num = int(input("Enter number of students: "))
            lis = [] 
            for i in range(num):
                name = input("Enter student name: ")
                age = int(input("Enter age: "))
                lis.append({"name": name, "age": age})
            create_many_documents(lis,collection) 
            
        elif choice == "4":
            read_one_document() 
            
        elif choice == "5":
            _id = input("Enter _id to find: ")
            read_document_by_id(ObjectId(_id))
                    
        elif choice == "6":
            field = input("Enter field: ")
            value = input("Enter value: ")
            read_documents_by_condition(field,value)
            
        elif choice == "7":
            field = input("Enter field: ")
            oldvalue = input("Enter value: ")
            newvalue = input("Enter new value: ")
            updateOne({field : oldvalue}, collection, {field : newvalue})
            
        elif choice == "8":
            field = input("Enter field: ")
            oldvalue = input("Enter value: ")
            newvalue = input("Enter new value: ")
            updateMany({field : oldvalue}, collection, {field : newvalue})
            
        elif choice == "9":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteOne({field : value}, collection) 
            
        elif choice == "10":
            field = input("Enter field: ")
            value = input("Enter value: ")
            deleteMany({field : value}, collection)  
             
        elif choice == "11":
            print("Exiting...")
            quit()

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
