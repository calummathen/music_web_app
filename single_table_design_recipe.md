_Copy this recipe template to design and create a database table from a specification._

## 1. Extract nouns from the user stories or specification

```
As a user I want to add an album
```

```
Nouns:

album, title, release year, artist_id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| album                 | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, 'artist_id'

## 3. Decide the column types

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL

```sql
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```