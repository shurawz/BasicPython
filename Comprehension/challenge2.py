inch_measurement = (3, 8, 20)

cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)

tu = tuple([inch * 2.54 for inch in inch_measurement] )
print(tu)
