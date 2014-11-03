__author__ = 'Nickolas'
def email():
    email = (input("email.address"))
    gtld=['gov','com','edu','org','mil','net']
    while True:
        try:
            username, domain = email.split('@')
            site, domaintype = domain.split('.')
            if domaintype in gtld:
                return username,site,domaintype
        except ValueError:
            email=input('invalid email address')




username, site, domaintype = email()
print(username)
print(site)
print(domaintype)