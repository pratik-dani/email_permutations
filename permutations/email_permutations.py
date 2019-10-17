# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:02:28 2019

@author: 1548
"""


plane_emails = """{fn}@{dn}
                  {ln}@{dn}
                  {fn}{ln}@{dn}
                  {fi}{ln}@{dn}
                  {fi}{li}@{dn}
                  {fn}{li}@{dn}
                  {ln}{fn}@{dn}
                  {ln}{fi}@{dn}
                  {li}{fn}@{dn}
                  {li}{fi}@{dn}
                  """
dot_emails = """{fn}.{ln}@{dn}
                {fi}.{ln}@{dn}
                {fn}.{li}@{dn}
                {fi}.{li}@{dn}
                {ln}.{fn}@{dn}
                {ln}.{fi}@{dn}
                {li}.{fn}@{dn}
                {li}.{fi}@{dn}
                """
hyph_emails = """{fn}-{ln}@{dn}
                 {fi}-{ln}@{dn}
                 {fn}-{li}@{dn}
                 {fi}-{li}@{dn}
                 {ln}-{fn}@{dn}
                 {ln}-{fi}@{dn}
                 {li}-{fn}@{dn}
                 {li}-{fi}@{dn}
                 """
unds_emails = """{fn}_{ln}@{dn}
                 {fi}_{ln}@{dn}
                 {fn}_{li}@{dn}
                 {fi}_{li}@{dn}
                 {ln}_{fn}@{dn}
                 {ln}_{fi}@{dn}
                 {li}_{fn}@{dn}
                 {li}_{fi}@{dn}
                 """
def email_permuter(first_name, last_name, domain_name):
    fn = first_name.lower()
    fi = first_name[0].lower()
    ln = last_name.lower()
    if last_name:
        li = last_name[0].lower()
    else:
        li = ""
    dn = domain_name.lower()
    plane_emails = f"""{fn}@{dn}
                       {ln}@{dn}
                       {fn}{ln}@{dn}
                       {fi}{ln}@{dn}
                       {fi}{li}@{dn}
                       {fn}{li}@{dn}
                       {ln}{fn}@{dn}
                       {ln}{fi}@{dn}
                       {li}{fn}@{dn}
                       {li}{fi}@{dn}
                       """.split()

    dot_emails = f"""{fn}.{ln}@{dn}
                     {fi}.{ln}@{dn}
                     {fn}.{li}@{dn}
                     {fi}.{li}@{dn}
                     {ln}.{fn}@{dn}
                     {ln}.{fi}@{dn}
                     {li}.{fn}@{dn}
                     {li}.{fi}@{dn}
                     """.split()

    hyph_emails = f"""{fn}-{ln}@{dn}
                      {fi}-{ln}@{dn}
                      {fn}-{li}@{dn}
                      {fi}-{li}@{dn}
                      {ln}-{fn}@{dn}
                      {ln}-{fi}@{dn}
                      {li}-{fn}@{dn}
                      {li}-{fi}@{dn}
                      """.split()

    unds_emails = f"""{fn}_{ln}@{dn}
                      {fi}_{ln}@{dn}
                      {fn}_{li}@{dn}
                      {fi}_{li}@{dn}
                      {ln}_{fn}@{dn}
                      {ln}_{fi}@{dn}
                      {li}_{fn}@{dn}
                      {li}_{fi}@{dn}
                      """.split()

    plane_emails.extend(dot_emails)#dot_emails, hyph_emails, unds_emails]
    plane_emails.extend(hyph_emails)
    plane_emails.extend(unds_emails)

    permuted_emails = plane_emails
    return permuted_emails