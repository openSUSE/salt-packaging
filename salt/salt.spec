#
# spec file for package salt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%if 0%{?suse_version} >= 1320
# SLE15
%global build_py3   1
%global build_py2   1
%global default_py3 1
%else
%if 0%{?suse_version} == 1315
# SLE12
%global build_py3   1
%global build_py2   1
%else
# RES7
%global build_py2   1
%endif
%endif
%define pythonX %{?default_py3: python3}%{!?default_py3: python2}

%if 0%{?suse_version} > 1210 || 0%{?rhel} >= 7 || 0%{?fedora}
%bcond_without systemd
%else
%bcond_with    systemd
%endif
%{!?python3_sitelib: %global python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%if 0%{?suse_version} > 1110
%bcond_without bash_completion
%bcond_without fish_completion
%bcond_without zsh_completion
%else
%bcond_with    bash_completion
%bcond_with    fish_completion
%bcond_with    zsh_completion
%endif
%bcond_with    test
%bcond_without docs
%bcond_with    builddocs

Name:           salt
Version:        2018.11.0
Release:        0
Summary:        A parallel remote execution system
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
#Source:         https://github.com/saltstack/salt/archive/v%{version}.tar.gz
Source:         fluorine.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml

Patch1:         run-salt-master-as-dedicated-salt-user.patch
Patch2:         run-salt-api-as-user-salt-bsc-1064520.patch
Patch3:         activate-all-beacons-sources-config-pillar-grains.patch
Patch4:         avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
Patch5:         fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46684
Patch6:         add-saltssh-multi-version-support-across-python-inte.patch
# PATCH-FIX_OPENSUSE bsc#1091371
Patch7:         enable-passing-a-unix_socket-for-mysql-returners-bsc.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch8:         add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_OPENSUSE
Patch9:         add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48781
Patch10:        avoid-incomprehensive-message-if-crashes.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49063
Patch11:        integration-of-msi-authentication-with-azurearm-clou.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49538
Patch12:        fix-for-suse-expanded-support-detection.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49508
Patch13:        x509-fixes-for-remote-signing-106.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48812
Patch14:        use-adler32-algorithm-to-compute-string-checksums.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49497
Patch15:        x509-fixes-111.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49696
Patch16:        loosen-azure-sdk-dependencies-in-azurearm-cloud-driv.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49737
Patch17:        do-not-load-pip-state-if-there-is-no-3rd-party-depen.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49480
Patch18:        early-feature-support-config.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49908
Patch19:        bugfix-any-unicode-string-of-length-16-will-raise-ty.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49936
Patch20:        make-profiles-a-package.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49930
Patch21:        get-os_family-for-rpm-distros-from-the-rpm-macros.-u.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49946
Patch22:        add-cpe_name-for-osversion-grain-parsing-u-49946.patch
# PATCH-FIX_OPENSUSE: Fix unit test for grains core
Patch23:        fix-unit-test-for-grains-core.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50049
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50072
Patch24:        preserving-signature-in-module.run-state-u-50049.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50095
Patch25:        support-config-non-root-permission-issues-fixes-u-50.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50018
Patch26:        add-multi-file-support-and-globbing-to-the-filetree-.patch


# BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

Requires:       %{pythonX}-%{name} = %{version}-%{release}

Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd

%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
%endif

%if 0%{?suse_version}
Requires(pre):  dbus-1
%else
Requires(pre):  dbus
%endif

Requires:       logrotate
Requires:       procps

%if 0%{?suse_version} >= 1500
Requires:       iproute2
%else
%if 0%{?suse_version}
Requires:       net-tools
%else
Requires:       iproute
%endif
%endif

%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre): %insserv_prereq
%endif
%endif

%if %{with fish_completion}
%define fish_dir %{_datadir}/fish/
%define fish_completions_dir %{_datadir}/fish/completions/
%endif

