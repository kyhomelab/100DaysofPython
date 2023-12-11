supplies = ["tent", "sleeping bags", "water", "rasberry pi", "knife", "fishing rod", "lighter", "marshmallows"]

site = ["Crystal Lake", 404, 89.3, True]

# supplies.append("toilet paper")
# supplies.append("bidet")

# supplies.extend(["toilet paper", "bidet"])

# supplies = supplies + ["toilet paper", "bidet"]
supplies.insert(0, "bidet")
supplies.insert(-1, "toilet paper")

print(supplies)

