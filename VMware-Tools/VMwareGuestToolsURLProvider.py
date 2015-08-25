#!/usr/bin/env python

import re
from xml.dom.minidom import parse, parseString
import urllib2

from autopkglib import Processor, ProcessorError

__all__ = ["VMwareGuestToolsURLProvider"]

FUSION_URL_BASE = 'http://softwareupdate.vmware.com/cds/vmw-desktop/'
DARWIN_TOOLS_URL_APPEND = 'packages/com.vmware.fusion.tools.darwin.zip.tar'
DEFAULT_VERSION_SERIES = '8.0.0'

class VMwareGuestToolsURLProvider(Processor):
	'''Provides URL to the latest Darwin ISO of the VMware Fusion tools.'''

	input_variables = {
		'VERSION_SERIES': {
			'required': False,
			'description': 'Version of VMware Fusion to target tools of. E.g. "8.0.0". Defaults to "8.0.0"',
			},
	}
	output_variables = {
		'url': {
			'description': 'URL to the latest SourceForge project download'
		}
	}

	def get_url(self, version_series):
		try:
			fusion_url = FUSION_URL_BASE + '/fusion.xml'
			f = urllib2.urlopen(fusion_url)
			fusion_xml = f.read()
			f.close()
		except BaseException as e:
			raise ProcessorError('Could not retrieve XML feed %s' % fusion_url)

		build_re = re.compile('^fusion\/([\d\.]+)\/(\d+)\/')

		last_build_no = 0
		last_url_part = None

		fusion_feed = parseString(fusion_xml)

		for i in  fusion_feed.getElementsByTagName('metadata'):
			productId = i.getElementsByTagName('productId')[0].firstChild.nodeValue
			version = i.getElementsByTagName('version')[0].firstChild.nodeValue
			url = i.getElementsByTagName('url')[0].firstChild.nodeValue

			if productId == 'fusion' and version == version_series:

				match = build_re.search(url)

				if match:
					build_ver = match.group(1)
					build_no = match.group(2)
					url_part = match.group(0)

					if build_no > last_build_no:
						last_build_no = build_no
						last_url_part = url_part

		if last_url_part:
			return FUSION_URL_BASE + last_url_part + DARWIN_TOOLS_URL_APPEND
		else:
			raise ProcessorError('Could not find suitable version/build')

	def main(self):
		version_series = self.env.get('VERSION_SERIES', DEFAULT_VERSION_SERIES)

		self.env['url'] = self.get_url(version_series)
		self.output('File URL %s' % self.env['url'])

