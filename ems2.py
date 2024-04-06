from tkinter import *
from sqlite3 import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt

def mtoa():
	mw.withdraw()
	aw.deiconify()
def atom():
	aw.withdraw()
	mw.deiconify()
def mtov():
	mw.withdraw()
	vw.deiconify()
	viewt()
def vtom():
	vw.withdraw()
	mw.deiconify()
	scroll_vw.delete(1.0,END)
def mtod():
	mw.withdraw()
	dw.deiconify()
def dtom():
	dw.withdraw()
	mw.deiconify()
def mtou():
	mw.withdraw()
	uw.deiconify()
def utom():
	uw.withdraw()
	mw.deiconify()

def save():
	id=entid_aw.get()
	name=entname_aw.get()
	salary=entsalary_aw.get()
	if name.strip()=="" or id.strip()=="" or salary.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		entid_aw.delete(0,END)
		entname_aw.delete(0,END)
		entsalary_aw.delete(0,END)
		entid_aw.focus()
		entname_aw.focus()
		entsalary_aw.focus()
	elif len(name.strip())>30 or len(salary.strip())>8:
		showinfo("Mistake","You can't enter so big name or big salary")
		entname_aw.delete(0,END)
		entsalary_aw.delete(0,END)
		entname_aw.focus()
		entsalary_aw.focus()
	elif not(id.isdigit()) or not(name.strip().isalpha()) or not(salary.isdigit()):
		showinfo("Mistake","Your id and salary should have digits and name should have alphabets only")
		entid_aw.delete(0,END)
		entname_aw.delete(0,END)
		entsalary_aw.delete(0,END)
		entid_aw.focus()
		entname_aw.focus()
		entsalary_aw.focus()
	elif int(id)<1 or int(salary)<1:
		showinfo("Mistake","id or salary entered wrong")
		entid_aw.delete(0,END)
		entsalary_aw.delete(0,END)
		entid_aw.focus()
		entsalary_aw.focus()
	else:
		con=None
		try:
			id=int(id)
			salary=int(salary)
			con=connect("database_name.db")
			cursor=con.cursor()
			sql="insert into table_name values('%d','%s','%d')"
			cursor.execute(sql % (id,name,salary))
			showinfo("Success","Record Created")
			con.commit()  
			entid_aw.delete(0,END)
			entname_aw.delete(0,END)
			entsalary_aw.delete(0,END)
			entid_aw.focus()
			entname_aw.focus()
			entsalary_aw.focus() 
		except Exception as e:
			showerror("Error",e)
			con.rollback() 
		finally:
			if con is not None:
				con.close()

def updatet():
	idu=uw_entid.get()
	nameu=entname_uw.get()
	salaryu=entsalary_uw.get()
	if nameu.strip()=="" or idu.strip()=="" or salaryu.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		uw_entid.delete(0,END)
		entname_uw.delete(0,END)
		entsalary_uw.delete(0,END)
		uw_entid.focus()
		entname_uw.focus()
		entsalary_uw.focus()
	elif len(nameu.strip())>30 or len(salaryu.strip())>8:
		showinfo("Mistake","You can't enter so big name or big salary")
		entname_uw.delete(0,END)
		entsalary_uw.delete(0,END)
		entname_uw.focus()
		entsalary_uw.focus()
	elif not(idu.isdigit()) or not(nameu.strip().isalpha()) or not(salaryu.isdigit()):
		showinfo("Mistake","Your id and salary should have digits and name should have alphabets only")
		uw_entid.delete(0,END)
		entname_uw.delete(0,END)
		entsalary_uw.delete(0,END)
		uw_entid.focus()
		entname_uw.focus()
		entsalary_uw.focus()
	elif int(idu)<1 or int(salaryu)<1:
		showinfo("Mistake","id or salary entered wrong")
		uw_entid.delete(0,END)
		entsalary_uw.delete(0,END)
		uw_entid.focus()
		entsalary_uw.focus()
	else:
		con=None
		try:
			idu=int(idu)
			salaryu=int(salaryu)
			con=connect("database_name.db")
			cursor=con.cursor()
			sql="update table_name set id='%d',name='%s',salary='%d' where id='%d' "
			cursor.execute(sql % (idu,nameu,salaryu,idu))
			showinfo("Success","Record Updated")
			con.commit()  
			uw_entid.delete(0,END)
			entname_uw.delete(0,END)
			entsalary_uw.delete(0,END)
			uw_entid.focus()
			entname_uw.focus()
			entsalary_uw.focus() 
		except Exception as e:
			showerror("Error",e)
			con.rollback() 
		finally:
			if con is not None:
				con.close()


def viewt():
	con=None
	try:
		con=connect("database_name.db")
		cursor=con.cursor()
		sql="select * from table_name"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			scroll_vw.insert(END,"id: "+str(d[0])+" name: "+str(d[1])+" salary: "+str(d[2])+'\n')
	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()

