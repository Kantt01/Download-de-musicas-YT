import tkinter as tk 
from tkinter import *
from pytube import YouTube 
from tkinter import messagebox, filedialog 
  
def Widgets(): 
    link_label = Label(root,  
                       text="Link do Youtube:", 
                       bg="#f2f6ff") 
    link_label.grid(row=1, 
                    column=0, 
                    pady=5, 
                    padx=5) 
   
    root.linkText = Entry(root, 
                          width=55, 
                          textvariable=video_Link) 
    root.linkText.grid(row=1,  
                       column=1, 
                       pady=5, 
                       padx=5, 
                       columnspan = 2) 
   
    destination_label = Label(root,  
                              text="Onde você quer salvar?:", 
                              bg="#f2f6ff") 
    destination_label.grid(row=2, 
                           column=0, 
                           pady=5, 
                           padx=5) 
   
    root.destinationText = Entry(root, 
                                 width=40, 
                                 textvariable=download_Path) 
    root.destinationText.grid(row=2,  
                              column=1, 
                              pady=5, 
                              padx=5) 
   
    browse_B = Button(root,  
                      text="Browse", 
                      command=Browse, 
                      width=10, 
                      bg="#ffffff") 
    browse_B.grid(row=2, 
                  column=2, 
                  pady=1, 
                  padx=1) 
   
    Download_B = Button(root, 
                        text="Download",  
                        command=Download,  
                        width=20, 
                        bg="#ffffff") 
    Download_B.grid(row=3, 
                    column=1, 
                    pady=3, 
                    padx=3) 
  
  
def Browse(): 
    
    
    
    
    
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 
   
    
    
    download_Path.set(download_Directory) 
def Download(): 
      
    
    Youtube_link = video_Link.get() 
      
    
    
    download_Folder = download_Path.get() 
   
    
    getVideo = YouTube(Youtube_link) 
   
    
    
    
    videoStream = getVideo.streams.get_audio_only() 
   
    
    
    videoStream.download(download_Folder) 
   
    
    messagebox.showinfo("DOWNLOAD COM SUCESSO",  
                        "MÚSICA SALVA EM\n" 
                        + download_Folder) 
root = tk.Tk() 
   
root.geometry("600x120") 
root.resizable(False, False) 
root.title("download de  musicas do youtube by:Matheus Braz") 
root.config(background="#f2f6ff") 
   
video_Link = StringVar() 
download_Path = StringVar() 
   
Widgets() 
   
root.mainloop() 