
users = [
      { "id": 1, "name": "Anna Administrator", "roles": ["superuser"] },
      { "id": 2, "name": "Charles N. Charge", "roles": ["charger", "rider"] },
      { "id": 7, "name": "Ryder", "roles": ["rider"] },
      { "id": 11, "name": "Unregistered Ulysses", "roles": [] },
      { "id": 18, "name": "Tessa Tester", "roles": ["beta tester"] },
    ]
    
permissions = [
      { "role": "superuser", "name": "lock user account", "active": True },
      { "role": "superuser", "name": "unlock user account", "active": True },
      { "role": "superuser", "name": "purchase widgets", "active": False },
      { "role": "charger", "name": "view pick up locations", "active": True },
      { "role": "rider", "name": "view my profile", "active": True },
      { "role": "rider", "name": "scooters near me", "active": True },
    ]


# @rtype: list of strings
# @returns: a list of all the active permission names that the user with the corresponding user_id has
# @note: The order in which the permission names are returned is not important
# @example: listPermissions(1) ➡ ["View Orders", "Block User Account"] (purchased widgets not included since it is not active)    
def list_permissions(user_id):
    user = next((u for u in users if u.get("id") == user_id), f"No user with {user_id}")
    roles =(user.get("roles", f"No roles with {user_id}"))
    result = [p.get('name') for p in permissions if p.get('active') and p.get('role') in roles]
    return result

# @rtype: boolean value
# @returns: true or false based on if the user with the corresponding user_id has the role that corresponds with the specific permission_name and that particular permission is active
# @example: Example (Based on data from graphic)
# checkPermitted("scooters near me", 2) ➡ true
# checkPermitted("scooters near me", 1) ➡ false    
def check_permitted(permission_name, user_id):
    user = next((u for u in users if u.get("id")==user_id),f"No user with id{user_id}")
    roles = (user.get("roles"),[])
    for p in permissions:
        if p.get("name") == permission_name and p.get("active") and p.get("role") in roles:
            return True
    return False



if __name__ == "__main__":
    print(list_permissions(2))
    print(check_permitted("lock user account",1))