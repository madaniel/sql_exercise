from connect import PostgresDatabaseHandler, PostgresConnectionHandler

db_handler = PostgresDatabaseHandler(connection=PostgresConnectionHandler())
rows = db_handler.run_command(command="SELECT * FROM actor")

for row in rows:
    print(row)