%if %{with bash_completion}
%if 0%{?suse_version} >= 1140
BuildRequires:  bash-completion
%else
BuildRequires:  bash
%endif
%endif

%if %{with zsh_completion}
BuildRequires:  zsh
%endif

%if 0%{?rhel}
BuildRequires:  yum
%endif

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.

%if 0%{?build_py2}
%package -n python2-salt
Summary:        python2 library for salt
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python >= 2.7
BuildRequires:  python-devel >= 2.7
# requirements/base.txt
%if 0%{?rhel}
BuildRequires:  python-jinja2
BuildRequires:  python-yaml
BuildRequires:  python-markupsafe
%else
BuildRequires:  python-Jinja2
BuildRequires:  python-PyYAML
BuildRequires:  python-MarkupSafe
%endif

BuildRequires:  python-futures >= 2.0
BuildRequires:  python-msgpack-python > 0.3
BuildRequires:  python-psutil
BuildRequires:  python-requests >= 1.0.0
BuildRequires:  python-tornado >= 4.2.1

# requirements/zeromq.txt
BuildRequires:  python-pycrypto >= 2.6.1
BuildRequires:  python-pyzmq >= 2.2.0
%if %{with test}
# requirements/dev_python27.txt
BuildRequires:  python-boto >= 2.32.1
BuildRequires:  python-mock
BuildRequires:  python-moto >= 0.3.6
BuildRequires:  python-pip
BuildRequires:  python-salt-testing >= 2015.2.16
BuildRequires:  python-unittest2
BuildRequires:  python-xml
%endif
%if %{with builddocs}
BuildRequires:  python-sphinx
%endif
Requires:       python >= 2.7
#
%if ! 0%{?suse_version} > 1110
Requires:       python-certifi
%endif
# requirements/base.txt
%if 0%{?rhel}
Requires:       python-jinja2
Requires:       python-yaml
Requires:       python-markupsafe
Requires:       yum
%if 0%{?rhel} == 6
Requires:       yum-plugin-security
%endif
%else
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-MarkupSafe
%endif

Requires:       python-futures >= 2.0
Requires:       python-msgpack-python > 0.3
Requires:       python-psutil
Requires:       python-requests >= 1.0.0
Requires:       python-tornado >= 4.2.1
%if 0%{?suse_version}
# required for zypper.py
Requires:       rpm-python
Requires(pre):  libzypp(plugin:system) >= 0
Requires:       zypp-plugin-python
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python-timelib
Suggests:       python-gnupg
# requirements/zeromq.txt
%endif
Requires:       python-pycrypto >= 2.6.1
Requires:       python-pyzmq >= 2.2.0
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python-xml
Suggests:       python-Mako
Recommends:     python-netaddr
%endif

%description -n python2-salt
Python2 specific files for salt

%endif

%if 0%{?build_py3}
%package -n python3-salt
Summary:        python3 library for salt
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildRequires:  python-rpm-macros
BuildRequires:  python3 < 3.7
BuildRequires:  python3-devel
# requirements/base.txt
%if 0%{?rhel}
BuildRequires:  python3-jinja2
%else
BuildRequires:  python3-Jinja2
%endif
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-PyYAML
BuildRequires:  python3-msgpack-python > 0.3
BuildRequires:  python3-psutil
BuildRequires:  python3-requests >= 1.0.0
BuildRequires:  python3-tornado >= 4.2.1

