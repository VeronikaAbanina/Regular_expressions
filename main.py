from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
import re

pattern_phone = r'(\+7|8)?\s*\(?(\d{3})\)?\s*?\-?(\d{3})[-\s]?(\d{2})[-\s]?(\d+)\s?(\(?\w{3}\.\)?\s*?\d{4})?'
substitution_phone = r'+7(\2)\3-\4-\5 \6'

contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page)
  format_page = re.sub(pattern_phone, substitution_phone, page_string)
  page_list = format_page.split(',')
  contacts_list_new.append(page_list)
#pprint(contacts_list_new)


pattern_name = r'(^[А-ЯЁа-яё]+)\s*\,?([А-ЯЁа-яё]+)\s*\,?([А-ЯЁа-яё]*)\,{1,10}'
substitution_name = r'\1,\2,\3, '

contacts_list_new2 = list()
for page in contacts_list_new:
  page_string = ','.join(page)
  format_page = re.sub(pattern_name, substitution_name, page_string)
  page_list = format_page.split(',')
  contacts_list_new2.append(page_list)
#pprint(contacts_list_new2)


# 3) объединить все дублирующиеся записи о человеке в одну.
phone_dict = {x[0]: x[1:] for x in contacts_list_new2}
pprint(phone_dict)



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)