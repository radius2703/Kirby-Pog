## WIP Discord bot :D

**KirbyPog is a WIP upcoming discord bot :D**
<br />
I have no intentions to release this bot (yet), but I might as time goes one ^^

Till now though, this bot is still a work in progress.

**To run the bot locally, follow the following steps:**

* Pip install the requirements in requirements.txt<br />
To do that, run this command: `pip install -r requirements.txt`<br />
**(This step can be skipped if you desire to use the docker instead.)**

* Create a copy of the `config.example.json` file and rename it to `config.json`.

```json
{
  "token": "<token goes here>",
  "prefix": "k.",
  "exts": [
    "events.member",
    "imaging.slappers",
    "imaging.blur",
    "imaging.noise",
    "imaging.pass_it_down",
    "imaging.peppo_pet"
  ]
}
```

* At this step, you could either do a docker build, or run the `bot.py` file.

**Steps for docker:**
* Clone the repo, cd into the root dir of the project. A `ls` (or `dir`) should give `bot.py`, etc.

* Build the docker using: `docker build -t kirby-pog .`.<br /> This step usually takes around a minute or so.

* Finally run the docker with: `docker run kirby-pog`.

<br /><br />
Sorry if I butchered the terminology :p
<br /><br />
That should do it! Hope you have fun with the bot!<br />
If you have any suggestion/improvements, be sure to make a PR with the changes!
