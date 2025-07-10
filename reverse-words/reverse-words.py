#Reverse the words


### -my own code- ###

def sentence(sen):
    sen_show = ""
    a = len(sen)
    for i in range(a-1,-1,-1):
        sen_show += sen[i]
    print(sen_show)

sen_input = input("Enter your sentence: ")
sentence(sen_input)

#---------------------------
### -Chat GPT code- ###

# def sentence(sen):
#     print(sen[::-1])  # برگرداندن رشته با slicing

# sen_input = input("Enter your sentence: ")
# sentence(sen_input)