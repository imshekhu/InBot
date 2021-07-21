from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time
import datetime
import random

# global driver
# #print'here')
import sys
import os
import django
from django.core.mail import send_mail

sys.path.append('..//')
os.environ['DJANGO_SETTINGS_MODULE'] = 'inbot.settings'
# print(os.environ.get('DJANGO_SETTINGS_MODULE'))
django.setup()

from webmaster.models import SettingsModel, TargetModel
# from inbot import settings
from scrapeTargets import scrapeTarget

def MasterSettings():
    settings = get_settings()
    if settings:
        settle = {}
        settle['username'] = settings.username
        settle['password'] = settings.password
        settle['frequencyfollow'] = settings.frequencyfollow
        settle['frequencyunfollow'] = settings.frequencyunfollow
        settle['frequencypostcheck'] = settings.frequencypostcheck
        settle['daysafterunfollow'] = settings.daysafterunfollow
        settle['state'] = settings.state
        settle['emailsuspicion'] = settings.emailsuspicion
        return settle
    return None


def get_settings():
    try:
        return SettingsModel.objects.get(pk=1)
    except SettingsModel.DoesNotExist:
        return None


def getInsta():
    #print'getInsta')
    try:
        try:
            driver.quit()
        except:
            pass
        # prox = Proxy()
        # prox.proxy_type = ProxyType.MANUAL
        # http_proxy = "65.184.156.234:52981"
        
        # capabilities = webdriver.DesiredCapabilities.CHROME
        # prox.add_to_capabilities(capabilities)
        options = Options()
        # options.headless = True
        # options = webdriver.ChromeOptions()
        # options.add_argument('--proxy-server=%s' % http_proxy)
        
        driver = webdriver.Chrome('./chromedriver.exe',  options=options)
        # driver.get("http://whatismyipaddress.com")
        driver.get('https://www.instagram.com/accounts/login/')
        driver.save_screenshot('./images/getInsta.png')
        # driver.minimize_window()
        return driver
    except Exception as e:
        print(e)
        return False


def login(driver, username, password):
    # #print'login')
    try:
        inputs = driver.find_elements_by_tag_name('input')
        #printlen(inputs))
        for input in inputs:
            if(input.get_attribute('type') =='text' ):
                uname = input
            if(input.get_attribute('type') =='password' ):
                pwd = input

        # uname.send_keys('strawberries_black')
        # pwd.send_keys('deltaforce')

        uname.send_keys(username)
        pwd.send_keys(password)
        pwd.send_keys(Keys.ENTER)
        driver.save_screenshot('./images/login.png')
        return driver
    except Exception as e:
        driver.save_screenshot('./images/loginError.png')
        return None
        

def mainPage(driver):
    #print'mainPage')
    try:
        try:
            time.sleep(5)
            btns = driver.find_elements_by_tag_name('button')
            for oneBtn in btns:
                # #printoneBtn.text)
                if oneBtn.text == 'Not Now':
                    oneBtn.click()
                    break
            driver.save_screenshot('./images/mainPageSaveInfo.png')
        except Exception as e:
            print(e)
            driver.save_screenshot('./images/mainPageSaveInfo_Error.png')
            pass
        time.sleep(6)
        try:
            notif = driver.find_elements_by_tag_name('button')
            #printlen(notif))
            for noti in notif:
                if(noti.get_attribute('class') == 'aOOlW   HoLwm '):
                    if(noti.text == 'Not Now'):
                        nowbtn = noti
            nowbtn.click()
            driver.save_screenshot('./images/mainPageNotNow.png')
        except Exception as e:
            print(e)
            driver.save_screenshot('./images/mainPageNotNow_Error.png')
            pass
        time.sleep(6)
        headerClass = driver.find_element_by_class_name('_47KiJ')
        try:
            profileSpans = headerClass.find_elements_by_tag_name('span')
            for profileSpan in profileSpans:
                if profileSpan.get_attribute('role')=='link':
                    profileSpan.click()
                    break
            time.sleep(6)
            dropDownClass = driver.find_element_by_class_name('_01UL2')
            dropDownBtns = dropDownClass.find_elements_by_tag_name('a')
            for btn in dropDownBtns:
                if btn.text == 'Profile':
                    btn.click()
                    time.sleep(6)
                    driver.save_screenshot('./images/mainPageProfileBtnClicked.png')
                    return driver
        except:
            try:
                profileBtn = headerClass.find_element_by_tag_name('button')
                profileBtn.click()
                time.sleep(6)
                dropDownClass = driver.find_element_by_class_name('_01UL2')
                dropDownBtns = dropDownClass.find_elements_by_tag_name('a')
                for btn in dropDownBtns:
                    if btn.text == 'Profile':
                        btn.click()
                        time.sleep(6)
                        driver.save_screenshot('./images/mainPageProfileBtnClicked2.png')
                        return driver
            except Exception as e:
                print(e)
                driver.save_screenshot('./images/mainPageProfileBtnClicked_Error.png')
                return None

        
    except Exception as e:
        print(e)
        driver.save_screenshot('./images/mainPage_Error.png')
        return None


