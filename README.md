<h1>CLI_TASK_MANAGER_PYTHON</h1>

<p>
This is a simple command-line task manager built using Python. It lets users add, view, and delete tasks using text-based commands. The project is designed for learning basic Python concepts like dictionaries, functions, loops, and input handling.
</p>

<h2>Overview</h2>

<ul>
  <li>Add tasks with a title and description</li>
  <li>Delete tasks using the title</li>
  <li>View all stored tasks in a list format</li>
  <li>Interactive CLI-based system</li>
</ul>

<p>
This project is intended for beginners who want to understand how a simple command-line application works.
</p>

<h2>Commands</h2>

<h3>Add Task</h3>

<pre>
add 'title' 'task'
</pre>

<p>Stores a new task in memory using a title and description.</p>

<h3>Delete Task</h3>

<pre>
del 'title'
</pre>

<p>Removes a task from storage based on its title.</p>

<h3>List Tasks</h3>

<pre>
list
</pre>

<p>Displays all existing tasks with numbering.</p>

<h3>Exit Program</h3>

<pre>
exit
</pre>

<p>Terminates the CLI application.</p>

<h2>Internal Structure</h2>

<ul>
  <li><b>Dictionary</b>: Used to store tasks as key-value pairs (title → task)</li>
  <li><b>In-memory storage</b>: Data is not saved permanently</li>
</ul>

<h2>Limitations</h2>

<ul>
  <li>No file/database storage</li>
  <li>No user authentication</li>
  <li>Data is lost after program exit</li>
</ul>

<h2>Purpose</h2>

<p>
This project is created for educational purposes to practice building a simple CLI application in Python.
</p>