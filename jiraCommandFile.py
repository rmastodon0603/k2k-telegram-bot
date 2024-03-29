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

def myTasksInJira():
	my_tasks_in_jira = jira.search_issues('assignee = currentUser() and status = "In progress"', maxResults=5)
	for issue in my_tasks_in_jira:
		print (str('{}: {}'.format(issue.key, issue.fields.summary)))

	return my_tasks_in_jira

def teamTasksInJira():
	team_tasks_in_jira = jira.search_issues('status = "In progress"', maxResults=15)
	for issue in team_tasks_in_jira:
		print (str('{}: {}: {}'.format(issue.key, issue.fields.summary, issue.fields.assignee)))

	return team_tasks_in_jira

def myTasksInJiraBacklog():
	team_tasks_in_jira_backlog = jira.search_issues('assignee = currentUser() and status = "Backlog"', maxResults=15)
	for issue in team_tasks_in_jira_backlog:
		print (str('{}: {}: {}'.format(issue.key, issue.fields.summary, issue.fields.assignee)))

	return team_tasks_in_jira_backlog

def CurerentUserTasksInOneMessage():
	all_tasks = {}
	backlog_tasks = jira.search_issues('assignee = currentUser() and status = "Backlog"', maxResults = 10)
	inprogress_tasks = jira.search_issues('assignee = currentUser() and status = "In progress"', maxResults=10)
	selectedDevelope_tasks = jira.search_issues('assignee = currentUser() and status = "Selected for Development"', maxResults=10)

	for issue in backlog_tasks:
		all_tasks[issue.key] = issue.fields.summary

	for issue in inprogress_tasks:
		all_tasks[issue.key] = issue.fields.summary

	for issue in selectedDevelope_tasks:
		all_tasks[issue.key] = issue.fields.summary

	return all_tasks

def testtask():
	todo_tasks = jira.search_issues('assignee = currentUser() and status = "Selected for Development"')
	for issue in todo_tasks:
		print(str('{}: {}'.format(issue.key, issue.fields.summary)))

if __name__ == '__main__':
	CurerentUserTasksInOneMessage()
