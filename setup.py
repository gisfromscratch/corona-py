# Copyright 2020 Jan Tschada
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="corona-py",
    version="0.1",
    scripts=["src"],
    author="Jan Tschada",
    author_email="gisfromscratch@live.de",
    description="Simple python module for accessing Coronavirus datasources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gisfromscratch/corona-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
     ],
 )