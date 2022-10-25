from selenium import webdriver
from selenium.webdriver.common.by import By
DRIVER_PATH = '/home/mostapollo/chromedriver'


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://ro-dyn-backend.bosch.com/c-corpweb-tc/es/bosch-ro-backend-*-de/ro_bosch_backend__job_posting/_search"
url = "https://www.bosch.de/karriere/jobs/?sortBy=releasedDate&utm_medium=cpc&utm_source=google&utm_campaign=pac&gclid=EAIaIQobChMIvuTAyPz4-gIVQ_53Ch0GrADdEAAYASAAEgJZnPD_BwE"
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


xpath = "/html/body/main/section[1]/div/o-job-search-dynamic-component/div/m-job-search-results-group-dynamic/div[2]/a-load-more-dynamic/a-frok-button-dynamic/button/span"

import time


driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(12)



xpath_over = "/html/body/div[2]/div/div/div[5]/button[1]"

h0 = driver.find_element(By.XPATH, xpath_over)
h0.click()

time.sleep(2)

h1 = driver.find_element(By.XPATH,"/html/body/main/section[1]/div/o-job-search-dynamic-component/div/m-job-search-results-group-dynamic/div[2]/a-load-more-dynamic/a-frok-button-dynamic/button/span")

while True:
    try:
        loadMoreButton = h1
        time.sleep(2)
        print("try")
        loadMoreButton.click()
        print("clicked!")
        
        time.sleep(2)
    except Exception as e:
        print (e)
        break
print ("Complete")
a = driver.find_elements(By.CLASS_NAME,"A-JobPanel__header")
print(len(a))

saved = []
import numpy as np

for item in a:
    saved.append(item.text)
saved = np.asarray(saved)

np.savez("./jobs.npz", saved = saved)
abc = np.load("jobs.npz", allow_pickle=True)
time.sleep(10)
driver.quit()
def findPraktikum():
    for i in abc["saved"]:
        if "Praktikum" in i:
            print(i)


findPraktikum()