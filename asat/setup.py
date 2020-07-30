from setuptools import setup

setup(name='asat',
      version='0.1',
      description='ASAT',
      url='https://github.com/atifghulamnabi/frAmework-clouD-bAsed-buG-predIctiOn',
      author='Anna Jancso',
      author_email='anna.jancso@uzh.ch',
      license='MIT',
      packages=['asat'],
      zip_safe=False,
      install_requires=['tqdm', 'matplotlib', 'toml', 'PyYAML']
      )
