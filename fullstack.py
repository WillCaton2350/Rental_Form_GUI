import tkinter
from PIL import Image, ImageTk
import customtkinter


root = tkinter.Tk()
root.geometry("915x715")
root.title("Rental Form")

Header = tkinter.Label(root,text="Men's Wearhouse", font="Nanum+Myeongjo 30 bold")
Header.place(x=540,y=10)

logo = ImageTk.PhotoImage(Image.open("/Users/Mac/PythonWorks/img/mwlogo.png"))
logo_Label = tkinter.Label(root, image=logo)
logo_Label.place(x=365,y=10)

# checkboxes

MemberLabel = tkinter.Label(root,text="Member(s):",font="Nanum+Myeongjo 14 bold")
MemberLabel.place(x=810,y=60)


checkLabel = tkinter.Label(root,text="Group:")
check = customtkinter.CTkCheckBox(root, text="")
checkLabel.place(x=810,y=100)
check.place(x=860,y=100)

indi_checkLabel = tkinter.Label(root,text="Single:")
indi_check = customtkinter.CTkCheckBox(root, text="")
indi_checkLabel.place(x=810,y=130)
indi_check.place(x=860,y=130)


# entry fields
entryLabel = tkinter.Label(root,text="Reservation #")
entry = customtkinter.CTkEntry(root)
entryLabel.place(x=20,y=10)
entry.place(x=20,y=30)

Store_entryLabel = tkinter.Label(root,text="Store #")
Store_entry = customtkinter.CTkEntry(root)
Store_entryLabel.place(x=180,y=10)
Store_entry.place(x=180,y=30)

date_entryLabel = tkinter.Label(root,text="Todays Date:")
date_entry = customtkinter.CTkEntry(root)
date_entryLabel.place(x=20,y=60)
date_entry.place(x=20,y=80)

Store_entryLabel = tkinter.Label(root,text="Employee Contact:")
Store_entry = customtkinter.CTkEntry(root)
Store_entryLabel.place(x=180,y=60)
Store_entry.place(x=180,y=80)

