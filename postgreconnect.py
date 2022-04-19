import psycopg2

def runquery(sql):
    try:
        connection=psycopg2.connect(user="yfxpgallicmvhs",
                                    password="b42a0e5bddc705436e3b39271057b781cc398451ad2292d785d2311927cfbfa1",
                                    host="ec2-52-54-212-232.compute-1.amazonaws.com",
                                    database="dc802bu83sg0v6")
        cur=connection.cursor()
        cur.execute(sql)
        record = cur.fetchall()
        return(record)
    except:
        print("Error while fetching data")
    finally:
        cur.close()
        connection.close()
