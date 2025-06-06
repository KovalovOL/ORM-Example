from db import Base, engine
from crud import create_user, read_users, update_user, delete_user

# Create tables
Base.metadata.create_all(bind=engine)

# Run CRUD operations
# create_user("name", "email@example.com")


print("All users:")
for user in read_users():
    print(user.id, user.name, user.email)

update_user(1, new_name="new name")
delete_user(2)

print("After changes:")
for user in read_users():
    print(user.id, user.name, user.email)
