from selenium import webdriver
import time
from subprocess import PIPE, Popen
from selenium.webdriver.common.by import By
import username

class Gsb:

    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def giris(self):
        self.browser.get("https://wifi.gsb.gov.tr/login.html")
        time.sleep(2)
        username = self.browser.find_element(By.XPATH, '//*[@id="containerall"]/form/table/tbody/tr[1]/td[2]/input')
        password = self.browser.find_element(By.XPATH, '//*[@id="containerall"]/form/table/tbody/tr[2]/td[2]/input')
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(2)
        self.browser.find_element(By.XPATH, "//*[@id='containerall']/form/table/tbody/tr[3]/td/input").click()
        time.sleep(10)
        self.browser.close()


komut = 'NETSH WLAN SHOW INTERFACE | findstr /r "^....SSID"'
p = Popen(komut, shell=True, stderr=PIPE, stdout=PIPE)
(out, err) = p.communicate()
out = str(out)
wifi_adi = out[31:-5]


while wifi_adi == "GSBWIFI":
    a = Gsb(username.username, username.password)
    a.giris()
