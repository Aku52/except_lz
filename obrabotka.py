import pandas as pd
import os.path


class Processing:

    def __init__(self,df):
        self.df = df
           
    def file_open (self,) :
        try:
           self.df = pd.read_csv('var2.csv')
           print(u' открыть файл')
        except IOError as e:
            print(u'Не удалось открыть файл')
        except NameError as e:
            print(u'Неверное имя файла')
           

       
'''  def load_dataframe(self):
        if os.path.isfile(self.file_path):
            self.dataframe = pd.read_csv(self.file_path)
            print("Данные успешно загружены:")
            print(self.dataframe.head())
        else:
            print("Файл не найден!") '''
   
       

        