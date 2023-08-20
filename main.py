# https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/

import json
import csv

with open('qa-groups-roles.json') as groups_roles_file:
  groups_roles_contents = groups_roles_file.read()

with open('qa-roles-entitlements.json') as roles_entitlements_file:
  roles_entitlements_contents = roles_entitlements_file.read()

parsed_groups_roles = json.loads(groups_roles_contents)
parsed_roles_entitlements = json.loads(roles_entitlements_contents)

# groups = parsed_groups_roles["groups"]
# for group in groups:
#   print("Group:", group["groupName"])
#   roles = group["roles"]
#   for role in roles:
#     print(" Role:", role)
# print

roles = parsed_roles_entitlements["roles"]
with open('groups-roles-entitlements.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Role", "Group", "Platform", "Tenant", "Case Type", "Case Subtype", "Entitlement"])

  for role in roles:
    print("Role:",role["roleName"])
    entitlements = role["entitlements"]
    for entitlement in entitlements:
      # example entitlement = "omnius_case|complaints_case|tier_2|complaint_servicing|create_case"
      entitlementParts = entitlement.split('|')
      platform = entitlementParts[0]
      tenant = entitlementParts[1]
      caseType = entitlementParts[2]
      caseSubtype = entitlementParts[3]
      theEntitlement = entitlementParts[4]

      print(" Role: ",role["roleName"], " Entitlement:", entitlement)
      # find the groups for this role from Groups - will need a filter on groups to find?
      # print out one line for each Entitlement, Role and Group
      writer.writerow([role["roleName"], "this is the group", platform, tenant, caseType, caseSubtype, theEntitlement])
