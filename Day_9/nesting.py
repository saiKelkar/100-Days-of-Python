# {Key: Value}
# {
#   Key: [List],  
#   Key: {Dict}
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    },
}

print(travel_log["Germany"]["cities_visited"][2])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])