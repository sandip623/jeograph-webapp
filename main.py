from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase

azureconfig = AzureDBconfig().getconfig()
azuresqldb = AzureSqlDatabase(server=azureconfig["server"],
                              database=azureconfig["database"],
                              username=azureconfig["username"],
                              password=azureconfig["password"],
                              driver=azureconfig["driver"])
azuresqldb.connect()

azuresqldb.execute_query("SELECT * FROM [jeographserverauthsink].[listingstable1];")

azuresqldb.disconnect()