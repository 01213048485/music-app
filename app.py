import tkinter

top = tkinter.Tk()

left_frame = tkinter.Frame(top, height="500px", width="200px", bg="Black")
middle_frame = tkinter.Frame(top, height="500px", width="400px", bg="Green")
right_frame = tkinter.Frame(top, height="500px", width="200px", bg="Black")

left_frame.grid(column=0)
right_frame.grid(column=2)
middle_frame.grid(column=1)

search_bar = tkinter.Entry(middle_frame, width="100",bg="Yellow",bd=5)
search_bar.grid(column=0)

search_button = tkinter.Button(middle_frame, text="Search", height="2")
search_button.grid(column=1)

list_songs_frame = tkinter.Frame(middle_frame, height="300px", width="400px", bg="Purple")

top.mainloop()