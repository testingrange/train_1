import logging
import os
import inspect
import time

def logger(loglevel=logging.INFO, logname="automation_session.log"):
    logger_name = inspect.stack()[1][3]

    logger = logging.getLogger(logger_name)
    logger.setLevel(loglevel)

    proj_dir = os.getcwd()
    cur_date = time.strftime("%Y%m%d")
    file_name = f"{cur_date}_{logname}"
    log_dir = f"{proj_dir}/REPORTS111/"
    full_log_dir = log_dir + file_name
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    print(full_log_dir)

    file_handler = logging.FileHandler(full_log_dir, mode="a")
    file_handler.setLevel(loglevel)

    formatter = logging.Formatter("%(asctime)s- %(name)s- %(levelname)s- %(message)s", datefmt="%Y/%m/%d_%H:%M:%S")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger

def test_mode():
    log = logger(logging.INFO)
    log.info("Test message - TEST TEST")

#test_mode()
#
# c = [
#   ".w....",
#   ".w....",
#   "..w...",
#   "....w.",
#   "......",
#   "......"
# ]
# def path_finder(maze):
#    x = 0
#    y = 0
#    y_length = len(maze)
#    x_length = len(maze[y_length-1])
#    last = [y_length-1, x_length - 1]
#    counter = 0
#    while True:
#        for i in maze[y]:
#            if x != "w":
#                counter +=1
#            else:
#                break
#            y+=1
#        print(f"x is {x}")
#        print(f"y is {y}")
#        if x == x_length -1 and y == y_length - 1:
#            False
#
#
# path_finder(c)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Orange():

    def test(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        sleep(1)
        userName = driver.find_element(By.XPATH, "//input[@name='username']")
        userName.send_keys("Admin")
        passwordField = driver.find_element(By.XPATH, "//input[@name='password']")
        passwordField.send_keys("admin123")
        loginBtn = driver.find_element(By.XPATH, "//button[@type='submit']")
        loginBtn.click()
        sleep(3)
        #userName.clear()
        #passwordField.clear()
        #sleep(2)
        #print("clearing userName input field")
        #userName = driver.find_element(By.XPATH, "//input[@name='username']")
        #userName.clear()
        #userName.send_keys(Keys.DELETE)
        #wait = WebDriverWait(driver, 15, 0.5)
        #action = ActionChains(driver)
        #print("Clearing input field")
        #print("Getting lenght of text")
        #userName = driver.find_element(By.XPATH, "//input[@name='username']")
        #textLenght = len(userName.get_attribute('value'))
        #print(textLenght)
        #userName = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))

        #userName.click()
        #sleep(1)
        #for i in range(textLenght):
        #    print("Deleting characters")
        #    userName.send_keys(Keys.CLEAR)

        #userName.clear()
        #print("Click on login button")
        #loginBtn.click()
        #sleep(60)
        #driver.quit()
        leave_btn = driver.find_element(By.LINK_TEXT, "Leave")
        print("Clicking on leave button")
        leave_btn.click()
        sleep(3)
        time_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Time")
        print("Clicking on time button")
        time_btn.click()
        sleep(2)
        directory_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Directory")
        print("Clickcint on directory button")
        directory_btn.click()
        sleep(3)

testProject = Orange()
#testProject.test()
def path_finder(maze):
    maze = maze.split()
    print(maze)
    pos = maze[0][0]
    x = y = len(maze)
    #print(x, y)
    steps = 0
    i=j=0
    while j!=len(maze)-1:
        print(j)
        while i!=len(maze)-1:
            if maze[i][j] =='W':
                j+=1
                break
            else:
                i+=1
            print(f"maze[{i}][{j}] = {maze[i][j]}")


    # while True:
    #
    #     if maze[i][j] != 'W':
    #
    print(f"This is maze[1][2] - '{maze[0][1]}'")
    for i in range(x):
        for j in range(y):
            #print(i, j)
            print(i,j)
            if maze[i][j] == 'W':
                break
            else:
                steps +=1


    #x = y
    #x = len(maze[0])
    #print(y, x)
    #pos = {x: 0,
    #       y: 0}

    #maze_schema = (x, y)
    #print(pos)

    #steps = 0
    # while True:
    #     pos[x] +=1
    #     if pos[x] == "W":
    #         pos[x] -=1
    #         pos[y] +=1
    #     else:
    #         steps += 1




a = "\n".join([
  ".W.",
  ".W.",
  "..."
])
#print(a)
#path_finder(a)


#for i in ".W.":
#    print(i)

#print(len(".W."))

print("|.|W|.|\n"
      "|.|W|.|\n"
      "|.|.|.|")




a = [1, 303, 10000, 5, -100000, 5252352]
print(f"length is {len(a)}")
myName = 'myName'
newDict = {
    'myName': "Stan",
    'myAge': 40,
    'real': True
}
print(newDict['myName'])
print(newDict['myAge'])
print(newDict['real'])
print(max(a))

from random import randrange
def game():
    def one_more():
        user_input = input("One more game? Y or N for quit")
        if user_input.upper() == "Y":
            return "Y"
        else:
            return "N"

    items = ['papper', 'scisors', 'rock']
    game = True
    user_choice = None
    selection = False
    while game:
        while not selection:
            try:
                user_choice = int(input("your choice. 0 for papper, 1 for scisors, 2 for rock"))
                print(user_choice)
                if 2 < user_choice or user_choice < 0:
                    print("2 < user_choice or user_choice < 0")
                else:
                    selection = True
            except:
                print("Input number for item only")
        user = items[user_choice]
        print(f"User's choise is {user}")
        computer_choice = items[randrange(3)]
        print(f"Computer's choice is {computer_choice}")
        if user == "papper" and computer_choice == "papper":
            print("It s Draw. Repeat the choice!")
            selection = False
            continue
        elif user == "papper" and computer_choice == "scisors":
            print("Computer won")
            if one_more() == "Y":
                selection = False
                continue
            else:
                print("Sorry to see you go. See you!")
                for i in range(5):
                    os.system('cls')
                    sleep(0.5)
                    print("See you!")
                    time.sleep(0.5)
                game = False
        else:
            selection = False


#game()
a = 0
b = 1

a,b = b,a
print("a is : ", a)
print("b is : ", b)


class Car():
    wheels = 4
    transport = "automobile"

    def __init__(self, make, model, engine, doors=4):
        self.make = make
        self.model = model
        self.doors = doors
        self.engine = engine

    def __str__(self):
        print(f"This is a {self.transport} made by {self.make} and model is {self.model} car with {self.doors} doors and {self.engine} engine and {self.wheels} wheels")

    def drive(self):
        print("wroom, wroom")

my_Toyota = Car('Toyota', 'Prius', 1.5)
# my_Toyota.description()

print(type(my_Toyota))
print(my_Toyota.engine)


my_Toyota.__str__()
print(my_Toyota.wheels)

class Moto(Car):
    wheels = 2
    transport = "motorcycle"

    def __init__(self, make, model, engine, doors=0):
        super().__init__(self, make, model, engine)
        self.make = make
        self.model = model
        self.engine = engine
        self.doors = doors

    def drive(self):
        super().drive()
        print("Drive this motorcycle")

my_moto = Moto("Suzuki", "SportBike400s", 3.5)

my_moto.__str__()
my_moto.drive()

class Fruit():
    def __init__(self, nutrition, item_color):
        self.nutrition = nutrition
        self.item_color = item_color

    def nutricion(self):
        print(f"Nutriotion level is {self.nutrition}")

    def color(self):
        print(f"Color is {self.item_color}")

apple = Fruit("medium", "green")

apple.nutricion()
apple.color()

class Apple(Fruit):
    def __init__(self, nutrition, item_color):
        super().__init__(nutrition, item_color)


big_apple = Apple("Very nutritious", "red")
big_apple.nutricion()
big_apple.color()

class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        print(f"make is {self.make} and model is {self.model}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

audi = Car("Toyota", "Prius")
audi.__str__()

car = {
    "make": "toyota",
    "model": "prius",
    "year": 2008
}

try:
    print(car["make"])
    print(car["year"])
    print(car["color"])
except:
    print("Such parameter doesn't exist")

from math import log

def isPowOfThree(n):
    print(f"{log(n, 3)}")


isPowOfThree(27)
isPowOfThree(9)
isPowOfThree(8)

my_list = [1,2,3]
my_file = open("test_report_071223.txt", "a")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()


new_file = open("test_report_071223.txt", "r")
new_data = new_file.read()
print(new_data)
new_file.close()

print("Line by line ==============>>")

my_file_line = open("test_report_071223.txt", 'r')
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
print(str(my_file_line.readline()))
my_file_line.close()

with open("test_report_071223.txt", "a") as file:
    file.write("New line \n")

with open("test_report_071223.txt", "r") as file:
    print(file.read())


print(log(8)/log(2))
print(9//2)

def buy_tofu(cost, box):
    wallet = {1: 0,
              5: 0,
              "total": 0}
    for item in list(filter(lambda x: (x in ["mon", "monme"]), box.split(' '))):
        if item == "mon":
            wallet[1] += 1
        else:
            wallet[5] += 1
    print(wallet)

buy_tofu(150, "mon mon mon mon mon apple mon mon mon mon mon mon mon monme mon mon monme mon mon mon mon cloth monme mon mon mon mon mon mon mon mon cloth mon mon monme mon mon mon mon monme mon mon mon mon mon mon mon mon mon mon mon mon mon")

print(type(2.5))

# from selenium import webdriver
#
# from selenium.webdriver.firefox.service import Service as FF_driver
#
# service = FF_driver(executable_path="")
#
# driver = webdriver.Firefox(service=service)

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
        sleep(2)
        section = self.driver.find_element(By.XPATH, "//h2[contains (text(), 'Reinforce Your JS DataTable with DHTMLX Suite')]")
        # print(len(tables))
        # Scrolling down to the element of interest on the page to be visible
        self.actions.move_to_element(section).perform()
        self.driver.execute_script("window.scrollBy(0,800);")
        sleep(10)
        # identifying correct iframe to work with
        frames = self.driver.find_elements(By.XPATH, "//iframe")
        print("Total iframes on the page", len(frames))
        self.driver.switch_to.frame(5)
        sleep(10)
        button = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Add a new row')]")
        button.click()
        sleep(2)

test_cycle = Table()
test_cycle.test()