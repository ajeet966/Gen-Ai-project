from setuptools import find_packages, setup

print("Found packages:", find_packages())
setup(
    name='mcqgenrator',
    version='0.0.1',
    author='ajeet kumar',
    author_email='ajeetdadanpur@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)
