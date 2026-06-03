COURSE: CSE 340 - Advanced Database Systems
DATE: May 14, 2026
TOPIC: Graph Databases, Index-Free Adjacency, and Cypher Query Optimization

---

## 1. Architectural Paradigms: Relational (SQL) vs. Graph (NoSQL)
Relational databases organize data into rigid tabular rows and columns. When traversing deeply nested relationships (e.g., "Find products purchased by friends of user X"), SQL must compute expensive set intersections at runtime using foreign keys and table JOIN operations. As data depth increases, query latency scales exponentially.

Graph databases utilize Index-Free Adjacency (IFA). Nodes point directly to adjacent nodes via physical memory addresses stored on disk. Relationships are first-class structural entities. Traversing a relationship is a localized O(1) pointer chase, meaning query performance scales relative to the size of the specific subgraph being explored, independent of the billions of rows elsewhere in the global database.

Relational Approach (Join Tables):
[Users Table] ──> [User_Friends Join] ──> [Friends Table] ──> [Orders Table]

Graph Approach (Direct Pointers):
(User) ───[:FRIEND]───> (Friend) ───[:PURCHASED]───> (Product)

---

## 2. Property Graph Modeling Fundamentals
A Labeled Property Graph consists of four specific primitives:
1. Nodes: Discrete entities (analogous to table records).
2. Labels: Typestate tags used to group and index nodes (e.g., :Person, :Organization, :Vehicle). A node can hold multiple labels.
3. Relationships: Directed, typed edges connecting two nodes (e.g., -[r:DRIVES]->). Relationships must have a direction and a singular type.
4. Properties: Arbitrary key-value pairs stored directly inside nodes or relationships (e.g., user.signup_date = "2026-05-01", works_at.role = "Data Intern").

---

## 3. Cypher Syntax & Traversal Mechanics
Cypher is a declarative, pattern-matching query language that relies on an ASCII-art style syntax to map graph topologies.

- Nodes are wrapped in parentheses: (p:Person)
- Relationships are wrapped in brackets with directional hyphens/arrows: -[r:KNOWS]-> or <-[:MANUFACTURED]-

### Production Query Example: Targeted Collaborative Filtering
The goal is to find friends-of-friends who aren't currently connected to Alice, but who have purchased products within the "Machine Learning" category, returning recommended items.

// Step 1: Match local ego network boundary
MATCH (alice:Person {id: "usr_9981"})-[:FRIEND]-(friend:Person)-[:FRIEND]-(fof:Person)

// Step 2: Ensure we filter out Alice herself and her direct friends
WHERE fof <> alice 
  AND NOT (alice)-[:FRIEND]-(fof)

// Step 3: Traverse out to item interactions
MATCH (fof)-[:PURCHASED]->(prod:Product)-[:BELONGS_TO]->(cat:Category {name: "Machine Learning"})

// Step 4: Aggregate results and compute recommendation weight
RETURN prod.id AS recommendation, 
       prod.title AS product_name, 
       COUNT(DISTINCT fof) AS community_endorsements
ORDER BY community_endorsements DESC
LIMIT 10;

---

## 4. Query Optimization & Execution Strategy
- Anchor Nodes: Neo4j evaluates queries by locating an "anchor node" via a schema index lookup (e.g., looking up Alice by her specific ID usr_9981).
- Directionality: If a relationship direction doesn't matter for the domain logic, omit the arrow tip -(r:REL)- to allow the engine to traverse edges bidirectionally, though specifying direction -> optimizes traversal by skipping invalid directional paths early.
- Profile vs. Explain:
    * EXPLAIN: Shows the execution plan compiled by the database engine without executing the query (useful for checking index hits).
    * PROFILE: Executes the query completely and reports exact memory allocations and db hits per operation block. Aim to minimize db hits inside deep traversal loops.