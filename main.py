import pandas as pd
from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase, stored_procs
from gcp_bindings import ApiServiceKeys

azureconfig = AzureDBconfig().getconfig()
azuresqldb = AzureSqlDatabase(server=azureconfig["server"],
                              database=azureconfig["database"],
                              username=azureconfig["username"],
                              password=azureconfig["password"],
                              driver=azureconfig["driver"])
azuresqldb.connect()
rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByLocation"])
azuresqldb.disconnect()
data = [tuple(row) for row in rows]
df = pd.DataFrame(data, columns=columns)

print(df)