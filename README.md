# barq_weather_task
# Tasks

---

#### Task1

- Read the file `f1.csv` in `files` directory
- Find the difference between the `Max TemperatureC` and `Min TemperatureC` columns
- e.g. for first row: 27 - 15 = 12. for second row: 26 - 16 = 10
- Your answer should be: `[12, 10, 7, 4, 9, 9, 10, 10, 10, 8, 7, 11, 11, 9, 10, 12, 13,
  11, 11, 10, 11, 11, 14, 10, 12, 12, 11, 10, 9, 8, 10]`

---

#### Task 2

- Read the file `f1.csv` in `files` directory
- Find the average of the `Max TemperatureC` and `Min TemperatureC` columns
- e.g. for first row: (27 - 15)/2 = 6.0. for second row: (26 - 16)/2 = 10
- Your answer should
  be: `[6.0, 5.0, 3.5, 2.0, 4.5, 4.5, 5.0, 5.0, 5.0, 4.0, 3.5, 5.5, 5.5, 4.5, 5.0, 6.0, 6.5, 5.5, 5.5, 5.0, 5.5, 5.5, 7.0, 5.0, 6.0, 6.0, 5.5, 5.0, 4.5, 4.0, 5.0]`

---

#### Task 3

Learn how to use `vim` editor. You should be able to do these things comfortably with vim.

- create and save a file with vim
- edit and save a file with vim

Your submission for this task should the steps for how to create and save a fil with vim editor.

Submit t3.txt and t4.txt in one pull request.

----

#### Task 4

Do the Task 3 but with `nano` editor.

**Note** that vim and nano are by default available on ubuntu terminals. If needed, install with apt. But dont
use any third party applications.

**Also note** that write in your own wording. Do not copy and paste from anywhere.

----

#### Task 5

There is a new file `f2.csv` in `files/`.

Find and print all the dates in which the Event "Snow", "Rain" or "Rain-Snow" occurred.

Your answer should
be `['2004-12-16', '2004-12-17', '2004-12-19', '2005-4-10', '2005-7-10', '2005-7-14', '2006-1-1', '2006-1-13', '2006-1-2', '2006-10-20', '2006-11-15', '2006-11-17', '2006-12-10', '2006-12-26', '2006-12-3', '2006-12-4', '2006-12-5', '2006-2-18', '2006-2-19', '2006-2-24', '2006-2-25', '2006-2-26', '2006-3-13', '2006-3-19', '2006-4-6']`


---

#### Task 6

In the `files/f2.csv`, find and print all the days in which the event "Thunderstorm" occurred.

Your output should
be `Friday, Sunday, Monday, Sunday, Monday, Friday, Saturday, Monday, Sunday, Sunday, Sunday, Tuesday, Sunday`

Hint: use the Python datetime's `strptime` to read the string in datetime format, and `strftime` to transform the date
to
desired string format.

Hint2: use "%Y-%m-%d" to convert string to datetime format. [__Full link
__](https://www.programiz.com/python-programming/datetime/strptime#:~:text=you%20can%20use.-,Directive,-Meaning) of
available formats
