from playwright.sync_api import sync_playwright
import random
import time


def random_sleep(min_time=0.5, max_time=1):
    time.sleep(random.uniform(min_time, max_time))

def find(chosenId,chosenFill): 
    search_box = page.locator(chosenId)
    search_box.click()
    random_sleep()
    search_box.fill(chosenFill)
    random_sleep()
    search_box.press("Enter")
    random_sleep(2, 4)

def findAndButton(chosenId):
    singUp = page.locator(chosenId)
    singUp.click()    
    random_sleep()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=random.randint(50, 150))      
    page = browser.new_page()

    page.goto("https://faruk-hasan.com/automation/signup.html")
    random_sleep()

    print(page.title())


    find("#username","Mario_Dario")
    find("#email","test@gmail.com")
    find("#password","IlikeMathPassword")
    find("#confirmPassword","IlikeMathPassword")
    # singUp = page.locator("‘button[type=“submit”]’")
    # singUp.click()
    find("#password","IlikeMathPassword")



    page.select_option("select#pizza-size", "small")
    random_sleep()

    page.get_by_label('cheese').check()
    random_sleep()

    page.locator("input[type='radio'][value='credit']").check()
    random_sleep()

    page.locator("input[type='date']").fill("2025-05-17")
    random_sleep()



    

    