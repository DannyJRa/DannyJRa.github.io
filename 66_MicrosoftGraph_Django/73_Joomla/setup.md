


nginx -v

sudo nano /etc/nginx/fastcgi_params

sudo apt-get install php7.2-fpm php7.2-common php7.2-mysql php7.2-xml php7.2-xmlrpc php7.2-curl php7.2-gd php7.2-imagick php7.2-cli php7.2-dev php7.2-imap php7.2-mbstring php7.2-opcache php7.2-soap php7.2-zip -y


php-fpm7.2 -v

php7.3-pgsql


## Joomla

Your website will be located in the home directory and have the following structure

Replace raschadvisory.com with your original domain name.

home
-- raschadvisory.com
---- logs
---- public
The public directory is your website’s root directory and logs directory for your error logs

Now we create these directories and set correct permissions

You need to SSH into your VM Instance and run these commands
```
mkdir -p raschadvisory.com/logs raschadvisory.com/public
sudo chmod -R 755 raschadvisory.com
```
## Setup Nginx for Joomla
Now create a new Nginx configuration for your website in the sites-available directory
```
sudo nano /etc/nginx/sites-available/raschadvisory.com
```
Copy and paste the following configuration, ensure that you change the server_name, error_log and root directives to match your domain name. Hit CTRL+X followed by Y to save the changes.


server {
    listen 80;
    listen [::]:80;

    server_name raschadvisory.com www.raschadvisory.com;

    error_log /home/danny/raschadvisory.com/logs/error.log;

    root /home/danny/raschadvisory.com/public/;
    index index.html index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
    }
}
To enable this newly created website configuration, symlink the file that you just created into the sites-enabled directory.
```
sudo ln -s /etc/nginx/sites-available/raschadvisory.com /etc/nginx/sites-enabled/raschadvisory.com
```
Check your configuration and restart Nginx for the changes to take effect
```
sudo nginx -t
sudo service nginx restart
```
Create SSL certificate and enable HTTP/2
HTTPS
HTTPS is a protocol for secure communication between a server (instance) and a client (web browser). Due to the introduction of Let’s Encrypt, which provides free SSL certificates, HTTPS are adopted by everyone and also provides trust to your audiences.

HTTP/2
HTTP/2 is the latest version of the HTTP protocol and can provide a significant improvement to the load time of your sites. There really is no reason not to enable HTTP/2, the only requirement is that the site must use HTTPS.
```
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx
```
Now we have installed Certbot by Let’s Encrypt for Ubuntu 18.04, run this command to receive your certificates.
```
sudo certbot --nginx certonly
```
Enter your email and agree to the terms and conditions, then you will receive the list of domains you need to generate SSL certificate.

To select all domains simply hit Enter

The Certbot client will automatically generate the new certificate for your domain. Now we need to update the Nginx config.

Redirect HTTP Traffic to HTTPS with www in Nginx
Open your site’s Nginx configuration file add replace everything with the following. Replacing the file path with the one you received when obtaining the SSL certificate. The ssl_certificate directive should point to your fullchain.pem file, and the ssl_certificate_key directive should point to your privkey.pem file.

server {
    listen [::]:80;
    listen 80;

    server_name raschadvisory.com www.raschadvisory.com;
    # redirect http to https www
    return 301 https://www.raschadvisory.com$request_uri;
}

server {
    listen [::]:443 ssl http2;
    listen 443 ssl http2;

    server_name raschadvisory.com;

    ssl_certificate /etc/letsencrypt/live/raschadvisory.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/raschadvisory.com/privkey.pem;

    root /home/danny/raschadvisory.com/public/;
    index index.html index.php;

    # redirect https non-www to https www
    return 301 https://www.raschadvisory.com$request_uri;
}

