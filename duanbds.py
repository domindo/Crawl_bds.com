import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver.v2 as uc
import json
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
# driver = webdriver.Chrome(
#     options=options, executable_path='C:/Users/WW/Downloads/chromedriver_win32 (1)/chromedriver.exe')
driver = uc.Chrome(options=options,
    executable_path='C:/Users/WW/Downloads/chromedriver_win32 (1)/chromedriver.exe')


class DuanbdsSpider(CrawlSpider):
    name = 'duanbds'
    allowed_domains = ['batdongsan.com.vn']

    def start_requests(self):

        self.driver = webdriver.Chrome(
            'C:/Users/WW/Downloads/chromedriver_win32 (1)/chromedriver.exe')
        self.driver.get('https://duan.batdongsan.com.vn/du-an-bat-dong-san')

        sel = Selector(text=self.driver.page_source)
        path = sel.xpath(
            "//a[@class='re__clearfix']/@href").extract()

        for path1 in path:
            url = 'https://duan.batdongsan.com.vn' + path1
            driver.get(url)

        # # overview = driver.find_element(
        # #     By.XPATH, "//div[@class='re__project-main-number re__clearfix']")
            title = "No title"
            size = "No size"
            location = "No location"
            Number_of_apartments = "No number of apartments"
            Court_number = "No Court number"
            Investor = "No investor"
            Juridical = 'Juridical'
            try:
                # for detail in overview:
                title = driver.find_element(
                    By.XPATH, "//h1[@class='re__project-name']").text
            except:
                pass
            try:
                # for detail in overview:
                location = driver.find_element(
                    By.XPATH, "//div[@class='re__project-address']").text
            except:
                pass

            try:
                # for detail in overview:
                size = driver.find_element(
                    By.XPATH, "//label[contains(text(), 'Diện tích')]/parent::div/span").text
            except:
                pass

            try:
                # for detail in overview:
                Number_of_apartments = driver.find_element(
                    By.XPATH, "//label[contains(text(), 'Số căn hộ')]/parent::div/span").text
            except:
                pass
            try:
                # for detail in overview:
                Court_number = driver.find_element(
                    By.XPATH, "//label[contains(text(), 'Số tòa')]/parent::div/span").text
            except:
                pass
            try:
                # for detail in overview:
                Investor = driver.find_element(
                    By.XPATH, "//label[contains(text(), 'Chủ đầu tư')]/parent::div/span/a").text
            except:
                pass
            try:
                # for detail in overview:
                Juridical = driver.find_element(
                    By.XPATH, "//label[contains(text(), 'Pháp lý')]/parent::div/span").text
            except:
                pass

            write_json({
                "Tên Dự án": title,
                "Diện tích": size,
                "Vị trí": location,
                "Số căn hộ": Number_of_apartments,
                "Số tòa": Court_number,
                "Pháp lý": Juridical,
                "Chủ đầu tư": Investor,
                "Url": url
            })

        while True:
            try:
                next_page = self.driver.find_element(
                    "xpath", "//a[@class='re__pagination-icon']/i[@class='re__icon-chevron-right']")
                time.sleep(1)
                next_page.click()

                sel = Selector(text=self.driver.page_source)
                path = sel.xpath(
                    "//a[@class='re__clearfix']/@href").extract()

                for path1 in path:
                    url = 'https://duan.batdongsan.com.vn' + path1
                    driver.get(url)

            # # overview = driver.find_element(
            # #     By.XPATH, "//div[@class='re__project-main-number re__clearfix']")
                    title = "No title"
                    size = "No size"
                    location = "No location"
                    Number_of_apartments = "No number of apartments"
                    Court_number = "No Court number"
                    Investor = "No investor"
                    Juridical = 'Juridical'
                    try:
                        # for detail in overview:
                        title = driver.find_element(
                            By.XPATH, "//h1[@class='re__project-name']").text
                    except:
                        pass
                    try:
                        # for detail in overview:
                        location = driver.find_element(
                            By.XPATH, "//div[@class='re__project-address']").text
                    except:
                        pass

                    try:
                        # for detail in overview:
                        size = driver.find_element(
                            By.XPATH, "//label[contains(text(), 'Diện tích')]/parent::div/span").text
                    except:
                        pass

                    try:
                        # for detail in overview:
                        Number_of_apartments = driver.find_element(
                            By.XPATH, "//label[contains(text(), 'Số căn hộ')]/parent::div/span").text
                    except:
                        pass
                    try:
                        # for detail in overview:
                        Court_number = driver.find_element(
                            By.XPATH, "//label[contains(text(), 'Số tòa')]/parent::div/span").text
                    except:
                        pass
                    try:
                        # for detail in overview:
                        Investor = driver.find_element(
                            By.XPATH, "//label[contains(text(), 'Chủ đầu tư')]/parent::div/span/a").text
                    except:
                        pass
                    try:
                        # for detail in overview:
                        Juridical = driver.find_element(
                            By.XPATH, "//label[contains(text(), 'Pháp lý')]/parent::div/span").text
                    except:
                        pass

                    write_json({
                        "Tên Dự án": title,
                        "Diện tích": size,
                        "Vị trí": location,
                        "Số căn hộ": Number_of_apartments,
                        "Số tòa": Court_number,
                        "Pháp lý": Juridical,
                        "Chủ đầu tư": Investor,
                        "Url": url
                    })

            except NoSuchElementException:
                self.driver.quit()
                break


with open("data.json", "w", encoding='utf8') as f:
    json.dump([], f, ensure_ascii=False)


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+', encoding='utf8') as file:
        file_data = json.load(file)
        file_data.append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4, ensure_ascii=False)
