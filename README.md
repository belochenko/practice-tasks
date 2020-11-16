# practice-tasks
[![CodeFactor](https://www.codefactor.io/repository/github/belochenko/practice-tasks/badge)](https://www.codefactor.io/repository/github/belochenko/practice-tasks)

When you start work with a new laboratory work (assignment) pls follow next steps:
1. git pull
2. git checkout dev
3. git checkout -b t-[number_of_your_task_card]-two_words_about_task

@@ Do some work 😊 @@ 
**Look carefully at what you are commiting and pushing, otherwise all requests will be sent for revision and will not be automatically checked. Pay special attention to possible conflicts and incompatibilities**

All changes you make are in your branch, which is a copy of dev (git checkout dev -> git checkout -b branch_name). 
1. One task (card) - one commit
2. After you have finished the task, write tests for it (hereinafter pytest) if it needed. 
3. If the tests are successful -> make a Push (git add . -> git commit -m "YOUR MESSAGE". -> git push -u origin your_branch_name). It is better to form a commit -m "Done card #(card number)".
For example: git commit -m "Complete #47"
4. *git push -u origin **your_branch_name***
5. Attach the number of your commit to your card in the Trello. 


Whatever happens, do not give in to provocations from the git - do not do ![git push --force](https://media.makeameme.org/created/git-push-force-5c1228.jpg)

Do not forget change task status in Trello from *"Open Task"* to *"In Progress"*. If you finished your task, commit all source code and make pull requests to the **dev branch**.

![Fire Alert](https://hikaruzone.files.wordpress.com/2015/10/in-case-of-fire-1-git-commit-2-git-push-3-leave-building2.png)
