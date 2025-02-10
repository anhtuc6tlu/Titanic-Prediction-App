from customtkinter import *
from PIL import Image, ImageTk
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = CTk()
app.title("Titanic Prediction")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")
app.geometry("800x600")

# Hàm hiển thị frame
def showFrame(frame):
    frame.lift()

# Tạo các frame
intro_frame = CTkFrame(app, fg_color='#3e3354')
main_frame = CTkFrame(app, fg_color='#3e3354')
###------------------------------------------------------------------------
intro_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
main_frame.grid_columnconfigure(0, weight=40)
main_frame.grid_columnconfigure(1, weight=60)
main_frame.grid_rowconfigure(0, weight=1) 
#-------------------------------------------------------------------------
# Logo
image = Image.open("logo.png")
image = image.resize((800, 800))
photo = ImageTk.PhotoImage(image)

image1 = Image.open("logo1.png")
image1 = image1.resize((300,300))
photo1 = ImageTk.PhotoImage(image1)
app.photo = [photo,photo1]

# Label chứa logo
label = CTkLabel(intro_frame, image=photo,text="")
label.place(relx=0.5, rely=0.35, anchor="center")

# Thêm nút START vào intro_frame
buttonStart = CTkButton(master=intro_frame,
                        text="START",
                        font=("Poppins",14,'bold'),
                        command=lambda: showFrame(main_frame))
buttonStart.place(relx=0.5, rely=0.8, anchor="center",relwidth=0.2,relheight=0.07)

#Tạo frame con ở trong main_frame
#---------------------
#| Logo          | Nhập     |
#| Description  |Thông tin |
#---------------------


# Tạo Frame bên trái, phải
left_frame = CTkFrame(main_frame, fg_color="#2e283b")
right_frame = CTkFrame(main_frame, fg_color="#3e3354")

left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")
# Sub-Frame cho bên trái--------------------
logo_frame = CTkLabel(left_frame,fg_color="#2e283b",text="",image=photo1,anchor="center")
white = CTkLabel(left_frame,fg_color="white",
                             text="""""",
                            corner_radius=20)
description = CTkLabel(left_frame,fg_color="#2e283b",bg_color="white",
                             font=("Helvetica",16,"italic"),
                             text="""Drag mouse the tag\nto view description!""",anchor="center",
                            corner_radius=10)
logo_frame.place(relx=0.25, rely=0, relwidth=0.5, relheight=0.5)
white.place(relx=0.08, rely=0.485, relwidth=0.84, relheight=0.33)
description.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)

def on_hover_sex(event):
    description.configure(text="""Sex: Giới tính\n\n•Male: Nam\n•Female: Nữ""",
                          fg_color="#2e283b")
def on_hover_age(event):
    description.configure(text="""
Age: Độ tuổi
    
    •Dao động từ       \n 0 đến 100 tuổi.
    """, fg_color="#2e283b")
def on_hover_pclass(event):
    description.configure(text="""
    P-Class: Hạng vé
    
  •1st: Thượng lưu
•2nd: Trung lưu
•3rd: Phổ thông
    """,fg_color="#2e283b")
def on_hover_fare(event):
    description.configure(text="""Fare: Giá vé ($)\n\n•Dao động từ 0 - 500""", fg_color="#2e283b")
def on_hover_embarked(event):
    description.configure(text="""
    Embarked: Cảng lên tàu

•C: Cherbourg  
•Q: Queenstown
•S: Southampton
    """, fg_color="#2e283b")
def on_hover_sibsp(event):
    description.configure(text="""
    SibSp: Số lượng anh chị em và\n vợ chồng trên tàu

    (*) Chỉ tính:                    
    •Anh chị em ruột/kế.
    •Vợ chồng               
    (không tính tình nhân và hôn thê)
    """, fg_color="#2e283b")
def on_hover_parch(event):
    description.configure(text="""
    Parch: Số lượng bố mẹ/trẻ em\n trên tàu

    (*) Chỉ tính:                    
    •Bố mẹ ruột/nuôi.    
    •Con ruột/nuôi/riêng """, fg_color="#2e283b")

