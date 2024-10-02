# IPO Pulse Parser
Fetches data from IPO Pulse Supplier and generates a simple html

# Play using doker
```
# build docker image
docker build -t ipo-pulse-parser .

# start ipo-pulse-api container
docker run --rm -p 5678:5678 amangoyal8110/ipo-pulse-api:latest

# Generated HTML
sudo docker run -e BASE_URL=http://localhost:5678 -v $PWD/generated:/app/generated amangoyal8110/ipo-pulse-parser:latest
```

# Scope of Improvements
1. Add templating
2. Add docker images
3. Add versioning