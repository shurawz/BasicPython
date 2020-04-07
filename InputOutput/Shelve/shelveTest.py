import shelve #Since, shelve is the library right here

family = shelve.open("shelft")
family["Julpa"] = "House captain"
family["Dilbdr"] = "House Vice-captian"
family["Sumitra"] = "Leader of the whole house"
family["Suraj"] = "Elder son of the family"
family["Susan"] = "Young son of the family"

print(family["Julpa"])
print(family["Susan"])



family.close()

#Too many files like .bak, .dat, .dir are created on the same directory

