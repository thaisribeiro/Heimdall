from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='heimdall-bank-validate',
    version='1.0.0',
    url='https://github.com/thaisribeiro/heimdall',
    license='MIT License',
    author='Thais Ribeiro',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='thaisribeirodn@gmail.com',
    keywords='Bank Validate, Validação de Dados Bancários',
    description=u'Python implementation for bank account validation',
    packages=['heimdall-bank-validate'],
    install_requires=['setuptools','nose','isort','coverage','flake8','wheel','pytest-cov','pytest-runner','pytest'])
