# Password Generator

## Explanation

The Password Generator is a Python program that creates random passwords based on the length selected by the user.

## Problem Statement

Create a Python program that generates a random password containing uppercase letters, lowercase letters, numbers, and special characters.

## Features

* Custom password length
* Random password generation
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Input validation

## How It Works

1. Ask the user for the desired password length.
2. Create a collection of letters, numbers, and special characters.
3. Randomly select characters from the collection.
4. Combine the selected characters.
5. Display the generated password.

## Technologies Used

* Python
* `random` module
* `string` module
* Functions
* Loops

## Data Structure Used

* String

## Methods Used

* `generate_password()`
* `main()`

## Program Flow

```text id="f2n6a8"
Start
  ↓
Enter Password Length
  ↓
Validate Length
  ↓
Create Character Set
  ↓
Generate Random Characters
  ↓
Display Password
  ↓
End
```

## Sample Input

```text id="p6gq2c"
Enter password length: 12
```

## Sample Output

```text id="a6qk3d"
Generated Password: X7@kP2#mQ9!a
```

> The generated password will be different each time because it is randomly created.

## Time Complexity

O(n), where `n` is the password length.

## Space Complexity

O(n)

## Key Learning

* Using Python's `random` and `string` modules
* Generating random values
* Working with strings
* Using functions and loops
* Validating user input

## File Location

`password_generator.py`

## Repository Structure

```text id="w2e3v7"
python-password-generator/
│
├── password_generator.py
└── README.md
```

## Author

V.Harini
