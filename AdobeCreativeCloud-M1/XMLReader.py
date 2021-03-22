#!/usr/bin/python

from __future__ import absolute_import

import os.path
import xml.etree.cElementTree as ET

from autopkglib import Processor, ProcessorError

__all__ = ['XMLReader']


class XMLReader(Processor):
    input_variables = {
        "xml_path": {
            "required": True,
            "description": "Path to an XML file to be read.",
        },
        "elements": {
            "required": True,
            "description": "Array of dictionaries that defines what elements to search for.",
        },
    }
    output_variables = {
        "xml_reader_output_variables": {
            "description": "Output variables per 'elements' supplied as input."
        },
    }

    def main(self):
        elements = self.env['elements']

        path = os.path.normpath(self.env['xml_path'])
        if not os.path.exists(path):
            raise ProcessorError("Path '%s' does not exist!" % path)

        self.output('Reading: %s' % path)
        tree = ET.parse(path)

        root = tree.getroot()

        self.env["xml_reader_output_variables"] = {}

        for query in elements:
            if not 'xpath' in query:
                raise ProcessorError("Query key 'xpath' is missing!")

            xpath = query['xpath']
            try:
                element = root.findall(xpath)[0]
            except IndexError:
                raise ProcessorError("XPath '%s' could not be found in XML file %s!"
                                     % (xpath, path))

            if 'attributes' in query:
                attributes = query['attributes']
                for key, val in attributes.items():
                    self.env[val] = element.get(key)
                    if self.env[val] is None:
                        raise ProcessorError(
                            "Could not find attribute named '%s' at XPath '%s'!"
                            % (key, xpath))
                    self.output("Assigning value of '%s' to output variable '%s'"
                                % (self.env[val], val))
                    self.env["xml_reader_output_variables"][val] = (self.env[val])

            if 'text' in query:
                var = query['text']
                self.env[var] = element.text
                if self.env[var] is None:
                    raise ProcessorError("No text found at XPath '%s'!"
                                         % xpath)
                self.output("Assigning value of '%s' to output variable '%s'"
                            % (self.env[var], var))


if __name__ == '__main__':
    PROCESSOR = XMLReader()
    PROCESSOR.execute_shell()