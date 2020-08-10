import requests
resp = requests.get('https://todolist.example.com/tasks/')
if resp.statuscode !=200:
	raise ApiError('GET/tasks/{}.format(resp.status_code)')
for todo_item in resp.json():
	print('{} {}'.format(todo_item['id'],todo_item['summary']))