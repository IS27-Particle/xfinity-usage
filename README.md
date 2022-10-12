## Description
This is a Docker application script which uses selenium to web scrape the xFinity website in order to collect usage details

## Use Cases
### How to currently run it
    git clone IS27-Particle27/
    docker run is27/xfinity-usage --env-file .env -v /home/$USERNAME/xfinity-usage/config:/config
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
