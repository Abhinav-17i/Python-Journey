dic = {
    "student1": {
        "Name" : "Robert Terravox",
        "Age": 27,
        "Marks": {
            "Maths" : 97,
            "Physics" : 98,
            "Chemisry" : 92
        }   
    }
}

insert = {"Name": "Murthy","Age": 25,"Marks" : {"maths":85,"Physics":78,"Chemistry":75}}
dic["student2"] = insert 
print(dic)