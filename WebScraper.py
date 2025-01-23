import pandas as pd
import json
import requests

print("Hello World")
#Target URL we wish to capture
baseURL = "https://webapps.utrgv.edu/aa/dm/api/DMUser/"

class ScrapeEvals:
    #Function which calls the api and returns a list of each faculty members username
    def getFacultyList():
        response = requests.get(f"{baseURL}GetDMList")
        
        #Convert response text into JSON
        jsonData = json.loads(response.text)

        FacultyRecords = jsonData['Data']['Record']
        
        #Return a list of each username found
        usernameList = []
        for record in FacultyRecords:
            usernameList.append(record['@username'])

        return usernameList

    #Function which calls the api for the profile of a faculty member, which includes all courses taught alongside evaluation data
    def getFacultyProfile(username):
        try:
            response = requests.get(f"{baseURL}GetDMUser?username={username}")

            #Convert resonse text into JSON
            jsonData = json.loads(response.text)

            evaluations = jsonData['Data']['Record']['SCHTEACH']
            if evaluations is None:
                evaluations = "0"

            firstName = jsonData['Data']['Record']['PCI']["FNAME"]
            middleName = jsonData['Data']['Record']['PCI']["MNAME"]

            if middleName is None:
                middleName = ""

            lastName = jsonData['Data']['Record']['PCI']["LNAME"]
            return evaluations, firstName, middleName, lastName
        except Exception as e:
            print(e)
            return 0, 0, 0, 0

    #Function whihc filters the evaluations that have data
    def parseEvalData(db, data, firstName, middleName, lastName):
        if middleName is None:
            instructorName = firstName + " " + lastName
        else:
            instructorName = firstName + " " + middleName + " " + lastName

        #Here we capture the courses that have course evaluation data
        for course in data:
            try:
                #Here we get necessary information from the data and push it to our dataframe
                if (course['NUM_EVAL'] != None):
                    courseInfo = [instructorName,
                                  course["TYT_TERM"], 
                                  course["TYY_TERM"], 
                                  course['COURSEPRE'], 
                                  course["COURSEID"], 
                                  course["TITLE"], 
                                  course["COURSENUM"],
                                  course["SECTION"],
                                  course["ENROLL"], 
                                  course['NUM_EVAL'], 
                                  course['AGGREGATED_AVG'],
                                  course['EVAL']['DEFINED_AVG'],
                                  course['EVAL']['PREPARED_AVG'],
                                  course['EVAL']['COMMUNICATED_AVG'],
                                  course['EVAL']['ENCOURAGED_AVG'],
                                  course['EVAL']['AVAILABLE_AVG'],]

                    length = len(db)
                    db.loc[length] = courseInfo
            except Exception as e: 
                print(f'Error: {e}')

#Here, we instantiate a Pandas Dataframe
EvaluationResults = pd.DataFrame(columns = ['Instructor',
                                            'Semester', 
                                            'Year', 
                                            'Subject',
                                            'CRN', 
                                            'Course', 
                                            'Course Number', 
                                            'Section', 
                                            'NUM_ENROLLED', 
                                            'NUM_EVALS', 
                                            'AGGREGATED_AVG_SCORE',
                                            'DEFINED_AVG',
                                            'PREPARED_AVG',
                                            'COMMUNICATED_AVG',
                                            'ENCOURAGED_AVG',
                                            'AVAILABLE_AVG'])

#Here we call the API and parse the list of all usernames accredited to each faculty member
userNameList = ScrapeEvals.getFacultyList()


#We will iterate through the list of faculty members and get evaluation data for each of their taught courses
for user in userNameList:
    print(f"Fetching Data for user: {user}")

    records, first, middle, last = ScrapeEvals.getFacultyProfile(user)

    #If the current faculty member has no evaluation records, skip
    if records == 0:
        continue

    ScrapeEvals.parseEvalData(EvaluationResults, records, first, middle, last)
    print('Fetched Data Successfully\n')

#Once finished collecting data, convert Dataframe to CSV for later processing
print(EvaluationResults)
EvaluationResults.to_csv("test.csv", index = False)


