# Python Base Project

This a base python runnable project that has the following features:

* Plugin based modules
* Bus event System to load features
* Sample pusher client for external integrations
* Sample Slack client for external notifications

## Run it!

### To run 

```
  python3 main.py
```

### To integrate with pusher, make a copy of the client_secrets file and change to match your secure info
  *Remenber not to check this in with your code*
```
  cp client_secrets.sample.json client_secrets.json
```

## All settings are stored in *config.py*

## Plugins

To add a plugin, place the file in the plugins plugins folder, then add the name to the plugins array in the *config.py* . Plugins can be executed in their own thread if necessary
r can wire up other non blocking processes such as responding to bus or other events

## Logging / Debugging

Standard Python loggers are also included and are configured in the *config.py* 



# Acknowledgments

Large sections of the code came from [swehner](https://github.com/swehner/foos) who made an excellent foosball table game system.