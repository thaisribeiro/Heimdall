from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='heimdall_bank_validate',
    description='Python implementation for bank account validation.',
    version='0.0.14',
    url='https://github.com/thaisribeiro/heimdall',
    license='MIT License',
    author='Thais Ribeiro',
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    long_description_content_type="text/markdown",
    author_email='thaisribeirodn@gmail.com',
    keywords=['heimdall', 'bank', 'validate'],
    packages=find_packages(),
    python_requires=">=3"
)

if __name__ == '__main__':
    setup(**setup_args)
