# pypwnage
**pypwnage** is a small library, written in Python, that is used to interact with the haveibeenpwned API.

## Requirements
- Requests
- re

## Usage
Getting started with **pypwnage** is straightforward and simple. Just import the library and you're all set.

```python
import pypwnage
```

## Getting all breaches for an account
There are two ways you can do this:

-----

#### Without Parameters
- Returns a list of all breaches a particular account has been involved in.
```python
print pyhibp.get_all_breaches_for_account("foo@bar.com")
```
[All breaches for an account...][1]

-----
#### With Parameters
- Can be used to truncate the response so that only the name attribute is returned.
```python
print pyhibp.get_all_breaches_for_account("foo@bar.com", truncateResponse=True)
```
[Using truncateResponse=][2]

- Or filter the results to a specific domain.
```python
print pyhibp.get_all_breaches_for_account("foo@bar.com", domain="adobe.com")
```
[Using domain=][3]

- Or both.
```python
print pyhibp.get_all_breaches_for_account("foo@bar.com", domain="adobe.com", truncateResponse=True)
```
[Using both domain= and truncateResponse=][4]

-----

## Getting all breached sites in the system
- Returns the details of each of breach stored in haveibeenpwned
```python
print pyhibp.get_all_breached_sites()
```
[All breached sites...][5]

- Filters the result set to only breaches against the domain specified
```python
print pyhibp.get_all_breached_sites(domain="linkedin.com")
```
[All breached sites filtered to specific site...][6]

## Getting a single breached site
- Returns the details of a single breach. (Searchable by the breach "name")
```python
print pyhibp.get_single_breached_site("MySpace")
```
[Single breached site...][7]

## Getting all data classes in the system
- Returns the different types of data classes that are associated with a breach. A "data class" is an attribute of a record compromised in a breach.
```python
print pyhibp.get_all_data_classes()
```
[Get all data classes...][8]

## Getting all pastes for an account
- Returns all of the pastes which contain the specified email address.
```python
print pyhibp.get_all_pastes_for_account("example@email.com")
```
[All pastes for "example@email.com"...][9]

## Getting all paste URL's for an account
Returns a list of paste URL's that the account was exposed in. The function takes a parameter called `raw` which can be set to `True`. When set to `True` the function will return the raw pastebin URL's `https://pastebin.com/raw/paste_id`.

- Returns all paste URL's and normal pastebin URL's
```python
print pyhibp.get_paste_urls("example@email.com")
```
```
[u'https://pastebin.com/fJaC0QyC', u'https://pastebin.com/zeLCvYGm', etc...]
```

- Return all paste URL's and raw pastebin URL's
```python
print pyhibp.get_paste_urls("example@email.com", raw=True)
```
`[u'https://pastebin.com/raw/fJaC0QyC', u'https://pastebin.com/raw/zeLCvYGm', etc...]`


[1]: https://haveibeenpwned.com/api/v2/breachedaccount/foo@bar.com
[2]: https://haveibeenpwned.com/api/v2/breachedaccount/foo@bar.com?truncateRepsonse=True
[3]: https://haveibeenpwned.com/api/v2/breachedaccount/foo@bar.com?domain=adobe.com
[4]: https://haveibeenpwned.com/api/v2/breachedaccount/foo@bar.com?domain=adobe.com&truncateRepsonse=True
[5]: https://haveibeenpwned.com/api/v2/breaches
[6]: https://haveibeenpwned.com/api/v2/breaches?domain=linkedin.com
[7]: https://haveibeenpwned.com/api/v2/breach/MySpace
[8]: https://haveibeenpwned.com/api/v2/dataclasses
[9]: https://haveibeenpwned.com/api/v2/pasteaccount/example@email.com
