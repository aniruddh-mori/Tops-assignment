
def mask_phone_number(phone):
    if (len(phone)==10):
        newstr = ""
        for i in range(0,10,1):
            if (i<6):
                newstr += "*"
            else:
                newstr+=phone[i]
        return newstr
    else:
        print("Please Enter a valid Phone Number !!!")
    
print(mask_phone_number("1234567890"))
