# Using Python code challenge as the week 5 assignment.


#Read the contents of the txt file.
with open("input.txt" ,"r") as file:
    data=file.read()
    
#Count the number of words in the text file.
# Write the word count to a new file called output.txt.
try:
    with open("input.txt","r") as file, open("output" , "a") as output:
        word_count=len(file.read().split())
        output.write(str(word_count) + "\n")
        
except ModuleNotFoundError:
    print("File Error")
finally:
    file.close()
    
#Convert all text to uppercase
#Write the processed text to a new file called output.txt
try:
    with open("input.txt" , "r") as upper_case, open("output.txt", "a") as result:
        output=upper_case.read().upper()
        result.write(output)
        print(output)
        
except FileExistsError:
    print("code error")

#Print a success message once the new file is created.
print("success!")
    
    
    
    