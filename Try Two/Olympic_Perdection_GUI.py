from tkinter import *
from tkinter import ttk
import pandas as pd

def import_data() -> pd.DataFrame:
    medals = pd.read_csv('Number_of_Medals_Won', sep=",")
    #print(medals)
    return(medals)

def tk(medal_data) -> int:

    # Create object 
    root = Tk() 
    
    # root window title and dimension
    root.title("Paris 2024 Predictor")

    # Adjust size 
    root.geometry( "300x200" ) 
    
    # Create Label 
    label2 = Label( root , text = "" ) 

    # Change the label text 
    def show(): 
        label2.config( text = clicked.get() ) 

    # Dropdown menu options 
    options = medal_data['Country'].tolist()

    def on_select(event):
        selected_item = combo_box.get()
        label2.config(text="Country: " + selected_item + 
                     "\nGolds: " + str(medal_data.iloc[options.index(selected_item)]['Gold']) +
                     "\nSilvers: " + str(medal_data.iloc[options.index(selected_item)]['Silver']) +
                     "\nBronzes: " + str(medal_data.iloc[options.index(selected_item)]['Bronze']) +
                     "\nTotal: " + str(medal_data.iloc[options.index(selected_item)]['Total']))
    
    # datatype of menu text 
    clicked = StringVar() 
    
    # initial menu text 
    clicked.set("") 
    
    label1 = Label( root , text = "Which Country do you want to look at?" )
    label1.pack() 

    # Create a Combobox widget
    combo_box = ttk.Combobox(root, values=options)
    combo_box.pack(pady=5)
    
    # Bind event to selection
    combo_box.bind("<<ComboboxSelected>>", on_select)

    # Create button, it will change label text 
    button = Button(root , text = "click Me" , command = show() )
    button.pack()

    label2.pack() 
    
    # Execute tkinter 
    root.mainloop() 


if __name__ == '__main__':
    data = import_data()
    tk(data)