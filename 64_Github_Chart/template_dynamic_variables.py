#For anyone trying to pass variables for these queries, I suggest looking at string.Template in python:

from string Import Template

queryTemplate = Template(
"""{
  viewer {
    repositories(first: $num) {
      pageInfo {
        hasNextPage
        endCursor
      }
      edges {
        node {
          name
        }
      }
    }
  }
}"""
)

query = queryTemplate.substitute(num=n)





################
query = """
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""