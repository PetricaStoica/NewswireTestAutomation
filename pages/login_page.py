from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username: str, password: str):
        self.page.fill('input[id="user_email"]', username)
        self.page.fill('input[id="user_password"]', password)
        
        # Locate the iframe containing the CAPTCHA
        captcha_frame = self.page.frame_locator('[title="reCAPTCHA"]')
        # Click the "I'm not a robot" checkbox
        captcha_frame.get_by_role('checkbox', name="I'm not a robot").click()

        # I havent implemented captcha challenges before 
        # usually they were disabled on test environments or disabled for the test account 
        # I introduced this manual step and will return to it if I have time after I finish the proper tests
        captcha = ''
        while captcha != 'y':
            print('Have you manually completed the CAPTCHA challenge? (confirm with: y)')
            captcha = input()
        print('Thank you! The tests will continue now')

        self.page.click('button#send')
        


