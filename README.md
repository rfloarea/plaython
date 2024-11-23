# Plaython

Some playful things written in python.

## Playthings (so far)

- Basic CLI seconds timer (see: [timer_sec.py](./timer_sec.py))
  - Learned about
    - import statements
    - time module
    - format strings (removed, but played with)
    - `.sleep` method
    - `input()` function
    - `int()` function
    - basic function, conditionals, and while loops
    - how to run scripts from terminal
- Basic CLI minute timer (see: [timer_min.py](./timer_min.py))
  - Learned about
    - simple uses of format strings
    - `len()` function
    - cleaner `while` loop logic (removed `if` condition within loop and simply allowed the loop to complete)
- Rock, Paper, Scissors (see: [rps.py](./rps.py))
  - Learned about
    - `random` module
    - `random.randint(a, b)` - Interestingly, it returns a value inclusive of both arguments. I replaced this with `.choice()`
    - `random.choice()` - returns an element from a non-empty sequence
    - Figured out how to break `if` conditions across multiple lines with `()` and `or`
    - Functions look cool, but I decided they aren't needed for this problem. And I want to practice writing code that's appropriate for the problem at hand rather then to adhere to Best Practices. (I had a few functions at first, but simplified to what we have left)
    - Simple format strings with `f` and `{}`
- Simple math script (see: [do_math.py](./do_math.py))
  - Learned about
    - Exiting a program using different techniques:
      - `sys.exit()` - Must include an import statement: `import sys`. Essentially calls `SystemExit`. Exists without raising exceptions.
      - `raise SystemExit` - Seems like a clever way to avoid an import line. Exists without raising exceptions.
      - `raise Exception("Helpful description about the error")` - This one is nice if you want to provide a "real" error in the code. But I just wanted to kill the process, not get all tied up in errors.
    - `try` blocks. I only need `try...except` for this program. But I read into `try except else finally`. Cool stuff.
    - Infinite `while` loop with initial `True` conditions can be useful! So that's something I never thought had a practical use.
