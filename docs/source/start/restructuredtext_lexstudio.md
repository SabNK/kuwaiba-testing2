### Make RestructuredText by LexStudio work

Below is a process of installing RT in Windows.

1. Check that Python is installed on your machine.

    <kbd>⊞ Win</kbd>  + <kbd>cmd</kbd> and print

     ```console
     python --version
     ```

    your version should be highter than 3.8.0
    If python is missed or the version is old you should get it from [official](https://www.python.org/downloads/windows/)
2. Than install `sphinx`,  [blue-white](https://blog.readthedocs.com/new-theme-read-the-docs/) RTD [theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/) and [sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/) package, mentioned in `./docs/requirements.txt`
    
    ```console
    pip install -r ./docs/requirements.txt
    ```

3. In VSCode press <kbd>⌃ Control</kbd> + <kbd>⇧ Shift</kbd> + <kbd>X</kbd> to extension marketplace, find [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) and install.
    * In case of multiple Python installation choose the correct one by <kbd>⌃ Control</kbd> + <kbd>⇧ Shift</kbd> + <kbd>P</kbd> and command `Python: Select Interpreter`
    > **Important**  
    > For correct work reStructuredText requires some additional dependencies - `esBonio` and `reStructuredText Syntax highlighting`, that will be prompted to you during installation of reStructuredText, so be careful and agree to install them and later install esbonio server.  
4. In VS Code extension marketplace find [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext).   and press `Install`. Follow prompts to install dependencies and run them.

Gongrat! Now you can use preview button ![open preview](https://raw.githubusercontent.com/microsoft/vscode-codicons/eaa030691d720b9c5c0efa93d9be9e2e45d7262b/src/icons/open-preview.svg) on `.rst` files
