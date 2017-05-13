import tkinter as tk
from tkinter import messagebox
import pickle

window = tk.Tk()
var_username = tk.StringVar()
var_password = tk.StringVar()

def w_window():
    window.title('welcome to login interface')
    window.geometry('650x300') #width x height

def w_canvas():
    global image, image_file
    canvas = tk.Canvas(window, height=100, width=650)
    canvas.pack(side='top')
    image_file = tk.PhotoImage(file='login.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)

def w_label():
    tk.Label(window, text='Username').place(x=180, y=150)
    tk.Label(window, text='Password').place(x=180, y=190)

def w_entry():
    global entry_username, entry_password, var_username, var_password
    var_username.set('student ID')
    entry_username = tk.Entry(window, textvariable=var_username, show=None).place(x=270, y=150)
    entry_password = tk.Entry(window, textvariable=var_password, show='*').place(x=270, y=190)

def w_button():
    button_username = tk.Button(window, text='Login', command=login)
    button_username.place(x=230, y=250)
    button_password = tk.Button(window, text='Sign up', command=signup)
    button_password.place(x=330, y=250)
    button_forgotpassword = tk.Button(window, text='Forgot password', bg='red', command=reset_password)
    button_forgotpassword.place(x=520, y=260)

def login():
    username = var_username.get()
    password = var_password.get()
    user_information()
    if username in user_info:
        if password == user_info[username]:
            tk.messagebox.showinfo(title='Welcome', message='Glad to see you ' + username)
        else:
            tk.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:
        login_confirm = tk.messagebox.askyesno('Opt!', 'the username does not exist,please try again')
        if login_confirm:
            pass
        else:
            is_signup = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up now?')
            if is_signup:
                signup()

def signup():
    global new_name, new_pwd, new_pwd_confirm, window_signup
    window_signup = tk.Toplevel(window)
    window_signup.title('welcome to sign up interface')
    window_signup.geometry('350x300')  # width x height

    new_name = tk.StringVar()
    new_name.set('Student ID')
    tk.Label(window_signup, text='User name: ').place(x=30, y=30)
    entry_new_name = tk.Entry(window_signup, textvariable=new_name)
    entry_new_name.place(x=150, y=30)

    new_pwd = tk.StringVar()
    tk.Label(window_signup, text='Password: ').place(x=30, y=80)
    entry_usr_pwd = tk.Entry(window_signup, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=80)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_signup, text='Confirm password: ').place(x=30, y=130)
    entry_usr_pwd_confirm = tk.Entry(window_signup, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=130)

    btn_comfirm_sign_up = tk.Button(window_signup, text='Sign up', command=sign_to_user)
    btn_comfirm_sign_up.place(x=150, y=180)

def reset_password():
    global old_name, rnew_pwd, rnew_pwd_confirm, window_reset_pass
    window_reset_pass = tk.Toplevel(window)
    window_reset_pass.title('welcome to reset password')
    window_reset_pass.geometry('350x300')  # width x height

    old_name = tk.StringVar()
    tk.Label(window_reset_pass, text='User name: ').place(x=30, y=30)
    entry_old_name = tk.Entry(window_reset_pass, textvariable=old_name)
    entry_old_name.place(x=150, y=30)

    rnew_pwd = tk.StringVar()
    tk.Label(window_reset_pass, text='Reset password: ').place(x=30, y=80)
    entry_rusr_pwd = tk.Entry(window_reset_pass, textvariable=rnew_pwd, show='*')
    entry_rusr_pwd.place(x=150, y=80)

    rnew_pwd_confirm = tk.StringVar()
    tk.Label(window_reset_pass, text='Confirm password: ').place(x=30, y=130)
    entry_rusr_pwd_confirm = tk.Entry(window_reset_pass, textvariable=rnew_pwd_confirm, show='*')
    entry_rusr_pwd_confirm.place(x=150, y=130)

    btn_comfirm_reset_password = tk.Button(window_reset_pass, text='Confirm reset', bg='red', command=confirm_reset)
    btn_comfirm_reset_password.place(x=150, y=180)

def confirm_reset():
    rnp = rnew_pwd.get()
    rnpf = rnew_pwd_confirm.get()
    rnn = old_name.get()
    with open('user_info.pickle', 'rb') as user_file:
        exist_userinfo = pickle.load(user_file)
    if rnn in exist_userinfo:
        if rnp != rnpf:
            tk.messagebox.showerror('Error', 'Password and Confirm password must be the same!')
        else:
            exist_userinfo[rnn] = rnp
            with open('user_info.pickle', 'wb') as user_file:
                pickle.dump(exist_userinfo, user_file)
            tk.messagebox.showinfo('Congratulation ', 'You have reset your password!')
            window_reset_pass.destroy()
    else:
        reset_confirm = tk.messagebox.askyesno('Opt!', 'the username does not exist,please try again')
        if reset_confirm:
            pass
        else:
            window_reset_pass.destroy()
            is_reset = tk.messagebox.askyesno('Welcome', 'You have not sign up yet. Sign up now?')
            if is_reset:
                signup()

def sign_to_user():
    np = new_pwd.get()
    npf = new_pwd_confirm.get()
    nn = new_name.get()
    with open('user_info.pickle', 'rb') as user_file:
        exist_userinfo = pickle.load(user_file)
    if nn in exist_userinfo:
        tk.messagebox.showerror('Error', 'The user has already signed up!')
    elif np != npf:
        tk.messagebox.showerror('Error', 'Password and Confirm password must be the same!')
    else:
        exist_userinfo[nn] = np
        with open('user_info.pickle', 'wb') as user_file:
            pickle.dump(exist_userinfo, user_file)
        tk.messagebox.showinfo('Congratulation ', 'You have successfully signed up!')
        window_signup.destroy()

def user_information():
    global user_info, user_file
    try:
        with open('user_info.pickle', 'rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file:
            user_info = {'admin': 'admin', '13900124': '13900124'}
            pickle.dump(user_info, user_file)

if __name__ == '__main__':
    w_window()
    w_canvas()
    w_label()
    w_entry()
    w_button()
    window.mainloop()