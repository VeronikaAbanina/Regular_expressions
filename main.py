from pprint import pprint
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
import re

pattern_phone = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
substitution_phone = r'+7(\2)-\3-\4-\5 \6\7'

contacts_list_new = list()
for page in contacts_list:
  page_string = ','.join(page)
  format_page = re.sub(pattern_phone, substitution_phone, page_string)
  page_list = format_page.split(',')
  contacts_list_new.append(page_list)
#pprint(contacts_list_new)


pattern_name = r'(^[А-ЯЁа-яё]+)\s*\,?([А-ЯЁа-яё]+)\s*\,?([А-ЯЁа-яё]*)\,{1}'
substitution_name = r'\1,\2,\3, '

contacts_list_new2 = list()
for page in contacts_list_new:
  page_string = ','.join(page)
  format_page = re.sub(pattern_name, substitution_name, page_string)
  page_list = format_page.split(',')
  contacts_list_new2.append(page_list)
#pprint(contacts_list_new2)


phone_dict = {}
for x in contacts_list_new2:
  key = f"{x[0]} {x[1]}"
  if not phone_dict.get(key):
    phone_dict[key] = x
  else:
    phone_dict[key] = [i[0] if i[0] else i[1] for i in zip(phone_dict[key], x)]
#pprint(phone_dict)

t = list(phone_dict.items())
pprint(t)


# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(t)