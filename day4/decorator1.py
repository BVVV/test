
login_status = False
def login(auth_type):
    def outer(func):
        def inner(*args, **kwargs):
            uname = "wenjie"
            password = "123"
            global login_status
            if not login_status:
                iuname = input("please input user name: ")
                ipassword = input("please input password: ")
                print("auth_type: %s" % auth_type)
                print(type(args))
                print(type(kwargs))
                if iuname == "wenjie" and ipassword == "123":
                    print("login successfully!")
                    login_status = True
            if login_status:
                func(*args, **kwargs)
        return inner
    return outer


@login("wx")
def japan():
    print("japan".center(80,'-'))


@login("qq")
def american(style):
    print("American".center(80,"-"))

japan()
american("3p")
