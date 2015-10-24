Before using the **DbVisualizer** recipes, you will need to add Facebook's AutoPkg repo from GitHub. The reason for this is that the download recipe for **DbVisualizer** is available from there and referenced in the following recipe:

`DbVisualizer.pkg`

The `DbVisualizer.pkg` recipe is in turn referenced by these two other recipes:


`DbVisualizer.install`

`DbVisualizer.jss`


Facebook's AutoPkg repo is available from the following address:

[https://github.com/facebook/Recipes-for-AutoPkg](https://github.com/facebook/Recipes-for-AutoPkg)

To add this repo to AutoPkg, please run the following command:

`autopkg repo-add https://github.com/facebook/Recipes-for-AutoPkg`

