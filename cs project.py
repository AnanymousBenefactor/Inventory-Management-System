import mysql.connector as sql
x=sql.connect(host="localhost",user="root",passwd="DeviPython03#",database="ims8")
cur=x.cursor()


"""cur.execute("create table grocery (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
cur.execute("create table electronics (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
cur.execute("create table clothing (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
cur.execute("create table beauty_store (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
cur.execute("create table stationary (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
cur.execute("create table schoolneeds (pdt_name char(50),pdt_size integer,specifications char(250),mfd date,expiry_date date,cost decimal(4),price decimal(4),category char(20),hsn_code integer(5),location char(55),availability integer,in_Stock char(20))")
print("success")"""
def insert_rec():
      
      print('''1.to insert in grocery
2.to insert in electronics
3.to insert into clothing
4.to insert into beauty_store
5.to insert into stationary
6.to insert into schoolneeds''')
      ch=int(input("enter your choice:"))
      if ch==1:
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=int(input("enter hsn code:"))
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO grocery values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            
            
      if ch==2:
            
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=int(input("enter hsn code:"))
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO electronics values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #create list of values typed from user to insert in Product table
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            
      if ch==3:
            
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=int(input("enter hsn code:"))
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO clothing values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #create list of values typed from user to insert in Product table
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            
      if ch==4:
            
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=int(input("enter hsn code:"))
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO beauty_store values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #create list of values typed from user to insert in Product table
            val = (pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            
      if ch==5:
            
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=input("enter hsn code:")
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO stationary values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #create list of values typed from user to insert in Product table
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            
      if ch==6:
            
            pName=input("Enter Product Name:")
            pQty=int(input("Enter Product Qty:"))
            spec=input("enter product details:")
            mfd=input("enter mfd:")
            expd=input("expiry date:")
            cp=int(input("enter cost price:"))
            sp=int(input("Enter selling Price:"))
            cat=input("enter category:")
            hsn=int(input("enter hsn code:"))
            loc=input("enter location:")
            ava=int(input("enter availability:"))
            isl=input("enter whether pdt is in stock or not (y/n):")
            #create the Insert query
            sql = "INSERT INTO schoolneeds values('{}',{},'{}','{}','{}',{},{},'{}',{},'{}',{},'{}')".format(pName,pQty,spec,mfd,expd,cp,sp,cat,hsn,loc,ava,isl)
            #create list of values typed from user to insert in Product table
            #Execute query with values
            cur.execute(sql)
            #commit for permanent storage in database
            x.commit()
            

def update():
    
      print('''1.to update in grocery
2.to update in electronics
3.to update in clothing
4.to update in beauty_store
5.to update in stationary
6.to update in schoolneeds''')
      ch=int(input("enter your choice:"))
      if ch==1:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update grocery set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update grocery set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update grocery set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update grocery set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update grocery set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update grocery set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update grocery set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update grocery set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': #j=ava k=isl
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update grocery set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update grocery set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update grocery set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
      if ch==2:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update electronics set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update electronics set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update electronics set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update electronics set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update electronics set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update electronics set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update electronics set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update electronics set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': #j=ava k=isl
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update electronics set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update electronics set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update electronics set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
      elif ch==3:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update clothing set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update clothing set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update clothing set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update clothing set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update clothing set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update clothing set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update clothing set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update clothing set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': 
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update clothing set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update clothing set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update clothing set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
      elif ch==4:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update beauty_store set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update beauty_store set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update beauty_store set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update beauty_store set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update beauty_store set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update beauty_store set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update beauty_store set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update beauty_store set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': 
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update beauty_store set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update beauty_store set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update beauty_store set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
      elif ch==5:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update stationary set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update stationary set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update stationary set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update stationary set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update stationary set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update stationary set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update stationary set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update stationary set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': 
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update stationary set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update stationary set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update stationary set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
      elif ch==6:
            print("which column you want to update a) pname/b)pqty/c)spec/d)mfd/e)expd/f)cp/g)sp/h)cat/i)loc/j)ava/k)isl:")
            ch=input("enter any letter in a-k:")
            if ch=='a' or ch=='A':
                  hsn=int(input("enter hsn:"))
                  pname=input("enter pname:")
                  cur.execute("update schoolneeds set pdt_name='{}'where hsn_code={}".format(pname,hsn))
                  x.commit()
            if ch=='b' or ch=='B':
                  hsn=int(input("enter hsn:"))
                  pqty=int(input("enter pqty:"))
                  cur.execute("update schoolneeds set pdt_size={} where hsn_code={}".format(pqty,hsn))
                  x.commit()
            if ch=='c' or ch=="C":
                  hsn=int(input("enter hsn:"))
                  spec=input("enter spec:")
                  cur.execute("update schoolneeds set specifications='{}' where hsn_code={}".format(spec,hsn))
                  x.commit()
            if ch=='d' or ch=="D":
                  hsn=int(input("enter hsn:"))
                  mfd=input("enter date in YYYY-MM-DD format:")
                  cur.execute("update schoolneeds set mfd='{}' where hsn_code={}".format(mfd,hsn))
                  x.commit()
            if ch=='e' or ch=="E":
                  hsn=int(input("enter hsn:"))
                  expd=input("enter expd date:")
                  cur.execute("update schoolneeds set expiry_date='{}' where hsn_code={}".format(expd,hsn))
                  x.commit()
            if ch=='f' or ch=='F':
                  hsn=int(input("enter hsn:"))
                  cp=int(input("enter cost price:"))
                  cur.execute("update schoolneeds set cost={} where hsn_code={}".format(cp,hsn))
                  x.commit()
            if ch=='g' or ch=="G":
                  hsn=int(input("enter hsn:"))
                  sp=int(input("enter selling price:"))
                  cur.execute("update schoolneeds set price={} where hsn_code={}".format(sp,hsn))
                  x.commit()
            if ch=='h' or ch=="H":
                  hsn=int(input("enter hsn:"))
                  cat=input("enter category:")
                  cur.execute("update schoolneeds set category='{}' where hsn_code={}".format(cat,hsn))
                  x.commit()
            if ch=='i' or ch=='I': 
                  hsn=int(input("enter hsn:"))
                  loc=input("enter location:")
                  cur.execute("update schoolneeds set location='{}' where hsn_code={}".format(loc,hsn))
                  x.commit()
            if ch=='j' or ch=="J":
                  hsn=int(input("enter hsn:"))
                  ava=int(input("enter availability:"))
                  cur.execute("update schoolneeds set availability={} where hsn_code={}".format(ava,hsn))
                  x.commit()
            if ch=='k' or ch=='K':
                  hsn=int(input("enter hsn:"))
                  isl=input("enter whether pdt is in stock or not:")
                  cur.execute("update schoolneeds set in_stock={} where hsn_code={}".format(isl,hsn))
                  x.commit()
def display():
       print('''1.to display from grocery
2.to display from electronics
3.to display from clothing
4.to display from beauty_store
5.to display from stationary
6.to display from schoolneeds''')
       ch=int(input("enter choice 1-6:"))
       if ch==1:
             cur.execute("select * from grocery")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   
       elif ch==2:
             cur.execute("select * from electronics")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   

       elif ch==3:
             cur.execute("select * from clothing")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   

       elif ch==4:
             cur.execute("select * from beauty_store")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   

       elif ch==5:
             cur.execute("select * from stationary")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   

       elif ch==6:
             cur.execute("select * from schoolneeds")
             x=cur.fetchall()
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             print("prod name      Prod size    spec          mfd          expd        cp      sp    cat        hsn       loc   availability     in stock                                 ")
             print("------------------------------------------------------------------------------------------------------------------------------------------")
             for i in x:
                   print(i[0],"      " ,i[1],"    "  ,i[2],   "     ",i[3],"       "  ,i[4],"     "  ,i[5],"    ",i[6],"    ",i[7],"  ",i[8],"    "  ,i[9],"   "  ,i[10],"   "  ,i[11])
                   

       else:
             print("invalid choice:")
def delete():
       print('''1.to display from grocery
2.to display from electronics
3.to display from clothing
4.to display from beauty_store
5.to display from stationary
6.to display from schoolneeds''')
       ch=int(input("enter choice 1-6:"))
       if ch==1:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from grocery where hsn_code={}".format(hsn))
             x.commit()
       elif ch==2:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from electronics where hsn_code={}".format(hsn))
             x.commit()
       elif ch==3:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from clothing where hsn_code={}".format(hsn))
             x.commit()
       elif ch==4:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from beauty_store where hsn_code={}".format(hsn))
             x.commit()
       elif ch==5:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from stationary where hsn_code={}".format(hsn))
             x.commit()
       elif ch==6:
             hsn=int(input("enter hsn code:"))
             cur.execute("delete from schoolneeds where hsn_code={}".format(hsn))
             x.commit()
       else:
             print("invalid choice!!!!")


#_main_

print("""****************************************************
enter choice 1 for inserting records
enter choice 2 for updating records
enter choice 3 for displaying records
enter choice 4 for deleting records
enter choice 5 to exit the program
****************************************************""")

while True:
      c=int(input("enter a choice:"))
      if c==1:
            insert_rec()
      elif c==2:
            update()
      elif c==3:
            display()
      elif c==4:
            delete()
      elif c==5:
            print("exiting the program thanks for visiting :) !!")
            break
else:
      print(":)")
      
             
             
