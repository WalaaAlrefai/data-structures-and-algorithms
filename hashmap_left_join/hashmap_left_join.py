from hash_table.hash_table import Hashtable

# class HashTable:
#     def __init__(self):
#         self.table = {}

#     def set(self, key, value):
#         self.table[key] = value

#     def remove(self, key):
#         if key in self.table:
#             del self.table[key]

#     def __str__(self):
#         return str(self.table)



def left_join(table_1, table_2):
    """ function that LEFT JOINs two hashmaps into a single data structure.
           - Arguments: two hash maps
           - The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
           - The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
           - Return: achieves the LEFT JOIN logic Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
    """

    table_1_join = []

    for key in table_1:
        join_left = [key, table_1.get(key), table_2.get(key) or "None"]
        table_1_join.append(join_left)


    return table_1_join



synonyms_hash_table = {
    "diligent": "employed",
    "fond": "enamored",
    "guide": "usher",
    "outfit": "garb",
    "wrath": "anger",
}

antonyms_hash_table = {
    "diligent": "idle",
    "fond": "averse",
    "guide": "follow",
    "flow": "jam",
    "wrath": "delight",
}

# Call the function with the hash tables as input
result =  left_join(synonyms_hash_table, antonyms_hash_table)
print (result)





