## Description
This is a Docker application script which uses selenium to web scrape the xFinity website in order to collect usage details

## Use Cases
### How to currently run it
    git clone IS27-Particle27/xfinity-usage /home/$USERNAME/xfinity-usage
    docker run -d is27/xfinity-usage --env-file .env -v /home/$USERNAME/xfinity-usage/config:/config
#### Verification Code handling
In order to inject the most recent verification code run the following
    docker exec <containernameorid> /config/verify.sh
Ensure the script is set to executable
    docker exec <containernameorid> chmod +x /config/verify.sh
### Output to CSV
### Syncthing Integration (In Progress)
### MQTT Database

## Configuration
### Variables
    xu_BASERATE=0.5
        BaseRate (Percentage of data to leave remaining) for remaining data usage (KBps)
    st_ENABLED=TRUE
        Enable Syncthing Integration
    xu_FILEPATH=""
        File Path to export the CSV
    xu_CONFIGPATH="/config/default"
        Path to the Google Chrome Profile
    xu_USERNAME=""
        xFinity username
    xu_PASSWORD=""
        xFinity Password
    xu_MANUAL=TRUE
        Manual Entry for Max Send/Recv and Actual In/Out
    st_ENABLED=FALSE
        Enable Syncthing pull for Max Send/Recv and Actual In/Out
        Takes prescedence over xu_MANUAL
    st_APIKEY=""
        Syncthing API Key
    st_SERVER="127.0.0.1"
        Syncthing Server Address
    st_PORT="8384"
        Syncthing Port
    xu_MAXSEND=0
    xu_MAXRECV=0
    xu_INTOTAL=0
    xu_OUTTOTAL=0

## Support
