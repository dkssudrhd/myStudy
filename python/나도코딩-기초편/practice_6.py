def std_weight(height, gender):
    if gender == "man":
        return height * height * 22 / 10000
    else: 
        return height * height * 21 / 10000


print(round(std_weight(175.0, "man"), 2))
