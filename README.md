HBNB - The Console
This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

Repository Contents by Project Task
TasksFilesDescription
0: Authors/README FileAUTHORSProject authors
1: Pep8N/AAll code is pep8 compliant
2: Unit Testing/testsAll class-defining modules are unittested
3. Make BaseModel/models/base_model.pyDefines a parent class to be inherited by all model classes
4. Update BaseModel w/ kwargs/models/base_model.pyAdd functionality to recreate an instance of a class from a dictionary representation
5. Create FileStorage class/models/engine/file_storage.py /models/_ init _.py /models/base_model.pyDefines a class to manage persistent file storage system
6. Console 0.0.1console.pyAdd basic functionality to console program, allowing it to quit, handle empty lines and ^D
7. Console 0.1console.pyUpdate the console with methods allowing the user to create, destroy, show, and update stored data
8. Create User classconsole.py /models/engine/file_storage.py /models/user.pyDynamically implements a user class
9. More Classes/models/user.py /models/place.py /models/city.py /models/amenity.py /models/state.py /models/review.pyDynamically implements more classes
10. Console 1.0console.py /models/engine/file_storage.pyUpdate the console and file storage system to work dynamically with all classes update file storage

General Use
First clone this repository.

Once the repository is cloned locate the console.py file and run it as follows:

/AirBnB_clone$ ./console.py
When this command is run the following prompt should appear:
(hbnb)
This prompt designates you are in the HBnB console. There are a variety of commands available within the console program.
Commands
* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)
