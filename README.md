# LLT kivy App

### Development Environment Configuration
1. You must create a local file named `config.env` which includes a Google Cloud API key, like this:
   ```shell
      API_KEY='<api-key>'
   
   ```

### Setup Build Environment
1. If you are developing on Windows you need to follow [this](https://buildozer.readthedocs.io/en/latest/installation.html#android-on-windows-10-or-11) tutorial before continuing (only section **Android on Windows 10 or 11**)
2. run the following command to enter the virtual environment: 
    ```shell
      source venv/bin/activate
    ```
3. Install Dependencies:
    ```bash
      pip install -r dev-requirements.txt
   ```

4. Follow the following [tutorial](https://wiki.gentoo.org/wiki/Android/adb#:~:text=Set%20up%20a%20device%20for%20development,-USB%20Communication&text=Enable%20the%20USB%20Debugging%20option,device%20under%20Settings%20%3E%20Developer%20options.&text=On%20the%20device%2C%20go%20to,Settings%20%3E%20Developer%20options%20available%20enable.) to enable Developer mode on your Android device
   
### Build Process
1. Plug your android device into your computer using USB, and enable file transfer
2. run the following command to enter the virtual environment: 
    ```shell
      source venv/bin/activate
    ```
3. Run the following command (inside your virtual environment):
   ```bash
      buildozer android debug deploy run
   ```
4. The first time your build you might have to install dependencies (you will be guided through this by the command)
5. The app should automatically be opened when you unlock your Android device 

### Common Build Errors
1. Some errors can be fixed by deleting the `bin` and `.buildozer` directories, keep in mind that the next time you
build it might take upwards of 10 minutes longer.

### Unit Tests
1. run the following command to perform unittests:
   ```shell
      python -m unittest
   ```
