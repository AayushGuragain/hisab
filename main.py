if __name__ == '__main__':
    title_of_split = input("What is the split for?: ")
    number_of_splits = int(input("How many splits are we talking about? : "))
    saved_No_Of_Split = number_of_splits

    name_of_people = []
    common_cat = input("Do you have a common category? Ans in (y/n): ")
    if common_cat[0] == 'y' or common_cat[0] == 'Y':
        number_of_splits +=1
    for i in range(number_of_splits):
        name_of_people.append(input(f"What is the category no {i}?: "))

    total_amount = float(input("Enter the total amount: "))
    total_tax = float(input("Enter the total tax: "))
    amount_to_divide = total_amount - total_tax
    print("")

    math_of_people = []
    i = 0
    total_so_far = 0

    while(i < number_of_splits):
        next_category = True
        math_done = 0
        while(next_category):
            bought_item = str(input(f'What did "{name_of_people[i]}" buy? Hit "q" to quit: '))
            if bought_item[0] == 'q' or bought_item[0] == 'Q':
                math_of_people.append(math_done)
                next_category = False
            else:
                bought_item = float(bought_item)
                math_done += bought_item
                total_so_far += bought_item
        print("")
        i += 1
    print(f"The total after one by one addition of the above maths is {total_so_far}.")
    if round(total_so_far) != round(amount_to_divide):
        print("\n!!!!!!!!!!!!!!!!!\nSomething is wrong!\n\n")


    print(f"The title is: {title_of_split}")
    print(f"Total number of categories: {number_of_splits}")
    print(name_of_people)
    print(math_of_people, end='')
    grand_total = 0
    for num in math_of_people:
        grand_total = grand_total + num
    print(f" = {grand_total}.")
    print(f"The total amount is {total_amount}")
    print(f"The total tax is {total_tax}")
    print(f"The total amount to divide is {amount_to_divide}")
