#!/usr/bin/env python
#
# Copyright 2016 Allister Banks, lovingly based on work by Hannes Juutilainen
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

from __future__ import absolute_import

import xml.etree.ElementTree as ET

from autopkglib import Processor, ProcessorError, URLGetter

__all__ = ["OfficeSuiteSKULessVersionProvider"]

FEED_URL = "https://macadmins.software/latest.xml"


class OfficeSuiteSKULessVersionProvider(URLGetter):
    """Provides the version of the latest SKU-Less Office 2016 Suite release"""

    input_variables = {}
    output_variables = {
        "version": {
            "description": "Version of the latest SKU-Less Office 2016 Suite release.",
        },
    }
    description = __doc__

    def get_version(self, FEED_URL):
        """Parse the macadmins.software/versions.xml feed for the latest O365 version number"""
        try:
            xml = self.download(FEED_URL)
        except Exception as e:
            raise ProcessorError("Can't download %s: %s" % (FEED_URL, e))

        root = ET.fromstring(xml)
        latest = root.find("latest")
        for vers in root.iter("latest"):
            version = vers.find("o365").text
        return version

    def main(self):
        self.env["version"] = self.get_version(FEED_URL)
        self.output("Found Version Number %s" % self.env["version"])


if __name__ == "__main__":
    processor = OfficeSuiteSKULessVersionProvider()
    processor.execute_shell()
