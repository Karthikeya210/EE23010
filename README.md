## Setup

### Installing Apps

1. Install [F-Droid](https://www.f-droid.org/).
2. Open f-droid on your mobile and install the following apps:
   - Termux
   - Termux:API

### Setting up Termux

1. Give termux access to your user directory in Android.

    ```bash
    termux-setup-storage
    ```

2. Upgrade packages (any **one** command)

    ```bash
    pkg upg
    ```

    ```bash
    apt update && apt update
    ```

3. Install mandatory packages (any **one** command)

    ```bash
    apt install build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

    ```bash
    pkg in build-essential openssh curl git wget subversion silversearcher-ag imagemagick proot proot-distro python bsdtar mutt nmap neovim
    ```

### Installing and Setting up Ubuntu on Termux

1. Install ubuntu

    ```bash
    proot-distro install debian
    ```
    ```bash
    proot-distro login debian
    ```

    Inside proot-distro

    ```bash
    apt update && apt upgrade
    ```
    ```bash
    apt install apt-utils build-essential cmake neovim git wget subversion imagemagick nano ranger
    ```

2. Installing python3

    ```bash
    apt install python3-pip python3-numpy python3-scipy python3-matplotlib python3-mpmath python3-sympy python3-cvxopt
    ```

3. Installing neovim and ranger

    ```bash
    apt install neovim ranger libxtst-dev libx11-dev python3-pynvim
    ```
    ```bash
    pip3 install ueberzug
    ```

    - Refer to this [document](https://raw.githubusercontent.com/gadepall/fwc-1/main/installation/neovim.txt) to setup neovim and ranger.
    - For usage tips refer to this [document](https://iith-my.sharepoint.com/:x:/g/personal/gadepall_ee_iith_ac_in/EaI2vt4wm7hMmFyQz1AZXr4BWLd1KSZX290xKXfqk-qcgQ?e=KOoUTH).

## Creating a virtual environment 
1. Enter proot-distro
   
    ```bash
    proot-distro login debian
  
2. Create and enter your virtual environment

    ```bash
    virtualenv venv
    
    ```bash
    source venv/bin/activate

3. 











    
