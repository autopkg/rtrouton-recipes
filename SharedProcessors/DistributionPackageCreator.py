#!/usr/local/autopkg/python
#
# Copyright 2010 Per Olofsson
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


import plistlib
import subprocess
import os

from autopkglib import Processor, ProcessorError


__all__ = ["DistributionPackageCreator"]


class DistributionPackageCreator(Processor):
    description = "Converts an existing component package to a distribution package using ProductBuild."
    input_variables = {
        "pkg_path": {
            "required": True,
            "description": "Path to the component package to be converted to a distribution package",
        },
    }
    output_variables = {
        "pkg_path": {"description": "Path to the distribution package."}
    }

    __doc__ = description

    def main(self):

        # Rename component package so that we can retain the original name for the distribution package.
        pkg_dir = os.path.dirname(self.env["pkg_path"])
        pkg_base_name = os.path.basename(self.env["pkg_path"])
        (pkg_name_no_extension, pkg_extension) = os.path.splitext(pkg_base_name)

        component_pkg_path = os.path.join(
            pkg_dir, pkg_name_no_extension + "-component" + pkg_extension
        )
        os.rename(self.env["pkg_path"], component_pkg_path)

        command_line_list = [
            "/usr/bin/productbuild",
            "--package",
            component_pkg_path,
            self.env["pkg_path"],
        ]

        print(command_line_list)

        # print command_line_list
        subprocess.call(command_line_list)


if __name__ == "__main__":
    processor = DistributionPackageCreator()
    processor.execute_shell()