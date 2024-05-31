  # Write a function that validates a URL string. Handle the ValueError by raising a custom
# exception if the URL format is invalid.
def validate_url(Url):
    if not (Url[:7] == "http://" or Url[:8] == "https://"):
        raise ValueError("Invalid URL format")
    return True
print(validate_url("https://www.youtube.com/"))