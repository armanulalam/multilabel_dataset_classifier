from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time
import pandas as pd

if __name__ == "__main__":

    driver = webdriver.Chrome()

    df = pd.read_csv("dataset_urls.csv")
    dataset_urls = df.url.to_list()

    dataset_info = []

    for dataset_url in tqdm(dataset_urls):
            
        try:
            driver.get(dataset_url)
            time.sleep(3)

            title_element = driver.find_element(By.CLASS_NAME, "sc-geUVBg")
            title = title_element.find_element(By.TAG_NAME, "h1").text

            descriptions = driver.find_elements(By.CLASS_NAME, "sc-kVhqWl")
            for desc in descriptions:
                description = desc.find_element(By.CLASS_NAME, 'sc-kGLCbq').text
                description = description.replace("\n", "")
            
            categories = driver.find_elements(By.CLASS_NAME, "sc-fSrjIW")
            for cat in categories:
                category = cat.find_element(By.CLASS_NAME, 'sc-bPNAxY').text
                category = category.replace("\n", ",")

            dataset_info.append({
                "title": title,
                "url": dataset_url,
                "description": description,
                "categories": category
            })
            time.sleep(3)

            # print(dataset_info)

            df = pd.DataFrame(data=dataset_info, columns=dataset_info[0].keys())
            df.to_csv("dataset_info.csv", index=False)
        
        except:
            time.sleep(3)