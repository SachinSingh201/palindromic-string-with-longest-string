# palndromic string with longest string code 
#Q5 LC


s = input("Enter the string for palindromic substring::")
length = len(s)
lst = []
for n in range(1,length+1):
    for i in range (length+1-n):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            lst.append(substring)
            


palindro_str = max(lst ,key =len ) if lst else ""
print("palindromic longesgt is {} and length is {}".format(palindro_str, len(palindro_str)))    