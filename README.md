![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Lab | IPython and Python Basics for Data Work

## Overview

This lab focuses on core Python basics and the interactive habits that make IPython productive for data work. You will practice exploring objects, reasoning about types and mutability, writing small functions, and validating results as you go. The work stays intentionally lightweight and uses small in-memory examples so you can focus on correctness and mental models rather than data volume. By the end, you will have a compact notebook that demonstrates clear, repeatable analysis steps using only Python fundamentals.

## Learning Goals

By the end of the lab, you should be able to use IPython to inspect objects and test ideas quickly, understand how Python handles types and mutability, and write small, reusable functions that transform data safely. You should also be able to structure a notebook so that it runs cleanly from top to bottom without hidden state.

## Setup and Context

You will build a small set of in-memory examples that mimic data tasks without relying on external files or datasets. The goal is to practice the mechanics of Python and IPython: object inspection, type conversion, control flow, and basic file I/O. You may work in a notebook or an interactive shell, but capture your final work in the submission file listed below.

## Requirements

- Fork this repository to your own GitHub account.
- Clone your fork to your machine.
- Make sure you can open and run Jupyter notebooks (for example via Jupyter Lab or VS Code).

## Getting Started

You will complete this lab primarily in the `Jupyter Notebook` file, and you’ll write a small `.py` file for the functions task.

- Create a new notebook and name it `m1-01-ipython-python-basics-lab.ipynb`.
- For Task 3, implement the functions in `m1-01-task-3-functions.py` (and optionally import them into your notebook to test them).
- Before you submit, restart your kernel and run the notebook **top to bottom** to make sure your results don’t depend on hidden state.

## Tasks

### Task 1: Establish your interactive workspace

Create a small collection of values that cover common data types: integers, floats, strings, lists, and dictionaries. Then do the following in order. First, use `type()` on each value and write the results in a short markdown cell. Second, call one method on a string, one on a list, and one on a dictionary and briefly describe what each returned. Third, use IPython introspection (for example, by appending a dot and pressing Tab or by calling `help()` on a method) and record one insight about an object’s available methods in a short markdown note.

### Task 2: Reason about mutability and references

Create a list called `values` with at least three elements, assign it to `alias`, and append one new value using `alias`. Show the contents of both names after the change. Next, make a copy using `list(values)` or `values.copy()`, append a different value to the copy, and show the contents of both. Repeat the same pattern with a dictionary called `record` and an alias called `record_alias`, then a copied dictionary called `record_copy`. End the task with a short markdown paragraph explaining what changed and why, and how that affects passing objects into functions.

### Task 3: Build small functions for cleaning and conversion

Write two small functions. The first function should take a string and return a float if the string represents a valid number, otherwise return `None` for any invalid input (such as letters or empty strings). The second function should take a string and return a cleaned version with surrounding whitespace removed and consistent casing. After defining the functions, create a list of at least five test inputs that include valid and invalid cases, then apply each function to the list and show the outputs. Keep the functions focused, return values instead of printing, and keep parameter names short and clear.

### Task 4: Apply control flow to a small record list

Create a list of at least 12 dictionaries representing user activity events with keys `user_id`, `event_type`, and `duration_seconds`. Include at least two records with invalid `duration_seconds` values (such as negative numbers or non-numeric strings). Write a loop that builds a new list called `cleaned_events` containing only valid records and adds a new key `duration_minutes` to each cleaned record. After the loop, verify two things: the count of `cleaned_events` matches the number of valid records you expect, and every cleaned record contains all required keys. Inspect two cleaned records in IPython to confirm the transformation.

### Task 5: Summarize and capture a small output

Compute the following summaries using only core Python structures. First, build a dictionary of event counts by `event_type`. Second, build a dictionary of average `duration_minutes` by `event_type`. Third, compute the number of unique users using a set. After computing the summaries, validate one result by recomputing it in a different way, such as summing the event counts and comparing to `len(cleaned_events)`.

Next, build a CSV-formatted string with three columns: `metric`, `key`, and `value`. Include one row per event type for the counts, one row per event type for the averages, and a final row for the unique user count. If you choose to save the string to disk while working, read it back and confirm one value matches your in-memory results. Include the final CSV string in your submission file.

## Common Pitfalls and Debugging Notes

A frequent mistake is assuming an object has the type you expect without checking. If you see errors like `TypeError` during arithmetic, inspect the offending values and convert them explicitly. Another common issue is relying on notebook state; if you re-run a later cell without re-running earlier ones, results can be inconsistent. Always test by running the notebook top to bottom.

Be careful with mutable objects when passing them into functions. If a function modifies a list or dictionary in place, it can affect later steps. Use copies when you need to preserve the original data.

## Submission

### What to submit

Submit the following files:

- A notebook file `m1-01-ipython-python-basics-lab.ipynb` containing Tasks 1, 2, 4, and 5
- A Python script `m1-01-task-3-functions.py` containing the two functions from Task 3

### Definition of done (checklist)

Before you submit, make sure:

- [ ] The notebook runs **top to bottom** without errors after a kernel restart.
- [ ] Tasks 1, 2, 4, and 5 are completed in `m1-01-ipython-python-basics-lab.ipynb` (with short markdown explanations where requested).
- [ ] `m1-01-task-3-functions.py` contains **both** functions, and they return values (they don’t rely on `print()`).
- [ ] Your cleaning logic excludes invalid durations, and every item in `cleaned_events` has `duration_minutes`.
- [ ] Your summaries are consistent (for example, the total of event counts equals `len(cleaned_events)`).
- [ ] Both required files are saved and included in your git commit.

### How to submit (Git workflow)

- When you’re done, make sure all changes are saved, then run:

```bash
git add .
git commit -m "Solved m1-01 lab"
git push -u origin HEAD
```

- Make a pull request.
- Paste the link to your pull request in the Student Portal.

## Evaluation Criteria

Your work will be evaluated on correctness, clarity, and structure. Correctness means your transformations and summaries are logically consistent and validated. Clarity means your code is readable, your functions are well named, and your reasoning steps are visible. Structure means your work runs cleanly from start to finish, each task is completed in order, and your captured output matches your computed summaries. The expectation is a disciplined, professional workflow that uses Python basics effectively.
