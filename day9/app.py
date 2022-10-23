# programming_dictionary = {
#     "Bug": "Lorem Ipsum dolor sit amet",
#     "Function": "A piece of code",
#     "Loop": "The action of doing something over and over again"
# }
#
# programming_dictionary["Loops"] = "The plural of loop"
#
# print(programming_dictionary)

# Nestiing
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
# Nesting a dictionary in a list
travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    },
]
