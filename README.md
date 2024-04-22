# CasaOS Management Tool

This Python script provides a command-line interface (CLI) tool for managing CasaOS. It supports updating CasaOS, resetting the username and password by backing up and managing the `user.db` file, and completely reinstalling CasaOS.

## Features

- **Update CasaOS**:
  - Downloads and installs the latest updates for CasaOS.
- **Reset Username and Password**: 
  - Backs up the current `user.db` and restarts the relevant service to apply changes.
- **Reinstall CasaOS**:
  - Uninstalls and reinstalls CasaOS, ideal for starting fresh or troubleshooting.

## Requirements
- Python 3.x
- CasaOS installed on the machine
- Administrative or sudo privileges
- * Tested it on Debian (Buster, Bullseye)

## Installation

To use this script, follow these steps:

1. Ensure Python 3 is installed on your system:
    ```bash
    python3 --version
    ```

2. Download the script to your preferred directory:
    ```bash
    wget https://github.com/0xleyth/casaos_manager/blob/main/casaos_manager.py -O casaos_manager.py
    ```

3. Make the script executable:
    ```bash
    chmod +x casaos_manager.py
    ```

## Usage

Run the script with one of the following commands based on the action you want to perform. You must run these commands as a user with sudo privileges.

```bash
./casaos_manager.py update                    # Updates CasaOS
./casaos_manager.py reset-username-password   # Resets username and password
./casaos_manager.py reinstall                 # Reinstalls CasaOS
```

### Optional: Running with Python directly

If you prefer, you can also run the script directly with Python:

```bash
python3 casaos_manager.py update
```

## Troubleshooting

- Ensure you have the necessary permissions to execute the script.
- Check that Python 3 is correctly installed and configured on your PATH.
- If you encounter issues with the script interpreting commands, ensure the shebang line at the top of the script is set to `#!/usr/bin/env python3`.

## Contributing

Contributions to this script are welcome, especially for expanding its functionality or improving error handling. Please fork the repository, make your changes, and submit a pull request.

## License

[MIT](https://github.com/sveltejs/kit/blob/master/LICENSE)