from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

if __name__ == "__main__":

    driver = webdriver.Chrome()
    base_url = "https://www.kaggle.com/datasets"
    driver.get(base_url)
    
    buttons = driver.find_elements(By.TAG_NAME,'button')
    buttons_name=[]
    buttons_link = []
    dataset_urls = []

    for btn in buttons:
        if (btn.text == 'All datasets' or btn.text == 'Computer Science' or btn.text == 'Education' or btn.text == 'Classification' or btn.text == 'Computer Vision' or btn.text == 'NLP' or btn.text == 'Data Visualization' or btn.text == 'Pre-Trained Model'):
            buttons_name.append(btn.text)

    for i in range(len(buttons_name)):            
        button = driver.find_element(By.XPATH, f'//button[@aria-label="{buttons_name[i]}"]')
        button.click()
        time.sleep(3)
        buttons_link.append(driver.current_url)
        driver.get(base_url)
    print(buttons_link)
        
    for i in range(len(buttons_link)):
        driver.get(buttons_link[i])    
        # if count == 0:
        for j in range(501):
            if j == 1:
                continue
            if i == 0:
                try:
                    driver.get(f'{buttons_link[i]}?page={j}')
                    time.sleep(3)
                    dataset = driver.find_element(By.CLASS_NAME, 'sc-hhJFul')
                    dataset_list = dataset.find_elements(By.TAG_NAME, 'li')
                    # print(len(dataset_list))  

                    for dataset_elem in dataset_list:
                        link = dataset_elem.find_element(By.TAG_NAME, 'a')
                        url = link.get_attribute('href')
                        # print(url)
                        dataset_urls.append({
                            'url':url
                        })
                except:
                    break
            else:
                try:
                    driver.get(f'{buttons_link[i]}&page={j}')
                    time.sleep(3)
                    dataset = driver.find_element(By.CLASS_NAME, 'sc-hhJFul')
                    dataset_list = dataset.find_elements(By.TAG_NAME, 'li')
                    # print(len(dataset_list))   

                    for dataset_elem in dataset_list:
                        link = dataset_elem.find_element(By.TAG_NAME, 'a')
                        url = link.get_attribute('href')
                        # print(url)
                        dataset_urls.append({
                            'url':url
                        })
                except:
                    break
            # driver.get(url)

    df = pd.DataFrame(data=dataset_urls, columns=dataset_urls[0].keys())
    df.to_csv("dataset_urls.csv", index=False)
                                
                # for k in range(20):
                    # elems = driver.find_elements(By.CLASS_NAME, "sc-cZpZpK")
                    # # # elems = driver.find_elements(By.TAG_NAME, 'a')
                    # for elem in elems:
                    #     link = elem.find_element(By.TAG_NAME, 'a')
                    #     url = link.get_attribute('href')
                    #     print(url)
                    #     driver.get(url)
                        
                    # headlines = driver.find_elements(By.TAG_NAME, 'h1')
                    # for head in headlines:
                    #     headline = head.find_element(By.CLASS_NAME,'sc-eTNRI sc-cmSatC iudEzZ imhhxQ')
                    #     headline = headline.text
                    # descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
                    # for desc in descriptions:
                    #     description = desc.find_element(By.TAG_NAME,'p')
                    #     description = description.text

                    # categories = driver.find_elements(By.TAG_NAME,'button')
                    # for cat in categories:
                    #     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
                    #     category = category.text

                    
                    
        #             dataset_info.append(
        #                 {
        #                     'Title':headline,
        #                     'Description':description,
        #                     'Categories':category
        #                 }
        #             )

                
        #         df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #         df.to_csv('kaggle_datasets_details.csv',index=False)
        
        # count = count + 1

        # driver.get(base_url)

        # if count == 1:
        #     for j in range(2,501):
        #             driver.get(f'{base_url}?tags=12107-Computer+Science&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 2:
        #     for j in range(2,431):
        #             driver.get(f'{base_url}?tags=11105-Education&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 3:
        #     for j in range(2,205):
        #             driver.get(f'{base_url}?tags=13302-Classification&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 4:
        #     for j in range(2,160):
        #             driver.get(f'{base_url}?tags=13207-Computer+Vision&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 5:
        #     for j in range(2,178):
        #             driver.get(f'{base_url}?tags=13207-Computer+Vision&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 6:
        #     for j in range(2,265):
        #             driver.get(f'{base_url}?tags=13208-Data+Visualization&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        # if count == 7:
        #     for j in range(2,501):
        #             driver.get(f'{base_url}?tags=16668-Pre-Trained+Model&page={j}')
        #             for k in range(20):
        #                 headline = driver.find_element(By.TAG_NAME, 'h1')
        #                 headline = headline[0].text
        #                 descriptions = driver.find_elements(By.CLASS_NAME, 'sc-kGLCbq fAhUHg sc-hpEtbN ianGAQ')
        #                 for desc in descriptions:
        #                     description = desc.find_element(By.TAG_NAME,'p')
        #                     description = description[0].text

        #                 categories = driver.find_elements(By.TAG_NAME,'button')
        #                 for cat in categories:
        #                     category = cat.find_element(By.CLASS_NAME,'sc-khjJXk sc-jtCqdw iiUvTE cgRbwq')
        #                     category = category.text
                        
        #                 dataset_info.append(
        #                     {
        #                         'Title':headline,
        #                         'Description':description,
        #                         'Categories':category
        #                     }
        #                 )

                    
        #             df = pd.DataFrame(data = dataset_info, columns = dataset_info[0].keys())
        #             df.to_csv('kaggle_datasets_details.csv',index=False)
            
        #     count = count + 1

        #     driver.get(base_url)

        

        
            
            
    
    # for i in range(501):
    #     driver.get(f'{base_url}?page={i}')

    
