# my_dictionary = {
#     "apple" : "123" ,
#     "orange" : "456",
#     "Student" :"id",
#     "roll.no" : "789"

# }

# words = input("enter the words: ")
# print(my_dictionary.get(words, "words not found"))



dictionary = {
    "Apple": "स्याउ",
    "Book": "किताब",
    "Cat": "बिरालो",
    "Dog": "कुकुर",
    "House": "घर",
    "Water": "पानी",
    "Food": "खाना",
    "School": "विद्यालय",
    "Teacher": "शिक्षक",
    "Student": "विद्यार्थी",
    "Computer": "कम्प्युटर",
    "Mobile": "मोबाइल",
    "Table": "टेबल",
    "Chair": "कुर्सी",
    "Window": "झ्याल",
    "Door": "ढोका",
    "Sun": "सूर्य",
    "Moon": "चन्द्रमा",
    "Star": "तारा",
    "Tree": "रुख",
    "Flower": "फूल",
    "River": "नदी",
    "Mountain": "पहाड",
    "Road": "सडक",
    "Car": "गाडी",
    "Bus": "बस",
    "Train": "रेल",
    "Airplane": "हवाईजहाज",
    "Friend": "साथी",
    "Family": "परिवार",
    "Mother": "आमा",
    "Father": "बुबा",
    "Brother": "दाजु/भाइ",
    "Sister": "दिदी/बहिनी",
    "Child": "बच्चा",
    "Morning": "बिहान",
    "Evening": "साँझ",
    "Night": "रात",
    "Day": "दिन",
    "Time": "समय",
    "Money": "पैसा",
    "Market": "बजार",
    "Hospital": "अस्पताल",
    "Doctor": "डाक्टर",
    "Nurse": "नर्स",
    "Work": "काम",
    "Love": "माया",
    "Happiness": "खुसी",
    "Peace": "शान्ति",
    "Success": "सफलता"
}


result = input("enter the words: ").title()

print (dictionary.get(result, "words not found"))
