"""Testsq for Balloonicorn's Flask app."""

import unittest
import party
# from flask import session


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # what's the difference on the page when you HAVE RSVPed?
            # treats
            # party details
        # what should you see if not?
            # form
        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        self.assertIn(b"<h2>Please RSVP</h2>", result.data)

        # session = {}
        # session['rsvp'] = True
        # if session['rsvp'] == True:
        #     result = self.client.get("/")
        #     self.assertIn(b"<h2>Party Details</h2>", result.data)
        # else
            # result = ...
            # self.assertIn(b"<form>...", result.data)
        #print("FIXME")

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!
        print("FIXME")

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself
        pass
        print("FIXME")


if __name__ == "__main__":
    unittest.main()
