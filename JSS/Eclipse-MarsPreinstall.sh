#!/bin/bash
# Eclipse installs a link in its directory which interferes with a straight
# package installation. Therefore, we remove the old application prior to
# updating.

ECLIPSE_INSTALL='/Applications/eclipse'

if [[ -d $ECLIPSE_INSTALL ]]; then
	rm -rf $ECLIPSE_INSTALL
fi

exit 0