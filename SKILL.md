# DB Mapper Generator

## Name
DB Mapper Generator

## Description
The DB Mapper Generator skill is designed to automatically generate database mapper classes based on the provided database schema. It simplifies the process of mapping database records to application objects, reducing the manual effort required for data access layers.

## Version
1.0.0

## Author
ysaisme

## Features
- Automatic generation of mappers for various databases.
- Customizable templates for generated code.
- Support for multiple database types (e.g., MySQL, PostgreSQL, SQLite).
- Easy integration with existing applications.
- Generate full CRUD operations.

## Flow
1. User provides database schema details.
2. The generator analyzes the schema and determines the required mapper structure.
3. Generated mapper classes are produced based on the defined templates.
4. Users can customize the generated classes as needed.
5. Output mappers are ready for immediate use in the application.

## Generated Mapper Methods
- `findById(id)`: Retrieves a record by its ID.
- `findAll()`: Retrieves all records.
- `create(entity)`: Inserts a new record into the database.
- `update(entity)`: Updates an existing record.
- `deleteById(id)`: Deletes a record by its ID.