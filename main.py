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
groups = parsed_groups_roles["groups"]
roles = parsed_roles_entitlements["roles"]

with open('groups-roles-entitlements.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Group", "Role", "Platform", "Tenant", "Case Type", "Case Subtype", "Entitlement"])

  for role in roles:
    roleName = role["roleName"]
    print("Role:",roleName)
    entitlements = role["entitlements"]
    for entitlement in entitlements:
      entitlementParts = entitlement.split('|')
      platform = entitlementParts[0]
      tenant = entitlementParts[1]
      caseType = entitlementParts[2]
      caseSubtype = entitlementParts[3]
      theEntitlement = entitlementParts[4]

      groupsForThisRole = [group for group in groups if roleName in group["roles"]]

      for group in groupsForThisRole:
        print(group["groupName"], role["roleName"], platform, tenant, caseType, caseSubtype, theEntitlement)
        writer.writerow([group["groupName"], role["roleName"], platform, tenant, caseType, caseSubtype, theEntitlement])