# Hàm khôi phục label khi chuột rời khỏi tag
def on_leave(event):
    description.configure(text="""Drag mouse the tag\nto view description!""", fg_color="#2e283b")


# Sub-Frame cho bên phải--------------------#3e3354
info_frame = CTkFrame(right_frame,fg_color='#3e3354')
info_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.7)

submit_frame = CTkFrame(right_frame,fg_color='#3e3354')
submit_frame.place(relx=0.1, rely=0.85, relwidth=0.8, relheight=0.1)



label_sex = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                     fg_color="#2e283b",height=30,width=100, text="Sex",corner_radius=10)
label_pclass = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                        fg_color="#2e283b",height=30,width=100, text="P-Class",corner_radius=10)
label_embarked = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                       fg_color="#2e283b",height=30,width=100, text="Embarked",corner_radius=10)
label_age = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                     fg_color="#2e283b",height=30,width=100, text="Age",corner_radius=10)
label_fare = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                      fg_color="#2e283b",height=30,width=100, text="Fare",corner_radius=10)
label_sibsp = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                       fg_color="#2e283b",height=30,width=100, text="SibSp",corner_radius=10)
label_parch = CTkLabel(info_frame,font=("Helvetica", 16, "italic"),
                       fg_color="#2e283b",height=30,width=100, text="Parch",corner_radius=10)

sex = CTkComboBox(info_frame, fg_color="#3e3354",values=["Male","Female"],font=("Calibri",16),state="readonly")
pclass = CTkComboBox(info_frame,fg_color="#3e3354",values=["1","2","3"],font=("Calibri",16),state="readonly")
embarked = CTkComboBox(info_frame,fg_color="#3e3354",values=["S","Q","C"],
                    font=("Calibri",16),state="readonly")
age = CTkEntry(info_frame, fg_color="#3e3354",font=("Calibri",16))
fare = CTkEntry(info_frame,fg_color="#3e3354",font=("Calibri",16))
sibsp = CTkEntry(info_frame,fg_color="#3e3354",font=("Calibri",16))
parch = CTkEntry(info_frame,fg_color="#3e3354",font=("Calibri",16))



###------------------------------------------------------------------
label_sex.grid(row=0, column=0, padx=30, pady=15,sticky="NSEW")
label_pclass.grid(row=1, column=0, padx=30, pady=15,sticky="NSEW")
label_embarked.grid(row=2, column=0, padx=30, pady=15,sticky="NSEW")
label_age.grid(row=3, column=0, padx=30, pady=15,sticky="NSEW")
label_fare.grid(row=4, column=0, padx=30, pady=15,sticky="NSEW")
label_sibsp.grid(row=5, column=0, padx=30, pady=15,sticky="NSEW")
label_parch.grid(row=6, column=0, padx=30, pady=15,sticky="NSEW")


sex.grid(row=0, column=1, padx=20, pady=15,sticky="NSEW")
pclass.grid(row=1, column=1, padx=20, pady=15,sticky="NSEW")
embarked.grid(row=2, column=1, padx=20, pady=15,sticky="NSEW")
age.grid(row=3, column=1, padx=20, pady=15,sticky="NSEW")
fare.grid(row=4, column=1, padx=20, pady=15,sticky="NSEW")
sibsp.grid(row=5, column=1, padx=20, pady=15,sticky="NSEW")
parch.grid(row=6, column=1, padx=20, pady=15,sticky="NSEW")

### Gắn tag-------------------------
label_sex.bind("<Enter>", on_hover_sex)
label_sex.bind("<Leave>", on_leave)
label_age.bind("<Enter>", on_hover_age)
label_age.bind("<Leave>", on_leave)
label_pclass.bind("<Enter>", on_hover_pclass)
label_pclass.bind("<Leave>", on_leave)
label_fare.bind("<Enter>", on_hover_fare)
label_fare.bind("<Leave>", on_leave)
label_embarked.bind("<Enter>", on_hover_embarked)
label_embarked.bind("<Leave>", on_leave)
label_sibsp.bind("<Enter>", on_hover_sibsp)
label_sibsp.bind("<Leave>", on_leave)
label_parch.bind("<Enter>", on_hover_parch)
label_parch.bind("<Leave>", on_leave)

