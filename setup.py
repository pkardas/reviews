from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt") as file:
        return [package.strip() for package in file.readlines() if not package.startswith("git")]


setup(
    name="reviews",
    version="1.0.0",
    description="Download reviews",
    author="Piotr Kardaś",
    author_email="pkardas.it@gmail.com",
    url="https://github.com/pkardas/reviews",
    packages=find_packages(exclude=["tests", "scripts"]),
    install_requires=requirements(),
    package_data={"reviews": ["py.typed"]},
)