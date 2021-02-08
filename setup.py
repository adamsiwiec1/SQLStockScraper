from distutils.core import setup
import py2exe

# Choose all the files you want in exe

setup(name='StockScraper',
      version='1.0.0',
      description='This script updates my stock_db database in SQL with detailed, current stock data.',
      author='Adam Siwiec',
      author_email='adam2.siwiec@gmail.com',
      url='https://github.com/adamsiwiec1/SQLStockScraper',
      data_files=[('Stocks', ['db/config.py', 'db/sql.py', 'etc/smsAlert.py'])],
      console=['main.py'],
     )