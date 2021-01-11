# -*- coding: utf8 -*-
import datetime
import logging
import os.path
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from jira import *
from jiraCommandFile import *


logging.basicConfig(level=logging.INFO)

now = datetime.datetime.now()

bot = Bot(token="967548998:AAG_L68xhcsQtWbXRroeKpcKUHJQA__1_IE") # Test Vova it Bot
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Тест")

@dp.message_handler(commands=['mytasks'])
async def showTasksOfMe(message: types.Message):
    my_tasks_in_jira = myTasksInJira()
    await message.answer("Мои задачи в работе: \n")
    for task in my_tasks_in_jira:
    	await message.answer(str('{}: {}'.format(task.key, task.fields.summary)))

@dp.message_handler(commands=['teamtasks'])
async def showTasksOfTeam(message: types.Message):
	team_tasks_in_jira = teamTasksInJira()
	await message.answer("Задачи команды в работе: \n")
	for task in team_tasks_in_jira:
		await message.answer(str('{}: {}: {}'.format(task.key, task.fields.summary, task.fields.assignee)))

@dp.message_handler(commands=['mytasksbacklog'])
async def showTasksOfTeam(message: types.Message):
    team_tasks_in_jira = teamTasksInJira()
    await message.answer("Мой backlog задач: \n")
    for task in team_tasks_in_jira:
        await message.answer(str('{}: {}: {}'.format(task.key, task.fields.summary, task.fields.assignee)))

if __name__ == '__main__':
    executor.start_polling(dp)