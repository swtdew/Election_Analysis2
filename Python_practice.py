# print("Hello World")

# counties =['Arapahoe','Denver', "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# for county in counties:
#     print(county)
# for i in range(len(counties)):
#     print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county, voters in counties_dict.items():
    print(county, voters)
print(f "counties[1] county has")