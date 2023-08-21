# https://www.freecodecamp.org/news/loading-a-json-file-in-python-how-to-read-and-parse-json/
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.scaler.com/topics/how-to-create-a-csv-file-in-python/
# https://stackoverflow.com/questions/598398/searching-a-list-of-objects-in-python

import json
import csv

with open('qa-groups-roles.json') as groups_roles_file:
  groups_roles_contents = groups_roles_file.read()

with open('qa-roles-entitlements.json') as roles_entitlements_file:
  roles_entitlements_contents = roles_entitlements_file.read()

parsed_groups_roles = json.loads(groups_roles_contents)
parsed_roles_entitlements = json.loads(roles_entitlements_contents)
allGroups = parsed_groups_roles["groups"]
allRoles = parsed_roles_entitlements["roles"]

with open('groups-roles-entitlements.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["Group", "Role", "Platform", "Tenant", "Case Type", "Case Subtype", "Entitlement"])

  for group in allGroups:
    groupName = group["groupName"]
    roles = group["roles"]
    print("Group: ",groupName)
    for role in roles:
      print(" Role: ",role)

      roleEntitlements = next((roleEntitlement for roleEntitlement in allRoles if roleEntitlement["roleName"] == role), None)

      entitlements = roleEntitlements["entitlements"]
      for entitlement in entitlements:
        print("  Entitlement: ",entitlement)
        entitlementParts = entitlement.split('|')
        platform = entitlementParts[0]
        tenant = entitlementParts[1]
        caseType = entitlementParts[2]
        caseSubtype = entitlementParts[3]
        theEntitlement = entitlementParts[4]
        # print(groupName, role, platform, tenant, caseType, caseSubtype, theEntitlement)
        writer.writerow([groupName, role, platform, tenant, caseType, caseSubtype, theEntitlement])
