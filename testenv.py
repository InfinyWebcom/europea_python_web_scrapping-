import environ


env = environ.Env(
    EMAIL_HOST_USER=str,
    EMAIL_HOST_PASSWORD=str,
    IMAP_GMAIL_SERVER=str,
    SMTP_GMAIL_SERVER=str,
    
)

EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
IMAP_GMAIL_SERVER=env("IMAP_GMAIL_SERVER")
SMTP_GMAIL_SERVER=env("SMTP_GMAIL_SERVER")


print(EMAIL_HOST_USER)
print(EMAIL_HOST_PASSWORD)
print(IMAP_GMAIL_SERVER)
print(SMTP_GMAIL_SERVER)
