source = "0123456789"
#
# hot = len(source)
# # creating iterator:
my_iterator = iter(source) #iter() means function to process each iteration.
#
# print("\n {}".format(hot))
# print(my_iterator)
# print(next(my_iterator))

for i in range(0, len(source)):   #for(i=0;i<len(source),i++)
    next_item = next(my_iterator)

    print(next_item)