EventType_entryLabel = tkinter.Label(root,text="Event Type:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=20,y=110)
EventType_entry.place(x=20,y=130)

EventType_entryLabel = tkinter.Label(root,text="Event Date:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=180,y=110)
EventType_entry.place(x=180,y=130)

EventType_entryLabel = tkinter.Label(root,text="Event Time:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=340,y=110)
EventType_entry.place(x=340,y=130)

EventType_entryLabel = tkinter.Label(root,text="Pickup Date:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=20,y=160)
EventType_entry.place(x=20,y=180)

EventType_entryLabel = tkinter.Label(root,text="Return Date:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=180,y=160)
EventType_entry.place(x=180,y=180)

EventType_entryLabel = tkinter.Label(root,text="Ship to Store:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=340,y=160)
EventType_entry.place(x=340,y=180)

EventType_entryLabel = tkinter.Label(root,text="Return Store:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=340,y=160)
EventType_entry.place(x=340,y=180)

EventType_entryLabel = tkinter.Label(root,text="Ship to Store:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=20,y=210)
EventType_entry.place(x=20,y=230)

EventType_entryLabel = tkinter.Label(root,text="Group #:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=340,y=210)
EventType_entry.place(x=340,y=230)

EventType_entryLabel = tkinter.Label(root,text="Group Name:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=180,y=210)
EventType_entry.place(x=180,y=230)

EventType_entryLabel = tkinter.Label(root,text="Customer Name:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=20,y=260)
EventType_entry.place(x=20,y=280)

EventType_entryLabel = tkinter.Label(root,text="Customer Phone:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=180,y=260)
EventType_entry.place(x=180,y=280)

EventType_entryLabel = tkinter.Label(root,text="Customer Email:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=340,y=260)
EventType_entry.place(x=340,y=280)

# checkbox2

short_checkLabel = tkinter.Label(root,text="***Measured by:")
short_checkLabel.place(x=660,y=383)

short_check = customtkinter.CTkCheckBox(root, text="")
short_check.place(x=777,y=383)

short_Label = tkinter.Label(root,text="Short name:")
short_Label.place(x=660,y=330)


short_Entry = customtkinter.CTkEntry(root)
short_Entry.place(x=660,y=350)


# measurement combobox / dropdown

top_measurement_Label = tkinter.Label(root,text="Coat:")
chest = customtkinter.CTkComboBox(root,values=(["chest","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))
overarm = customtkinter.CTkComboBox(root,values=(["overarm","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))
sleeve = customtkinter.CTkComboBox(root,values=(["sleeve","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))

bottom_measurement_Label = tkinter.Label(root,text="Pants:")
waist = customtkinter.CTkComboBox(root,values=(["waist","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))
hip = customtkinter.CTkComboBox(root,values=(["hip","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))
outseam = customtkinter.CTkComboBox(root,values=(["outseam","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))

shirt_measurement_Label = tkinter.Label(root,text="Shirt:")
neck = customtkinter.CTkComboBox(root,values=(["neck","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))
shirt_sleeve = customtkinter.CTkComboBox(root,values=(["sleeve","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60"]))

measurement_Label = tkinter.Label(root,text="Size:")
height = customtkinter.CTkComboBox(root,values=(["Ft","5'0","5'1","5'2","5'3","5'4","5'5","5'6","5'7","5'8","5'9","5'10","5'11","6'0","6'1","6'2","6'3","6'4","6'5","6'6","6'7","6'8","6'9","6'10",]))
weight = customtkinter.CTkComboBox(root,values=(["lbs","140","145","150","155","160","165","170","175","180","185","190","195","200","205","210","215","220","225","230","235","240","245","250"]))



bottom_measurement_Label.place(x=180,y=330)
waist.place(x=180,y=350)
hip.place(x=180,y=380)
outseam.place(x=180,y=410)

top_measurement_Label.place(x=20,y=330)
chest.place(x=20,y=350)
overarm.place(x=20,y=380)
sleeve.place(x=20,y=410)

shirt_measurement_Label.place(x=340,y=330)
neck.place(x=340,y=350)
shirt_sleeve.place(x=340,y=380)

measurement_Label.place(x=500,y=330)
height.place(x=500,y=350)
weight.place(x=500,y=380)

EventType_entryLabel = tkinter.Label(root,text="Jewelry:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=660,y=110)
EventType_entry.place(x=660,y=130)

EventType_entryLabel = tkinter.Label(root,text="Shoes:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=660,y=160)
EventType_entry.place(x=660,y=180)

EventType_entryLabel = tkinter.Label(root,text="Pants:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=500,y=110)
EventType_entry.place(x=500,y=130)

EventType_entryLabel = tkinter.Label(root,text="Shirt:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=500,y=160)
EventType_entry.place(x=500,y=180)

EventType_entryLabel = tkinter.Label(root,text="Vest:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=500,y=210)
EventType_entry.place(x=500,y=230)

EventType_entryLabel = tkinter.Label(root,text="Coat:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=500,y=60)
EventType_entry.place(x=500,y=80)

EventType_entryLabel = tkinter.Label(root,text="Pocket Square:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=660,y=210)
EventType_entry.place(x=660,y=230)

EventType_entryLabel = tkinter.Label(root,text="Neckwear:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=660,y=60)
EventType_entry.place(x=660,y=80)

EventType_entryLabel = tkinter.Label(root,text="Additional Item:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=660,y=260)
EventType_entry.place(x=660,y=280)

EventType_entryLabel = tkinter.Label(root,text="Cummberbund:")
EventType_entry = customtkinter.CTkEntry(root)
EventType_entryLabel.place(x=500,y=260)
EventType_entry.place(x=500,y=280)

EventType_entryLabel = tkinter.Label(root,text="Comments:")
EventType_entry = customtkinter.CTkEntry(root,width=780)
EventType_entryLabel.place(x=20,y=460)
EventType_entry.place(x=20,y=480)
EventType_entry = customtkinter.CTkEntry(root,width=780)
EventType_entry.place(x=20,y=520)
EventType_entry = customtkinter.CTkEntry(root,width=780)
EventType_entry.place(x=20,y=560)

enterBTN = customtkinter.CTkButton(root,text="Enter")
enterBTN.place(x=170,y=630)

deleteBTN = customtkinter.CTkButton(root,text="Delete")
deleteBTN.place(x=320,y=630)

deleteBTN = customtkinter.CTkButton(root,text="Edit")
deleteBTN.place(x=470,y=630)

footer = tkinter.Label(root,text="MW©", font="Nanum+Myeongjo 16 ")
footer.place(x=850,y=680)




root.mainloop()