import requests
import re

api_url = "https://haveibeenpwned.com/api/v2/"
bad_request_string = "<Response [400]: Bad Request> The account does not " \
                     "comply with an acceptable format"
forbidden_string = "<Response [403]: Forbidden> - No user agent was specified" \
                   " in the request"
not_found_string = "<Response [404]: Not Found> - No information was returned"


# Checks the status code of each request and returns either a string signifying
# that the request was unsuccessful and why, or a JSON list of the results.
def check_status_code(r):
    if r.status_code == 400:
        return bad_request_string
    elif r.status_code == 403:
        return forbidden_string
    elif r.status_code == 404:
        return not_found_string
    else:
        return r.json()


# Returns a JSON list of all breaches a particular account has been involved in.
# Usernames that are not email addresses can be searched for.
def get_all_breaches_for_account(account, domain=None, truncateResponse=None):
    action = "breachedaccount/"
    url_to_fetch = api_url + action + account
    payload = {"truncateRepsonse": truncateResponse, "domain": domain}
    r = requests.get(url_to_fetch, params=payload)
    return check_status_code(r)


# Returns a JSON list with the details of each breached site stored by hibp.com.
# A domain parameter may be passed to filter the result set to only breaches
# against the specific domain.
def get_all_breached_sites(domain=None):
    action = "breaches"
    url_to_fetch = api_url + action
    payload = {"domain": domain}
    r = requests.get(url_to_fetch, params=payload)
    return check_status_code(r)


# Returns the information about a specified breach "name".
def get_single_breached_site(name):
    action = "breach/"
    url_to_fetch = api_url + action + name
    r = requests.get(url_to_fetch)
    return check_status_code(r)


# Returns all of the attributes used for the compromised records in a breach
def get_all_data_classes():
    action = "dataclasses"
    url_to_fetch = api_url + action
    r = requests.get(url_to_fetch)
    return check_status_code(r)


# Usernames that are not email addresses cannot be searched for
def get_all_pastes_for_account(account):
    pattern = r"[\w.-]+@[\w.-]+"
    match = re.search(pattern, account)

    if match is None:
        return "The provided account is not an email address"

    action = "pasteaccount/"
    url_to_fetch = api_url + action + account
    r = requests.get(url_to_fetch)
    return check_status_code(r)


# Returns a list of paste urls the account was involved in.
def get_paste_urls(account, raw=False):
    urls = []

    for paste in get_all_pastes_for_account(account):
        if paste["Source"] == "Pastebin":
            if raw:
                urls.append("https://pastebin.com/raw/" + paste["Id"])
            else:
                urls.append("https://pastebin.com/" + paste["Id"])
        elif paste["Source"] == "AdHocUrl":
            urls.append(paste["Id"])

    return urls
