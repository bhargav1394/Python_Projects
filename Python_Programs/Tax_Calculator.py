user_input = int(input("Welcome to program \n"
                       "We providing below services. please select any one you want \n"
                       "1) Tax Calculator \n"
                       "2) Monthly Salary If you expected package\n"))

if user_input == 1:
    package_user=int(input("Please enter your Annual package"))
    sta_ded_package = package_user - 75_000
    if sta_ded_package >= 4_00_000:
        first_ded = sta_ded_package - 4_00_000
        first_ded_per = first_ded * 0.05
        print("Your Tax:", first_ded_per)
    elif sta_ded_package >= 8_00_000:
        first_ded = (sta_ded_package - 4_00_000) * 0.05
        first_ded_per = first_ded * 0.05
        print("Your Tax:", first_ded_per)

    else:
        print("Enjoy year No TAX for you")