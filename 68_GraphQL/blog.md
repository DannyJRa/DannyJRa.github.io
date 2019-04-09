### Run docker 

The following changes have to be made to the command:

Database URL
Network config

How do I turn off telemetry (opt-out)
HASURA_GRAPHQL_ENABLE_TELEMETRY=false

Run the docker command with an admin-secret env var
-e HASURA_GRAPHQL_ADMIN_SECRET=myadminsecretkey \

```Bash
docker run -d -p 8095:8080 \
  -e HASURA_GRAPHQL_DATABASE_URL=postgres:<inser>
  -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
  -e HASURA_GRAPHQL_ENABLE_TELEMETRY=false \
  -e HASURA_GRAPHQL_ADMIN_SECRET=myadminsecretkey \
  hasura/graphql-engine:latest
```



docker start 59ccb61e10eb925b6dd2b897cef27b4848690c2b95f44b1d4b410d218f7ef4d8
See docker logs

 docker ps
 docker logs 4e78dd617046

${S_email}