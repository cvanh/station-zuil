# database
the database is contained in a docker compose file. This is to prevent vendor locking.


## setup

### localy
assuming you have docker and docker compose installed you can run the datase locally with:
```
docker compose up
```

### cloud
To run this container on azure you need to have setup an docker aci context for the resource group you want to use. 
you can do this by following [this guide](https://docs.docker.com/cloud/aci-integration/#sign-in-to-azure).

If you a docker aci context setup and [set that as your default context](https://docs.docker.com/cloud/aci-integration/#running-compose-applications) 
you can run the application with:
```
docker compose up```