def profilePage(driver):
    # #print'profilePage')
    time.sleep(5)

    driver.get('https://www.instagram.com/strawberries_black/')
    driver.minimize_window()

    try:
        divs = driver.find_elements_by_tag_name('div')
        for div in divs:
            if div.get_attribute('class') == 'Nnq7C weEfm':
                #print'foundClass')
                firstRowDiv = div
                break
        posts = firstRowDiv.find_elements_by_tag_name('div')
        for post in posts:
            if post.get_attribute('class') == 'v1Nh3 kIKUG  _bz0w':
                latestPost = post
                break
        latestPost.click()
        driver.save_screenshot('./images/profilePageLatestBtnClicked.png')

        time.sleep(6)

        try:
            while True:
                btnss = driver.find_elements_by_tag_name('span')
                for btn in btnss:
                    if btn.get_attribute('aria-label') == 'Load more comments':
                        plusBtn = btn
                        break
                plusBtn.click()
                driver.save_screenshot('./images/profilePagePlusBtnClicked.png')
                time.sleep(5)
        except Exception as e:
                print(e)
                driver.save_screenshot('./images/profilePagePlusBtnClicked_Error.png')

                pass

        uls = driver.find_elements_by_tag_name('ul')
        targets = []
        for ul in uls:
            if ul.get_attribute('class') == 'Mr508':
                aTag = ul.find_element_by_tag_name('a')
                
                targets.append(aTag.get_attribute('href'))
        #Like function needs to be called
        
        try:
            likeDivs = driver.find_element_by_class_name('Nm9Fw')
            btn = likeDivs.find_element_by_tag_name('button')
            getTotalLikeNumber = btn.find_element_by_tag_name('span')
            # print(type(getTotalLikeNumber.text))
            btn.click()
            
            loopTimes = int(int(getTotalLikeNumber.text)/15)+1
            time.sleep(4)
            #Now To scroll limited Times
            counter = 0
            while counter<loopTimes:
                element_inside_popup=driver.find_element_by_xpath('//div[@style="max-height: 356px; min-height: 200px;"]//a')
                element_inside_popup.send_keys(Keys.END)
                counter+=1
                time.sleep(3)
                lols = driver.find_elements_by_tag_name('div')
                dialogControl = False
                for lol in lols:
                        if(lol.get_attribute('role')=='dialog'):
                            try:
                                windowDivs = lol.find_element_by_class_name('_1XyCr')
                                linkA = windowDivs.find_elements_by_tag_name('a')
                            except Exception as e:
                                print(e)
                                driver.save_screenshot('./images/profilePageLikeDialog_Error.png')
                for link in linkA:
                    if len(link.get_attribute('title')) > 0:
            #             print(link.get_attribute('href'))
            #             counter+=1
                        targets.append(link.get_attribute('href'))
            driver.save_screenshot('./images/profilePageLike.png')

        except Exception as e:
            print(e)
            driver.save_screenshot('./images/profilePageLike_Error.png')
            
        targets = list(set(targets))
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        for oneTarget in targets:
            existence = findTarget(oneTarget)
            # #printexistence.link)
            if existence is None:
                fillTarget(oneTarget)
                #print'filled')
        return driver

    except Exception as e:
        driver.save_screenshot('./images/profilePage_Error.png')
        driver.quit()
        return False

def findTarget(link):
    try:
        return TargetModel.objects.get(link=link)
    except TargetModel.DoesNotExist:
        return None

def fillTarget(oneTarget):
    instance = TargetModel(link=oneTarget)
    instance.save()
    return instance

def getAllToFollow(frequencyfollow):
    try:
        return TargetModel.objects.filter(is_followed_ever=False)[:1]
    except TargetModel.DoesNotExist:
        return None

def doneFollow(link):
    instance = TargetModel.objects.get(link=link)
    instance.followed_at = datetime.datetime.now()
    instance.is_followed_ever = True
    instance.save()
    return True

def doneUnFollow(link):
    instance = TargetModel.objects.get(link=link)
    instance.unfollowed_at = datetime.datetime.now()
    instance.is_unfollowed = True
    instance.save()
    return True

