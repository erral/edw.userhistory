from setuptools import setup, find_packages
import os

version = open('version.txt').read()

setup(name='edw.userhistory',
      version=version,
      description="User login history",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='David Batranu',
      author_email='david.batranu@eaudeweb.ro',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['edw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
            'test': [
                'plone.app.testing',
                    ],
                        },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