def deletet():
	idd=dw_entid.get()
	if idd.strip()=="":
		showinfo("Mistake","Don't leave blank spaces")
		dw_entid.delete(0,END)
		dw_entid.focus()	
	elif not(idd.isdigit()):
		showinfo("Mistake","Your id should have digits only")
		dw_entid.delete(0,END)
		dw_entid.focus()
	elif int(idd)<1:
		showinfo("Mistake","id entered wrong")
		dw_entid.delete(0,END)
		dw_entid.focus()
	else:
		con=None
		try:
			idd=int(idd)
			con=connect("database_name.db")
			cursor=con.cursor()
			sql="delete from table_name where id='%d' "
			cursor.execute(sql % (idd))
			if cursor.rowcount==1:
				con.commit()  
				showinfo("Success","record deleted") 
			else:
				showinfo("Success","record does not exist")
			dw_entid.delete(0,END)
			dw_entid.focus()
		except Exception as e:
			showerror("Error",e)
			con.rollback() 
		finally:
			if con is not None:
				con.close()

def create_chart():
	con =connect("database_name.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM table_name ORDER BY salary DESC LIMIT 5")
	data = cursor.fetchall()
	con.close()
	if not data:
		showerror("Error","No data found")
	names,salaries=[],[]
	for d in data:
		names.append(d[1])
		salaries.append(d[2])
	plt.bar(names, salaries)
	plt.xlabel('Employee Names')
	plt.ylabel('Salary')
	plt.title('Employee Salary Chart')
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.show()

mw=Tk()
mw.title("Employee Management System")
mw.geometry("500x700+500+100")
mw.configure(bg="aquamarine")
mw.resizable(False, False)

f=("Arial",20,"bold")

add=Button(mw,text="Add Employee",font=f,bg="red",fg="white",command=mtoa)
view=Button(mw,text="View Employee",font=f,bg="red",fg="white",command=mtov)
delete=Button(mw,text="Delete Employee",font=f,bg="red",fg="white",command=mtod)
update=Button(mw,text="Update Employee",font=f,bg="red",fg="white",command=mtou)
chart=Button(mw,text="Chart",font=f,bg="red",fg="white",command=create_chart)

y=20
add.pack(pady=y)
view.pack(pady=y)
delete.pack(pady=y)
update.pack(pady=y)
chart.pack(pady=y)

aw=Toplevel(mw)
aw.title("Add Employee")
aw.geometry("500x700+500+100")
aw.configure(bg="lightblue")
aw.resizable(False, False)

id_aw=Label(aw,text="Enter id: ",font=f,bg="lightblue",fg="black")
entid_aw=Entry(aw,font=f)
name_aw=Label(aw,text="Enter name: ",font=f,bg="lightblue",fg="black")
entname_aw=Entry(aw,font=f)
salary_aw=Label(aw,text="Enter salary: ",font=f,bg="lightblue",fg="black")
entsalary_aw=Entry(aw,font=f)
save_aw=Button(aw,text="Save",font=f,bg="red",fg="white",command=save)
back_aw=Button(aw,text="Back",font=f,bg="red",fg="white",command=atom)

id_aw.pack(pady=y)
entid_aw.pack(pady=y)
name_aw.pack(pady=y)
entname_aw.pack(pady=y)
salary_aw.pack(pady=y)
entsalary_aw.pack(pady=y)
save_aw.pack(pady=y)
back_aw.pack(pady=y)



vw=Toplevel(mw)
vw.title("View Employee")
vw.geometry("500x700+500+100")
vw.configure(bg="lightyellow")
vw.resizable(False, False)

scroll_vw=ScrolledText(vw,height=15,width=30,font=f)
back_vw=Button(vw,text="Back",font=f,bg="red",fg="white",command=vtom)

scroll_vw.pack(pady=y)
back_vw.pack(pady=y)



dw=Toplevel(mw)
dw.title("Delete Employee")
dw.geometry("500x700+500+100")
dw.configure(bg="lightblue")
dw.resizable(False, False)

id_dw=Label(dw,text="Enter id: ",font=f,bg="lightblue",fg="black")
dw_entid=Entry(dw,font=f)
dw_save=Button(dw,text="Delete",font=f,bg="red",fg="white",command=deletet)
back_dw=Button(dw,text="Back",font=f,bg="red",fg="white",command=dtom)

id_dw.pack(pady=y)
dw_entid.pack(pady=y)
dw_save.pack(pady=y)
back_dw.pack(pady=y)



uw=Toplevel(mw)
uw.title("Update Employee")
uw.geometry("500x700+500+100")
uw.configure(bg="orange")
uw.resizable(False, False)

id_uw=Label(uw,text="Enter id: ",font=f,bg="orange",fg="black")
uw_entid=Entry(uw,font=f)
name_uw=Label(uw,text="Enter name: ",font=f,bg="orange",fg="black")
entname_uw=Entry(uw,font=f)
salary_uw=Label(uw,text="Enter salary: ",font=f,bg="orange",fg="black")
entsalary_uw=Entry(uw,font=f)
uw_save=Button(uw,text="Save",font=f,bg="red",fg="white",command=updatet)
back_uw=Button(uw,text="Back",font=f,bg="red",fg="white",command=utom)

id_uw.pack(pady=y)
uw_entid.pack(pady=y)
name_uw.pack(pady=y)
entname_uw.pack(pady=y)
salary_uw.pack(pady=y)
entsalary_uw.pack(pady=y)
uw_save.pack(pady=y)
back_uw.pack(pady=y)

aw.withdraw()
vw.withdraw()
dw.withdraw()
uw.withdraw()

mw.mainloop()