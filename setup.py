try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README') as file:
    long_description = file.read()

setup(name='betacode-flask-restful-swagger-2',
      version='0.37',
      url='https://github.com/swege/flask-restful-swagger-2.0',
      zip_safe=False,
      packages=['betacode_flask_restful_swagger_2'],
      package_data={
        'betacode_flask_restful_swagger_2': [
        ]
      },
      description='Extract swagger specs from your flask-restful project. Project based on flask-restful-swagger by Ran Tavory.',
      author='Soeren Wegener',
      license='MIT',
      long_description=long_description,
      install_requires=['Flask-RESTful>=0.2.12'],
      tests_require=['nose'],
      test_suite='nose.collector'
      )
