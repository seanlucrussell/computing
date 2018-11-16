var taskList = [];
var completedTasks = [];

document.getElementById("textField").addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
	addNewTask();
    }
});

window.onload = function() {
    if (localStorage.getItem('taskList'))
	taskList = JSON.parse(localStorage.getItem('taskList'));
    for (var i = taskList.length-1; i >=0; --i) {
	createTask(taskList[i]);
    }

    if (localStorage.getItem('completedTasks'))
	completedTasks = JSON.parse(localStorage.getItem('completedTasks'));
    for (var i = 0; i < completedTasks.length; ++i) {
	var tmpl = document.getElementById("completed-task-template");
	var complete = tmpl.content.cloneNode(true);
	complete.children[0].textContent = completedTasks[i];
	document.getElementById('finished').prepend(complete);
    }
}

function completeTask(task) {
    var tmpl = document.getElementById("completed-task-template");
    var complete = tmpl.content.cloneNode(true);
    complete.children[0].textContent = task;
    document.getElementById('finished').prepend(complete);
    completedTasks.unshift(task);
    localStorage.setItem('completedTasks',JSON.stringify(completedTasks));
}

function deleteTask(task) {
    var taskContents = task.parentNode.children[1].textContent;
    var index = taskList.indexOf(taskContents);
    taskList.splice(index, 1);
    if (task.parentNode.children[0].checked) {
	completeTask(taskContents);
    }
    task.parentNode.remove()
    localStorage.setItem('taskList',JSON.stringify(taskList));
}

function moveUp(element) {
    var parent = element.parentNode;
    if (parent.previousElementSibling) {
	var taskContents = parent.children[1].textContent;
	var index = taskList.indexOf(taskContents);
	taskList[index] = taskList[index-1];
	taskList[index-1] = taskContents;
	localStorage.setItem('taskList',JSON.stringify(taskList));
	parent.parentNode.insertBefore(parent, parent.previousElementSibling);
    }
}

function moveDown(element) {
    var parent = element.parentNode;
    if(parent.nextElementSibling) {
	var taskContents = parent.children[1].textContent;
	var index = taskList.indexOf(taskContents);
	taskList[index] = taskList[index+1];
	taskList[index+1] = taskContents;
	localStorage.setItem('taskList',JSON.stringify(taskList));
	parent.parentNode.insertBefore(parent.nextElementSibling, parent);
    }
}

function createTask(task) {
    var tmpl = document.getElementById("task-template");
    var newTask = tmpl.content.cloneNode(true);
    newTask.children[0].children[1].textContent = task;
    document.getElementById('tasks').prepend(newTask);
}

function addNewTask() {
    var textField = document.getElementById("textField");
    var task = textField.value;
    if (taskList.includes(task))
	return;
    createTask(textField.value);
    taskList.unshift(task);
    localStorage.setItem('taskList',JSON.stringify(taskList));
    textField.value = "";
}
