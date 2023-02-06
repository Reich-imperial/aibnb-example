![alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230206%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230206T144320Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b0f41cdf03f111851606c5ddd0b8d2c8f562fd3d1d9dcdc8f729cff09db2b32e)
# Project Description
This project is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB.

The project currently only implements the back-end console.

# Description of the command interpreter
The interface of the application is similar to Bash shell. The difference is that it has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:

- show
- create
- update
- destroy
- count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

- Creating new objects (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object

## How to start it
These instructions will enable a copy of the project to run on your local machine (Linux distro) for development and testing purposes.

### Installing
Clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
```
git clone https://github.com/jzamora5/AirBnB_clone.git
```
The following files will be contained in the cloned repository:

<blockquote>
/console.py: The main executable of the project, the command interpreter.

models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances

models/__ init __.py: A unique FileStorage instance for the application

models/base_model.py: Class that defines all common attributes/methods for other classes.

models/user.py: User class that inherits from BaseModel

models/state.py: State class that inherits from BaseModel

models/city.py: City class that inherits from BaseModel

models/amenity.py: Amenity class that inherits from BaseModel

models/place.py: Place class that inherits from BaseModel

models/review.py: Review class that inherits from BaseModel
</blockquote>



**Command** |	**Description**
-|-
**quit or EOF**	| Exits the program
**Usage**	| By itself
**---** | **---**
**help** | Provides a text describing how to use a command
**Usage**	| By itself --or-- **help \<command\>**
**---** | **---**
**create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`. Valid classes are: `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, `Review`
**Usage**	| **create \<class name\>**
**---** | **---**
**show**	| Prints the string representation of an instance based on the class name and `id`
**Usage** |	**show \<class name\> \<id\> --or-- \<class name\>.show(\<id\>)**
**---** | **---**
**destroy**	| Deletes an instance based on the class name and id (saves the change into a JSON file).
**Usage**	| **destroy \<class name\> \<id\> --or-- .destroy()**
**---** | **---**
**all**	| Prints all string representation of all instances based or not on the class name.
**Usage** |	By itself or **all \<class name\> --or-- \<class name\>.all()**
**---** | **---**
**update** | Updates an instance based on the class name and id by adding or updating attribute (saves the changes into a JSON file).
**Usage**	| **update \<class name\> \<id\> \<attribute name\> "\<attribute value\>" ---or--- \<class name\>.update(\<id\>, \<attribute name\>, \<attribute value\>) --or-- \<class name\>.update(\<id\>, \<dictionary representation\>)**
**---** | **---**
**count**	| Retrieve the number of instances of a class.
**Usage**	| **\<class name\>.count()**
