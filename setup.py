from setuptools import setup

with open('README.md') as file:
    long_description = file.read()

setup(name='python-domintell-ws',
      version='0.0.17',
      url='https://github.com/ZonderPit/python-domintell-ws',
      license='MIT',
      author='Zilvinas Binisevicius, ZonderPit',
      install_requires=['pyserial', 'websockets', 'voluptuous'],
      author_email='zilvinas@binis.me, zonderp@milkymail.org',
      description='Python Library with WebSockets support for the Domintell protocol',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['domintell', 'domintell.utils', 'domintell.connections', 'domintell.messages', 'domintell.modules'],
      platforms='any',
     )
