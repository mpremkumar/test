from setuptools import setup, find_packages

 

setup(

    name         = 'project',

    version      = '1.0',

    packages     = find_packages(),

    scripts      = ['bin/financials.py'],

    entry_points = {'scrapy': ['settings = sc_scripts_demo.settings']},
)