from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector

# Function to establish a database connection
def connect_to_database():
    try:
        # Replace these values with your MySQL server configuration
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="equity"
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error: ", err)
        return None
    
def clear():
    nameEntry.delete(0,END)
    accountnumberEntry.delete(0,END)
    phoneEntry.delete(0,END)
    emailEntry.delete(0,END)
    pinEntry.delete(0,END)
    confirmpinEntry.delete(0,END)
    checkValue.set(0)
    

# Function to insert registration data into the database
def register():
    mydb = connect_to_database()
    if mydb:
        cursor = mydb.cursor()
        name_info = nameValue.get()
        accountnumber_info = accountnumberValue.get()
        phone_info = phoneValue.get()
        email_info = emailValue.get()
        pin_info = pinValue.get()
        confirmpin_info=confirmpinValue.get()

        # Define the SQL query to insert data into a table
        insert_query = "INSERT INTO login(name, accountnumber, phone, email, pin,confirmpin) VALUES (%s, %s, %s, %s, %s, %s)"

        # Execute the query with the user's data
        cursor.execute(insert_query, (name_info, accountnumber_info, phone_info, email_info, pin_info, confirmpin_info))

        mydb.commit()  # Commit the changes to the database
        mydb.close()  # Close the database connection

        if (name_info=="" or accountnumber_info=="" or phone_info=="" or email_info==""or pin_info=="" or  confirmpin_info==""):
           messagebox.showerror("Error", "All fields are required!!", parent =root)
        elif pin_info != confirmpin_info:
            messagebox.showerror("Error", "pin mismatch", parent =root)
        elif checkValue.get()==0:
            messagebox.showerror("Error", "click remember me!", parent =root)
            
        else:
                 Label(root, text="Registration successfully", fg="maroon", bg="white",font=("Times New Roman", 11)).place(x=450, y=550)
                 clear()
                 
    
def login_page():
    root.destroy()
    import Bank
root = Tk()
root.title("Registration")
root.geometry("1100x600")
root.resizable(False, False)

# Use PIL to load the background image
root.bg = ImageTk.PhotoImage(file="images/equi.png")
root.bg_label = Label(image=root.bg)
root.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="REGISTRATION FORM", font=("Impact", 25, "bold"), fg="maroon").pack(pady=50)

Label(text="Name", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=150)
Label(text="Account Number", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=200)
Label(text="Phone", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=250)
Label(text="Email", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=300)
Label(text="Pin", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=350)
Label(text="Confirm Pin", font=("Helvetica", 12, "bold"), fg="maroon").place(x=190, y=400)


nameValue = StringVar()
accountnumberValue = StringVar()
phoneValue = StringVar()
emailValue = StringVar()
pinValue = StringVar()
confirmpinValue=StringVar()
checkValue=IntVar()


nameEntry = Entry(root, textvariable=nameValue, width=30, bd=2, font=("Helvetica", 12))
accountnumberEntry = Entry(root, textvariable=accountnumberValue, width=30, bd=2, font=("Helvetica", 12))
phoneEntry = Entry(root, textvariable=phoneValue, width=30, bd=2, font=("Helvetica", 12))
emailEntry = Entry(root, textvariable=emailValue, width=30, bd=2, font=("Helvetica", 12))
pinEntry = Entry(root, textvariable=pinValue, width=30, bd=2, font=("Helvetica", 12))
confirmpinEntry = Entry(root, textvariable=confirmpinValue, width=30, bd=2, font=("Helvetica", 12))


nameEntry.place(x=400, y=150)
accountnumberEntry.place(x=400, y=200)
phoneEntry.place(x=400, y=250)
emailEntry.place(x=400, y=300)
pinEntry.place(x=400, y=350)
confirmpinEntry.place(x=400, y=400)

checkValue = IntVar()
checkbtn = Checkbutton(root, text="Remember me?", fg="maroon", variable=checkValue)
checkbtn.place(x=400, y=450)

Button(root, text="Register", font=("Helvetica", 12, "bold"), bg="maroon", fg="white", width=11, height=1, command=register).place(x=400, y=500)
Button(root, text="Back to login", font=("Helvetica", 12, "bold"), bg="maroon", fg="white", width=11, height=1,command=login_page).place(x=550, y=500)


# Start the main loop
root.mainloop()
