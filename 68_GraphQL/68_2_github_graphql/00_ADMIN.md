# Open Folder 68_


python 68_2_github_graphql/01_main_github_graphql.py

History only last 100 commits

{
  repository(owner: "facebook", name: "react") {
    object(expression: "master") {
      ... on Commit {
        total: history {
          totalCount
        }
        first100: history(first: 100) {
          edges {
            cursor
            node {
              committedDate
            }
          }
        }
        second100: history(after: "700f17be6752a13a8ead86458e343d2d637ee3ee 99") {
          edges {
            cursor
            node {
              committedDate
            }
          }
        }
      }
    }
  }
}
However I had to manually enter the cursor String that I'm passing in the second connection: second100: history(after: "cursor-string") {}.

How can I recursively run this connection until I have a query for all the committedDates of commits in a repository?



Yes, you can query them in batches of 100 until you have all of them. The cursor value that you placed in the `second100` part of the query you can obtain as part of the original query by rewriting it like this:

 

{
  repository(owner: "facebook", name: "react") {
    object(expression: "master") {
      ... on Commit {
        history {
          nodes {
            committedDate
          }
          pageInfo {
            endCursor
          }
        }
      }
    }
  }
}
This results in a query response that ends like this:

 

...
            },
            {
              "committedDate": "2019-03-07T12:39:15Z"
            },
            {
              "committedDate": "2019-03-07T00:39:39Z"
            },
            {
              "committedDate": "2019-03-06T23:50:02Z"
            },
            {
              "committedDate": "2019-03-06T22:41:45Z"
            },
            {
              "committedDate": "2019-03-06T18:17:54Z"
            }
          ],
          "pageInfo": {
            "endCursor": "b93a8a9bb8460a3d582072d3b252ecc15c6ea0f5 99"
          }
        }
      }
    }
  }
}
And the `endCursor` value is the one you want to pass as the `after` value in the next query.