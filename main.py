# time is library that you need to import, it allows you to use the function time.sleep
# webdriver is the other library that you need , it contains selenium
# you will need to right click the words and select import library to actually import the files to your directory
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.support.ui import Select

# global window_before
# global window_after


# this selects the webdriver you will be using. I chose chrome

driver = webdriver.Chrome()
# driver2 = webdriver.Chrome()
# this opens the browser on this selected URL , insert whichever URL you'd like to open
driver.get("https://www.solanart.io/")

window_before = driver.window_handles[0]


# driver2.get("https://www.solanart.io/collections/sollamasgraves")
# sleeps the program for 2 seconds
# basically allows the browser to load before running any code, might need a longer sleep depending on ur computer

btnWelcome = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/p/button/span[1]')
btnWelcome.click()
time.sleep(1)
btnConnectWallet = driver.find_element_by_xpath('/html/body/div/div/header/div[1]/div/button')
btnConnectWallet.click()
time.sleep(2)
btnSollet = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/button[1]')
btnSollet.click()
time.sleep(2)
btnConnectWalletConfirm = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/button')
btnConnectWalletConfirm.click()
time.sleep(2)
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
btnOK = driver.find_element_by_xpath('/html/body/div[2]/div[3]/form/div[3]/button[2]')
btnOK.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
btnRestoreWallet = driver.find_element_by_xpath('/html/body/div/main/div/a')
btnRestoreWallet.click()
time.sleep(2)
inputSeedPhrase = driver.find_element_by_xpath('/html/body/div/main/div/div/div[1]/div[1]/div/textarea')
inputSeedPhrase.send_keys(
    'sudden still glare essay leg enhance please rude maze hockey castle radar into dust hope '
    'blade danger army domain misery teach few will soccer')
btnNext = driver.find_element_by_xpath('/html/body/div/main/div/div/div[2]/button[2]/span[1]')
btnNext.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
btnRestore = driver.find_element_by_xpath('/html/body/div/main/div/div/div[2]/button[2]/span[1]')
btnRestore.click()
btnConnect = driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]/span[1]')
btnConnect.click()
driver.switch_to.window(window_before)


# loadWallet()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# time.sleep(5)

driver.set_window_size(1920, 1080)
driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()

time.sleep(3)

driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/div/div[11]/div/a/div/button/button").click()
time.sleep(2)

driver.execute_script("window.scrollTo(0, 170)")

select = Select(driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[5]/div/div/select'))

select.select_by_value('2')
select.select_by_value('0')

btnRefresh = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/button')

blnOutOfMoney = False
blnItemBought1 = False
blnItemBought2 = False
blnItemBought3 = False

time.sleep(2)

intPrice = 1.21

while not blnOutOfMoney:
        try:
            btnRefresh.click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 180)")
            time.sleep(2)
            nft = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[2]/div/div/div['
                                               '1]/div/div/div[2]/div[3]/span')
            nftPrice = nft.text[0:-4]

            nft2 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div['
                                                '2]/div/div/div[2]/div[3]')
            nftPrice2 = nft2.text[0:-4]
            nft3 = driver.find_element_by_xpath('/html/body/div/div[1]/div/div/div/div/div[3]/div[2]/div/div/div['
                                                '3]/div/div/div[2]/div[3]')
            nftPrice3 = nft3.text[0:-4]
            print(nftPrice2)
            print(nftPrice)
            if float(nftPrice) < intPrice and not blnItemBought1:
                nft.click()
                time.sleep(1.3)
                driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]').click()
                blnItemBought1 = True
                break
            if float(nftPrice2) < intPrice and not blnItemBought2:
                nft2.click()
                time.sleep(1.3)
                driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]').click()
                blnItemBought2 = True
                break
            if float(nftPrice3) < intPrice and not blnItemBought3:
                nft2.click()
                time.sleep(1.3)
                driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]').click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]').click()
                blnItemBought23= True
                break
        except StaleElementReferenceException:
            print('in stale element error')
            time.sleep(3)
            btnLetsGo = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/p/button')
            btnLetsGo.click()
            time.sleep(1)
            btnConnectWallet = driver.find_element_by_xpath('/html/body/div/div/header/div[1]/div/button')
            btnConnectWallet.click()
            time.sleep(2)
            btnSollet = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/button[1]')
            btnSollet.click()
            time.sleep(2)
            btnConnectWalletConfirm = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/button')
            btnConnectWalletConfirm.click()
            time.sleep(2)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            btnCompleteConnect = driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]')
            btnCompleteConnect.click()
            time.sleep(2)
            driver.switch_to.window(window_before)
            driver.execute_script("window.scrollTo(0, 180)")
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/a/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div/div[2]/div/div[2]/div/div[11]/div/a/div/button/button").click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 170)")
            select = Select(
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[5]/div/div/select'))
            select.select_by_value('2')
            select.select_by_value('0')
            time.sleep(2)
            btnRefresh = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/button')
            print('in no such element')
            time.sleep(2)
            btnRefresh.click()
            continue
        except NoSuchElementException:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/a/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div/div[2]/div/div[2]/div/div[11]/div/a/div/button/button").click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 170)")
            select = Select(
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[5]/div/div/select'))
            select.select_by_value('2')
            select.select_by_value('0')
            btnRefresh = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/button')
            print('in no such element')
            time.sleep(2)
            btnRefresh.click()
            continue
        except ElementClickInterceptedException:
            print('elementclickerror')
            continue
        except ValueError:
            print('value error')
            time.sleep(3)
            btnLetsGo = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/p/button')
            btnLetsGo.click()
            time.sleep(1)
            btnConnectWallet = driver.find_element_by_xpath('/html/body/div/div/header/div[1]/div/button')
            btnConnectWallet.click()
            time.sleep(2)
            btnSollet = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/div[2]/button[1]')
            btnSollet.click()
            time.sleep(2)
            btnConnectWalletConfirm = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div/button')
            btnConnectWalletConfirm.click()
            time.sleep(2)
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            btnCompleteConnect = driver.find_element_by_xpath('/html/body/div/main/div/div[2]/button[2]')
            btnCompleteConnect.click()
            time.sleep(2)
            driver.switch_to.window(window_before)
            continue
        except ElementClickInterceptedException:
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/a/button').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[3]').click()
            time.sleep(3)
            driver.find_element_by_xpath(
                "/html/body/div/div[1]/div/div/div[2]/div/div[2]/div/div[11]/div/a/div/button/button").click()
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, 170)")
            select = Select(
                driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/div[3]/div[1]/div[5]/div/div/select'))
            select.select_by_value('2')
            select.select_by_value('0')
            btnRefresh = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div/button')
            print('in no such element')
            time.sleep(2)
            btnRefresh.click()
            continue

# btnSolBears = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div[2]/div/div['
#      '3]/div/a/div/button/div[1]')
# btnSolBears.click()


# listTitle = []
# for i in channel_title:
# listTitle.append("[" + i.get_attribute('innerHTML') + "]")


# print(str(res))

# i = 1

# scroll_pause_time = 1
# screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web


# this is the start of your loop , while True , honestly not sure entirely how it works idk python
# while True:
# scroll one screen height each time
# driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
# i += 1
# time.sleep(scroll_pause_time)
# update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
# scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")
# Break the loop when the height we need to scroll to is larger than the total scroll height
# if (screen_height) * i > scroll_height:
#  break

# this is where we are when we've broken the loop , bottom of the web page , now we can process the data
# this finds all the titles on the web page and adds them to this array called channel_title
