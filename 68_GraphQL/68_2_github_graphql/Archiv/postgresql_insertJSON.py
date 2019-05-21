import psycopg2


conn=psycopg2.connect(dbname='hasuradb', user='postgres', password="", host="",port="5434")
cur = conn.cursor()
ur_dict ={
  "brand": "Ford2",
  "model": "Mustang2",
  "year": 1965
}
cur.execute("""INSERT INTO t_json (  c_json ) VALUES ( '{0}' ) """.format(json.dumps(ur_dict)))
 
cur.close()
 
conn.commit()
conn.close()