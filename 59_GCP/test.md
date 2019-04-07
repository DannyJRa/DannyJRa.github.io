Create security for Nifi Cluster
	Password to complicated

### Create SSH Tunnel to NiFi-Port
	BASH
		gcloud compute ssh instance3 \
		    --project workplacedanny \
		    --zone europe-west3-c \
		    -- -L 8090:localhost:8090 -L 8050:localhost:8050
	
Connect to GCP

Connect to SFTP
