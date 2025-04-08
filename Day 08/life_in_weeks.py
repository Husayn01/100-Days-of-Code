def life_in_weeks(age):
    # Define the total number of years you expect to live
    total_years = 90
    
    # Calculate the remaining years
    remaining_years = total_years - age
    
    # Calculate the number of weeks left
    weeks_left = remaining_years * 52
    
    # Output the result with f-strings
    print(f"You have {weeks_left} weeks left.")