def show_validation_message(message):
    x = app.winfo_x()
    y = app.winfo_y()
    validation_window = CTkToplevel(main_frame,fg_color="#3e3354")
    validation_window.title("Thông báo")
    validation_window.geometry("480x240")
    validation_window.geometry(f"480x240+{x+200}+{y+200}")
    validation_window.lift()  # Dùng lift để đưa cửa sổ lên trên
    validation_window.attributes('-topmost', 1)  # Cửa sổ luôn ở trên cùng
    validation_window.after(1000, lambda: validation_window.attributes('-topmost', 0))

    # Tạo label trong cửa sổ thông báo
    label = CTkLabel(validation_window, text=message, fg_color="#3e3354",font=("Helvetica",15))
    label.place(relx=0,rely=0,relwidth=1, relheight=0.8)

    # Tạo nút để đóng cửa sổ thông báo
    button = CTkButton(validation_window, text="Đóng",font=("Helvetica",15,"italic"), command=validation_window.destroy)
    button.place(relx=0,rely=0.8,relwidth=1, relheight=0.2)


def load_model(n):
    with open('knn_model.pkl', 'rb') as model_file:
        knn_loaded = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler_loaded = pickle.load(scaler_file)
    n_scaled = scaler_loaded.transform(n)
    value = knn_loaded.predict(n_scaled)
    print("-------------- value:------",value)
    mess = "Kết quả dự đoán:\n"
    if value ==0:
        mess += "Người này đã ngỏm!"
    else:
        mess += "Người này đã sống sót!"
    show_validation_message(mess)
    

#Check validate:
global model
def checkValidate():
    message = ""
    if (sex.get()==""):
        message += "Vui lòng nhập giới tính!\n"
    if (pclass.get()==""):
        message += "Vui lòng nhập P-Class!\n"
    if (embarked.get()==""):
        message += "Vui lòng nhập tên cảng lên tàu!\n"
    if (age.get()==""):
        message += "Vui lòng nhập lứa tuổi!\n"
    else:
        if (not age.get().isdigit()):
            message += "Sai giá trị, vui lòng nhập lại Age!\n"   
    
    if (fare.get()==""):
        message += "Vui lòng nhập giá vé!\n"
    else:
        if (not fare.get().isdigit()):
            message += "Sai giá trị, vui lòng nhập lại Fare!\n" 
    if (sibsp.get()==""):
        message += "Vui lòng nhập số lượng anh chị em trên tàu!\n"
    else:
        if (not sibsp.get().isdigit()):
            message += "Sai giá trị, vui lòng nhập lại SibSp!\n"
    if (parch.get()==""):
        message += "Vui lòng nhập số lượng bố mẹ/con cái trên tàu!\n"
    else:
        if (not parch.get().isdigit()):
            message += "Sai giá trị, vui lòng nhập lại Parch!\n"
    if message=="":
        #pclass,age,sibsp,parch,fare,sex,embarked
        param = {
            'Pclass':[int(pclass.get())],
            'Age':[float(age.get())],
            'SibSp':[int(sibsp.get())],
            'Parch':[int(parch.get())],
            'Fare':[float(fare.get())],
            'Sex_female':[1 if sex.get()=="Female" else 0],
            'Sex_male':[1 if sex.get()=="Male" else 0],
            'Embarked_C': [1 if embarked.get()=="C" else 0],
            'Embarked_Q': [1 if embarked.get()=="Q" else 0],
            'Embarked_S': [1 if embarked.get()=="S" else 0]
        }
        data_new = pd.DataFrame(param)
        scaler1 = StandardScaler()
        print(data_new)
        print(data_new.shape)
        print(data_new.info())
        load_model(data_new)
    else:
        show_validation_message(message)
submit_button = CTkButton(submit_frame,width=100,height=50,text="Prediction",
                         corner_radius=10,font=("Helvetica",20, "bold"),command=checkValidate)
submit_button.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.8)
showFrame(intro_frame)


app.mainloop()