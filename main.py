import start
import tkinter as tk
import re
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), resample=Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

def create_window():
    global has_icon_var, window, team1_icon_button, team2_icon_button, hasPeriod, period
    global timer_var, timer_entry, possession_checkbutton, switch_sides_var, team1_entry, team2_entry, colored_sides_var, home_icon_path, away_icon_path
    window = tk.Tk()
    window.title("Create Graphics")
    window.geometry("400x400")
    window.config(bg='light gray')
    home_icon_path = False
    away_icon_path = False

    # Checkbox with label and entry box (entry box only enabled if checked): Timer
    timer_var = tk.BooleanVar()
    timer_checkbutton = tk.Checkbutton(window, text="Timer (00:00, minute:second)", variable=timer_var)
    timer_checkbutton.place(x=200, y=20, anchor='center')
    timer_entry = tk.Entry(window, state="disabled")
    timer_entry.config(bg='white', fg='black')
    def toggle_timer_entry():
        if timer_var.get():
            timer_entry.delete(first=0, last=10000)
            timer_entry.config(state="normal")
            timer_entry.config(bg='white', fg='black')
        else:
            timer_entry.delete(first=0, last=10000)
            timer_entry.config(state="disabled")
            timer_entry.config(bg='white', fg='black')
    timer_checkbutton.config(command=toggle_timer_entry)
    timer_checkbutton.config(bg='white', fg='black')
    timer_entry.config(bg='white', fg='black')
    timer_entry.place(x=200, y=50, anchor='center')

    # Checkbox with label: Possession
    possession_var = tk.BooleanVar()
    possession_checkbutton = tk.Checkbutton(window, text="Possession", variable=possession_var)
    possession_checkbutton.config(bg='white', fg='black')
    possession_checkbutton.place(x=200, y=80, anchor='center')

    # Checkbox with label: Switch Sides Possible
    switch_sides_var = tk.BooleanVar()
    switch_sides_checkbutton = tk.Checkbutton(window, text="Switch Sides Possible", variable=switch_sides_var, fg='black', bg='white')
    switch_sides_checkbutton.place(x=200, y=110, anchor='center')

    # Entry box with placeholder: Team 1
    team1_entry = tk.Entry(window)
    team1_entry.insert(0, "Home")
    team1_entry.config(bg='white', fg='black')
    team1_entry.place(x=200, y=140, anchor='center')

    # Entry box with placeholder: Team 2
    team2_entry = tk.Entry(window)
    team2_entry.insert(0, "Away")
    team2_entry.config(bg='white', fg='black')
    team2_entry.place(x=200, y=160, anchor='center')

    # Checkbox with label: Has Icon
    has_icon_var = tk.BooleanVar()
    has_icon_checkbutton = tk.Checkbutton(window, text="Has Icon", variable=has_icon_var)
    has_icon_checkbutton.config(bg='white', fg='black')
    has_icon_checkbutton.place(x=200, y=220, anchor='center')

    hasPeriod = tk.BooleanVar()
    period = tk.Checkbutton(window, text="Periods", variable=hasPeriod)
    period.config(bg="white", fg='black')
    period.place(x=200, y=250, anchor='center')

    def submit():
        global has_icon_var, home_icon_path, away_icon_path, window, team1_icon_button, team2_icon_button, tk_images, hasPeriod, period
        global timer_var, timer_entry, possession_checkbutton, switch_sides_var, team1_entry, team2_entry, colored_sides_var

        tk_images = []
        def show_image(image_path, x, y, width, height):
            print("showing image...")
            print("Icon Path (show_image) 1: " + image_path)
            global window, tk_images

            # Load the image using PIL
            original_image = Image.open(image_path)

            # Resize the image
            resized_image = original_image.resize((width, height), resample=Image.LANCZOS)

            # Create a PhotoImage object from the resized image
            tk_image = ImageTk.PhotoImage(resized_image)
            # Keep a reference to the PhotoImage to prevent it from being garbage collected
            tk_images.append(tk_image)
            print("Icon Path (show_image) 2: " + image_path)
            
            for i in tk_images:
                # Create a Tkinter label and display the image at specified (x, y) coordinates
                image_label = tk.Label(window, image=i)
                image_label.place(x=x, y=y)

        if not (re.match(r"^\d\d:[0-5]\d$", timer_entry.get())) and timer_var.get():
            messagebox.showerror("ERROR", "Timer input must be in the format XX:XX where minutes [0-59]")
        else:
            window.geometry('320x300')  # Adjust the size accordingly
            window.config(bg='white')
            print(timer_entry.get())
            all = [timer_var.get(), timer_entry.get(), possession_var.get(), switch_sides_var.get(), team1_entry.get(),
                team2_entry.get(), False, hasPeriod.get()]
            var1 = team1_entry.get()
            var2 = team2_entry.get()
            timer_checkbutton.destroy()
            possession_checkbutton.destroy()
            has_icon_checkbutton.destroy()
            period.destroy()
            team2_entry.destroy()
            # team2_icon_button.destroy()
            team1_entry.destroy()
            # team2_icon_button.destroy()
            timer_entry.destroy()
            switch_sides_checkbutton.destroy()
    
            def finalSubmit():
                print("Submitted")
                global timer_var, timer_entry, possession_checkbutton, switch_sides_var, team1_entry, team2_entry, home_icon_path, away_icon_path
                window.destroy()
                a = all[0]
                b = all[1]
                c = all[2]
                d = all[3]
                e = all[4]
                f = all[5]
                g = all[6]
                h = all[7]
                print("Away Icon (finalSubmit): " + str(away_icon_path))
                print("Home Icon (finalSubmit): " + str(home_icon_path))
                start.ScoreboardApp(a, b, c, d, e, f, g, home_icon_path, away_icon_path, h)


            if has_icon_var.get():
                # Adding buttons for each team's icon
                team1_icon_button = tk.Button(window, text=f"{var1} Icon")
                team1_icon_button.place(x=50, y=210, anchor='center')

                team2_icon_button = tk.Button(window, text=f"{var2} Icon")
                team2_icon_button.place(x=250, y=210, anchor='center')

            def browseIcon(button, x, y, buttonSide):
                global home_icon_path, away_icon_path
                if buttonSide == 'left':
                    home_icon_path = filedialog.askopenfilename(title=f"Select {button.cget('text')}",
                                                                filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                    print(f"Selected Home Path:", home_icon_path)
                    show_image(home_icon_path, x, y, 100, 100)
                    print("Home Icon Path (browseIcon): " + home_icon_path)
                    print("===========================================")
                elif buttonSide == 'right':
                    away_icon_path = filedialog.askopenfilename(title=f"Select {button.cget('text')}",
                                                                filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                    print(f"Selected Away Path:", away_icon_path)
                    show_image(away_icon_path, x, y, 100, 100)
                    print("Away Icon Path (browseIcon): " + away_icon_path)
                    print("===========================================")
                else: 
                    print("Error")



            if has_icon_var.get():
                team1_icon_button.config(command=lambda: browseIcon(team1_icon_button, 10, 20, "left"))
                team2_icon_button.config(command=lambda: browseIcon(team2_icon_button, 200, 20, "right"))


            submit_button = tk.Button(window, text="Submit", command=finalSubmit, anchor="center")
            submit_button.place(x=150, y=250, anchor='center')


    submit_button = tk.Button(window, text="Submit", command=submit, anchor="center")
    submit_button.place(x=200, y=350, anchor='center')

    window.mainloop()

create_window()


# icon_path = filedialog.askopenfilename(title=f"Select {button.cget('text')}", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
# print(f"Selected {button.cget('text')} Path:", icon_path)