# requirements/zeromq.txt
BuildRequires:  python3-pycrypto >= 2.6.1
BuildRequires:  python3-pyzmq >= 2.2.0
%if %{with test}
# requirements/dev_python27.txt
BuildRequires:  python3-boto >= 2.32.1
BuildRequires:  python3-mock
BuildRequires:  python3-moto >= 0.3.6
BuildRequires:  python3-pip
BuildRequires:  python3-salt-testing >= 2015.2.16
BuildRequires:  python3-unittest2
BuildRequires:  python3-xml
%endif
%if %{with builddocs}
BuildRequires:  python3-sphinx
%endif
Requires:       python3 < 3.7
#
%if ! 0%{?suse_version} > 1110
Requires:       python3-certifi
%endif
# requirements/base.txt
%if 0%{?rhel}
Requires:       python3-jinja2
Requires:       yum
%if 0%{?rhel} == 6
Requires:       yum-plugin-security
%endif
%else
Requires:       python3-Jinja2
%endif
Requires:       python3-MarkupSafe
Requires:       python3-PyYAML
Requires:       python3-msgpack-python > 0.3
Requires:       python3-psutil
Requires:       python3-requests >= 1.0.0
Requires:       python3-tornado >= 4.2.1
%if 0%{?suse_version}
# required for zypper.py
Requires:       python3-rpm
Requires(pre):  libzypp(plugin:system) >= 0
Requires:       python3-zypp-plugin
# requirements/opt.txt (not all)
# Suggests:     python-MySQL-python  ## Disabled for now, originally Recommended
Suggests:       python3-timelib
Suggests:       python3-gnupg
# requirements/zeromq.txt
%endif
Requires:       python3-pycrypto >= 2.6.1
Requires:       python3-pyzmq >= 2.2.0
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python3-xml
Suggests:       python3-Mako
Recommends:     python3-netaddr
%endif

%description -n python3-salt
Python3 specific files for salt

%endif

%package api
Summary:        The api for Salt a parallel remote execution system
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?default_py3}
Requires:       python3-CherryPy >= 3.2.2
%else
Requires:       python-CherryPy >= 3.2.2
%endif

%description api
salt-api is a modular interface on top of Salt that can provide a variety of entry points into a running Salt system.

%package cloud
Summary:        Generic cloud provisioning tool for Saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
Requires:       python3-apache-libcloud
%if 0%{?suse_version}
Recommends:     python3-botocore
Recommends:     python3-netaddr
%endif

%description cloud
public cloud VM management system
provision virtual machines on various public clouds via a cleanly
controlled profile and mapping system.

%if %{with docs}
%package doc
Summary:        Documentation for salt, a parallel remote execution system
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This contains the documentation of salt, it is an offline version of http://docs.saltstack.com.
%endif

%package master
Summary:        The management component of Saltstack with zmq protocol supported
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version}
Recommends:     python3-pygit2 >= 0.20.3
%endif
%ifarch %{ix86} x86_64
%if 0%{?suse_version}
%if 0%{?suse_version} > 1110
Requires:       dmidecode
%else
Requires:       pmtools
%endif
%endif
%endif
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description master
The Salt master is the central server to which all minions connect.
Enabled commands to remote systems to be called in parallel rather
than serially.

%package minion
Summary:        The client component for Saltstack
Group:          System/Management
Requires(pre):  %{name} = %{version}-%{release}

%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description minion
Salt minion is queried and controlled from the master.
Listens to the salt master and execute the commands.

%package proxy
Summary:        Component for salt that enables controlling arbitrary devices
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description proxy
Proxy minions are a developing Salt feature that enables controlling devices that,
for whatever reason, cannot run a standard salt-minion.
Examples include network gear that has an API but runs a proprietary OS,
devices with limited CPU or memory, or devices that could run a minion, but for
security reasons, will not.


%package syndic
Summary:        The syndic component for saltstack
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description syndic
Salt syndic is the master-of-masters for salt
The master of masters for salt-- it enables
the management of multiple masters at a time..

%package ssh
Summary:        Management component for Saltstack with ssh protocol
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-master = %{version}-%{release}
%if 0%{?suse_version}
Recommends:     sshpass
%endif
%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre):  %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif

%description ssh
Salt ssh is a master running without zmq.
it enables the management of minions over a ssh connection.

%if %{with bash_completion}
%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description bash-completion
Bash command line completion support for %{name}.

%endif

%if %{with fish_completion}
%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description fish-completion
Fish command line completion support for %{name}.
%endif