def follow(driver, frequencyfollow):
    target = getAllToFollow(frequencyfollow)
    # #printtarget)
    if target:
        driver.get(target[0].link)
        driver.minimize_window()
        time.sleep(5)
        try:
            followSt = False
            header = driver.find_element_by_tag_name('header')
            buttons_in_header = header.find_elements_by_tag_name('button')
            for flwbtn in buttons_in_header:
                if(flwbtn.text == 'Follow') or flwbtn.text == 'Follow Back' :
                    flwbtn.click()
                    doneFollow(target[0].link)
                    time.sleep(3)
                    followSt = True
                    break
            # If already following but not updated in Database
            if followSt is False:
                try:
                    spans = header.find_elements_by_tag_name('span')
                    for span in spans:
                        if span.get_attribute('aria-label') == 'Following':
                            doneFollow(target[0].link)
                            break
                except:
                    pass

            driver.save_screenshot('./images/followSuccess.png')
            return driver
        except Exception as e:
            print(e)
            driver.save_screenshot('./images/follow_Error.png')
            doneFollow(target[0].link)
            return None
            
    return None

def getTargeToUnFollow(Undays):
    lastDay =  datetime.datetime.now() - datetime.timedelta(days=Undays)
    try:
        return TargetModel.objects.filter(is_unfollowed=False, followed_at__lte=lastDay)
    except TargetModel.DoesNotExist:
        return None

def unfollow(driver, daysAfterUnfollow):
    target = getTargeToUnFollow(daysAfterUnfollow)

    if target:
        driver.get(target[0].link)
        driver.minimize_window()
        time.sleep(5)

        try:
            header = driver.find_element_by_tag_name('header')
            spans = header.find_elements_by_tag_name('span')
            for span in spans:
                if span.get_attribute('aria-label') == 'Following':
                    span.click()
                    break
            time.sleep(2)
            bts = driver.find_elements_by_tag_name('button')
            for bt in bts:
                if bt.text == 'Unfollow':
                    bt.click()
                    break
            driver.save_screenshot('./images/unfollowSuccess.png')
            doneUnFollow(target[0].link)
            time.sleep(3)
            return driver
        except :
            try:
                header = driver.find_element_by_tag_name('header')
                buttons_in_header = header.find_elements_by_tag_name('button')
                for flwbtn in buttons_in_header:
                    if(flwbtn.text == 'Requested') :
                        flwbtn.click()                       
                        time.sleep(3)
                bts = driver.find_elements_by_tag_name('button')
                for bt in bts:
                    if bt.text == 'Unfollow':
                        bt.click()
                        doneUnFollow(target[0].link)
                        break
                driver.save_screenshot('./images/unfollowSuccess.png')
                return driver
            except Exception as e:
                print(e)
                doneUnFollow(target[0].link)
                driver.save_screenshot('./images/unfollow_Error.png')
                return None
    return None

def logout(driver):
    try:
           
        headerClass = driver.find_element_by_class_name('_47KiJ')
        profileSpans = headerClass.find_elements_by_tag_name('span')
        for profileSpan in profileSpans:
            if profileSpan.get_attribute('role')=='link':
                profileSpan.click()
                time.sleep(3)
                break
        logoutClass = driver.find_element_by_class_name('_01UL2')
        dropDownBtns = logoutClass.find_elements_by_tag_name('div')
        for btn in dropDownBtns:
            if btn.get_attribute('role') == 'button' and btn.text == 'Log Out':
                #print'found')
                btn.click()
                
    except Exception as e:
        try:
                profileBtn = headerClass.find_element_by_tag_name('button')
                profileBtn.click()
                time.sleep(6)
                dropDownClass = driver.find_element_by_class_name('_01UL2')
                dropDownBtns = dropDownClass.find_elements_by_tag_name('a')
                for btn in dropDownBtns:
                    if btn.text == 'Profile':
                        btn.click()
                        time.sleep(6)
                        return driver
        except Exception as e:
                print(e)
                driver.quit()
                return None
        

def getFollowersListThisHour():
    lastHour =  datetime.datetime.now() - datetime.timedelta(hours = 1)
    try:
        return TargetModel.objects.filter(followed_at__gte=lastHour).count()
    except TargetModel.DoesNotExist:
        return None

def getUnFollowersCountThisHour():
    lastHour =  datetime.datetime.now() - datetime.timedelta(hours = 1)
    try:
        return TargetModel.objects.filter(unfollowed_at__gte=lastHour).count()
    except TargetModel.DoesNotExist:
        return None

def followBrain(driver, frequencyfollow):
    hourCount = getFollowersListThisHour()
    # #print'Hour Count :', hourCount)
    if hourCount < frequencyfollow or hourCount is None:
        followDriver = follow(driver, frequencyfollow)
        return followDriver
    return driver

def unFollowBrain(driver, frequencyUnfollow, daysAfterUnfollow):
    hourCount = getUnFollowersCountThisHour()
    # #print'Hour Count :', hourCount)
    if hourCount < frequencyUnfollow or hourCount is None:
        followDriver = unfollow(driver, daysAfterUnfollow)
        
        return followDriver
    return driver

