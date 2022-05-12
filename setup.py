try:
    from setuptools import setup
except:
    from distutils.core import setup
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='toautosyspath',
    author='dragons',
    version='0.0.1',
    description='A python automatically adds the current project sys Path tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='521274311@qq.com',
    url='https://github.com/dragons96/autosyspath',
    packages=setuptools.find_packages(),
    install_requires= [
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
    ],
    zip_safe=True,
)