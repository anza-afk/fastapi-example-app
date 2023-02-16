from setuptools import setup

setup(
    name='app-example',
    version='0.0.1',
    author='Anatoly Zapravaov',
    author_email='zapokami@yandex.ru',
    description='Fastapi app',
    insall_requires=[
        'fastapi==0.92.0',
        'uvicorn==0.20.0',
        'SQLAlchemy==2.0.3',
        'pytest==7.2.1',
        'requests==2.28.2',
    ],
    scripts=['app/main.py']
)