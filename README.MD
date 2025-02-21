## Python Debian Package & Launchpad PPA Upload Guide

### 📋 Prerequisites
```bash
# Install dependencies
sudo apt install -y \
    dh-python \
    python3-all \
    debhelper \
    devscripts \
    build-essential \
    python3-dev \
    python3-setuptools \
    python3-venv \
    gnupg \
    ubuntu-dev-tools
```

### Create a Launchpad Account & Generate GPG Keys
```bash
gpg --full-generate-key
gpg --list-keys
gpg --send-keys --keyserver keyserver.ubuntu.com <YOUR_KEY_ID>
```
Generate key using full-generate and send keys to the key server.
Copy the key and add it to the Launchpad's OpenPGP keys

###  Initialize packaging
```bash
dh_make --native --indep --packagename hello-ppa_0.1 --email <email> -y

# Clean template files
rm debian/*.ex debian/*.EX debian/README.*
```

####  Edit debian/control
```bash
Source: hello-ppa
Section: python
Priority: optional
Maintainer: Name <email>
Build-Depends: debhelper-compat (= 13), dh-python, python3-all, python3-setuptools
Standards-Version: 4.6.2
Rules-Requires-Root: no

Package: hello-ppa
Architecture: all
Depends: ${python3:Depends}, ${misc:Depends}
Description: Example Python PPA package
```

####  Edit debian/changelog
```bash
hello-ppa (0.1-1~ppa1) jammy; urgency=medium
  * Initial release
 -- Name <email>  Mon, 01 Jan 2024 12:00:00 +0000
 ```

####  Edit debian/rules (TAB-indented!)
```bash
#!/usr/bin/make -f

%:
  dh $@ --with python3
 ```

###  Generate source tarball
```bash
python3 setup.py sdist
mv dist/hello-ppa-0.1.tar.gz ../hello-ppa_0.1.orig.tar.gz
```

### Install build dependencies
```bash
sudo mk-build-deps --install --remove debian/control
```

### Build source package
```bash
debuild -S -sa -kYOUR_GPG_KEY_ID
```

### Upload to Launchpad PPA
```bash
dput ppa:your-launchpad-username/ppa-name ../hello-ppa_0.1-1~ppa1_source.changes
```