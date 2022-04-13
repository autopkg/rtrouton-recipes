#!/usr/bin/env python

from __future__ import absolute_import

import re
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError
from distutils.version import LooseVersion

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from autopkglib import URLGetter, ProcessorError

__all__ = ["VMwareGuestToolsURLProvider"]

FUSION_URL_BASE = "https://softwareupdate.vmware.com/cds/vmw-desktop/"
DARWIN_TOOLS_URL_APPEND = "com.vmware.fusion.zip.tar"
DEFAULT_VERSION_SERIES = "12.0.0"


class VMwareGuestToolsURLProvider(URLGetter):
    """Provides URL to the latest Darwin ISO of the VMware Fusion tools."""

    input_variables = {
        "VERSION_SERIES": {
            "required": False,
            "description": (
                "Version of VMware Fusion to target tools of. E.g. "
                '"11.5.0". Defaults to {}'.format(DEFAULT_VERSION_SERIES)
            ),
        }
    }
    output_variables = {
        "url": {"description": "URL to the latest VMware Guest Tools download"},
        "version": {"description": "Version number of the VMware Guest Tools"},
    }

    def get_fusion_feed(self):
        """Parse the XML feed into a data structure."""
        fusion_url = urljoin(FUSION_URL_BASE, "fusion.xml")
        self.output("Base URL: {}".format(fusion_url), verbose_level=2)
        fusion_xml = self.download(fusion_url, text=True)
        return fusion_xml

    def find_all_versions(self, fusion_feed, version_series):
        """Find the highest version number in a minidom XML data structure.
        Return a dictionary of version numbers to URL suffixes."""
        build_re = re.compile(r"^fusion\/([\d\.]+)\/(\d+)\/")
        versions = {}
        for metadata in fusion_feed:
            version = metadata.find("version")
            url = metadata.find("url")
            if version_series == "latest" or version.text in version_series:
                # We actually want the URL, instead of the version itself
                self.output(
                    "Found version: {} with URL: {}".format(version.text, url.text),
                    verbose_level=4,
                )
                match = build_re.search(url.text)
                print(match.groups())
                if match.groups():
                    real_url = url.text.replace(
                        "metadata.xml.gz", DARWIN_TOOLS_URL_APPEND
                    )
                    versions[match.group(1)] = real_url
        if not versions:
            raise ProcessorError(
                "Could not find any versions for the "
                "major_version '{}'.".format(version_series)
            )
        return versions

    def find_highest_version(self, versions_dict):
        """Find the URL of the highest version in the versions dictionary."""
        return sorted(versions_dict.keys(), key=LooseVersion)[-1]

    def get_version_and_url(self, version_series):
        """Return the version and URL string for the Guest Tools."""
        fusion_xml = self.get_fusion_feed()
        self.output("Searching for version series {}".format(version_series))
        try:
            fusion_feed = ElementTree.fromstring(fusion_xml)
        except ExpatError:
            raise ProcessorError("Unable to parse XML data from string.")
        versions_dict = self.find_all_versions(fusion_feed, version_series)
        latest_version_key = self.find_highest_version(versions_dict)
        self.output(
            "Latest version URL suffix: {}".format(versions_dict[latest_version_key]),
            verbose_level=2,
        )
        full_url = urljoin(FUSION_URL_BASE, versions_dict[latest_version_key])

        if full_url:
            return (latest_version_key, full_url)
        else:
            raise ProcessorError("Could not find suitable version/build")

    def main(self):
        self.env["version"], self.env["url"] = self.get_version_and_url(
            self.env.get("VERSION_SERIES", DEFAULT_VERSION_SERIES)
        )
        self.output("URL: {}".format(self.env["url"]))
        self.output("Version: {}".format(self.env["version"]))