def sendMailToUser(emailId):
    #Email to Send Here
    print('In mail')
    subject = 'Suspicion Page found in Inbot'
    msg = 'Hi I am Inbot, I have encountered a SUSPICION PAGE or The Code entered was Not the latest One, Please Help me out of this by providing the Code in my Settings Page.'
    fromEmail = 'sharmashourya80@gmail.com'
    res = send_mail(subject, msg, fromEmail, [emailId], fail_silently= False)
    print('mail Sent')
    print(res)
    return True

def setBotSuspicionState():
        instance = get_settings()
        instance.suspicion = True
        instance.suspicioncode = None
        instance.save()
        return instance.suspicion

def getSuspicionState():
    instance = get_settings()
    return instance.suspicion
    
def getSuspicionCode():
    instance = get_settings()
    return instance.suspicioncode

def changeSuspicionToNormal():
    instance = get_settings()
    instance.suspicion = False
    instance.suspicioncode = None
    instance.save()
    return None

def suspicionBrain(driver, emailsuspicion):
    #To control actions of suspicion Page
    try:
        suspicionFound = False
        btns = driver.find_elements_by_tag_name('button')
        for btn in btns:
            if btn.text =='Send Security Code' and 'Suspicious Login Attempt' in driver.page_source:
                securityBtn = btn
                suspicionFound = True
        if suspicionFound is True:
            sendMailToUser(emailsuspicion)
            securityBtn.click()
            suspicionState = setBotSuspicionState()
            while suspicionState is True:
                suspicionState = getSuspicionState()
                # print('sus :: ', suspicionState)
                time.sleep(5)
            code = getSuspicionCode()
            if code:
                findInputs = driver.find_elements_by_tag_name('input')
                for oneInput in findInputs:
                    if oneInput.get_attribute('id') == 'security_code':
                        securityInput = oneInput
                securityInput.send_keys(str(code))
                time.sleep(2)
                findBtn = driver.find_elements_by_tag_name('button')
                for oneBtn in findBtn:
                    if oneBtn.text == 'Submit':
                        foundSubmitBtn = oneBtn
                foundSubmitBtn.click()
                time.sleep(5)
                if 'Please check the code we sent you and try again.' in driver.page_source:
                    driver.quit()
                    return None
                #To change the state of bot back to Normal    
                changeSuspicionToNormal()
                return driver
        else:
            return driver
    except Exception as e:
        print(e)
        return None

def checkTarget(link):
    try:
        return TargetModel.objects.get(link=link)
    except TargetModel.DoesNotExist:
        return None    

def brain():
    settings = MasterSettings()
    if settings and settings['state'] is True:
        driver = getInsta()
        time.sleep(random.randint(5,10))
        loggedInDriver = login(driver, settings['username'], settings['password'])
        if loggedInDriver:
            time.sleep(random.randint(4,8))
            # print('above')
            clearSuspicionDriver = suspicionBrain(loggedInDriver, settings['emailsuspicion'])
            # print('below')
            if clearSuspicionDriver:
                time.sleep(3)
                mainPageDriver =  mainPage(clearSuspicionDriver)
                #print299)
                if mainPageDriver:
                    time.sleep(5)
                    """ -------------- --------------------------"""
                    scraper = False
                    # scraper = True
                    
                    if scraper == True: 
                        url = 'https://www.instagram.com/nayantharaaa/'
                        nis, driver = scrapeTarget(mainPageDriver, url)
                        # print(len(nis))
                        for person in nis[25:]:#start from people href instead of trash pages
                            # print('under person')
                            try:
                                a_tag = person.find_element_by_tag_name('a').get_attribute('href')
                                check = checkTarget(a_tag)
                                if check:
                                    pass
                                else:
                                    fillTarget(a_tag)
                            except:
                                pass
                        profilePageDriver = profilePage(driver)
                    """ -------------------- --------------------- """
                    profilePageDriver = profilePage(mainPageDriver)
                    #print302)
                    if profilePageDriver:
                        #print304)                    
                        followBrain(profilePageDriver, settings['frequencyfollow'])
                        #print306)
                        time.sleep(5)
                        driver = unFollowBrain(profilePageDriver, settings['frequencyunfollow'], settings['daysafterunfollow'])
                        profilePageDriver.quit()
                    else:
                        print('Error in Profile Page')
                        mainPageDriver.quit()
                else:
                    print('Error in Main Page')
                    loggedInDriver.quit()
            else:
                print('suspicionEncountered')
                time.sleep(10)
                return None
        else:
            print('Error in Login')
            driver.quit()
    else:
        print('settings Not found')
        

if __name__ == "__main__":
    while True:
        brain()
        time.sleep(random.randint(180,250))
