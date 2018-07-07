import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='payment_card_text',
    version='0.0.1',
    author='Yngve Høiseth',
    author_email='yngve@hoiseth.net',
    description='Clean texts from payment card transactions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yhoiseth/payment_card_text',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ),
)
