## Setup for vector database
In this case the vectordatabase is in postgres using **pg vector**

### Docker Setup

regular:
```sh
docker run --name note-finder-db -e POSTGRES_PASSWORD=password -p 5431:5432 -d postgres
```

pgvector:
```sh
docker run --name note-finder-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=note-finder-db -p 5431:5432 -d pgvector/pgvector:pg16

docker restart note-finder-db
```

### Delete commands (for clearing embeddings)
delete all current embeddings given a collection name
```sql
DELETE FROM langchain_pg_embedding WHERE collection_id = (SELECT uuid FROM langchain_pg_collection WHERE name = COLLECTION_NAME)
```