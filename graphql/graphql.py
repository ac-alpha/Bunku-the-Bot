from graphqlclient import GraphQLClient
import json

client = GraphQLClient('https://banku-synfour.herokuapp.com/v1alpha1/graphql')

def startRecording(email):
	result = client.execute('''
	mutation insert_leavetrack{
  		insert_leavetrack(
    		objects:[
    		{
        		email : "'''+ email + '''"
        		hss01: 0
        		min106: 0
        		ecn203: 0
        		csn221: 0
        		csn291: 0
        		csn261: 0
      		}
    	]){
    		returning{
      			email
    		}
  		}
	}

	''')
	print(result)

# startRecording("aagarwal9782@gmail.com")

# result = client.execute('''
# {
#   timetable {
#     day
#     t8_9
#     t9_10
#   }
# }
# ''')

# r = json.loads(result)

# print(result)
# print(r['data']['timetable'][0]['day'])