import pandas as pd

lst=[]

dict1={"Name":"Harshal","Salary":25000, "Id":"HRK5" }
lst.append(dict1)

dict2={"Name":"Prathamesh","Salary":23000, "Id":"PAK2"}
lst.append(dict2)

dict3={"Name":"Ayush","Salary":20000, "Id":"AAA3" }
lst.append(dict3)

df=pd.DataFrame(lst)

print(df)

