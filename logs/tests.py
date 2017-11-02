import django
from django.test import TestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
import re

# Create your tests here.

class ViewTest(TestCase):

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()
            cls.u1 = User.objects.create_user(username='testclient', password='password')


    def test_selenium(self):
        driver = webdriver.Firefox()

        def inputSignup(firstname, secondname, username, password): # searches for sign up input elements and inserts values
            inputFirstname = driver.find_element_by_name("fname")
            inputFirstname.send_keys(firstname)
            pause()
            inputSecondname= driver.find_element_by_name("lname")
            inputSecondname.send_keys(secondname)
            pause()
            inputUsername = driver.find_element_by_id("username2")
            inputUsername.send_keys(username)
            pause()
            inputPassword = driver.find_element_by_id("password2")
            inputPassword.send_keys(password)
            pause()
            signupButton = driver.find_element_by_id("signup-button")
            signupButton.click()
            pause()

        def clearSignup():
            inputFirstname = driver.find_element_by_name("fname")
            inputFirstname.clear()
            pause()
            inputSecondname= driver.find_element_by_name("lname")
            inputSecondname.clear()
            pause()
            inputUsername = driver.find_element_by_id("username2")
            inputUsername.clear()
            pause()
            inputPassword = driver.find_element_by_id("password2")
            inputPassword.clear()
            pause()

        def inputLogin(username, password): # searches for log in input elements and inserts values
            inputUsername = driver.find_element_by_id("username")
            inputUsername.send_keys(username)
            pause()
            inputPassword = driver.find_element_by_id("password")
            inputPassword.send_keys(password)
            pause()
            loginButton = driver.find_element_by_id("login-button")
            loginButton.click()
            pause()

        def clearLogin():
            inputUsername = driver.find_element_by_id("username")
            inputUsername.clear()
            pause()
            inputPassword = driver.find_element_by_id("password")
            inputPassword.clear()
            pause()

        def clickAddButton():
            try:
                addButton = driver.find_element_by_id("add")
                addButton.click()
            except:
                print("button with element id 'add' not located")

        def clickLogSubmitButton():
            try:
                logButton = driver.find_element_by_id("log-button")
                logButton.click()
            except:
                print("button with element id 'log-button' not located")

        def clickLogOutButton():
            try:
                logOutButton = driver.find_element_by_id("logout-button")
                logOutButton.click()
            except:
                print("button with element id 'logout-button' not located")

        def addLogEntry(Text):
            try:
                inputLogEntry = driver.find_element_by_id("addLog")
                inputLogEntry.send_keys(Text)
            except:
                print("text input with element id 'addLog' not located")

        def inputLogEntry(Text):
            clickAddButton()
            addLogEntry(Text)
            clickLogSubmitButton()

        def deleteFirstEntry():
            firstDeleteButton = driver.find_element_by_xpath("//html/body/div[2]/div/table/tbody/tr[1]/td[3]/a[2]/i")
            firstDeleteButton.click()

        def switchForms(): # function that searches for switch form button (between login and signup)
            try:
                toSignUp = driver.find_element_by_link_text("Create an account")
                toSignUp.click()
            except:
                toLogin = driver.find_element_by_link_text("Sign In")
                toLogin.click()
            finally:
                pause()

        def pause():
            time.sleep(1)

        def compareTitles(title1, title2):
            if (title1 == title2):
                return True
            else:
                return False

        def checkTitlesAre(state, title1, title2): # state assumes either 'diff' or 'notdiff'
            if (compareTitles==False and (state == "diff")):
                return True
            elif (compareTitles==True and (state == "notdiff")):
                return True
            else:
                return False

        def goToForm(currentstate, location): # function that decides if switchform should be used
            if ((currentstate == "login") and (location == "signup")):
                try:
                    switchForms()
                except:
                    print("Form switch error. Make sure you are on the index page")
                return location
            elif ((currentstate == "signup") and (location == "login")):
                try:
                    switchForms()
                except:
                    print("Form switch error. Make sure you are on the index page")
                return location
            else:
                return currentstate

        def locateTextInPage(text):
            try:
                src = driver.page_source
                text_found = re.search(text, src)
                print("Element found.")
                if (text_found):
                    return True
                else:
                    return False
                return True
            except:
                print("Element not found.")
                return False

        def correctLogIn():
            inputLogin("bobby135", "lamb786")


        def test_index(self):
            response = self.client.get('/')
            self.assertEqual(response.status_code,200)

        def test_login_and_logout(self):
            response = self.client.get('/homepage/')
            self.assertRedirects(response, '/?next=/homepage/')
            self.client.force_login(self.u1)
            response = self.client.get('/homepage/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['user'].username, 'testclient')
            response = self.client.get('/logout/')
            self.assertRedirects(response, '/')

        driver.get("http://snifflog.uksouth.cloudapp.azure.com")
        # driver.get("http://localhost:8000")
        currentstate = "login"
        OriginalTitle = driver.title
        print(driver.title)

        currentstate = goToForm(currentstate, "login")

        #------------------------------- Beginning of login/registration test

        # Non existing user login test
        try:
            currentstate = goToForm(currentstate, "login")
            inputLogin("bobbo135", "lamb781")
        except:
            print("Non-existing user login test failed due to exception")
        else:
            if checkTitlesAre("notdiff", OriginalTitle, driver.title):
                print("Non-existing user login test passed")
            else:
                print("Non-existing user login test passed")
        clearLogin()


        # Blank firstname signup test
        try:
            currentstate = goToForm(currentstate, "signup")
            inputSignup("", "Earl", "bobby135", "lamb786")
        except:
            print("Blank firstname signup test failed due to exception")
        else:
            if checkTitlesAre("notdiff", OriginalTitle, driver.title):
                print("Blank firstname signup test passed")
            else:
                print("Blank firstname signup test passed")
        clearSignup()

        # Blank secondname signup test
        try:
            currentstate = goToForm(currentstate, "signup")
            inputSignup("Bob", "", "bobby135", "lamb786")
        except:
            print("Blank secondname signup test failed due to exception")
        else:
            if checkTitlesAre("notdiff", OriginalTitle, driver.title):
                print("Blank secondname signup test passed")
            else:
                print("Blank secondname signup test passed")
        clearSignup()

        # Blank username signup test
        try:
            currentstate = goToForm(currentstate, "signup")
            inputSignup("Bob", "Earl", "", "lamb786")
        except:
            print("Blank username signup test failed due to exception")
        else:
            if checkTitlesAre("notdiff", OriginalTitle, driver.title):
                print("Blank username signup test passed")
            else:
                print("Blank username signup test passed")
        clearSignup()

        # Blank password signup test
        try:
            currentstate = goToForm(currentstate, "signup")
            inputSignup("Bob", "Earl", "bobby135", "")
        except:
            print("Blank password signup test failed due to exception")
        else:
            if checkTitlesAre("notdiff", OriginalTitle, driver.title):
                print("Blank password signup test passed")
            else:
                print("Blank password signup test passed")
        clearSignup()

        # Correct credentials login test

        driver.get("http://snifflog.uksouth.cloudapp.azure.com")
        currentstate = "login"

        # --------------------------------- LogBookTest

        try:
            currentstate = goToForm(currentstate, "login")
            correctLogIn()
        except:
            print("Correct credentials login test failed due to exception")
        else:
            if checkTitlesAre("diff", OriginalTitle, driver.title):
                print("Correct credentials login test passed")
            else:
                print("Correct credentials login test passed")
        pause()

        # will be logged in at this point

        # adding a log entry test
        inputText = "Testing testing 123, Please delete this log after."
        inputLogEntry(inputText)
        if (locateTextInPage(inputText) == True):
            print("Log entry with matching text found. Adding log entry test passed.")
        elif (locateTextInPage(inputText) == False):
            print("Log entry with no matching text found. Adding log entry test failed due to unexpected result")

        # deleting a log entry test
        deleteFirstEntry()
        pause()
        if (locateTextInPage(inputText) == False):
            print("Log entry with no matching text found. Deleting log entry test passed.")
        elif (locateTextInPage(inputText) == True):
            print("Log entry with matching text found. Deleting log entry test failed due to unexpected result")

        # logging out test
        clickLogOutButton()
        time.sleep(4)
        print("Logout test passed")

        pause()
        driver.quit()
