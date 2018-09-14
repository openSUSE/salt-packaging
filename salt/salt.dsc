Format: 3.0 (quilt)
Source: salt
Binary: salt-common, salt-master, salt-minion, salt-syndic, salt-ssh, salt-cloud, salt-api
Architecture: all
Version: 2018.3.0+ds-1
Maintainer: nobody
Uploaders: nobody
Homepage: http://saltstack.org/
Standards-Version: 3.9.6
Vcs-Browser: https://github.com/openSUSE/salt.git
Vcs-Git: git://github.com/openSUSE/salt.git
Build-Depends: bash-completion, debhelper (>= 9.20120410~), dh-python, dh-systemd (>= 1.4), python | python-all | python-dev | python-all-dev, python-debian, python-setuptools, python-sphinx (>= 1.0)
Package-List:
 salt-api deb admin extra arch=all
 salt-cloud deb admin extra arch=all
 salt-common deb admin extra arch=all
 salt-master deb admin extra arch=all
 salt-minion deb admin extra arch=all
 salt-ssh deb admin extra arch=all
 salt-syndic deb admin extra arch=all
Debtransform-Tar: salt_2018.3.0.orig.tar.gz
Files:
 bde96bf2362fb8784abc175fbd5112c3 13469511 salt_2018.3.0+ds.orig.tar.gz
