import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        for index in range(15):
            homepage_nav.get_nav_links()[index].click()
            time.sleep(1.5)
