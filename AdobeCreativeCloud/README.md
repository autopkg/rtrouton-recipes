The following recipes are available for Intel Macs:

* AdobeCreativeCloudInstaller.download
* AdobeCreativeCloudInstaller.install
* AdobeCreativeCloudInstaller.pkg
* AdobeCreativeCloudInstaller.jss (available in the **JSS** directory of the main recipe repo's directory.)

The following recipes are available for Apple Silicon Macs:

* AdobeCreativeCloudInstallerAppleSilicon.download
* AdobeCreativeCloudInstallerAppleSilicon.install
* AdobeCreativeCloudInstallerAppleSilicon.pkg
* AdobeCreativeCloudInstallerAppleSilicon.jss (available in the **JSS** directory of the main recipe repo's directory.)

The following recipes are available for Intel and Apple Silicon Macs:

* AdobeCreativeCloudInstallerUniversal.download
* AdobeCreativeCloudInstallerUniversal.install
* AdobeCreativeCloudInstallerUniversal.pkg
* AdobeCreativeCloudInstallerUniversal.jss (available in the **JSS** directory of the main recipe repo's directory.)

The **AdobeCreativeCloudInstaller** recipes will download the latest version of Adobe's Creative Cloud Installer for Intel Macs. These are the original recipes and are being left in place unaltered to avoid disrupting anyone's existing workflows.

The **AdobeCreativeCloudInstallerAppleSilicon** recipes will download the latest version of Adobe's Creative Cloud Installer for Apple Silicon Macs.

The **AdobeCreativeCloudInstallerUniversal** recipes will download the latest version of Adobe's Creative Cloud Installer for both Apple Silicon and Intel Macs. The **AdobeCreativeCloudInstallerUniversal.pkg** recipe will build an installer package which detects what kind of processor a Mac has (Intel or Apple Silicon) and installs the correct Creative Cloud desktop software for the Mac's processor.

The `XMLReader` processor used by this recipe was written by Tyler Riti ([https://github.com/triti](https://github.com/triti)). The latest version of the processor is available from the following location:

[https://github.com/autopkg/triti-recipes/tree/master/SharedProcessors](https://github.com/triti)