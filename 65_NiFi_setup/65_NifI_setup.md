

## HTTPS/SSL Configuration

 https://mintopsblog.com/2017/11/01/apache-nifi-configuration/




```
cd NiFi
wget https://www-eu.apache.org/dist/nifi/1.9.1/nifi-toolkit-1.9.1-bin.tar.gz 

tar xvf nifi-toolkit-1.9.1-bin.tar.gz
```

```
cd nifi-toolkit-1.9.1/bin
sudo ./tls-toolkit.sh standalone -n '*.djr.local'
```


Move the * directory to a better readable name and also move the certificates created.

sudo mv *.mintopsblog.local star.mintopsblog.local
sudo mv nifi-* star.mintopsblog.local/


You should end up with the following folder structure:


sudo mv star.mintopsblog.local/* /NiFi/nifi/conf/

/NiFi/nifi-toolkit-1.9.1/bin$ cd star.mintopsblog.local

sudo mv /home/danny/NiFi/nifi-toolkit-1.9.1/bin/star.mintopsblog.local/* /home/danny/NiFi/nifi/conf/


sudo chown -R danny ~/NiFi

sudo nano Nifi/nifi/conf/nifi.properties