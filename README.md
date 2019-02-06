# ordoro-interview
Python version: Python 3.7.2

### set up virtiual env
```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

### running script
```
python3 david_barron_ordoro.py
```

### running tests
```
python3 ordoro_test.py 
```

### deactivate virtual env
```
deactivate
```

### Notes on assignment

**Time to complete:** ~3 hours, so a little over the estimated 2. It was a pretty straightforward assignment. Originally wrote up the assignment on my Windows machine so some of the extra time was spent jiggling the hangles making sure everything was OK to run elsewhere and wasn't carrying dome weird dependency. Also spent some of that time cleaning up some test functions that I ended up moving to a seperate test class, and added some other simple test cases there. 

**Runtime complexity:** Overall the runtime of the script is linear. 

`get_distinct_emails` is O(n); I'm iterating through every entry in the data list once and using the Python set module handle uniqueness which it does in O(1) time.

`get_multiple_domain_counts` is O(n); Same reason as above except there's also a check to a dictionary as well as a set which are each O(1) and have no effect on anything else.

`get_april_logins` is O(n); Same as first reason.

If we wanted to be more descriptive, since we went through the reponse list 3 seperate times(once for each function) we could say the runtime of the script is O(3n).

**Misc. thoughts**
I included some light error checking where it was easy, but there's room for improvement. A big easy win would be to create another function to run the response entry list where error checking was done; remove entries that that don't have valid emails and datetimes (with something more robust like string patterns instead of a simple `in`). This would allow for the cleanup of the other 3 major functions and make them a little more readable. It would also allow for the cleanup of my unit tests since several of the cases overlap. There's no need to be checking for valid emails in every function, just do it once before and be done with it.
