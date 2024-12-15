# API Documentation for Personal Knowledge Base Simple API

## Overview

This API is designed to manage a personal knowledge base, allowing users to store and retrieve commands, categories, and their respective descriptions.

## Endpoints

### Categories

- GET /categories: Retrieves a list of all categories.
- POST /categories: Creates a new category.
- GET /categories/int:category_id: Retrieves a specific category by ID.
- DELETE /categories/int:category_id: Deletes a category by ID.

### Commands

- GET /categories/int:category_id/commands: Retrieves a list of commands for a specific category.
- POST /categories/int:category_id/commands: Creates a new command for a specific category.
- GET /categories/int:category_id/commands/int:id: Retrieves a specific command by ID.
- DELETE /categories/int:category_id/commands/int:id: Deletes a command by ID.
- PUT /categories/int:category_id/commands/int:id: Updates a command by ID.

## Request and Response Formats

- Request bodies should be in JSON format.
- Response bodies will be in JSON format.

### Request Parameters

- kb_post_args:
  - id: ID of the category (integer)
  - command: Command to be stored (string)
  - command_description: Description of the command (string)
- kb_update_args:
  - command: Command to be updated (string)
  - command_description: Description of the command (string)

## Response Fields

- category_resource_fields:
  - id: ID of the category (integer)
  - category: Name of the category (string)
- command_resource_fields:
  - id: ID of the command (integer)
  - category_id: ID of the category (integer)
  - category: Name of the category (string)
  - command: Command (string)
  - command_description: Description of the command (string)

## Error Handling

- Errors will be returned in JSON format with a corresponding HTTP status code.

## Examples

Create a new category

```
curl -X POST \
  http://127.0.0.1:5000/categories \
  -H 'Content-Type: application/json' \
  -d '{"category": "Linux"}'
```

Create a new command

```
curl -X POST \
  http://127.0.0.1:5000/categories/1/commands \
  -H 'Content-Type: application/json' \
  -d '{"command": "ls -l", "command_description": "List files in long format"}'
```

Retrieve a list of commands for a category

```
curl -X GET \
  http://127.0.0.1:5000/categories/1/commands
```

Update a command

```
curl -X PUT \
  http://127.0.0.1:5000/categories/1/commands/1 \
  -H 'Content-Type: application/json' \
  -d '{"command": "ls -la", "command_description": "List files in long format with hidden files"}'
```

Delete a command

```
curl -X DELETE \
  http://127.0.0.1:5000/categories/1/commands/1
```
