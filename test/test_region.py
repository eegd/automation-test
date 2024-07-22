from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option(
    "prefs",
    {"profile.password_manager_enabled": False, "credentials_enable_service": False},
)


class Test:
    def setup(self):
        self.URL = "https://www.buyandship.com.tw/"
        self.driver = webdriver.Chrome(options=options)
        self.action = ActionChains(self.driver)
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()

    # 香港 - 正體中文
    def test_hong_kong_chinese_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[1]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "香港 - 繁體中文"

        self.tear_down()

    # 香港 - English
    def test_hong_kong_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[2]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Hong Kong - English"

        self.tear_down()

    # 澳門 - 正體中文
    def test_macao_chinese_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[3]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "澳門 - 繁體中文"

        self.tear_down()

    # 台灣 - 正體中文
    def test_taiwan_chinese_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[4]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "台灣 - 正體中文"

        self.tear_down()

    # 日本 - 日本語
    def test_japan_japanese_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[5]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "日本 - 日本語"

        self.tear_down()

    # 新加坡 - English
    def test_singapore_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[6]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Singapore - English"

        self.tear_down()

    # 馬來西亞 - English
    def test_malaysia_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[7]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Malaysia - English"

        self.tear_down()

    # 印度 - English
    def test_india_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[8]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "India - English"

        self.tear_down()

    # 阿聯酋 - English
    def test_uae_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[9]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "UAE - English"

        self.tear_down()

    # 澳洲 - English
    def test_australia_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[10]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Australia - English"

        self.tear_down()

    # 菲律賓 - English
    def test_philippine_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[11]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Philippines - English"

        self.tear_down()

    # 英國 - English
    def test_england_english_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[12]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "United Kingdom - English"

        self.tear_down()

    # 越南 - Tiếng Việt
    def test_vietnam_vietnamese_region(self):
        self.setup()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="html"]/body/aside/div[2]/div[2]/ul/a[13]/span[2]',
                )
            )
        )
        element.click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="bsHeader"]/div/div/div/div/span')
            )
        )
        assert element.text == "Vietnam - tiếng Việt"

        self.tear_down()
