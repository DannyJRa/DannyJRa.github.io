Source: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04#step-5-setting-up-server-blocks-(recommended)




Create the directory for example.com as follows, using the -p flag to create any necessary parent directories:

sudo mkdir -p /var/www/test/html
Next, assign ownership of the directory with the $USER environment variable:

sudo chown -R $USER:$USER /var/www/test/html
The permissions of your web roots should be correct if you haven't modified your umask value, but you can make sure by typing:

sudo chmod -R 755 /var/www/test
Next, create a sample index.html page using nano or your favorite editor:

nano /var/www/test/html/index.html
Inside, add the following sample HTML:

/var/www/test/html/index.html
<html>
    <head>
        <title>Welcome to Example.com!</title>
    </head>
    <body>
        <h1>Success!  The example.com server block is working!</h1>
    </body>
</html>
Save and close the file when you are finished.

In order for Nginx to serve this content, it's necessary to create a server block with the correct directives. Instead of modifying the default configuration file directly, let’s make a new one at /etc/nginx/sites-available/example.com:

sudo nano /etc/nginx/sites-available/test
Paste in the following configuration block, which is similar to the default, but updated for our new directory and domain name:

/etc/nginx/sites-available/example.com
server {
        listen 80;
        listen [::]:80;

        root /var/www/example.com/html;
        index index.html index.htm index.nginx-debian.html;

        server_name example.com www.example.com;

        location / {
                try_files $uri $uri/ =404;
        }
}
Notice that we’ve updated the root configuration to our new directory, and the server_name to our domain name.

Next, let's enable the file by creating a link from it to the sites-enabled directory, which Nginx reads from during startup:

sudo ln -s /etc/nginx/sites-available/test /etc/nginx/sites-enabled/
Two server blocks are now enabled and configured to respond to requests based on their listen and server_name directives (you can read more about how Nginx processes these directives here):

example.com: Will respond to requests for example.com and www.example.com.
default: Will respond to any requests on port 80 that do not match the other two blocks.
To avoid a possible hash bucket memory problem that can arise from adding additional server names, it is necessary to adjust a single value in the /etc/nginx/nginx.conf file. Open the file:

sudo nano /etc/nginx/nginx.conf
Find the server_names_hash_bucket_size directive and remove the # symbol to uncomment the line:

/etc/nginx/nginx.conf
...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
Next, test to make sure that there are no syntax errors in any of your Nginx files:

sudo nginx -t
Save and close the file when you are finished.

If there aren't any problems, restart Nginx to enable your changes:

sudo systemctl restart nginx
Nginx should now be serving your domain name. You can test this by navigating to http://test.raschadvisory.com, where you should see something like this:




# SSL
Source: https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
sudo nano /etc/nginx/sites-available/test

Step 4 — Obtaining an SSL Certificate
Certbot provides a variety of ways to obtain SSL certificates through plugins. The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary. To use this plugin, type the following:

sudo certbot --nginx -d test.raschadvisory.com


Now https is....


Step 5 — Verifying Certbot Auto-Renewal
Let's Encrypt's certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process. The certbot package we installed takes care of this for us by adding a renew script to /etc/cron.d. This script runs twice a day and will automatically renew any certificate that's within thirty days of expiration.

To test the renewal process, you can do a dry run with certbot:

sudo certbot renew --dry-run
If you see no errors, you're all set. When necessary, Certbot will renew your certificates and reload Nginx to pick up the changes. If the automated renewal process ever fails, Let’s Encrypt will send a message to the email you specified, warning you when your certificate is about to expire.




#Test2


sudo nano /etc/nginx/sites-available/airflow


# This is the nginx configuration before Certbot is run

server {
        listen 80 default_server;
        server_name airflow.raschadvisory.com;

        server_name _;

        root /var/www/html;

        location ~ /.well-known
        {
          allow all;
        }
}


sudo service nginx reload

sudo certbot --nginx

If all the above is true, then you can install the following repositories and packages:

sudo su
# Nginx as TLS terminator and reverse proxy for Airflow
apt install nginx
# Needed added repositories and packages for certbot
apt update
apt install software-properties-common -y
add-apt-repository ppa:certbot/certbot -y
apt update
apt upgrade
apt install python-certbot-nginx -y


Run once on a new machine to create a new dhparam.pem file:

sudo su
cd /etc/ssl/private
openssl dhparam -out dhparam.pem 4096
chmod o-rwx dhparam.pem


sudo nano /etc/nginx/nginx.conf


sudo service nginx reload
systemctl status nginx.service
journalctl -xe

sudo certbot --nginx



