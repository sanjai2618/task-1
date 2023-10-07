import unittest
import time
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    platformVersion='11.0',
    deviceName='emulator-5554',
    appPackage='com.ATG.World',
    appActivity='com.atg.world.activity.SplashActivity',
)

option = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723/wd/hub'
session_data = {
    'capabilities': capabilities,
    'desiredCapabilities':capabilities
    
}
response = requests.post(f'{appium_server_url}/session', json=session_data)
if response.status_code == 200:
    print('Session created successfully')
    print("")
    print("")
    session_id = response.json()['sessionId']
    print(session_id)
else:
    print('Failed to create a session. Response content:')
    print(response.content)
    

class Appium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=option)

    def test_find_element(self):
        print("")
        print("")
        print("Session started successfully")
        self.driver.find_element(by=AppiumBy.ID, value='com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/getStartedTv").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/login_email").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/email_phone_login").send_keys("wiz_saurabh@rediffmail.com")
        
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/signinbutton").click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/password").send_keys("Pass@123")
       
        self.driver.find_element(by=AppiumBy.ID, value="com.ATG.World:id/passwordloginbutton").click()
        
        time.sleep(2)
        print("")
        print("")
        print("test_LoginWithRightCredential passed")
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/btnGotit').click()
        time.sleep(2)
        print("")
        print("")
        print(" start posting the image")
        
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/fab').click()
        time.sleep(2)
        
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/image_fab_clicked').click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.ImageView').click()
        time.sleep(3)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/toolbar_post_action').click()
        time.sleep(3)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/caption_edit_text').send_keys("appium automated testing")
        time.sleep(3)
        self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]').click()
        time.sleep(3)
        self.driver.back()
        print("")
        print("")
        print(" image posted successfully")
        
        print("")
        print("")
        print("started signing out")
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/homeBottomSheetFragment').click()
        time.sleep(3)
        self.driver.swipe(225,737,242,184,300)
        #time.sleep(3)
        self.driver.swipe(225,737,242,184,300)
        time.sleep(3)
        self.driver.find_element(by=AppiumBy.ID, value='com.ATG.World:id/signOutLabelTextView').click()
        time.sleep(2)
        self.driver.find_element(by=AppiumBy.ID, value='android:id/button1').click()
        time.sleep(3)
        print("")
        print("")
        print(" sign out successfully")
        self.driver.back()
        self.driver.back()
        print("")
        print("")
        print("session completed successfull")
        self.driver.quit()
        
        
               
        





if __name__ == '__main__':
    unittest.main()
