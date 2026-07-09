# T1=()
# print(type(T1))

# point = (10, 20)
# colors = ("red", "green", "blue")
# print(point[0]) # 10 (indexing works like a list)
# print(colors[-1]) # blue


# # point = (10, 20)
# # point[0] = 99 # ERROR!
# # # TypeError: 'tuple' object does not support item assignment
# person = "Rajeev", 34, "Varanasi"
# print(person) # ('Rajeev', 34, 'Varanasi')
# # Unpacking — pulling values out
# name, age, city = person
# print(name) # Rajeev
# print(city) # Varanasi
# # The classic: swap two variables with no temp!
# a, b = 1, 2
# a, b = b, a
# print(a, b) # 2 1
# # Star unpacking — grab the rest
# first, *rest = (1, 2, 3, 4)
# print(first, rest) # 1 [2, 3, 4]

# # set

# nums = {1, 2, 2, 3, 3, 3}
# print(nums) # {1, 2, 3} duplicates gone!
# # Remove duplicates from a list instantly
# items = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(items))
# print(unique) # [1, 2, 3, 4, 5]   

# s = {1, 2, 3}
# s.add(4) # {1, 2, 3, 4}
# s.remove(2) # {1, 3, 4} (errors if missing)
# s.discard(99) # safe — no error if missing
# print(s)


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b) # {1,2,3,4,5,6} UNION (all items)
# print(a & b) # {3, 4} INTERSECTION (common)
# print(a - b) # {1, 2} DIFFERENCE (in a, not b)
# print(a ^ b) # {1,2,5,6} SYMMETRIC (not shared)


# # frozenset — the immutable set
# fs = frozenset([1, 2, 3])
# print(fs) # frozenset({1, 2, 3})
# fs.add(4) # ERROR — can't change a frozenset


big_list = [1, 2, 3, ..., 1000000]
big_set = {1, 2, 3, ..., 1000000}
999999 in big_list # SLOW — checks items one by one (O(n))
999999 in big_set # FAST — jumps straight to it (O(1))
