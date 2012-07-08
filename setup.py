try:
    from setuptools import setup
except:
    from distutils.core import setup

dependencies = [
            'PyYAML >= 3.10'
        ]

setup(name='pomolog'
      ,version='0.0.1'
      ,packages=['pomolog',]
      ,entry_points={
            'console_scripts':[
                    'pomolog = pomolog.cli:begin'
                ]
          }
      )
