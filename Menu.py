from tkinter import *

def submit():
    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    print("You have ordered:")
    for i in food:
        print(i)

def add(event=None):
    item = entry_box.get()
    if item:
        listbox.insert(END, item)
        listbox_images.append(None)  # Add a placeholder for the image
        listbox.config(height=listbox.size())
        entry_box.delete(0, END)

def delete(event=None):
    selected_indices = listbox.curselection()
    for i in selected_indices[::-1]:
        listbox.delete(i)
        listbox_images.pop(i)  # Remove the corresponding image
    listbox.config(height=listbox.size())

def update_selected_image(event=None):
    selected_index = listbox.curselection()
    if selected_index:
        canvas.delete("all")  # Clear previous image
        canvas.create_image(50, 50, image=listbox_images[selected_index[0]])

window = Tk()

icon = PhotoImage(file='logo in png.png')
window.iconphoto(True,icon)
window.title("Welcome to Hungry Hub! Please order!")

# Create a Listbox for text
listbox = Listbox(window, bg='#a6cfcb', fg='#333333', font=('Comic Sans MS', 20), width=20, selectmode=MULTIPLE)
listbox.pack(side=LEFT, fill=Y)

# Create a Canvas for images
canvas = Canvas(window, bg='#a6cfcb', width=100, height=100)
canvas.pack(side=LEFT, padx=10)

# Load images
pizza_img = PhotoImage(file='pizza.png')
pasta_img = PhotoImage(file='pasta.png')
sushi_img = PhotoImage(file='sushi.png')
butter_chicken_img = PhotoImage(file='butter.png')
lasagna_img = PhotoImage(file='Lasagna.png')
momos_img = PhotoImage(file='Momos.png')
hamburger_img = PhotoImage(file='hamburger.png')
garlic_bread_img = PhotoImage(file='Garlic Bread.png')
cold_coffee_img = PhotoImage(file='coffee.png')
cocktails_img = PhotoImage(file='drink.png')
pepsi_img = PhotoImage(file='pepsi.png')

# Store images corresponding to each item
item_images = {
    "Pizza": pizza_img,
    "Pasta": pasta_img,
    "Sushi": sushi_img,
    "Butter Chicken": butter_chicken_img,
    "Lasagna": lasagna_img,
    "Momos": momos_img,
    "Hamburger": hamburger_img,
    "Garlic Bread": garlic_bread_img,
    "Cold Coffee": cold_coffee_img,
    "Cocktails": cocktails_img,
    "Pepsi": pepsi_img
}

# Store images alongside items
listbox_images = [None] * len(item_images)

for item_index, (item_name, item_image) in enumerate(item_images.items()):
    listbox.insert(END, item_name)
    listbox_images[item_index] = item_image

# Bind the selection event to update the image on the canvas
listbox.bind("<<ListboxSelect>>", update_selected_image)

entry_box = Entry(window)
entry_box.pack()

entry_box.bind("<Return>", add)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

window.mainloop()

