from setuptools import setup, find_packages

setup(
    name='pyqt-resize-frame',
    version='0.0.2',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt resize frame',
    url='https://github.com/yjg30737/pyqt-resize-frame.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)