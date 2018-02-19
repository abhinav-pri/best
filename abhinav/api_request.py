"""code to request Api"""
import requests,json,xlsxwriter,MySQLdb

	


def dbaseentry(information):
##################################################################
#####################################################################
 db=MySQLdb.connect("localhost","testuser","test623","testdb")
 cursor =db.cursor()
 cursor.execute("DROP TABLE IF EXISTS STORE_INFO")
 sql="""CREATE TABLE STORE_INFO(
        STORE_ID VARCHAR(100) NOT NULL,
        REGISTRATION_ID VARCHAR(100),
        PHONE_NO VARCHAR(100),
        NAME VARCHAR(100),
        WARRANTY  VARCHAR(100),
        STATE VARCHAR(100),
        UPDATE_DATE VARCHAR(100),
        CREATE_DATE VARCHAR(100),
        CITY VARCHAR(100),
        Is_VERIFIED VARCHAR(100),
        LAT VARCHAR(100),
        LON VARCHAR(100)
        )"""
   
 cursor.execute(sql)        
 for values in information:
  cursor.execute("INSERT INTO STORE_INFO VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (values[0], values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9],values[10],values[11]))

 
 db.commit()
 db.close()      






##################################################################	
########################################################################
def writexlsheet(information):
 workbook = xlsxwriter.Workbook("day1.xlsx")
 worksheet = workbook.add_worksheet()
 row = 0
 col = 0
 worksheet.write(row,col,"store_id")
 worksheet.write(row,col+1,"registration_id")
 worksheet.write(row,col+2,"phoneNos")
 worksheet.write(row,col+3,"name")
 worksheet.write(row,col+4,"warranty")
 worksheet.write(row,col+5,"state")
 worksheet.write(row,col+6,"updated_at")
 worksheet.write(row,col+7,"created_at")
 worksheet.write(row,col+8,"city")
 worksheet.write(row,col+9,"is_verified")
 worksheet.write(row,col+10,"lat")
 worksheet.write(row,col+11,"lon")
 
 
 
 
 row+=1
  
 for values in information:
	 inc=0
	 for r in values:
		 worksheet.write(row,col+inc,r)
		 inc+=1
	 row+=1	 
		 
	 
	 
	 





 workbook.close()
 

def dats(data):
 
 r=requests.post("http://139.162.30.235/stores/search/", data=json.dumps(data), headers={"Content-type": "application/json"})

 information=[]
 if(r.json()["success"]==True):
   store_info=r.json()["data"]

   for r in  store_info:

       store_id=r["store_id"]

       registration_id=r["registration_id"]
       phoneNos=r["phoneNos"][0]
       name=r["name"]
       warranty=r["warranty"]
       state=r["state"]
       updated_at=r["updated_at"]
       created_at=r["created_at"]
       city=r["city"]
       is_verified=r["is_verified"]
       lat=r["location"]["lat"]
       lon=r["location"]["lon"]
       data_store=[str(store_id),str(registration_id),str(phoneNos),str(name),str(warranty),str(state),str(updated_at),str(created_at),str(city),str(is_verified),str(lat),str(lon)]
       information.append(data_store)    
 else:
	 print("not available")
	  
 writexlsheet(information)
 dbaseentry(information)
 
  

######writing data###########

if __name__== "__main__":
	data={}
	
	
	val=str(raw_input(" enter the option "))
	data[val]=str(raw_input(" enter the value of  "+val))
	
	
	dats(data)
