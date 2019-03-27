#%%
import nipyapi



#%%
nipyapi.config.nifi_config.host = 'http://0.0.0.0:8080/nifi-api'
nipyapi.config.registry_config.host = 'http://0.0.0.0:18080/nifi-registry-api'


#%%

id=nipyapi.canvas.get_root_pg_id()
print(id)

#%%
print(nipyapi.templates.list_all_templates())


List all process groups:
#%%
nipyapi.canvas.list_all_process_groups()



#%%
nipyapi.canvas.get_flow(pg_id='f69da007-f2f5-3913-e8fa-2b0a967fcd2e')


#%%
nipyapi.canvas.list_all_process_groups(pg_id='root')



tail -f log/nifi-app.log | grep b3a7e890-0168-1000-8e1d-331981e02a37 >> ExecuteScript.log


Using REst API
curl 'http://0.0.0.0:8080/nifi-api/flow/processors/b5465d9c-0168-1000-2e3d-2e82cb2778e0/status/history'