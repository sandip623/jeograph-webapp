import pandas as pd
import gmaps 
from azure_bindings import AzureDBconfig
from azuresqldb import AzureSqlDatabase, stored_procs

azureconfig = AzureDBconfig().getconfig()
azuresqldb = AzureSqlDatabase(server=azureconfig["server"],
                              database=azureconfig["database"],
                              username=azureconfig["username"],
                              password=azureconfig["password"],
                              driver=azureconfig["driver"])
azuresqldb.connect()
rows, columns = azuresqldb.execute_query(stored_procs["getJobCountByCity"])
data = [tuple(row) for row in rows]
df = pd.DataFrame(data, columns=columns)
print(df)
azuresqldb.disconnect()
