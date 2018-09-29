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

def updateLeave(email, course):
	
	leaveStats = getLeaveStats(email)
	leave = leaveStats[course] + 1; # TODO : change

	result = client.execute('''
	mutation update_leavetrack{
  		update_leavetrack(
    		where: {email : {_eq: "'''+email+'''"}}
    		_set: {'''+course+''': '''+str(leave)+'''}
  		){
    		affected_rows
  		}
  
	}

	''')
	print(result)

def getLeaveStats(email):
	result = client.execute('''
	{
  		leavetrack(
    		where: {email: {_eq:"'''+email+'''"}}
  		){
    		hss01
    		min106
    		ecn203
    		csn221
    		csn291
    		csn261
  		}
	}

	''')
	# print(result)
	r = json.loads(result)
	return r['data']['leavetrack'][0]

def getDaysInfo():
	result = client.execute('''
	{
  		daysinfo{
    		startsession
    		endsession
    		hss01
    		min106
    		ecn203
    		csn221
    		csn291
    		csn261
  		}
	}

	''')

	r = json.loads(result)
	return r['data']['daysinfo'][0]

def getTimeTable():
	result = client.execute('''
	{
  		timetable{
    		t8_9
    		t9_10
    		t10_11
    		t11_12
    		t12_1
    		t1_2
    		t2_3
    		t3_4
    		t4_5
    		t5_6
  		}
	}

	''')

	r = json.loads(result)
	return r['data']['timetable']

print(getTimeTable())

# print(getLeaveStats("aagarwal9782@gmail.com"))

# updateLeave("aagarwal9782@gmail.com", "min106")

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