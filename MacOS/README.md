# About
Setting up a VM that has half the resources of your device has never been a favorite amongst security enthusiasts. Some have tried to make MacOS Homebrew tap's before, but this requires a lot of maintenance and eventually they have abandoned the project.

My goal for this project is to use formula's and casks directly from Homebrew to have an easy and automated version control. I believe this will provide a long lasting solution.

If you can contribute or you want to, feel free to do it at [Buy me a coffee! ☕](https://www.buymeacoffee.com/stevenh), I will be really thankfull for anything even if it is a coffee or just a kind comment towards my work, because that helps me a lot. Whenever you contribute with a donation, I will read your message and it will be shown in my main site.

# Setup
The installation time depends on your bandwidth.
This install is generally worth taking a long coffee break ;)
## Prerequirements
    xcode-select --install
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

## Install
    brew update && brew upgrade
    curl -LJO https://raw.githubusercontent.com/stevenhiltrop/pentesting/master/MacOS/kali_tools.txt
    brew install $(cat kali_tools.txt)
## Post installation
    brew install --cask wireshark
# Sources
- Credits go to Sidaf for his admirable work that inspired me to do this (https://github.com/sidaf/)
- GitHub download guide using curl (https://gist.github.com/jwebcat/5122366)
- Homebrew (https://brew.sh/)
- Kali linux tools (https://tools.kali.org/tools-listing)

# Notes
Most of the enumeration, priviledge escalation and maintaining shell access tools are not yet accepted in Homebrew.
Common ones are wpscan, unix-privesc-check, Powersploit, enum4linux, wfuzz.
Please make an effort to help grow Homebrew by adding these formula's/casks and which in turn I will be able to add to our tooling list (https://docs.brew.sh/Formula-Cookbook).

# TODO:
- [ ] Pull https://http.kali.org/dists/kali-rolling/main/source/Sources.gz
- [ ] Create a cask converting linux to brew requirements as stated on (https://docs.brew.sh/Formula-Cookbook)
- [ ] Create an app with dropdown listing tools per category


