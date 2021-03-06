from setuptools import setup, find_packages


def requirements():
    with open('requirements.txt') as f:
        return f.read().split('\n')


def version():
    with open('VERSION') as f:
        return f.read().strip()


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='contres',
    author='Mirko Mälicke',
    author_email='mirko.maelicke@kit.edu',
    license='GPL v3',
    install_requires=requirements(),
    version=version(),
    description='Continuous research command line interaface',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    scripts=['contres/contres'],
    include_package_data=True,
    zip_safe=False
)