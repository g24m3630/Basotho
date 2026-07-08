

# University Student Database Management System (MongoDB CRUD)

A comprehensive command-line interface (CLI) application built with Python and PyMongo to manage a student record database hosted on MongoDB Atlas. This system supports robust CRUD operations, complex array manipulation, logical/comparison queries, and custom aggregation pipelines.

## Features

- **Full CRUD Support:** Create (single/many), Read (all, by ID, by condition), Update (single/many), and Delete (single/many) student records.
- **Advanced Query Operators:** Filter records using logical (`$and`, `$or`, `$not`), comparison (`$gt`, `$lt`), and element (`$in`, `$exists`) operations.
- **Array Manipulation:** Append (`$push`) or remove (`$pull`) embedded values inside complex document lists such as `advisors` or `enrolled_courses`.
- **Aggregation Pipelines:** Run complex multi-stage aggregations to query total student enrollments per course, or sort and isolate the top 10 students inside specific course divisions.
- **Interactive Menu System:** Fully driven command-line dashboard allowing users to select and test tasks seamlessly.

---

## Document Schema Strategy

The application handles highly structured MongoDB documents with embedded objects and nested arrays. Below is an example structure representing the target schema used:

```json
{
  "_id": "ObjectId('...')",
  "name": "Student Name",
  "student_id": "ST123456",
  "contact_info": {
    "email": "student@university.ac.za",
    "phone": "0123456789"
  },
  "enrolled_courses": [
    {
      "course_id": "ObjectId('...')",
      "course_code": "CS301",
      "semester": "Semester 1",
      "grade": "75",
      "status": "Enrolled"
    }
```
## Prerequisites
Before running the application, ensure you have the following installed:

Python 3.8 or higher

## Access to a MongoDB database environment (such as a MongoDB Atlas Cluster)

Installation & Setup
Clone or copy the project files to your local workspace directory.

Install Required Dependencies:
Install the official MongoDB driver for Python (pymongo) using pip:

```Bash
pip install pymongo
```
## Configure Database Connection:
Open the Python script and locate the Database Connection setup block. Replace the default connection URI string with your actual cluster connection string:

Python
client = MongoClient("your-mongodb-atlas-connection-string-here")

How To Run
Execute the main script via your terminal:

```Bash
python your_script_name.py
```
## Error Handling
All processing routines inside the script are decoupled using dedicated try-except blocks. If database connection drops, syntax verification fails, or an incorrect ObjectId formatting mismatch happens, the program prints the captured runtime error to the console without crashing the running interface wrapper.
  ],
  "advisors": ["Advisor_ID_1", "Advisor_ID_2"]
}
