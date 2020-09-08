[<img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:24px !important;">Buy me a coffee</span></a>](https://www.buymeacoffee.com/pratikdani)

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
