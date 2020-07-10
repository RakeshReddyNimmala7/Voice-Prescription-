from tkinter import *
import smtplib
import speech_recognition as sr

def START():
    print("Hello Doctor")   

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Doctor Tell me patient's  name")
        audio=r.listen(source)

        try:
            pname=r.recognize_google(audio)
            print("Patient's name is:",pname)
        except:
            print("Sorry can't recognize your voice")


        print("Ok Doctor please tell me " + pname + "'s age ")
        ageaudio = r.listen(source)

        try:
            page = r.recognize_google(ageaudio)
            age=pname+"'sage is  "+page+"years"
            print(pname+"'sage is ", page)
        except:
            print("Sorry cann't recognize your voice")

            
        print("Doctor please tell me " + pname + "'s gender")
        genderaudio = r.listen(source)

        try:
            pgender = r.recognize_google(genderaudio)
            age=pname+"'sgender is  "+pgender
            print(pname+"'s gender is", pgender)
        except:
            print("Sorry cann't recognize your voice")


        print("Doctor do you want to to suggest any medicines")
        suggest = r.listen(source)

        try:
            ans = r.recognize_google(suggest)
            print(ans)
        except:
            print("Sorry cann't recognize your voice")


        if(ans=="yes" or ans=="Yes"or ans==None):
            
            print("tell me name of medicine")
            med = r.listen(source)

            try:
                mname = r.recognize_google(med)
                print(mname)
            except:
                print("Sorry cann't recognize your voice")
            
           
            
            print("Doctor please tell me time for consumption of medicines")
            medtime = r.listen(source)

            try:
                mtime = r.recognize_google(medtime)
                print(mtime)
            except:
                print("Sorry cann't recognize your voice")


    root = Tk()
    heading=Label(root,text="N HOSPITALS",padx=300,pady=50,width=30,font=(None,30)).grid(row=1,column=2)
    name=Label(root,text="Medical Receipt",padx=300,pady=50,width=30,font=(None,30)).grid(row=2,column=2)

    name=Label(root,text="Name of patient",font=(None,15),padx=20).grid(row=4,column=1)
    iname=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    iname.insert(0,pname)
    iname.grid(row=4,column=2)


    age=Label(root,text="Age of patient",font=(None,15),padx=20).grid(row=5,column=1)
    iage=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    iage.insert(0,page)
    iage.grid(row=5,column=2)

    Gender=Label(root,text="Gender of patient",font=(None,15),padx=20).grid(row=6,column=1)
    igender=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    igender.insert(0,pgender)
    igender.grid(row=6,column=2)

    medi=Label(root,text="Medicine name ",font=(None,15),padx=20).grid(row=7,column=1)
    imed=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    imed.insert(0,mname)
    imed.grid(row=7,column=2)

    time=Label(root,text="Consumption time",font=(None,15),padx=20).grid(row=8,column=1)
    itime=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    itime.insert(0,mtime)
    itime.grid(row=8,column=2)


    def printSomething():
        df = pd.DataFrame({
            'Name of patient': [pname],
            'Age':[page],
            'Gender': [pgender],
            'Medicine name': [mname],
            'Medicine time':[mtime]})


        writer = pd.ExcelWriter('hospitals.xlsx', engine='xlsxwriter')


        df.to_excel(writer, sheet_name="sheet1")


        writer.save()
        print("Don't forgot to fill email address:")
        sender_email = "enter email id"
        rec_email = email.get()
        password = "enter your password here"
        subject="Medical Prescription"
        message = "N HOSPITALS \n \n Medical prescription \n \n"+"Patient Name ="+pname+"\n"+"Age ="+page+"\n"+"Gender=" +pgender+"\n"+"medicine="+mname+"\n"+"Medicine Time="+mtime
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        print("login successfull")
        server.sendmail(sender_email, rec_email, message)
        print("email send successfully")



    Patient_Email=Label(root,text="Email address of patient",font=(None,15),padx=20).grid(row=9,column=1)
    email=Entry( root ,width=50,bg="#f7f7f5",borderwidth=2)
    email.insert(0,"@gmail.com")
    email.grid(row=9,column=2)




    mybutton=Button(root,text="Send email",padx=20,pady=7,command=printSomething,fg="black",bg="white").grid(row=11,column=2)

    root.mainloop()

    
def main_screen():
    global screen
   
    
    screen = Tk()
    width_of_window=600
    height_of_window=600
    screen_width=screen.winfo_screenwidth()
    screen_height=screen.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width_of_window/2)
    y_coordinate=(screen_height/2)-(height_of_window/2)
    screen.geometry("%dx%d+%d+%d" %(width_of_window, height_of_window,x_coordinate,y_coordinate))

    C = Canvas(screen,bg="blue",height = 400, width=400)
    name = PhotoImage(file= "D:\MINI PROJECT RAKESH\Capture335.PNG")
    background_label = Label(screen,image=name)
    background_label.place(x=0,y=0,relwidth=1,relheight=1)
    
    screen.title("Voice Prescription")
    Label(text="VOICE PRESCRIPTION",bg='#3c3d41',font=("calibri",21)).pack()
    Label().pack()
    
   
    button=Button(text="START",command = START).pack()
    
   

    screen.mainloop()
   

main_screen()
