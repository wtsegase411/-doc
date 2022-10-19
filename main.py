# number 1
def yearInSchool():
    grade = int(input("Enter students class grade (1 - 12): "))
    score = int(input("Enter the students score (0 - 100): "))
    if grade >= 1 and grade <= 5:
        print("The student is in Elementary")
    elif grade >= 6 and grade <= 8:
        print("The student is in Middle school")
    elif grade >= 9 and grade <= 12:
        print("The student is in High school")
    else:
        print("Invalid class grade")
    if score >= 40 and score <= 59:
        print("The student scored poor")
    elif score >= 60 and score <= 79:
        print("The student scored distinct")
    elif score >= 80 and score <= 100:
        print("The student scored excellent")
    else:
        print("The score is invalid")


# number 2
def ageGender():
    age = int(input("Enter age (1 - 100): "))
    gender = (input("Enter gender (m or f): "))

    if age <= 1 and age < 10 and gender == 'm':
        print("He is a " + str(age) + " year old kid")
    elif age <= 1 and age <= 10 and gender == 'f':
        print("She is a " + str(age) + " year old kid")
    elif age <= 10 and age < 20 and gender == 'm':
        print("He is a " + str(age) + " year old teenager")
    elif age <= 10 and age < 20 and gender == 'f':
        print("She is a " + str(age) + " year old teenager")
    elif age <= 20 and age < 40 and gender == 'm':
        print("He is a " + str(age) + " year old young man")
    elif age <= 20 and age < 40 and gender == 'f':
        print("She is a " + str(age) + " year old young woman")
    elif age <= 40 and age < 60 and gender == 'm':
        print("He is a " + str(age) + " year old adult")
    elif age <= 40 and age < 60 and gender == 'f':
        print("She is a " + str(age) + " year old adult")
    elif age <= 60 and age < 100 and gender == 'm':
        print("He is a " + str(age) + " year old man")
    elif age <= 60 and age < 100 and gender == 'f':
        print("She is a " + str(age) + " year old woman")
    else:
        print("Invalid")


# number 3
def twoSum(nums, x):
    dictt = {}
    for i in range(len(nums)):
        nextPair = x - nums[i]
        if nextPair in dictt:
            return nextPair, nums[i]

        dictt[nums[i]] = i


# number 4
def monthName(letter):
    switch = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switch.get(letter, "No month exists")

# yearInSchool()
# ageGender()
# liss = [2,3,4,4,9]
# print(twoSum(liss, 8))
# print(monthName(7))
