
# coding: utf-8

# ## Exploring Data with DataFrames and Spark SQL
# In this exercise, you will explore data using the Spark DataFrames API and Spark SQL.
# 
# ### Load Data Using an Explicit Schema
# To explore data, you must load it into a programmatic data object such as a DataFrame. If the structure of the data is known ahead of time, you can explicitly specify the schema for the DataFrame.
# 
# In this exercise, you will work with data that records details of flights.

# In[ ]:


from pyspark.sql.types import *

flightSchema = StructType([
  StructField("DayofMonth", IntegerType(), False),
  StructField("DayOfWeek", IntegerType(), False),
  StructField("Carrier", StringType(), False),
  StructField("OriginAirportID", IntegerType(), False),
  StructField("DestAirportID", IntegerType(), False),
  StructField("DepDelay", IntegerType(), False),
  StructField("ArrDelay", IntegerType(), False),
])

flights = spark.read.csv('wasb:///data/raw-flight-data.csv', schema=flightSchema, header=True)
flights.show()


# ### Infer a Data Schema
# If the structure of the data source is unknown, you can have Spark auomatically infer the schema.
# 
# In this case, you will load data about airports without knowing the schema.

# In[ ]:


airports = spark.read.csv('wasb:///data/airports.csv', header=True, inferSchema=True)
airports.show()


# ### Use DataFrame Methods
# Spark DataFrames provide functions that you can use to extract and manipulate data. For example, you can use the **select** function to return a new DataFrame containing columns selected from an existing DataFrame.

# In[ ]:


cities = airports.select("city", "name")
cities.show()


# ### Combine Operations
# You can combine functions in a single statement to perform multiple operations on a DataFrame. In this case, you will use the **join** function to combine the **flights** and **airports** DataFrames, and then use the **groupBy** and **count** functions to return the number of flights from each airport.

# In[ ]:


flightsByOrigin = flights.join(airports, flights.OriginAirportID == airports.airport_id).groupBy("city").count()
flightsByOrigin.show()


# ### Count the Rows in a DataFrame
# Now that you're familiar with working with DataFrames, a key task when building predictive solutions is to explore the data, determing statistics that will help you understand the data before building predictive models. For example, how many rows of flight data do you actually have?

# In[ ]:


flights.count()


# ### Determine Summary Statistics
# Predictive modeling is based on statistics and probability, so you will often start by looking at summary statistics. The **describe** function returns a DataFrame containing the **count**, **mean**, **standard deviation**, **minimum**, and **maximum** values for each numeric column.

# In[ ]:


flights.describe().show()


# ### Determine the Presence of Duplicates
# The data you have to work with won't always be perfect - often you'll want to *clean* the data; for example to detect and remove duplicates that might affect your model. You can use the **dropDuplicates** function to create a new DataFrame with the duplicates removed, enabling you to determine how many rows are duplicates of other rows.

# In[ ]:


flights.count() - flights.dropDuplicates().count()


# ### Identify Missing Values
# As well as determing if duplicates exist in your data, you should detect missing values, and either remove rows containing missing data or replace the missing values with a suitable relacement. The **dropna** function creates a DataFrame with any rows containing missing data removed - you can specify a subset of columns, and whether the row should be removed in *any* or *all* values are missing. You can then use this new DataFrame to determine how many rows contain missing values.

# In[ ]:


flights.count() - flights.dropDuplicates().dropna(how="any", subset=["ArrDelay", "DepDelay"]).count()


# ### Clean the Data
# Now that you've identified that there are duplicates and missing values, you can clean the data by removing the duplicates and replacing the missing values. The **fillna** function replaces missing values with a specified replacement value. In this case, you'll remove all duplicate rows and replace missing **ArrDelay** and **DepDelay** values with **0**.

# In[ ]:


data=flights.dropDuplicates().fillna(value=0, subset=["ArrDelay", "DepDelay"])
data.count()


# ### Check Summary Statistics
# After cleaning the data, you should re-check the statistics - removing rows and changing values may affect the distribution of the data, which in turn could affect any predictive models you might create.

# In[ ]:


data.describe().show()


# ### Explore Relationships in the Data
# Predictive modeling is largely based on statistical relationships between fields in the data. To design a good model, you need to understand how the data points relate to one another and identify any apparent correlation. The **corr** function calculates a correlation value between -1 and 1, indicating the strength of correlation between two fields. A strong positive correlation (near 1) indicates that high values for one column are often found with high values for the other, which a string negative correlation (near -1) indicates that *low* values for one column are often found with *high* values for the other. A correlation near 0 indicates little apparent relationship between the fields.

# In[ ]:


data.corr("DepDelay", "ArrDelay")


# ### Use Spark SQL
# In addition to using the DataFrame API directly to query data, you can persist DataFrames as table and use Spark SQL to query them using the SQL language. SQL is often more intuitive to use when querying tabular data structures.

# In[ ]:


data.createOrReplaceTempView("flightData")
spark.sql("SELECT DayOfWeek, AVG(ArrDelay) AS AvgDelay FROM flightData GROUP BY DayOfWeek ORDER BY DayOfWeek").show()


# ### Use the Inline SQL *Magic*
# Jupyter Notebooks support *magics*, which enable you to include inline code and functionality. For example, the **%%sql** magic enables you to write SQL queries and visualize the results directly in the notebook.
# 
# Run the following query, and view the table of results that is returned.

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT DepDelay, ArrDelay FROM flightData')


# Change the **Table** visualization of results above to a **Scatter** visualization to see the relationship between the **DepDelay** and **ArrDelay** values more clearly (use the **-** function to plot the actual values) - visualizations like this make it easier to show relationships as apparent *structure* in the data. For example, the positive correlation between **DepDelay** and **ArrDelay** seems to be a linear relationsip, creaing a diagonal line of plotted points.

# ### Query Multiple Tables
# You can create and query multiple temporary tables. Run the cells below to create a temporary table from the **airports** DataFrame, and then use an inline query to query it together with the flights data.

# In[ ]:


airports.createOrReplaceTempView("airportData")


# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT a.name, AVG(f.ArrDelay) AS avgdelay\nFROM flightData AS f JOIN airportData AS a\nON f.DestAirportID = a.airport_id\nGROUP BY a.name')


# As you saw previously, it can sometimes be useful to visualize the results of a query. Change the visualization above to a **Bar** chart, using the **-** function, to see the everage lateness (or earliness) of flights at all destinations.
