from testpage import OperationsHelper
import time
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step2(browser):
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(f"{testdata['username']}")
    testpage.enter_pass(f"{testdata['password']}")
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(f"{testdata['name']}")
    testpage.enter_email(f"{testdata['email']}")
    testpage.enter_content(f"{testdata['content']}")
    time.sleep(testdata['sleep_time'])
    testpage.click_contact_us_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_alert_text() == 'Form successfully submitted'




