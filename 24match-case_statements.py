# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a valuue matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It is Monday"
        case 2:
            return "It is Tuesday"
        case 3:
            return "It is Wednesday"
        case 4:
            return "It is Thursday"
        case 5:
            return "It is Friday"
        case 6:
            return "It is Saturday"
        case 7: 
            return "It is Sunday"
        case _:
            return "Not a valid day"
        
print(day_of_week(2))
# | means OR
def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":
            return True
        case _:
            return False
        
print(is_weekend("Monday"))