import cx_Oracle
import os


DB_SERVER = os.environ.get("DB_SERVER")
DB_PORT = os.environ.get("DB_PORT")
DB_SERVICE_NAME = os.environ.get("DB_SERVICE_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

class dbOps:

    def fetchOneRecord(self, query):
        value = ""
        try:
            dsn_tns = cx_Oracle.makedsn(DB_SERVER, DB_PORT, service_name=DB_SERVICE_NAME)
            con = cx_Oracle.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn_tns, encoding='UTF-8')
            cur = con.cursor()
        except cx_Oracle.DatabaseError as error:
            module_logger.error("Failed to connect to Database ")
            module_logger.error(error)
            return False
        try:
            for row in cur.execute(query):
                value = row
            return value
        except cx_Oracle.Error as error:
            module_logger.error("Failed to fetch record ")
            module_logger.error(error)
            return False
        finally:
            cur.close()
            con.commit()
            con.close()




query = "select * from GES_NOVEGO_PROGRAM WHERE PERSON_ID=684393"
result = obj.fetchOneRecord(query)
print(maxjobid)
('684393', 'Depressions-Programm', datetime.datetime(2020, 5, 1, 0, 0))
print(type(maxjobid))
<class 'tuple'>
