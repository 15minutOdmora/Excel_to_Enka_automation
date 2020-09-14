import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class OneUpload:
    def __init__(self, website_url=None):
        self.current_directory = os.getcwd()
        self.driver_path = self.current_directory + '\\' + "Drivers"
        self.website_url = website_url
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

        self.location_check = True
        self.trenutna_obcina = ""

        driver_list = os.listdir(self.driver_path)
        if len(driver_list) == 1:
            self.driver_path += '\\' + driver_list[0]
        else:
            print("There is no driver installed or there are too many installed in " +
                  "{} \n".format(self.driver_path) +
                  "please install the correct version of chrome driver to said path.")
        try:
            self.driver = webdriver.Chrome(self.driver_path, options=self.chrome_options)
        except:
            print("Driver Error")
            raise

        try:
            self.driver.get(self.website_url)
        except:
            print("URL Error")
            raise

    def login(self, username, password):
        """ METHOD:
            Log into the page."""
        search_email = self.driver.find_element_by_id("em")
        search_email.send_keys(username)
        time.sleep(0.5)
        search_password = self.driver.find_element_by_name("pass")
        search_password.send_keys(password)
        time.sleep(0.5)
        search_password.send_keys(Keys.RETURN)

    def select_survey(self, link_text):
        """METHOD:
            Clicks on the survey link """
        self.driver.find_element_by_link_text(link_text).click()

    def click_on_data(self):
        """METHOD:
            Clicks on Podatki button """
        self.driver.find_element_by_xpath('//*[@id="firstNavigation"]/ol[1]/li[10]/a/div').click()

    def enable_edit(self):
        """METHOD:
            Clicks on Urejanje checkbox """
        self.driver.find_element_by_id("dataIcons_edit").click()

    def get_survey_answered_value(self, index):
        """FUNCTION:
            Returns the value of td=9 of certain row (2 or 1), odgovorjeno ali ne """
        return self.driver.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr[{}]/td[9]'.format(index))[0].text

    def get_survey_community_id(self, index):
        """FUNCTION:
            Returns the value of the community id, td=8, id občine """
        data = self.driver.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr[{}]/td[8]'.format(index))[0].text
        self.trenutna_obcina = data
        return data

    def click_on_edit_for_row(self, index):
        """METHOD:
            Clicks on the edit button of the row, uredi vrstico """
        try:
            self.driver.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr[{}]/td[5]'.format(index))[0].click()
        except:
            print("Could not click on edit line")

    def go_back_to_previous_page(self):
        """METHOD:
            Goes one step back, to previous page, puscica nazaj """
        self.driver.execute_script("window.history.go(-2)")

    # Sklop vpisovanja podatkov za posamezno občino
    def ans_1(self, input):
        """ FUNCTION(This should be always run before ans_2):
            Checks the Da or No option, depending on input 1 = Da -> True, 2 = Ne -> False """
        if input == 1:
            self.driver.find_element_by_id("spremenljivka_9985122_vrednost_10029277").click()
        elif input == 2:
            self.driver.find_element_by_id("spremenljivka_9985122_vrednost_10029278").click()


    def ans_2(self, list1, list2, list3, list4, list5):
        """ METHOD(elements of list that are equal to '' are skipped through):
            Inputs the location fields where list1-5 are lenght 5 lists wich answer the rows """
        print("going through answer2")
        if self.location_check:
            print("list1", list1)
            # list1 1 vrstica
            counter = 0
            for element in list1:
                print(element, "element")
                counter += 1
                self.driver.find_element_by_id("vrednost_10029279_grid_{}".format(counter)).clear()
                if element != '':
                    self.driver.find_element_by_id("vrednost_10029279_grid_{}".format(counter)).send_keys(element)
            # list2 2 vrstica
            counter = 0
            for element in list2:
                counter += 1
                if element != '':
                    self.driver.find_element_by_id("vrednost_10029283_grid_{}".format(counter)).clear()
                    self.driver.find_element_by_id("vrednost_10029283_grid_{}".format(counter)).send_keys(element)
            # list3 3 vrstica
            counter = 0
            for element in list3:
                counter += 1
                if element != '':
                    self.driver.find_element_by_id("vrednost_10029280_grid_{}".format(counter)).clear()
                    self.driver.find_element_by_id("vrednost_10029280_grid_{}".format(counter)).send_keys(element)
            # list4 4 vrstica
            counter = 0
            for element in list4:
                counter += 1
                if element != '':
                    self.driver.find_element_by_id("vrednost_10029281_grid_{}".format(counter)).clear()
                    self.driver.find_element_by_id("vrednost_10029281_grid_{}".format(counter)).send_keys(element)
            # list5 5 vrstica
            counter = 0
            for element in list5:
                counter += 1
                if element != '':
                    self.driver.find_element_by_id("vrednost_10029282_grid_{}".format(counter)).clear()
                    self.driver.find_element_by_id("vrednost_10029282_grid_{}".format(counter)).send_keys(element)
        else:
            print("{}... Variable self.location_check was False".format(self.trenutna_obcina))

    def ans_3(self, input):
        """ METHOD:
            Anwsers the question 3 """
        if input != '':
            self.driver.find_element_by_id("spremenljivka_9985124_vrednost_1").clear()
            self.driver.find_element_by_id("spremenljivka_9985124_vrednost_1").send_keys(input)
        else:
            print("{}... ans_3 Input was empty string".format(self.trenutna_obcina))

    def ans_4(self, ans1, ans1_v, ans2, ans3, ans4, ans5, ans6, ans7, ans7_v):
        """ METHOD:
                Anwsers the question 4 """
        # ans1
        if ans1 != '':
            self.driver.find_element_by_id("vrednost_10029290_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029290_grid_1").send_keys(str(ans1))
        if ans1_v != '':
            self.driver.find_element_by_name("textfield_10029290").clear()
            self.driver.find_element_by_name("textfield_10029290").send_keys(str(ans1_v))

        # ans 2
        if ans2 != '':
            self.driver.find_element_by_id("vrednost_10029285_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029285_grid_1").click()
            self.driver.find_element_by_id("vrednost_10029285_grid_1").send_keys(str(ans2))

        # ans 3
        if ans3 != '':
            self.driver.find_element_by_id("vrednost_10029286_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029286_grid_1").send_keys(str(ans3))

        # ans 4
        if ans4 != '':
            self.driver.find_element_by_id("vrednost_10029287_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029287_grid_1").send_keys(str(ans4))

        # ans 5
        if ans5 != '':
            self.driver.find_element_by_id("vrednost_10029288_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029288_grid_1").send_keys(str(ans5))

        # ans 6
        if ans6 != '':
            self.driver.find_element_by_id("vrednost_10029289_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029289_grid_1").send_keys(str(ans6))

        # ans7
        if ans7 != '':
            self.driver.find_element_by_id("vrednost_10029291_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029291_grid_1").send_keys(str(ans7))
        if ans7_v != '':
            self.driver.find_element_by_name("textfield_10029291").clear()
            self.driver.find_element_by_name("textfield_10029291").send_keys(str(ans7_v))

    def ans_6(self, ans1, ans2, ans3):
        """ METHOD:
                Anwsers the question 4 """
        # ans1
        if ans1 != '':
            self.driver.find_element_by_id("vrednost_10029293_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029293_grid_1").send_keys(ans1)

        # ans2
        if ans2 != '':
            self.driver.find_element_by_id("vrednost_10029294_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029294_grid_1").send_keys(ans2)

        # ans3
        if ans3 != '':
            self.driver.find_element_by_id("vrednost_10029295_grid_1").clear()
            self.driver.find_element_by_id("vrednost_10029295_grid_1").send_keys(ans3)

    def save_edit(self):
        """ Clicks on the save button """
        self.driver.find_element_by_xpath('//*[@id="vnos"]/span[1]/div/a').click()

    def click_on_sort(self):
        """ clicks on the sorting of columns"""
        self.driver.find_element_by_xpath('//*[@id="dataTable"]/thead/tr[3]/th[4]').click()



