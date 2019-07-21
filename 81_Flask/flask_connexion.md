# FLask with Connexion

The goal of this article is to show you how to use Python 3, Flask, and Connexion to build useful REST APIs that can include input and output validation, and provide Swagger documentation.

## Benefits of Connexion
That worked to demonstrate how the Connexion module helps you build a nice REST API along with interactive documentation.

	
### Swagger UI
The Swagger UI
Now you have a simple web API running with a single URL endpoint. At this point, it would be reasonable to think, “configuring this with the swagger.yml file was cool and all, but what did it get me?”
You’d be right to think that. We haven’t taken advantage of the input or output validation. All that swagger.yml gave us was a definition for the code path connected to the URL endpoint. However, what you also get for the extra work is the creation of the Swagger UI for your API.
If you navigate to localhost:5000/api/ui, the system will bring up a page that looks something like this:
	
This can be extremely useful when the API is complete as it gives you and your API users a way to explore and experiment with the API without having to write any code to do so.
Building an API this way is very useful to me at work. Not only is the Swagger UI useful as a way to experiment with the API and read the provided documentation, but it’s also dynamic. Any time the configuration file changes, the Swagger UI changes as well.
In addition, the configuration offers a nice, clean way to think about and create the API URL endpoints. I know from experience that APIs can develop in a sometimes random manner over time, making finding the code that supports the endpoints, and coordinating them, difficult at best.
By separating the code from the API URL endpoint configuration, we decouple one from the other. This alone has been very useful to me in my work building API systems supporting single page web applications.
	



## Frontend: Ajax
	
You’ll create a web application that displays the people on screen as well as allows the user to create new people, update existing people, and delete people. This will all be handled by AJAX calls from JavaScript to the people API URL endpoints.
	
Source: <https://realpython.com/flask-connexion-rest-api/#example-code> 
	
# Peristent data store

## SQLAlchemy
SQLAlchemy provides an Object Relational Model (ORM), which stores Python objects to a database representation of the object’s data. That can help you continue to think in a Pythonic way and not be concerned with how the object data will be represented in a database.
	

	
	
### Database Interaction
#### Raw SQL
A SQL query getting all of the data in our person table, sorted by last name, would look this this:
	SELECT * FROM person ORDER BY 'lname';
This query tells the database engine to get all the fields from the person table and sort them in the default, ascending order using the lname field.
If you were to run this query against a SQLite database containing the person table, the results would be a set of records containing all the rows in the table, with each row containing the data from all the fields making up a row. Below is an example using the SQLite command line tool running the above query against the person database table:
sqlite> SELECT * FROM person ORDER BY lname;

		
	
#### SQLALchemy[^1]
Object Oriented Programming allows you to connect data together with behavior, the functions that operate on that data. By creating SQLAlchemy classes, you’re able to connect the fields from the database table rows to behavior, allowing you to interact with the data. Here’s the SQLAlchemy class definition for the data in the person database table:
	class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, 
                          primary_key=True)
    lname = db.Column(db.String)
    fname = db.Column(db.String)
    timestamp = db.Column(db.DateTime, 
                          default=datetime.utcnow, 
                          onupdate=datetime.utcnow)

The class Person inherits from db.Model, which you’ll get to when you start building the program code. For now, it means you’re inheriting from a base class called Model, providing attributes and functionality common to all classes derived from it.
	
The rest of the definitions are class-level attributes defined as follows:
		 __tablename__ = 'person' connects the class definition to the person database table.
		 person_id = db.Column(db.Integer, primary_key=True) creates a database column containing an integer acting as the primary key for the table. This also tells the database that person_id will be an autoincrementing Integer value.
		 lname = db.Column(db.String) creates the last name field, a database column containing a string value.
		 fname = db.Column(db.String) creates the first name field, a database column containing a string value.
		 timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) creates a timestamp field, a database column containing a date/time value. The default=datetime.utcnow parameter defaults the timestamp value to the current utcnow value when a record is created. The onupdate=datetime.utcnowparameter updates the timestamp with the current utcnow value when the record is updated.
	
Note: UTC Timestamps
You might be wondering why the timestamp in the above class defaults to and is updated by the datetime.utcnow() method, which returns a UTC, or Coordinated Universal Time. This is a way of standardizing your timestamp’s source.
The source, or zero time, is a line running north and south from the Earth’s north to south pole through the UK. This is the zero time zone from which all other time zones are offset. By using this as the zero time source, your timestamps are offsets from this standard reference point.
Should your application be accessed from different time zones, you have a way to perform date/time calculations. All you need is a UTC timestamp and the destination time zone.
If you were to use local time zones as your timestamp source, then you couldn’t perform date/time calculations without information about the local time zones offset from zero time. Without the timestamp source information, you couldn’t do any date/time comparisons or math at all.
Working with a timestamps based on UTC is a good standard to follow. Here’s a toolkitsite to work with and better understand them.
	

	
Where are you heading with this Person class definition? The end goal is to be able to run a query using SQLAlchemy and get back a list of instances of the Person class. As an example, let’s look at the previous SQL statement:
	SELECT * FROM people ORDER BY lname;
	Show the same small example program from above, but now using SQLAlchemy:
 from models import Person
 
 people = Person.query.order_by(Person.lname).all()
 for person in people:
      print(f'{person.fname} {person.lname}')
	

	
	
	


## Serialization
Working with SQLAlchemy modeled data inside your programs is very convenient. It is especially convenient in programs that manipulate the data, perhaps making calculations or using it to create presentations on screen. Your application is a REST API essentially providing CRUD operations on the data, and as such it doesn’t perform much data manipulation.
The REST API works with JSON data, and here you can run into an issue with the SQLAlchemy model. Because the data returned by SQLAlchemy are Python class instances, Connexion can’t serialize these class instances to JSON formatted data. Remember from Part 1 that Connexion is the tool you used to design and configure the REST API using a YAMLfile, and connect Python methods to it.
	
In this context, serializing means converting Python objects, which can contain other Python objects and complex data types, into simpler data structures that can be parsed into JSON datatypes, which are listed here:
		• string: a string type
		• number: numbers supported by Python (integers, floats, longs)
		• object: a JSON object, which is roughly equivalent to a Python dictionary
		• array: roughly equivalent to a Python List
		• boolean: represented in JSON as true or false, but in Python as True or False
		• null: essentially a None in Python
	
	
	
#### Marshmallow
Marshmallow provides functionality to serialize and deserialize Python objects as they flow out of and into our JSON-based REST API. Marshmallow converts Python class instances to objects that can be converted to JSON.
		
Your Person class is simple enough so getting the data attributes from it and creating a dictionary manually to return from our REST URL endpoints wouldn’t be very hard. In a more complex application with many larger SQLAlchemy models, this wouldn’t be the case. A better solution is to use a module called Marshmallow to do the work for you.
		

[^1]: Adopted from <https://realpython.com/flask-connexion-rest-api-part-2/> 
