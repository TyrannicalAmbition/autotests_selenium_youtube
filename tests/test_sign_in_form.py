import time
import pytest
from pom.sign_in_form import SignInForm


@pytest.mark.usefixtures('setup')
class TestSignInForm:

    def test_login_omnibox(self):
        signin_form = SignInForm(self.driver)
        signin_form.get_sign_in_button().click()
        signin_form.get_login_omnibox().send_keys('abc@gmail.com')
        signin_form.get_next_button().click()
        time.sleep(1)
