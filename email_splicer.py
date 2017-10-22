#Email slicer project that takes a user's email and returns a username and domain name

email = input("What is your email address?: ").strip()

username = email[:email.index('@'):1]
domain = email[email.index('@') + 1::1]

output = 'Your username is "{}" and your domain name is "{}".'.format(username, domain)

print(output)