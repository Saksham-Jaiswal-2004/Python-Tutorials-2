import smtplib

my_email = "cse24083@iiitkalyani.ac.in"
password = "waxwivcixmeblezt"

connection = smtplib.SMTP("smtp.gmail.com", 587) # This is your email service provider specific
connection.starttls() # Secures our connection and encrypts our message so no one in between even if intercepted cannot read anything
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="sakshamgamer2004@gmail.com", msg="Subject:Python is Awesome\n\nThis is an automated email!")

connection.close()

# Another Approach to avoid writing connection.close()

# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="sakshamgamer2004@gmail.com", msg="Subject:Python is Awesome\n\nThis is an automated email!")