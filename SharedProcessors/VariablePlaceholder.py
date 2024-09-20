#!/usr/local/autopkg/python
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

from autopkglib import Processor

__all__ = ["VariablePlaceholder"]


class VariablePlaceholder(Processor):
    """This processor performs no action, but serves as a place to set variables for use by AutoPkg recipes."""
    
    input_variables = {}
    output_variables = {}
    description = __doc__

    def main(self):
        return


if __name__ == "__main__":
    PROCESSOR = VariablePlaceholder()
    PROCESSOR.execute_shell()