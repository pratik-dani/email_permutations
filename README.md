[<img align="right" src="https://cdn.buymeacoffee.com/buttons/default-orange.png" width="217px" height="51x">](https://www.buymeacoffee.com/pratikdani)

# Emails Permutations and Combinations from first name and last name

Email `permutations` provides a list of all possible combinations of email for a given first name
and last name.

## Installation

You can install **permutations** library via pip:

    $ pip install email-permutations

## Example Usage

```python

from permutations import email_permuter

# Specify the first name, last name and domain name
first_name = "Pratik"
last_name = "Dani"
domain_name = "gmail.com"

permuted_emails = email_permuter.all_email_permuter(first_name=first_name,
						    last_name=last_name,
						    domain_name=domain_name
						    )
```

## Contributions

If you find any bugs, please feel free to open an issue or send a pull request.
