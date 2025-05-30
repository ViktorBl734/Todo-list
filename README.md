# todo_list
A simple Django-based Todo List application that allows users to manage tasks and tags. Each task can have an optional deadline, completion status, and multiple associated tags.

🔧 Features
📋 Task Model:
content – description of the task.
created – datetime when the task was created.
deadline – optional due date.
is_done – boolean indicating whether the task is completed.
tags – many-to-many relationship with tags.

🏷️ Tag Model:
name – name of the tag.
A tag can be associated with multiple tasks, and each task can have multiple tags.
📄 Pages
🏠 Home Page (/)
Sidebar with links (visible on all pages):

Home

Tag List
Todo list displaying all tasks:
Sorted with not-done tasks first, then done, from newest to oldest.
All task details shown.

Buttons to:
Add a new task.
Update / Delete each task.
Toggle completion status (Complete / Undo).

🏷️ Tag List Page (/tags/)
Table showing all tags.

Buttons to:
Add a new tag.
Update / Delete existing tags.