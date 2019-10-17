import itertools

def all_email_permuter(first_name, last_name, domain_name):
    """
    Excepts first_name, last_name and domain_name as arguments and returns a
    list of all permutations of possible mail id's.
    """
    first_name = first_name.lower()
    last_name = last_name.lower()
    domain_name = domain_name.lower()
    all_names = [[first_name, first_name[0]], [last_name, last_name[0]]]
    punctuations =  ". _ - ".split()
    a = list(itertools.product(all_names[0], all_names[1], punctuations))
    b = list(itertools.product(all_names[0], all_names[1]))
    combinations = [s for x in a for s in itertools.permutations(x, 3) if s[0] not in punctuations if s[-1]not in punctuations]
    combinations.extend(["".join(s) for x in b
                                  for s in itertools.permutations(x, 2)
                                  if s[0] not in punctuations
                                  if s[-1]not in punctuations])
    combinations = ["".join(s) for s in combinations]
    combinations.extend([first_name, last_name])
    permuted_emails = [f"{s}@{domain_name}" for s in combinations]
    return permuted_emails