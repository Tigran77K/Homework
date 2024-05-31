#Write a function that swaps the values of two tuples.
tuple_1 = (1,2,3,4)
tuple_2 = (5,6,7,8)
def swap_tuples(tuple1, tuple2):
    tuple3 = tuple1
    tuple1 = tuple2
    tuple2 = tuple3
    return tuple1 , tuple2

print(swap_tuples(tuple_1,tuple_2))
print()
