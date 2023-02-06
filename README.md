# bypasserbot
A bot to bypass shorted links.
<details>
  <summary><b>Run Bot on VPS</b></summary>
<br/>
<p>

- Clone The Repo
```
git clone https://github.com/Greymattersbot/GreyMatters-Bypass-Bot
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
sudo docker run -p 80:80 bypass
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

### Variables

* `API_HASH` API Hash from my.telegram.org
* `API_ID` API ID from my.telegram.org
* `BOT_TOKEN` Bot token from @BotFather
* `PORT` server port of host. Defaults is `80`
* `Channel_id`
* `Drivebuzz_crypt`
* `Drivefire_crypt`
* `Jiodrive_crypt`
* `Gadrive_crypt`
* `Kolop_crypt`
* `Katdrive_crypt`
* `Gtot_crypt`
* `Appdrive_email`
* `Appdrive_password`
* `Hubdrive_crypt`
* `Sharerpw_xsrf_token`
* `Sharerpw_laravel_session`

## Credits 
* Thanks to Original Dev [Annihilatorrrr](https://github.com/annihilatorrrr)
* Thanks to [GreyMatter's](https://github.com/Greymattersbot) for making a Paid Repository Public for Free.
* Also Thanks to [khainee](https://github.com/khainee),[]()

## Note 
- I invite all the Devs to please come forward and contribute in this Open & Free Project by adding more URL Shorteners to it.
