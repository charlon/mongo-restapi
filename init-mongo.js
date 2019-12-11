db.createUser(
  {
    user: "YourUsername",
    pwd: "YourPasswordHere",
    roles: [
      {
        role: "readWrite",
        db: "my-database-name"
      }
    ]
  }
)
