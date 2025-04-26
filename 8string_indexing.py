# indexing = accessgin elements of a sequence using [] (indexing operator)
#            [start : end : step]
#        start:inclusive    end:exclusive
credit_number = "1234-5678-9012-3456"
#                012345678...
credit_number[0]

print(credit_number)

credit_number[0:4] # first four digits
credit_number[:4]  # first four digits
credit_number[5:9]
credit_number[5:] # 5: means everything since 5 till the end of the string
credit_number[-1] # last character in the string

#steps
credit_number[::2] # every second character in our string
credit_number[::3] # every third character in our string

last_digits = credit_number[-4:] #last four digits
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] # reverses the string