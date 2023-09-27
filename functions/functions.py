import re

def generate_email(row):
    name_parts = row["Student Name"].split()
    if len(name_parts) >= 3:
        first_letter = name_parts[0][0].lower()
        last_name = name_parts[2].lower()
        last_name_cleaned =  re.sub(r'[^a-zA-Z]', '', last_name)     
    else:
        first_letter = name_parts[0][0].lower()
        last_name = name_parts[1].lower()
        last_name_cleaned =  re.sub(r'[^a-zA-Z]','', last_name)

    return f"{first_letter.lower()}{last_name_cleaned.lower()}@strathmore.edu"



