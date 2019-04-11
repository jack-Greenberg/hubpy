from setuptools import setup

setup(
    name='hubpy',
    version='0.1',
    py_modules=['hubpy'],
    install_requires=[
        'Click', 'PyGithub',
    ],
    entry_points='''
        [console_scripts]
        hubpy=hubpy:hubpy
    ''',
)
