from setuptools import setup

setup(name='ccalnoir',
      version='1.0.1',
      description='CCAL but with "No R".',
      url='https://github.com/edjuaro/ccal-noir',
      author='Edwin F. Juarez',
      author_email='ejuarez@ucsd.edu',
      license='Modified BSD',
      packages=['ccalnoir'],
      zip_safe=False,
      install_requires=[
            'numpy',
            'scipy',
            'pandas',
            'matplotlib',
            'statsmodels',
            'seaborn',
            'validators',
            ],
      )