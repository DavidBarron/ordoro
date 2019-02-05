import unittest
from david_barron_ordoro import get_distinct_emails, get_multiple_domain_counts, get_april_logins


class TestOrdoro(unittest.TestCase):

    def test_get_distinct_emails_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'blah2@test.com'}]

        result = get_distinct_emails(given)

        self.assertCountEqual(result, ['blah2@test.com', 'blah1@test.com'])

    def test_get_distinct_emails_none_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": None}]

        result = get_distinct_emails(given)

        self.assertCountEqual(result, ['blah1@test.com'])

    def test_get_distinct_emails_empty_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": ''}]

        result = get_distinct_emails(given)

        self.assertCountEqual(result, ['blah1@test.com'])

    def test_get_distinct_emails_duplicate_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'blah1@test.com'}]

        result = get_distinct_emails(given)

        self.assertCountEqual(result, ['blah1@test.com'])

    def test_get_multiple_domain_counts_1_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'blah2@test.com'}]

        result = get_multiple_domain_counts(given)

        self.assertDictEqual(result, {'test.com': 2})

    def test_get_multiple_domain_counts_2_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'blah2@gmail.com'}]

        result = get_multiple_domain_counts(given)

        self.assertDictEqual(result, {})

    def test_get_multiple_domain_counts_3_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'some_dude@gmail.com'},
                 {"login_date": None, "email": 'blah45@test.com'}]

        result = get_multiple_domain_counts(given)

        self.assertDictEqual(result, {'test.com': 2})

    def test_get_multiple_domain_counts_none_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": None}]

        result = get_multiple_domain_counts(given)

        self.assertDictEqual(result, {})

    def test_get_multiple_domain_counts_not_email_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'}, {"login_date": None, "email": 'not an email, yo'}]

        result = get_multiple_domain_counts(given)

        self.assertDictEqual(result, {})

    def test_get_april_logins_1_pass(self):
        given = [{"login_date": '2014-04-18T05:43:51+08:00', "email": 'blah1@test.com'},
                 {"login_date": '2014-05-18T05:43:51+08:00', "email": 'blah2@test.com'}]

        result = get_april_logins(given)

        self.assertCountEqual(result, ['blah1@test.com'])

    def test_get_april_logins_2_pass(self):
        given = [{"login_date": '2014-04-18T05:43:51+08:00', "email": 'blah1@test.com'},
                 {"login_date": '2014-04-05T05:43:51+08:00', "email": 'blah2@test.com'}]

        result = get_april_logins(given)

        self.assertCountEqual(result, ['blah1@test.com', 'blah2@test.com'])

    def test_get_april_logins_none_login_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'},
                 {"login_date": '2014-04-05T05:43:51+08:00', "email": 'blah2@test.com'}]

        result = get_april_logins(given)

        self.assertCountEqual(result, ['blah2@test.com'])

    def test_get_april_logins_none_login_no_april_date_pass(self):
        given = [{"login_date": None, "email": 'blah1@test.com'},
                 {"login_date": '2014-07-05T05:43:51+08:00', "email": 'blah2@test.com'}]

        result = get_april_logins(given)

        self.assertCountEqual(result, [])


if __name__ == '__main__':
    unittest.main()
