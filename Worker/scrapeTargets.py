import time

def scrapeTarget(driver, url):
    driver.get(url)
    flowers = driver.find_elements_by_tag_name('a')

    for opnflw in flowers:
        if(opnflw.get_attribute('href')==url+"followers/"):
            opnflw.click()
    time.sleep(4)
    lols = driver.find_elements_by_tag_name('div')
    time.sleep(4)
    for lol in lols:
        if(lol.get_attribute('role')=='dialog'):
            print("dialog Found")
            secwin = lol.find_element_by_class_name('isgrP')
            lis = driver.find_elements_by_tag_name('li')
    
    oldlist = len(lis)

    driver.execute_script("arguments[0].scrollTo(0,1000);", secwin)
    time.sleep(3)
    driver.execute_script("arguments[0].scrollTo(1000,0);", secwin)
    time.sleep(3)
    driver.execute_script("arguments[0].scrollTo(100,500);", secwin)
    time.sleep(3)

    nis = driver.find_elements_by_tag_name('li')

    try:
        counter = 1500
        newlist = len(nis)
        check = 0
        while(oldlist<newlist):
            oldlist = newlist
            driver.execute_script("arguments[0].scrollTo(0,"+str(counter)+");", secwin)
            time.sleep(4)
            nis = driver.find_elements_by_tag_name('li')
            newlist = len(nis)
            counter+=1000
            check+=1
            if check >= 1000:
                break
        return (nis, driver)
    except:
        return (nis, driver)