This Azure Function is triggered by a new blob being added to a container in the storage account. The Function will process that blob, and convert it before saving it to another container in the same storage account.

## Prerequisites
Install Azure Functions Core Tools version 3.x, and Python 3.6 or later. See [Local development guide](https://docs.microsoft.com/azure/azure-functions/functions-develop-local) for details.

## Running the sample
1. Create a new storage account in the Azure portal.
1. Create a new intial container in the storage account.
1. Create a new final container in the storage account.

1. Create a new Function App in VS Code using the Azure Functions extension.
1. Create a new Blob Trigger Function in VS Code using the Azure Functions extension.

Follow the steps in getting_started.md to create a new Blob Trigger Function. When prompted for the path, enter the name of the initial container you created in step 2. When prompted for the language, select Python.