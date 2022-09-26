#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import os

# ************************************************************************************
def my_function(my_name:str):
   #********************** Copie des fichiers ***********************
   my_cmd = f'cp ~/fet-results/timetables/{my_date}-single/{my_date}_{my_name}_days_vertical.html ~/Downloads/planning_{my_name}.html'
   os.system(f'eval \'{my_cmd}\'')

   my_file = open(f'/home/laid/Downloads/planning_{my_name}.html', 'r')

   my_table =[]
   for my_line in my_file.readlines():
      my_table.append(my_line)

   my_file.close()

   i = 0
   for my_item in my_table:
      if 'stylesheet' in my_item:
         del my_table[i]
         my_table.insert(i, '    <link rel="stylesheet" media="all" href="planning.css" type="text/css" />')
         break
      i += 1

   for my_item in my_table:
      if '<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="fr">' in my_item:
         del my_table[i]
         my_table.insert(i, '<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="ar" dir="rtl">')
         break
      i += 1

   i = 0
   for my_item in my_table:
      i += 1

      if 'retour' in my_item:
         my_table[i - 1] = '    <p class="back"><a href="#top">السيد مدير المتوسطة</a></p>'

      if 'Dim' in my_item or 'Lun' in my_item or 'Mar' in my_item  or 'Mer' in my_item or 'Jeu' in my_item:
         del my_table[i - 1]
         del my_table[i - 2]
         del my_table[i - 3]
         my_table.insert(i - 3, '           <td>***</td>' + '\n')

      if f'colspan="4"' in my_item:
         my_string = str(my_item)
         my_item = my_string.replace(f'colspan="4"', f'colspan="9"')
         del my_table[i - 1]
         my_table.insert(i - 1, my_item)

      if '11:00--12:00' in my_item:
         if '----' in my_table[i]:
            continue
         else:
            z = i
            for j in range(j_max):
               my_table.insert(z + j, my_list[j] + '\n')
            continue

   my_file = open(f'/home/laid/Downloads/planning_{my_name}.html', 'w')

   for my_item in my_table:
      my_file.write(my_item)

   my_file.close()

   # ************** html to pdf  *************
   #my_cmd = f'html2pdf -B 0 -L 10 -R 10 -T 10 -O Landscape ~/Downloads/planning_{my_name}.html ~/Downloads/planning_{my_name}.pdf'
   my_cmd = f'html2pdf -B 0 -L 10 -R 10 -T 10 -O Landscape ~/Downloads/planning_{my_name}.html ~/Downloads/{my_date}_planning_{my_name}.pdf'
   os.system(f'eval \'{my_cmd}\'')

   #my_cmd=f'pdftk Downloads/planning_{my_name}.pdf output Downloads/{my_date}_planning_{my_name}.pdf'
   #os.system(f'eval \'{my_cmd}\'')

# ************************************************************************************
# ************************************************************************************

try:
   my_date = str(sys.argv[1])
except:
   my_date = ''

my_list = ['          <th class="xAxis">----</th>']
my_list.append(f'          <th class="xAxis">13:30--14:30</th>')
my_list.append(f'          <th class="xAxis">14:30--15:30</th>')
my_list.append(f'          <th class="xAxis">15:30--16:30</th>')
my_list.append(f'          <th class="xAxis">-X-</th>')

j_max = len(my_list)

my_function('groups')
my_function('teachers')
