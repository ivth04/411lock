# Guide to reproduce



### Update your respotry
  `sudo apt-get update`  
  `sudo apt-get upgrade`

### Checking OS version
  `cat /etc/os-release  `

### add Erlang Solutions repository and public key
  `wget http://packages.erlang-solutions.com/debian/erlang_solutions.asc`  
  `sudo apt-key add erlang_solutions.asc`  
  `sudo apt-get update`  

### install all build dependencies - note mutiple lines
  `sudo apt-get --no-install-recommends -y install \`  
  `build-essential pkg-config erlang libicu-dev \`  
  `libmozjs185-dev libcurl4-openssl-dev`    

### add couchdb user and home
  `sudo useradd -d /home/couchdb couchdb`  
  `sudo mkdir /home/couchdb`  
  `sudo chown couchdb:couchdb /home/couchdb`  

### Get source
  `wget https://github.com/ivth04/411lock/raw/master/apache-couchdb-2.3.1.tar.gz`

### extract source and enter source directory
  `tar zxvf apache-couchdb-2.3.1.tar.gz`  
  `cd apache-couchdb-2.3.1/`  

### configure build and make executables
  `./configure`  
  `make release`  

### copy built release to couchdb user home directory
  `cd ./rel/couchdb/`  
  `sudo cp -Rp * /home/couchdb`  
  `sudo chown -R couchdb:couchdb /home/couchdb`  
  `cd /home/couchdb/etc`  

### need to edit IP address to allow external access
`sudo vim local.ini`    
Change this line:
 `#bind_address = 127.0.0.1`  
 to:  
 `bind_address = 0.0.0.0`   

### Servicize Couchdb(Uncomfired step); Or
`wget https://raw.githubusercontent.com/ivth04/411lock/master/couchdb.service`  
`cp couchdb.service /etc/systemd/system`  
### Copy and Crontab program
`sudo apt-get install cron`   
`cd /home/couchdb`       
`rm couchdb_relay.py`     
`wget https://raw.githubusercontent.com/ivth04/411lock/master/couchdb_relay.py`   
`chmod +x couchdb_relay.py`   
#### Crontab configuration
Input this command `crontab -e`, and then navigate to the bottom of file and add the new line:      
`@reboot /home/couchdb/couchdb_relay.py`    
Reboot into desktop and check if evrything's working!

### References:
1.https://bigl.es/enabling-a-python-script-to-launch-when-booting-a-raspberry-pi/       
2.https://andyfelong.com/2019/07/couchdb-2-1-on-raspberry-pi-raspbian-stretch/        
3.https://www.linuxquestions.org/questions/linux-software-2/starting-couchdb-2-0-as-a-service-4175596921/   
    
