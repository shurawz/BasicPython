# import shelve
#
# with shelve.open("motor") as bike:
#     bike["Name"] = "Pulsar"
#     bike["Model"] = "280 NS"
#     bike["Date"] = "2019"
#
#     print(bike["Name"])
#     print(bike["Model"])

import shelve

with shelve.open("motor") as bike:
    bike["Name"] = "Pulsar"
    bike["Mode"] = "280 NS"
    bike["Date"] = "2019"

    # del bike["Mode"]

    print(bike["Name"])
    print(bike["Model"])
    print(bike["Mode"])


# import shelve
#
# with shelve.open("motor") as bike:
#     bike["Name"] = "Pulsar"
#     bike["Model"] = "280 NS"
#     bike["Date"] = "2019"
#     del bike['Mode']
#
#     for key in bike:
#         print(key)
#
#     print(bike["Name"])
#     print(bike["Model"])
    # print(bike["Mode"])
