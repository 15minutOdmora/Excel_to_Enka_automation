from EnkaUpload import OneUpload
from ExcelExtraction import ReadData
import json
import time


def col_to_index(col_str):
    """ FUNCTION:
        Returns the index of a column, where col is a string of letters """
    """ Convert base26 column string to number. """
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1
    return col_num - 1


def create_data_json():
    """ Main function """
    # initiate classes
    data = ReadData(0)
    data_dictionary = dict()

    n_rows, n_columns = data.get_size()
    for row_index in range(1, n_rows):
        tab = data.get_row(row_index)
        new_tab = []
        for element in tab:
            if element in ["//","/","-","_","?"]:
                new_tab.append("")
            elif element in ["o", "O","0.0"]:
                new_tab.append("0")
            else:
                new_tab.append(str(element))
        print(new_tab, str(tab[0]))
        data_dictionary[str(tab[0])] = new_tab

    with open('data.json', 'w') as fp:
        json.dump(data_dictionary, fp)


with open('data.json', 'r') as fp:
    data = json.load(fp)


def main(start=1, end=210):  #212-96-97-17
    """ Main function """
    en = OneUpload("https://irssv.1ka.si/")
    en.login("", "")
    en.select_survey("Storitve SV: OS in DP")
    en.click_on_data()
    en.enable_edit()
    time.sleep(2)
    en.click_on_sort()
    finished = 0
    did_not_find_in_excel = []
    # loop over all indexes from the website table
    for i in range(start, end):
        st_obcine = str(en.get_survey_community_id(i))
        en.click_on_edit_for_row(i)

        print(st_obcine, i)
        if st_obcine + ".0" in data.keys():
            en.click_on_edit_for_row(i)
            tab = data[st_obcine +".0"]
            print("opening...")

            en.ans_1(tab[col_to_index("B")])  # 1 vprasanje
            list1 = tab[col_to_index("C"):col_to_index("G") + 1]
            list2 = tab[col_to_index("H"):col_to_index("L") + 1]
            list3 = tab[col_to_index("M"):col_to_index("Q") + 1]
            list4 = tab[col_to_index("R"):col_to_index("V") + 1]
            list5 = tab[col_to_index("W"):col_to_index("AA") + 1]
            en.ans_2(list1, list2, list3, list4, list5)  # 2 vprasanje

            en.ans_3(tab[col_to_index("AB")])

            en.ans_4(tab[col_to_index("AC")],
                     tab[col_to_index("AD")],
                     tab[col_to_index("AE")],
                     tab[col_to_index("AF")],
                     tab[col_to_index("AG")],
                     tab[col_to_index("AH")],
                     tab[col_to_index("AI")],
                     tab[col_to_index("AJ")],
                     tab[col_to_index("AK")])

            en.ans_6(tab[col_to_index("AM")],
                     tab[col_to_index("AN")],
                     tab[col_to_index("AO")])

            print(tab)
            en.save_edit()
            finished += 1
            print("data writen...{} out of {}".format(finished, end))
        else:
            did_not_find_in_excel.append(st_obcine)

        print("going back. Didn't find in excel: {}".format(did_not_find_in_excel))
        en.go_back_to_previous_page()

    print("\nFinished")


# create_data_json()
main()

"""
# test
for key, tab in data.items():
    print(tab)
    print("----------------------------------------------")
    list1 = tab[col_to_index("C"):col_to_index("G") + 1]
    list2 = tab[col_to_index("H"):col_to_index("L") + 1]
    list3 = tab[col_to_index("M"):col_to_index("Q") + 1]
    list4 = tab[col_to_index("R"):col_to_index("V") + 1]
    list5 = tab[col_to_index("W"):col_to_index("AA") + 1]
    print(list1, list2, list3, list4, list5)
    print("______________________________________________")
"""

# prva vrstica Header
"""
['Prosimo, izberite občino, za katero boste izpolnjevali anketo:', 'Zanima nas, ali so v vaši občini oskrbovana stanovanja (najemna ali lastniška)?  Oskrbovana stanovanja so pravno-formalno organizirana kot posebna oblika\xa0institucionalnega varstva, v praksi pa so to stanovanja (bodisi najeta bodisi kupljena) z lastnim\xa0gospodinjstvom z organizirano podporo in pomočjo. Na ta način oskrbovana stanovanja ali\xa0nadomeščajo (model izbire) ali odlagajo (model stopnic) odhod v dom za starejše v\xa0institucionalno varstvo. ', 'Lokacija 1', 'Lokacija 2', 'Lokacija 3', 'Lokacija 4', 'Lokacija 5', 'Lokacija 1', 'Lokacija 2', 'Lokacija 3', 'Lokacija 4', 'Lokacija 5', 'Lokacija 1', 'Lokacija 2', 'Lokacija 3', 'Lokacija 4', 'Lokacija 5', 'Lokacija 1', 'Lokacija 2', 'Lokacija 3', 'Lokacija 4', 'Lokacija 5', 'Lokacija 1', 'Lokacija 2', 'Lokacija 3', 'Lokacija 4', 'Lokacija 5', 'Prosimo, navedite morebitne opombe k oskrbovanim stanovanjem:', 'Sredstva v letu 2019 (EUR):', '1. Višina sredstev, namenjenih za\xa0storitve institucionalnega varstva.\xa0Vrednost vpišite v desno polje =&gt,Prosimo, v polje spodaj vpišite podrobne podatke, ki ste jih sešteli pod to kategorijo:', 'Sredstva v letu 2019 (EUR):', 'Sredstva v letu 2019 (EUR):', 'Sredstva v letu 2019 (EUR):', 'Sredstva v letu 2019 (EUR):', 'Sredstva v letu 2019 (EUR):', 'Sredstva v letu 2019 (EUR):', '7. Druge\xa0aktivnosti oz. dejavnosti na področju varstva invalidov. Vrednost vpišite v desno polje =&gt,Prosimo, v polje spodaj vpišite podrobne podatke, ki ste jih sešteli pod to kategorijo:', '%', 'Vpišite:', 'Vpišite:', 'Vpišite:', 'V kolikor želite še kaj dodati, pojasniti oz. komentirati glede poročanih podatkov tako o pomoči na domu, o invalidskem varstvu ali o oskrbovanih stanovanjih, prosimo navedite: ']


"""
