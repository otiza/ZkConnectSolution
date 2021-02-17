# ZKConnect

ZK Connect is a python script written to send realtime attendance data from ZK Teco devices to an external API. It is designed to run using a service like Supervisor.

### Requirements

- python >= 3.5
- pyzk == 0.9
- requests == 2.25.1
- pyyaml == 5.4.1

### Supported Devices

This script uses [pyzk](https://github.com/fananimi/pyzk) library to communicate with devices, hence it should support any device supported by pyzk.

## Usage

### Dependency Install

After creating and activating a virtual environment for the script, install the required libraries by running:

```bash
pip install -r requirements.txt
```

### Config File

A `config.example.yaml` file is provided in this repository. Rename/create a new one as `config.yaml` and fill up following keys:

```yaml
device:
  host: XXX.XXX.XXX.XXX # your device's ip address
  port: 4370 # usually 4370 is used by most of the devices
endpoint: http://my-app.test/log # a post API route to your app
```

### Running

After configuring, you can run `python connect.py` to start sending realtime attendance log to your application. The payload is:

```json
{
  "device_user_id": 21,
  "timestamp": "2021-02-17 18:23:00"
}
```

> Note: You should use a service like Supervisor to keep the script running and restarting automatically in case of any exception.


### Debugging

The script keeps all transaction logs in a `transaction_log.txt` file within the directory with all the necessary information for debugging. 
