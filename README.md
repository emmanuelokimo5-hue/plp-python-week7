# PLP Python Week 7 - Working with Lists

## Files

- `list_warmup.py` - Demonstrates creating a list, accessing items by index, using append(), remove(), and len().
- `shopping_list.py` - Provides an interactive shopping list manager using append(), remove(), in, and loops.
- `list_report.py` - Prints a numbered list, counts item names with more than four letters, and finds the longest item using a loop.
- `screenshots/` - Contains screenshots showing the three programs running.

## Why is it safer to check `in` before calling `.remove()`?

Checking `in` first makes sure that the item actually exists in the list before trying to remove it. If we call `.remove()` on an item that does not exist, Python raises a ValueError and the program can stop unexpectedly.
