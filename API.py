import requests 
import tkinter as tk
from tkinter import messagebox
def get_joke():
    url ="https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw"
    response = requests.get(url)
    if response.status_code ==200 :
        joke =response.json()
        if joke["type"] == "single":
                  joke1= joke["joke"]
        elif joke["type"] == "twopart":
            joke1 = f"{joke['setup']} - {joke['delivery']}"
        joke_label.config(text=joke1)  
    else:
        messagebox.showerror("Error", f"Failed to retrieve joke. Status code: {response.status_code}")
    
       
root = tk.Tk()  

root.title = "Random Joke generator"
joke_label=tk.Label(root,text="click the button to get joke",wraplength="300", justify="center")
joke_label.pack(pady=20)
joke_button=tk.Button(root,text="get joke",command=get_joke)
joke_button.pack(pady=20)
root.mainloop()