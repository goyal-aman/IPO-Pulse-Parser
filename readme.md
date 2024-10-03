# IPO Pulse Parser
Fetches data from IPO Pulse Supplier and generates a simple html

# Play using doker
```
# build docker image
docker build -t ipo-pulse-parser .

# start ipo-pulse-api container
docker run --rm -p 5678:5678 amangoyal8110/ipo-pulse-api:latest

# start parser
sudo docker run -p 5679:5679 -e IPO_PULSE_BASE_URL=http://localhost:5678 amangoyal8110/ipo-pulse-parser:latest

# get parsed html
curl localhost:5679/api/html
```

# Scope of Improvements
1. Add templating
    1.1 make templates handle tags (with priority), and data at tag level. Example of tags are: upcoming, live, past
2. Add docker images
3. Add versioning