server {
    listen [::]:443 ssl http2;
    listen 443 ssl http2;

    server_name www.raschadvisory.com;

    ssl_certificate /etc/letsencrypt/live/raschadvisory.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/raschadvisory.com/privkey.pem;

    error_log /home/danny/raschadvisory.com/logs/error.log;

    root /home/danny/raschadvisory.com/public/;
    index index.html index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;

        add_header Content-Security-Policy "img-src * 'self' data: blob: https:; default-src 'self' https://*.googleapis.com https://*.googletagmanager.com https://*.google-analytics.com https://s.ytimg.com https://www.youtube.com https://www.raschadvisory.com https://*.googleapis.com https://*.gstatic.com https://*.gravatar.com https://*.w.org data: 'unsafe-inline' 'unsafe-eval';" always;
        add_header X-Xss-Protection "1; mode=block" always;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header Access-Control-Allow-Origin "https://www.raschadvisory.com";
        add_header Referrer-Policy "origin-when-cross-origin" always;
        add_header Strict-Transport-Security "max-age=31536000; includeSubdomains; preload";
    }
}
The http2 value is all that is needed to enable the HTTP/2 protocol.

Hit CTRL+X followed by Y to save the changes.

Check your configuration and restart Nginx for the changes to take effect.

sudo nginx -t
sudo service nginx restart
Renewing SSL Certificate
Certificates provided by Let’s Encrypt are valid for 90 days only, so you need to renew them often. Now you set up a cronjob to check for the certificate which is due to expire in next 30 days and renew it automatically.

sudo crontab -e
Add this line at the end of the file

0 0,12 * * * certbot renew >/dev/null 2>&1
Hit CTRL+X followed by Y to save the changes.

This cronjob will attempt to check for renewing the certificate twice daily.

### Download Joomla
Download the latest version of Joomla and extract inside our root directory

cd ~/raschadvisory.com/public

curl -LO https://github.com/joomla/joomla-cms/releases/download/3.9.1/Joomla_3.9.1-Stable-Full_Package.tar.gz
tar xzvf Joomla_3.9.1-Stable-Full_Package.tar.gz
sudo rm -f ~/raschadvisory.com/public/Joomla_3.9.1-Stable-Full_Package.tar.gz
Install Joomla
Setup Cloud SQL as mentioned in this guide and proceed to Install Joomla Setup Cloud SQL and connect with Compute Engine.

Visit your domain in the web browser to complete the installation steps for Joomla

Joomla Configuration

Fill all the administration details

Click Next

Joomla Database Setup

Enter the Cloud SQL database details (Hostname is the IP address of your Cloud SQL Instance)

Click Next

Joomla verify ownership

As you are connecting your Joomla with Cloud SQL, Joomla will create a file with a random name in the installation directory and asks you to verify the ownership by deleting the random file.

So copy the filename created by Joomla and delete it with the following command

cd ~/raschadvisory.com/public/installation
sudo rm -f filename.txt
Click Next

Install Joomla

 

Verify the details and click Install

Finally, remove the installation directory. You can remove the installation directory manually by running the following command

sudo rm -r ~/raschadvisory.com/public/installation
Now Joomla is installed on your domain name

Welcome to Joomla

Enjoy your Joomla installation on Google Cloud with Ubuntu 18.04 LTS, Nginx, PHP 7.2, Let’s Encrypt SSL and Cloud SQL.



###

Option 2 is highly recommended, find out username used by the Nginx worker processes:

grep 'user' /etc/nginx/nginx.conf
The most common ones are either www-data or nginx. Edit PHP FPM pool configuration file:

/etc/php5/fpm/pool.d/www.conf


#### Change nginx user
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ grep 'user' /etc/nginx/nginx.conf
user www-data;
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ sudo nano /etc/nginx/nginx.conf
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ service nginx restart
Failed to restart nginx.service: Interactive authentication required.
See system logs and 'systemctl status nginx.service' for details.
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ sudo systemctl restart nginx
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ sudo nano /etc/nginx/nginx.conf
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ grep 'user' /etc/nginx/nginx.conf
user danny;
(base) danny@workstation:~/OneDrive/DataScience/41_DannyJRa.github.io$ 


### mysql
sudo apt-get install mysql-server

sudo mysql -u root -p

CREATE DATABASE joomla;

GRANT ALL PRIVILEGES on joomla.* to 'insider_danny'@'localhost' identified by 'alfonstini';