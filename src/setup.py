import sys

from setuptools import setup, find_packages

version = '0.0.1'

requirements = [
    'setuptools',
    'netsight.async'
]

test_requirements = [
]

setup(
      # Metadata
      name='netsight.async_examples',
      version=version,
      description="Provides examples of netsight.async usage.",
      long_description='\n\n'.join([open(f).read() for f in [
                            "README.rst",
                            "HISTORY.rst",
                            'LICENSE.rst',
                             ]]),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
        ],
      keywords='Plone Zope Asynchronous Fork Process Task Browser View',
      author='Netsight Internet Solutions Limited',
      author_email='info@netsight.co.uk',
      maintainer='Richard Mitchell',
      maintainer_email='richard@netsight.co.uk',
      url='http://www.netsight.co.uk',
      license='3-clause BSD',
      
      # Distribution / build data
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = netsight.async
      """,
      
      # Dependencies
      install_requires=requirements,
      setup_requires=[],
      tests_require=test_requirements,
      extras_require={
        'test': test_requirements
      },
      )
