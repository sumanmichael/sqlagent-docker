# SQLAgent: A LangChain-Powered SQL Agent

**Overview**

SQLAgent is a Dockerized application that combines the power of LangChain and PostgreSQL to create a conversational SQL agent. This agent can interact with a PostgreSQL database using natural language input, making it easy to query and manage data.

**Getting Started**

To get started, clone this repository and navigate to the project root directory. Then, use the following command to start the application:

```
docker-compose up -d
```

This will start the PostgreSQL database and the SQLAgent service in detached mode. Once the service is up and running, you can access the API using `http://localhost:8000`.

**API Endpoints**

The SQLAgent API provides several endpoints for interacting with the PostgreSQL database:

* `/invoke`: Run a SQL query using natural language input.
* `/batch`: Run a batch of SQL queries using natural language input.
* `/stream`: Stream a SQL query result set using natural language input.
* `/stream_events`: Stream events from a SQL query result set using natural language input.

**Configuration**

The following environment variables can be configured:

* `OPENAI_API_KEY`: Your OpenAI API key.
* `DB_CONNECTION_STRING`: The connection string for your PostgreSQL database.

**Dependencies**

This project depends on the following libraries:

* LangChain
* Pydantic
* LangChain-Community
* LangChain-OpenAI
* LangServe
* Psycopg2-binary

**Build and Run**

To build the Docker image, navigate to the `sqlagent` directory and run:

```
docker build -t sqlagent .
```

To run the application, use the following command:

```
docker run -p 8000:8000 sqlagent
```

**Development**

This project uses Poetry for dependency management and Pydantic for schema validation. The `Dockerfile` is used to build the Docker image, and `docker-compose` is used to manage the application containers.

**License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

**Authors**

Suman Michael ([sumanmichael01@gmail.com](mailto:sumanmichael01@gmail.com))