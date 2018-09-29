from graphqlclient import GraphQLClient
import json

client = GraphQLClient('https://banku-synfour.herokuapp.com/v1alpha1/graphql')

result = client.execute('''
{
  timetable {
    day
    t8_9
    t9_10
  }
}
''')

r = json.loads(result)

print(result)
print(r['data']['timetable'][0]['day'])