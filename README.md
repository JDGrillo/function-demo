This Azure Function is triggered by a new blob being added to a container in the storage account. The Function will process that blob, and convert it before saving it to another container in the same storage account.

## Prerequisites
Install Azure Functions Core Tools version 3.x, and Python 3.6 or later. See [Local development guide](https://docs.microsoft.com/azure/azure-functions/functions-develop-local) for details.

## Running the sample
1. Create a Resource Group in the Azure portal.
1. Create a new storage account in the Azure portal.
1. Create a new intial container in the storage account. This is where you will upload the intiial file.
1. Create a new final container in the storage account. This is where the processed file will be saved.

1. Create an App Service Plan to host your Function App.
1. Create a new Function App in the Azure portal. Make sure to select the same Resource Group and App Service Plan you created in the previous steps.

1. Navigate to a VS Code window clone of this repo on your local machine.