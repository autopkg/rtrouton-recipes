#!/bin/bash

# preinstall.sh
# Marc Thielemann, 2019/09/15

# redirect all output to /dev/null
exec >/dev/null 2>&1

helperPlistPath="$3/Library/LaunchDaemons/corp.sap.privileges.helper.plist"

/usr/bin/killall Privileges

# unload the launchd plist only if installing on the boot volume
if [[ "$3" = "/" ]]; then
	/bin/launchctl bootout system "$helperPlistPath"
fi

/bin/rm -rf "$helperPlistPath" \
            "$3/Library/PrivilegedHelperTools/corp.sap.privileges.helper" \
            "$3/Applications/Privileges.app"

exit 0