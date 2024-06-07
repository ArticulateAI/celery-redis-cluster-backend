from setuptools import setup, find_packages

setup(
    name='celery-redis-cluster-backend',
    version='0.1.0',
    description="ArticulateAI Celery redis cluster backend",
    url='https://github.com/ArticulateAI/celery-redis-cluster-backend',
    author='ArticulateAI',
    author_email='kathyliu@articulateai.com',
    packages=find_packages(),
    zip_safe = True
)