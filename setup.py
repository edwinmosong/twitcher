from distutils.core import setup

setup(name='twitcher',
      author='Edwin Mo',
      description='A simple TwitchTV API wrapper',
      author_email='edwin.mo@live.com',
      version='0.0.1',
      package_dir={'twitcher': 'twitcher'},
      packages=['twitcher'],
      install_requires=['requests',
                        'colorama']
      )