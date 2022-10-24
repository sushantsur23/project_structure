from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below as per your requirements -
REPO_NAME = "Food Recommender System"
AUTHOR_USER_NAME = "SUSHANT SUR"
SRC_REPO = "food_src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="SUSHANT SUR",
    description="Package for Food recommendation system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sushantsur23/Food-Recommender-System",
    author_email="sushant.sur23@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)