%if %{with zsh_completion}
%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description zsh-completion
Zsh command line completion support for %{name}.

%endif

%prep
# %setup -q -n salt-%{version}
%setup -q -n salt-fluorine
cp %{S:1} .
cp %{S:5} ./.travis.yml
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1

%build
%if 0%{?build_py2}
%{__python} setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt
mv build _build.python2
%endif
%if 0%{?build_py3}
%{__python3} setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt
mv build _build.python3
%endif

%if %{with docs} && %{without builddocs}
# extract docs from the tarball
mkdir -p doc/_build
pushd doc/_build/
tar xfv %{S:3}
popd
%endif

%if %{with docs} && %{with builddocs}
## documentation
cd doc && make html && rm _build/html/.buildinfo && rm _build/html/_images/proxy_minions.png && cd _build/html && chmod -R -x+X *
%endif

%install
%if 0%{?build_py2}
mv _build.python2 build
%{__python} setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot}
mv build _build.python2
%endif
%if 0%{?build_py3}
mv _build.python3 build
%{__python3} setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot}
mv build _build.python3
%endif

%if 0%{?default_py3}
DEF_PYPATH=_build.python3/scripts-*/
%else
DEF_PYPATH=_build.python2/scripts-*/
%endif

rm -f %{buildroot}%{_bindir}/*
for script in $DEF_PYPATH/*; do
  install -m 0755 $script %{buildroot}%{_bindir}
done

## create missing directories
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d/
install -Dd -m 0755 %{buildroot}%{_sbindir}
install -Dd -m 0750 %{buildroot}%{_localstatedir}/log/salt
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/minion/extmod
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/jobs
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/proc
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/queues
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/roots
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/syndics
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/master/tokens
install -Dd -m 0750 %{buildroot}%{_localstatedir}/cache/salt/cloud
install -Dd -m 0750 %{buildroot}/var/lib/salt
install -Dd -m 0750 %{buildroot}/srv/salt
install -Dd -m 0750 %{buildroot}/srv/pillar
install -Dd -m 0750 %{buildroot}/srv/spm
install -Dd -m 0755 %{buildroot}%{_docdir}/salt
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.maps.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.profiles.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/cloud.providers.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/master.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/minion.d
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_autosign
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_denied
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_pre
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/master/minions_rejected
install -Dd -m 0750 %{buildroot}%{_sysconfdir}/salt/pki/minion

# Install salt-support profiles
%if 0%{?build_py2}
install -Dpm 0644 salt/cli/support/profiles/*  %{buildroot}%{python_sitelib}/salt/cli/support/profiles
%endif
%if 0%{?build_py3}
install -Dpm 0644 salt/cli/support/profiles/* %{buildroot}%{python3_sitelib}/salt/cli/support/profiles
%endif


## Install Zypper plugins only on SUSE machines
%if 0%{?suse_version}
install -Dd -m 0750 %{buildroot}%{_prefix}/lib/zypp/plugins/commit
%{__install} scripts/suse/zypper/plugins/commit/zyppnotify %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%if 0%{?default_py3}
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!/usr/bin/python3=' %{buildroot}%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
install -Dd %{buildroot}%{_prefix}/share/yum-plugins
install -Dd %{buildroot}/etc/yum/pluginconf.d
%{__install} scripts/suse/yum/plugins/yumnotify.py %{buildroot}%{_prefix}/share/yum-plugins
%{__install} scripts/suse/yum/plugins/yumnotify.conf %{buildroot}/etc/yum/pluginconf.d
%endif

## install init and systemd scripts
%if %{with systemd}
install -Dpm 0644 pkg/suse/salt-master.service %{buildroot}%{_unitdir}/salt-master.service
%if 0%{?suse_version}
install -Dpm 0644 pkg/suse/salt-minion.service %{buildroot}%{_unitdir}/salt-minion.service
%else
install -Dpm 0644 pkg/suse/salt-minion.service.rhel7 %{buildroot}%{_unitdir}/salt-minion.service
%endif
install -Dpm 0644 pkg/salt-syndic.service %{buildroot}%{_unitdir}/salt-syndic.service
install -Dpm 0644 pkg/suse/salt-api.service    %{buildroot}%{_unitdir}/salt-api.service
install -Dpm 0644 pkg/salt-proxy@.service %{buildroot}%{_unitdir}/salt-proxy@.service
ln -s service %{buildroot}%{_sbindir}/rcsalt-master
ln -s service %{buildroot}%{_sbindir}/rcsalt-syndic
ln -s service %{buildroot}%{_sbindir}/rcsalt-minion
ln -s service %{buildroot}%{_sbindir}/rcsalt-api
install -Dpm 644 %{S:2}                   %{buildroot}/usr/lib/tmpfiles.d/salt.conf
%else
mkdir -p %{buildroot}%{_initddir}
## install init scripts
install -Dpm 0755 pkg/suse/salt-master %{buildroot}%{_initddir}/salt-master
install -Dpm 0755 pkg/suse/salt-syndic %{buildroot}%{_initddir}/salt-syndic
install -Dpm 0755 pkg/suse/salt-minion %{buildroot}%{_initddir}/salt-minion
install -Dpm 0755 pkg/suse/salt-api %{buildroot}%{_initddir}/salt-api
ln -sf %{_initddir}/salt-master %{buildroot}%{_sbindir}/rcsalt-master
ln -sf %{_initddir}/salt-syndic %{buildroot}%{_sbindir}/rcsalt-syndic
ln -sf %{_initddir}/salt-minion %{buildroot}%{_sbindir}/rcsalt-minion
ln -sf %{_initddir}/salt-api %{buildroot}%{_sbindir}/rcsalt-api
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
install -Dpm 0755 scripts/suse/watchdog/salt-daemon-watcher %{buildroot}%{_bindir}/salt-daemon-watcher
%endif 

#
## install config files
install -Dpm 0640 conf/minion %{buildroot}%{_sysconfdir}/salt/minion
install -Dpm 0640 /dev/null   %{buildroot}%{_sysconfdir}/salt/minion_id
install -Dpm 0640 conf/master %{buildroot}%{_sysconfdir}/salt/master
install -Dpm 0640 conf/roster %{buildroot}%{_sysconfdir}/salt/roster
install -Dpm 0640 conf/cloud %{buildroot}%{_sysconfdir}/salt/cloud
install -Dpm 0640 conf/cloud.profiles %{buildroot}%{_sysconfdir}/salt/cloud.profiles
install -Dpm 0640 conf/cloud.providers %{buildroot}%{_sysconfdir}/salt/cloud.providers
#
## install logrotate file (for RHEL6 we use without sudo)
%if 0%{?rhel} > 6 || 0%{?suse_version}
install -Dpm 0644  pkg/suse/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
%else
install -Dpm 0644  pkg/salt-common.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/salt
%endif
#
## install SuSEfirewall2 rules
install -Dpm 0644  pkg/suse/salt.SuSEfirewall2 %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
#
## install completion scripts
%if %{with bash_completion}
install -Dpm 0644 pkg/salt.bash %{buildroot}%{_sysconfdir}/bash_completion.d/salt
%endif
%if %{with zsh_completion}
install -Dpm 0644 pkg/zsh_completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/salt
%endif

%if %{with fish_completion}
mkdir -p %{buildroot}%{fish_completions_dir}
install -Dpm 0644 pkg/fish-completions/* %{buildroot}%{fish_completions_dir}
%endif

%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_docdir}
%if 0%{?build_py2}
%fdupes %{buildroot}%{python_sitelib}
%endif
%if 0%{?build_py3}
%fdupes %{buildroot}%{python3_sitelib}
%endif
%endif

%check
%if %{with test}
%if 0%{?default_py3}
%{__python3} setup.py test --runtests-opts=-u
%else
%{__python} setup.py test --runtests-opts=-u
%endif
%endif

%pre
S_HOME="/var/lib/salt"
S_PHOME="/srv/salt"
getent passwd salt | grep $S_PHOME >/dev/null && usermod -d $S_HOME salt
getent group salt >/dev/null || %{_sbindir}/groupadd -r salt
getent passwd salt >/dev/null || %{_sbindir}/useradd -r -g salt -d $S_HOME -s /bin/false -c "salt-master daemon" salt
if [[ -d "$S_PHOME/.ssh" ]]; then
    mv $S_PHOME/.ssh $S_HOME
fi

%post
%if %{with systemd}
systemd-tmpfiles --create /usr/lib/tmpfiles.d/salt.conf || true
%else
dbus-uuidgen --ensure
%endif

%preun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-proxy@.service
%else
%systemd_preun salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-proxy
%endif
%endif

%pre proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-proxy@.service
%endif
%endif

%post proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-proxy@.service
%fillup_only
%else
%systemd_post salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun proxy
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-proxy@.service
%else
%systemd_postun_with_restart salt-proxy@.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-proxy
%endif
%endif

%preun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-syndic.service
%else
%systemd_preun salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-syndic
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-syndic stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-syndic
  fi
%endif
%endif

%pre syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-syndic.service
%endif
%endif

%post syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-syndic.service
%fillup_only
%else
%systemd_post salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun syndic
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-syndic.service
%else
%systemd_postun_with_restart salt-syndic.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-syndic
%endif
%endif

%preun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-master.service
%else
%systemd_preun salt-master.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-master
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-master stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-master
  fi
%endif
%endif

%pre master
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-master.service
%endif
%endif

%post master
if [ $1 -eq 2 ] ; then
  # Upgrading from an earlier version.  If this is from 2014, where daemons
  # ran as root, we need to chown some stuff to salt in order for the new
  # version to actually work.  It seems a manual restart of salt-master may
  # still be required, but at least this will actually work given the file
  # ownership is correct.
  for file in master.{pem,pub} ; do
    [ -f /etc/salt/pki/master/$file ] && chown salt /etc/salt/pki/master/$file
  done
  MASTER_CACHE_DIR="/var/cache/salt/master"
  [ -d $MASTER_CACHE_DIR ] && chown -R salt:salt $MASTER_CACHE_DIR
  [ -f $MASTER_CACHE_DIR/.root_key ] && chown root:root $MASTER_CACHE_DIR/.root_key
  true
fi
%if %{with systemd}
if [ `rpm -q systemd --queryformat="%%{VERSION}"` -lt 228 ]; then
  # On systemd < 228 the 'TasksTask' attribute is not available.
  # Removing TasksMax from salt-master.service on SLE12SP1 LTSS (bsc#985112)
  sed -i '/TasksMax=infinity/d' %{_unitdir}/salt-master.service
fi
%if 0%{?suse_version}
%service_add_post salt-master.service
%fillup_only
%else
%systemd_post salt-master.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-master
%endif
%endif

%postun master
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-master.service
%else
%systemd_postun_with_restart salt-master.service
%endif
%else
%if 0%{?suse_version}
%restart_on_update salt-master
%insserv_cleanup
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-master condrestart >/dev/null 2>&1 || :
  fi
%endif
%endif

%preun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-minion.service
%else
%systemd_preun salt-minion.service
%endif
%else
%if 0%{?suse_version}
%stop_on_removal salt-minion
%else
  if [ $1 -eq 0 ] ; then
      /sbin/service salt-minion stop >/dev/null 2>&1
      /sbin/chkconfig --del salt-minion
  fi
%endif
%endif

%pre minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-minion.service
%endif
%endif

%post minion
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-minion.service
%fillup_only
%else
%systemd_post salt-minion.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%else
  /sbin/chkconfig --add salt-minion
%endif
%endif

%postun minion
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-minion.service
%else
%systemd_postun_with_restart salt-minion.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update salt-minion
%else
  if [ "$1" -ge "1" ] ; then
      /sbin/service salt-minion condrestart >/dev/null 2>&1 || :
  fi
%endif
%endif

%preun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_preun salt-api.service
%else
%systemd_preun salt-api.service
%endif
%else
%stop_on_removal
%endif

%pre api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_pre salt-api.service
%endif
%endif

%post api
%if %{with systemd}
%if 0%{?suse_version}
%service_add_post salt-api.service
%else
%systemd_post salt-api.service
%endif
%else
%if 0%{?suse_version}
%fillup_and_insserv
%endif
%endif

%postun api
%if %{with systemd}
%if 0%{?suse_version}
%service_del_postun salt-api.service
%else
%systemd_postun_with_restart salt-api.service
%endif
%else
%if 0%{?suse_version}
%insserv_cleanup
%restart_on_update
%endif
%endif

%posttrans -n python2-salt
# force re-generate a new thin.tgz
rm -f %{_localstatedir}/cache/salt/master/thin/version
rm -f %{_localstatedir}/cache/salt/minion/thin/version

%if 0%{?build_py3}
%posttrans -n python3-salt
# force re-generate a new thin.tgz
rm -f %{_localstatedir}/cache/salt/master/thin/version
rm -f %{_localstatedir}/cache/salt/minion/thin/version
%endif

%files api
%defattr(-,root,root)
%{_bindir}/salt-api
%{_sbindir}/rcsalt-api
%if %{with systemd}
%{_unitdir}/salt-api.service
%else
%{_initddir}/salt-api
%endif
%{_mandir}/man1/salt-api.1.*

%files cloud
%defattr(-,root,root)
%{_bindir}/salt-cloud
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.maps.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.profiles.d
%dir               %attr(0750, root, salt) %{_sysconfdir}/salt/cloud.providers.d
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.profiles
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/cloud.providers
%dir               %attr(0750, root, salt) %{_localstatedir}/cache/salt/cloud
%if 0%{?default_py3}
%{python3_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%attr(755,root,root)%{python3_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%else
%{python_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%attr(755,root,root)%{python_sitelib}/salt/cloud/deploy/bootstrap-salt.sh
%endif
%{_mandir}/man1/salt-cloud.1.*

%files ssh
%defattr(-,root,root)
%{_bindir}/salt-ssh
%{_mandir}/man1/salt-ssh.1.gz

%files syndic
%defattr(-,root,root)
%{_bindir}/salt-syndic
%{_mandir}/man1/salt-syndic.1.gz
%{_sbindir}/rcsalt-syndic
%if %{with systemd}
%{_unitdir}/salt-syndic.service
%else
%{_initddir}/salt-syndic
%endif

%files minion
%defattr(-,root,root)
%{_bindir}/salt-minion
%{_mandir}/man1/salt-minion.1.gz
%config(noreplace) %attr(0640, root, root) %{_sysconfdir}/salt/minion
%config(noreplace) %attr(0640, root, root) %ghost %{_sysconfdir}/salt/minion_id
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/minion.d/
%dir               %attr(0750, root, root) %{_sysconfdir}/salt/pki/minion/
%dir               %attr(0750, root, root) %{_localstatedir}/cache/salt/minion/
#%dir %ghost        %attr(0750, root, salt) %{_localstatedir}/run/salt/minion
%{_sbindir}/rcsalt-minion

# Install plugin only on SUSE machines
%if 0%{?suse_version}
%{_prefix}/lib/zypp/plugins/commit/zyppnotify
%endif

# Install Yum plugins only on RH machines
%if 0%{?fedora} || 0%{?rhel}
%{_prefix}/share/yum-plugins/
/etc/yum/pluginconf.d/yumnotify.conf
%endif

%if %{with systemd}
%{_unitdir}/salt-minion.service
%else
%config(noreplace) %{_initddir}/salt-minion
%endif

## Install sysV salt-minion watchdog for SLES11 and RHEL6
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%{_bindir}/salt-daemon-watcher
%endif

%files proxy
%defattr(-,root,root)
%{_bindir}/salt-proxy
%{_mandir}/man1/salt-proxy.1.gz
%if %{with systemd}
%{_unitdir}/salt-proxy@.service
%endif

%files master
%defattr(-,root,root)
%{_bindir}/salt
%{_bindir}/salt-master
%{_bindir}/salt-cp
%{_bindir}/salt-key
%{_bindir}/salt-run
%{_mandir}/man1/salt-master.1.gz
%{_mandir}/man1/salt-cp.1.gz
%{_mandir}/man1/salt-key.1.gz
%{_mandir}/man1/salt-run.1.gz
%{_mandir}/man7/salt.7.gz
%config(noreplace) %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/salt
%{_sbindir}/rcsalt-master
%if %{with systemd}
%{_unitdir}/salt-master.service
%else
%config(noreplace) %{_initddir}/salt-master
%endif
#
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/master
%config(noreplace) %attr(0640, root, salt) %{_sysconfdir}/salt/roster
%dir               %attr(0755, root, salt) %{_sysconfdir}/salt/master.d/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_autosign/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_denied/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_pre/
%dir               %attr(0750, salt, salt) %{_sysconfdir}/salt/pki/master/minions_rejected/
%dir               %attr(0755, salt, salt) /var/lib/salt
%dir               %attr(0755, root, salt) /srv/salt
%dir               %attr(0755, root, salt) /srv/pillar
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/jobs/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/proc/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/queues/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/roots/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/syndics/
%dir               %attr(0750, salt, salt) %{_localstatedir}/cache/salt/master/tokens/
#%dir %ghost        %attr(0750, salt, salt) %{_localstatedir}/run/salt/master/

%files
%defattr(-,root,root,-)
%{_bindir}/spm
%{_bindir}/salt-call
%{_bindir}/salt-support
%{_bindir}/salt-unity
%{_mandir}/man1/salt-unity.1.gz
%{_mandir}/man1/salt-call.1.gz
%{_mandir}/man1/spm.1.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/salt
%if 0%{?suse_version} < 1500
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE
%else
%license LICENSE
%doc AUTHORS README.rst HACKING.rst README.SUSE
%endif
#
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt
%dir        %attr(0750, root, salt) %{_sysconfdir}/salt/pki
%dir        %attr(0750, salt, salt) %{_localstatedir}/log/salt
%dir        %attr(0750, root, salt) %{_localstatedir}/cache/salt
#%dir %ghost %attr(0750, root, salt) %{_localstatedir}/run/salt
%dir        %attr(0750, root, salt) /srv/spm
%if %{with systemd}
/usr/lib/tmpfiles.d/salt.conf
%endif
%{_mandir}/man1/salt.1.*

%if 0%{?build_py2}
%files -n python2-salt
%defattr(-,root,root,-)
%{python_sitelib}/*
%exclude %{python_sitelib}/salt/cloud/deploy/*.sh
%endif

%if 0%{?build_py3}
%files -n python3-salt
%defattr(-,root,root,-)
%{python3_sitelib}/*
%exclude %{python3_sitelib}/salt/cloud/deploy/*.sh
%endif

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%if %{with bash_completion}
%files bash-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/bash_completion.d/
%config %{_sysconfdir}/bash_completion.d/%{name}
%endif

%if %{with zsh_completion}
%files zsh-completion
%defattr(-,root,root)
%dir %{_sysconfdir}/zsh_completion.d/
%config %{_sysconfdir}/zsh_completion.d/%{name}
%endif

%if %{with fish_completion}
%files fish-completion
%defattr(-,root,root)
%{fish_completions_dir}/salt*
%dir %{fish_completions_dir}
%dir %{fish_dir}
%endif

%changelog


