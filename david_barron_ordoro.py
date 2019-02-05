import requests
from dateutil.parser import parse


MY_EMAIL = 'david.barron91@gmail.com'
ORDORO_API = 'https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest'
HTTP_OK = 200
APRIL = 4


def get_distinct_emails(data):
    """
    data is list of entry dicts with key "email"
    return list of strings of unique emails
    """
    return list({e['email'] for e in data if e['email'] and '@' in e['email']})  # let set() handle uniqueness


def get_domain_counts(data):
    """
    data is list of entry dicts with key "email"
    return dict of domain string and int count
    """
    dom_count = dict()

    for e in data:
        if e['email'] and '@' in e['email']:  # lazy check valid email
            domain = e['email'].split('@')[1]
            if domain in dom_count:
                dom_count[domain] += 1
            else:
                dom_count[domain] = 1

    return dom_count


def is_april_datetime(login_date):
    """
    login_date is datetime string with UTC offset
    return boolean
    """
    date = parse(login_date) # error check would be nic
    return date.month == APRIL


def get_april_logins(data):
    """
    data is list of entry dicts with keys "email" and "login_date"
    return list of strings of unique emails with datetime strings in the month of April
    """
    return list({e['email'] for e in data if e['email'] and e['login_date'] and is_april_datetime(e['login_date'])})


def do_etl():
    response = requests.get(ORDORO_API)

    if response.status_code != HTTP_OK:
        print(f"Error making API call. Returned status code: {response.status_code}.")
        return

    body = response.json()

    if not body:
        print("No body in response.")
        return

    emails = get_distinct_emails(body['data'])  # could error check here too, but don't wanna...
    domain_count = get_domain_counts(body['data'])
    april_logins = get_april_logins(body['data'])

    payload = {'your_email_address': MY_EMAIL, 'unique_emails': emails, 'user_domain_counts': domain_count,
               'april_emails': april_logins}

    post_response = requests.post(ORDORO_API, json=payload)

    if post_response.status_code != HTTP_OK:
        print(f"Failed to post payload to Ordoro. Returned status code: {post_response.status_code}")
    else:
        print("Successfully posted payload to Ordoro.")


if __name__ == "__main__":
    do_etl()
