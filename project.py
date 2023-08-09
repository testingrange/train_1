from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Table():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)

    def test(self):
        print("Start testing process")
        self.driver.maximize_window()
        self.driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/")
        sleep(4)
        ### Need to scroll down couple of times for tables to load properly
        ### If we do not scroll we get 500 error in all times when we use Selenium
        for i in range(4):
            self.driver.execute_script("window.scrollBy(0,800);")
            sleep(1.5)
        self.driver.execute_script("window.scrollBy(0,-3200);")
        section = self.driver.find_element(By.XPATH, "//h2[contains (text(), 'Reinforce Your JS DataTable with DHTMLX Suite')]")
        #Scrolling down to the element of interest on the page to be visible
        self.actions.move_to_element(section).perform()
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(2)
        # identifying correct iframe to work with
        frames = self.driver.find_elements(By.XPATH, "//iframe")
        print("Total iframes on the page", len(frames))
        for i in range(len(frames)):
            sleep(1)
            self.driver.switch_to.frame(i)
            print("Switched to frame number - ", str(i))
            sleep(0.5)
            try:
                print("In iframe")
                iframes = self.driver.find_elements(By.XPATH, "//iframe")
                print("Number of subframes is - ", len(iframes))
                if len(iframes) > 0:
                    self.driver.switch_to.frame(0)
                    print("Switched to sub frame")
                    try:
                        print("In sub frame")
                        iframes = self.driver.find_elements(By.XPATH, "//iframe")
                        print("Number of sub subframes is - ", len(iframes))
                        if len(iframes) == 0:
                            print("switching to default content")
                            self.driver.switch_to.default_content()
                        elif self.driver.find_element(By.ID, "content") is not None:
                            print("Iframe with id content was found. Switching to iframe")
                            self.driver.switch_to.frame("content")
                            print("Switched to sub sub iframe with id 'content'")
                            icon = self.driver.find_element(By.XPATH, "//button[@data-dhx-id='earth']")
                            if icon is not None:
                                print("Icon element was found")
                                sleep(2)
                                print("Trying to click Add new row button")
                                try:
                                    button = self.driver.find_element(By.XPATH,
                                                                  "//button[@data-dhx-id='add']")
                                    button.click()
                                    sleep(2)
                                    print("New row section added")
                                    title_fld = self.driver.find_element(By.XPATH, "//input[@data-dhx-id='title']")
                                    title_fld.send_keys("Title")
                                    authors_fld = self.driver.find_element(By.XPATH, "//input[@data-dhx-id='authors']")
                                    authors_fld.send_keys("Authors")
                                    rating_fld = self.driver.find_element(By.XPATH, "//input[@data-dhx-id='average_rating']")
                                    rating_fld.send_keys("Rating")
                                    publication_date_fld = self.driver.find_element(By.XPATH, "//input[@data-dhx-id='publication_date']")
                                    publication_date_fld.click()
                                    sleep(2)
                                    ### Selecting random date on the pop up calendar
                                    date = self.driver.find_element(By.XPATH, "//div[contains (@class, 'dhx_calendar-day') and contains (@role,'button') and contains (., '15')]")
                                    date.click()
                                    apply_button = self.driver.find_element(By.ID, "apply-button")
                                    apply_button.click()
                                    sleep(2)
                                    print("New row was successfully added.")
                                    sleep(2)
                                    new_row = self.driver.find_element(By.XPATH, "//div[contains (@class, '') and contains(text(), 'Title')]")
                                    if new_row.is_displayed():
                                        print("Added new row is displayed")
                                        print("Test completed")
                                    else:
                                        print("Couldn't verify that new row was added")
                                    break
                                except:
                                    print("Error occurred when tried to click add new row button")
                                    self.driver.switch_to.default_content()
                            else:
                                print("Icon element was NOT found!")

                    except:
                        print("Something went wrong!!!")
                        self.driver.switch_to.default_content()
                else:
                    self.driver.switch_to.default_content()
                    sleep(0.5)
                    print("Switched back to default content")
            except:
                print("Switching to frame has failed")

        self.driver.close()




test_cycle = Table()
test_cycle.test()