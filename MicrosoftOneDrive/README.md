The following recipes are available for Intel Macs:

* MicrosoftOneDrive.download
* MicrosoftOneDrive.install
* MicrosoftOneDrive.munki
* MicrosoftOneDrive.pkg
* MicrosoftOneDrive.jss (available in the **JSS** directory of the main recipe repo's directory.)

The following recipes are available for Apple Silicon Macs:

* MicrosoftOneDriveAppleSilicon.download
* MicrosoftOneDriveAppleSilicon.install
* MicrosoftOneDriveAppleSilicon.pkg

The following recipes are available for Intel and Apple Silicon Macs:

* MicrosoftOneDriveUniversal.download
* MicrosoftOneDriveUniversal.install
* MicrosoftOneDriveUniversal.pkg

The **MicrosoftOneDrive** recipes will download the latest version of Microsoft's OneDrive installer for Intel Macs. These are the original recipes and are being left in place unaltered to avoid disrupting anyone's existing workflows.

The **MicrosoftOneDriveAppleSilicon** recipes will download the latest version of Microsoft's OneDrive installer for Apple Silicon Macs.

The **MicrosoftOneDriveUniversal** recipes will download the latest version of Microsoft's OneDrive installer for both Apple Silicon and Intel Macs. The **MicrosoftOneDriveUniversal.pkg** recipe will build an installer package which detects what kind of processor a Mac has (Intel or Apple Silicon) and installs the correct OneDrive desktop software for the Mac's processor.