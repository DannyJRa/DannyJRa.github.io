# An example to get the remaining rate limit using the Github GraphQL API.
import os
try:
	os.chdir(os.path.join(os.getcwd(), '68_2_github_graphql'))
	print(os.getcwd())
except:
	pass

import requests

# main_with_json.py
import json

with open('/home/danny/OneDrive/DataScience/10_Secrets/Github/github_confi.json', 'r') as f:
    config= json.load(f)




def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

token = config['DEFAULT']['SECRET_KEY'] 
headers = {"Authorization": token}
        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       


query = """
{
  repository(name: "DannyJRa.github.io", owner: "DannyJRa") {
    ref(qualifiedName: "master") {
      target {
        ... on Commit {
          id
          history(first: 100) {
            pageInfo {
              hasNextPage
              endCursor
            }
            edges {
              node {
                messageHeadline
                oid
                message
                author {
                  name
                  email
                  date
                }
              }
            }
          }
        }
      }
    }
  }
}
"""












result = run_query(query) # Execute the query
type(result)

#Load to dictionary
github_dict = result#json.loads(result)

### Save json
with open('github.json', 'w') as f:  # writing JSON object
    json.dump(result, f,indent=4)

###Extract info
from glom import glom
messages=glom(github_dict,("data.repository.ref.target.history.edges",['node.message']))
dates=glom(github_dict,("data.repository.ref.target.history.edges",['node.author.date']))

dict = {'message': messages, 'date': dates}  
    
import pandas as pd
df = pd.DataFrame(dict) 
    
print(df.shape)

df['datetime'] = pd.to_datetime(df['date'])
df=df.drop(columns=['date'])
github_commits=df


### Open csv
#import csv

#with open('github_test.csv', 'rb') as csvfile:
#    github_csv = csv.reader(csvfile, delimiter=';')

### Save in database
import psycopg2



S_DB_PWD = config['DATABASE']['PWD'] 
S_DB_HOST = config['DATABASE']['HOST'] 

# con=psycopg2.connect(dbname='hasuradb', user='postgres', password=S_DB_PWD, host=S_DB_HOST,port="5434")
# #cur = conn.cursor()

# ###############
# with con:

#     cur = con.cursor()

#     cur.execute("DROP TABLE IF EXISTS github_commits")
#     cur.execute("CREATE TABLE github_commits(id SERIAL PRIMARY KEY, date TIMESTAMP, title VARCHAR(255))")

#     query = "INSERT INTO cars (id, date, title) VALUES (%s, %s, %s)"
#     cur.executemany(query, github_csv)

#     con.commit()



#import pandas as pd
#github_commits=pd.read_csv('github_test.csv', sep=';')



# ur_dict ={
#   "brand": "Github",
#   "model": result,
#   "year": datetime
# }
# cur.execute("""INSERT INTO t_json (  c_json ) VALUES ( '{0}' ) """.format(json.dumps(ur_dict)))
 
# cur.close()
 
# conn.commit()
# conn.close()



#remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
#print("Remaining rate limit - {}".format(remaining_rate_limit))




### SQLALchemy
import sqlalchemy  # Package for accessing SQL databases via Python
#dialect+driver://username:password@host:port/database
# Connect to database (Note: The package psychopg2 is required for Postgres to work with SQLAlchemy)
engine = sqlalchemy.create_engine(f'postgresql://postgres:{S_DB_PWD}@{S_DB_HOST}:5434/hasuradb')
con = engine.connect()

# Verify that there are no existing tables
print(engine.table_names())

table_name = 'github_commits'
github_commits.to_sql(table_name, con,if_exists='replace')
print("Success")