from graphqlclient import GraphQLClient
import json

client = GraphQLClient('https://banku-synfour.herokuapp.com/v1alpha1/graphql')

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
	return r['data']['leavetrack']

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

def getStats(email):
	return getDaysInfo(), getTimeTable(), getLeaveStats(email)

def updateLeave(email, course):
	
	leaveStats = getLeaveStats(email)[0]
	leave = leaveStats[course] + 1

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

def cancelClass(course):
	daysStats = getDaysInfo()
	workingDays = daysStats[course] - 1

	result = client.execute('''
	mutation update_daysinfo{
  		update_daysinfo(
    		where: {sno : {_eq: 1}}
    		_set: {'''+course+''': '''+str(workingDays)+'''}
  		){
    		affected_rows
  		}
  
	}

	''')
	print(result)

def extraClass(course):
	daysStats = getDaysInfo()
	workingDays = daysStats[course] + 1

	result = client.execute('''
	mutation update_daysinfo{
  		update_daysinfo(
    		where: {sno : {_eq: 1}}
    		_set: {'''+course+''': '''+str(workingDays)+'''}
  		){
    		affected_rows
  		}
  
	}

	''')
	print(result)


def startRecording(email):
  
  if getLeaveStats(email) == [] :
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

