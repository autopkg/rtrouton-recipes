#!/usr/bin/env python

from __future__ import absolute_import

import re
from xml.dom.minidom import parseString
from xml.parsers.expat import ExpatError

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from autopkglib import URLGetter, ProcessorError

__all__ = ["VMwareGuestToolsURLProvider"]

FUSION_URL_BASE = "https://softwareupdate.vmware.com/cds/vmw-desktop/"
DARWIN_TOOLS_URL_APPEND = "core/com.vmware.fusion.zip.tar"
DEFAULT_VERSION_SERIES = "11.5.0"


class VMwareGuestToolsURLProvider(URLGetter):
    """Provides URL to the latest Darwin ISO of the VMware Fusion tools."""

    input_variables = {
        "VERSION_SERIES": {
            "required": False,
            "description": (
                "Version of VMware Fusion to target tools of. E.g. "
                '"8.0.0". Defaults to "8.0.0"'
            ),
        }
    }
    output_variables = {
        "url": {"description": "URL to the latest VMware Guest Tools download"}
    }

    def get_url(self, version_series):
        """Download the metadata from the base URL."""
        fusion_url = urljoin(FUSION_URL_BASE, "fusion.xml")
        self.output("Base URL: {}".format(fusion_url), verbose_level=2)
        fusion_xml = self.download(fusion_url, text=True)

        build_re = re.compile(r"^fusion\/([\d\.]+)\/(\d+)\/")

        last_build_no = 0
        last_url_part = None

        try:
            fusion_feed = parseString(fusion_xml)
        except ExpatError:
            raise ProcessorError(
                "Unable to read XML data. The download was likely not XML."
            )

        for i in fusion_feed.getElementsByTagName("metadata"):
            productId = i.getElementsByTagName("productId")[0].firstChild.nodeValue
            version = i.getElementsByTagName("version")[0].firstChild.nodeValue
            url = i.getElementsByTagName("url")[0].firstChild.nodeValue

            if productId == "fusion" and version == version_series:

                match = build_re.search(url)

                if match:
                    build_ver = match.group(1)
                    build_no = int(match.group(2))
                    url_part = match.group(0)
                    self.output(
                        "Match results: "
                        "build_ver: {}, build_no: {}, url_part: {}".format(
                            build_ver, build_no, url_part
                        ),
                        verbose_level=2,
                    )

                    if build_no > last_build_no:
                        last_build_no = build_no
                        last_url_part = url_part

        if last_url_part:
            return urljoin(FUSION_URL_BASE, last_url_part + DARWIN_TOOLS_URL_APPEND)
        else:
            raise ProcessorError("Could not find suitable version/build")

    def main(self):
        version_series = self.env.get("VERSION_SERIES", DEFAULT_VERSION_SERIES)

        self.env["url"] = self.get_url(version_series)
        self.output("URL %s" % self.env["url"])
