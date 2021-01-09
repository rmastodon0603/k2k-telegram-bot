# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.
from jira import JIRA
import re

# By default, the client will connect to a Jira instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.

login = 'rmastodon0603@gmail.com'
api_key = '3iXildyU0COb4ahQ1bg11D52'
jira_options = {'server': 'https://kith2kin.atlassian.net'}
jira = JIRA(options=jira_options, basic_auth=(login, api_key))

# Get all projects viewable by anonymous users.
projects = jira.projects()


for project in projects:
	print (str(project))

issue = jira.issue('PPC-61')

issue_summary = issue.fields.summary # print name of issue ( issue - задача )
print (str(issue_summary))

issue_description = issue.fields.description # print description of task
print (str(issue_description))

issue_asignee = issue.fields.assignee # print Issue Asignee ( Asignee - Ответственный за задачу )
print (str(issue_asignee))

print ()


# First 50 issues in project
#issues_in_proj = jira.search_issues('project=PPC')
#for issue_in_project in issues_in_proj:
#	print (str(issue_in_project))

# Summaries of my last 3 assigne issues ( Название тасок за которые я ответственный )
for issue in jira.search_issues('assignee = currentUser() order by created desc', maxResults=3):
    print('{}: {}'.format(issue.key, issue.fields.summary))

print ()

def myTasksInJira():
	for issue in jira.search_issues('assignee = currentUser() order by created desc', maxResults=3):
		my_tasks_in_jira = '{}: {}'.format(issue.key, issue.fields.summary)

	return my_tasks_in_jira






