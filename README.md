# bypasserbot
A bot to bypass shorted links.
<details>
  <summary><b>Run Bot on VPS</b></summary>
<br/>
<p>

- Clone The Repo
```
git clone -b new https://github.com/Greymattersbot/GreyMatters-Bypass-Bot
```
- Change Directory 
```
cd GreyMatters-Bypass-Bot
```
- Update & Upgrade Packages
```
sudo apt-get update && sudo apt-get upgrade 
```

# Build And Run The Docker Image Using Official Docker Commands

- Start Docker daemon (SKIP if already running):
```
sudo dockerd
```
- Build Docker image:
```
sudo docker build . -t bypass
```
- Run the image:
```
sudo docker run -p 7:7 bypass
```
- To stop the running image:
```
sudo docker ps
```
```
sudo docker stop id
```

------
</p>
</br>
</details>


