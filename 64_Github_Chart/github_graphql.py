# An example to get the remaining rate limit using the Github GraphQL API.

import requests

# main_with_json.py
import json

with open('/home/danny/OneDrive/DataScience/10_Secrets/Github/github_confi.json', 'r') as f:
    config= json.load(f)

token = config['DEFAULT']['SECRET_KEY'] 


headers = {"Authorization": token}



def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       


query = """
{
  repository(name: "DannyJRa.github.io", owner: "DannyJRa") {
    ref(qualifiedName: "master") {
      target {
        ... on Commit {
          id
          history(first: 5) {
            pageInfo {
              hasNextPage
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

###Save json
with open('github.json', 'w') as f:  # writing JSON object
    json.dump(result, f,indent=4)



### Save in database
import psycopg2

import datetime as dt
from dateutil.tz import gettz
import time
unix_time = time.time()


datetime = dt.datetime.fromtimestamp(unix_time, gettz("Europe/London"))



S_DB_PWD = config['DATABASE']['PWD'] 
S_DB_HOST = config['DATABASE']['HOST'] 

conn=psycopg2.connect(dbname='hasuradb', user='postgres', password=S_DB_PWD, host=S_DB_HOST,port="5434")
cur = conn.cursor()

ur_dict ={
  "brand": "Github",
  "model": result,
  "year": datetime
}
cur.execute("""INSERT INTO t_json (  c_json ) VALUES ( '{0}' ) """.format(json.dumps(ur_dict)))
 
cur.close()
 
conn.commit()
conn.close()



#remaining_rate_limit = result["data"]["rateLimit"]["remaining"] # Drill down the dictionary
#print("Remaining rate limit - {}".format(remaining_rate_limit))