"""
we = OneUpload("https://irssv.1ka.si/")
time.sleep(0.5)
we.login("verena.radin@gmail.com", "grbe1ilegalno")
time.sleep(0.5)
we.select_survey("Storitve SV: OS in DP")
time.sleep(0.5)
we.click_on_data()
time.sleep(0.5)
we.enable_edit()
time.sleep(2)

# do 212, ub 211 samo zadnjega ne steje for loop
for i in range(1, 2):
    print(we.get_survey_community_id(i), we.get_survey_answered_value(i))
    we.click_on_edit_for_row(i)
    time.sleep(5)
    we.ans_1(1)
    time.sleep(0.5)
    we.ans_2(["neki1", "neki2", "neki3", "neki4", "neki5"],
             ["neki1", "", "neki3", "neki4", "neki5"],
             ["neki1", "neki2", "", "neki4", "neki5"],
             ["neki1", "neki2", "neki3", "", "neki5"],
             ["", "", "", "", ""])
    time.sleep(0.5)
    we.ans_3("testiram")
    time.sleep(0.5)
    we.ans_4("1","test","11","12","13","14","15","2","test")
    time.sleep(0.5)
    we.ans_6("test","test","test")
    time.sleep(100)
    we.go_back_to_previous_page()
"""

"""
id občine gre od tr=1 do tr=211  za td8
//*[@id="dataTable"]/tbody/tr[1]/td[8]
//*[@id="dataTable"]/tbody/tr[3]/td[8]
//*[@id="dataTable"]/tbody/tr[4]/td[8]
//*[@id="dataTable"]/tbody/tr[5]/td[8]

Št. odg=2 neodg=1: gre od tr1 do tr211  za td9
//*[@id="dataTable"]/tbody/tr[1]/td[9]
//*[@id="dataTable"]/tbody/tr[211]/td[9]

Edit button for row tr=1 do tr=211 za td5

ans_1
<input type="radio" name="vrednost_9985122" id="spremenljivka_9985122_vrednost_10029277" value="10029277" data-calculation="1" onclick="checkChecked(this); checkBranching();  setCheckedClass(this, '1');">
<input type="radio" name="vrednost_9985122" id="spremenljivka_9985122_vrednost_10029278" value="10029278" checked="" data-calculation="2" onclick="checkChecked(this); checkBranching();  setCheckedClass(this, '1');">

ans_2
<textarea class="width_80" rows="2" name="vrednost_10029279_grid_1" id="vrednost_10029279_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>
<textarea class="width_80" rows="2" name="vrednost_10029283_grid_1" id="vrednost_10029283_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>
<textarea class="width_80" rows="2" name="vrednost_10029280_grid_1" id="vrednost_10029280_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>
<textarea class="width_80" rows="2" name="vrednost_10029281_grid_1" id="vrednost_10029281_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>
<textarea class="width_80" rows="2" name="vrednost_10029282_grid_1" id="vrednost_10029282_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>

ans_3
<textarea name="vrednost_9985124_kos_10029284" id="spremenljivka_9985124_vrednost_1" rows="3" class="width_60" onkeyup="checkBranching();"></textarea>
<textarea name="vrednost_9985124_kos_10029284" id="spremenljivka_9985124_vrednost_1" rows="3" class="width_60" onkeyup="checkBranching();"></textarea>

ans_4
<input type="text" class="width_150" name="vrednost_10029290_grid_1" id="vrednost_10029290_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">
<textarea name="textfield_10029290" rows="5" style=" width:60%;"></textarea>

<input type="text" class="width_150" name="vrednost_10029285_grid_1" id="vrednost_10029285_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<input type="text" class="width_150" name="vrednost_10029286_grid_1" id="vrednost_10029286_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<input type="text" class="width_150" name="vrednost_10029287_grid_1" id="vrednost_10029287_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<input type="text" class="width_150" name="vrednost_10029288_grid_1" id="vrednost_10029288_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<input type="text" class="width_150" name="vrednost_10029289_grid_1" id="vrednost_10029289_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<input type="text" class="width_150" name="vrednost_10029291_grid_1" id="vrednost_10029291_grid_1" value="" data-calculation="1" onkeypress="checkNumber(this, 10, 3);" onkeyup="checkNumber(this, 10, 3); checkBranching();">

<textarea name="textfield_10029291" rows="5" style=" width:60%;"></textarea>

ans_6 
<textarea class="width_80" rows="1" name="vrednost_10029293_grid_1" id="vrednost_10029293_grid_1" data-calculation="1" onkeyup="checkBranching();"></textarea>



"""





