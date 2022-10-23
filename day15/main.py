'''
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }


    ingre = MENU["espresso"]["ingredients"]

    # print(ingre)
    # print(resources)

    for item in resources and ingre:
        resources[item] = resources[item] - ingre[item]


    print(resources)
'''