#
# spec file for package py26-compat-salt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%if 0%{?rhel} >= 8
%global __python /usr/bin/python2
%define pythonX python2
%else
%define pythonX python
%endif
 
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%bcond_with    test
%bcond_with    docs
%bcond_with    builddocs

%define compatdir %{_datadir}/susemanager/py26-compat
%define origname salt

Name:           py26-compat-salt
Version:        2016.11.10
Release:        0
Summary:        Python 2.6 compatible salt
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
BuildArch:      noarch
# Git: https://github.com/openSUSE/salt.git
Source0:        https://pypi.python.org/packages/a9/0a/31908d158c055248d5b5b22e66863eb98167aecad71edda92b58b223db7b/salt-2016.11.10.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml
Source6:        py26-compat-salt.conf
Source7:        py26-compat-salt-sle15-or-newer.conf

# PATCH-FIX-OPENSUSE use-forking-daemon.patch tserong@suse.com -- We don't have python-systemd, so notify can't work
# We do not upstream this patch because this is something that we have to fix on our side
Patch1:         tserong-suse.com-we-don-t-have-python-systemd-so-not.patch
# PATCH-FIX-OPENSUSE use-salt-user-for-master.patch -- Run salt master as dedicated salt user
# We do not upstream this patch because this is suse custom configuration
# (see: https://trello.com/c/wh96lCD4/1528-get-rid-of-0003-check-if-byte-strings-are-properly-encoded-in-utf-8-patch-in-the-salt-package)
Patch2:         run-salt-master-as-dedicated-salt-user.patch
# PATCH-FIX-OPENSUSE https://github.com/saltstack/salt/pull/30424
# We do not upstream this patch because it has been fixed upstream
Patch3:         check-if-byte-strings-are-properly-encoded-in-utf-8.patch
# PATCH-FIX-OPENSUSE prevent rebuilds in OBS
# We do not upstream this patch because the issue is on our side
Patch4:         do-not-generate-a-date-in-a-comment-to-prevent-rebui.patch
# PATCH-FIX-OPENSUSE Generate events from the Salt minion,
# We do not upstream this because this is for SUSE only (15.08.2016) if Zypper has been used outside the Salt infrastructure
Patch5:         add-zypp-notify-plugin.patch
# PATCH-FIX_OPENSUSE
Patch6:         run-salt-api-as-user-salt-bsc-990029.patch
# PATCH-FIX_OPENSUSE
Patch7:         change-travis-configuration-file-to-use-salt-toaster.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/37856 (pending to include in 2016.11)
Patch8:         setting-up-os-grains-for-sles-expanded-support-suse-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/34165
Patch9:         fix-salt-summary-to-count-not-responding-minions-cor.patch
# PATCH-FIX_OPENSUSE
Patch10:        avoid-failures-on-sles-12-sp2-because-of-new-systemd.patch
# PATCH-FIX_OPENSUSE
Patch11:        add-yum-plugin.patch
# PATCH-FIX_OPENSUSE
Patch12:        add-ssh-option-to-salt-ssh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38806
Patch13:        add-a-salt-minion-service-control-file.patch
# Description N/A
Patch14:        add-options-for-dockerng.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/39762
Patch15:        fix-regression-in-file.get_managed-add-unit-tests.patch
# PATCH-FIX_OPENSUSE
Patch16:        translate-variable-arguments-if-they-contain-hidden-.patch
# PATCH-FIX_OPENSUSE
Patch17:        special-salt-minion.service-file-for-rhel7.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40266
Patch18:        adding-support-for-installing-patches-in-yum-dnf-exe.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40761
Patch19:        search-the-entire-cache_dir-because-storage-paths-ch.patch
# PATCH-FIX_OPENSUSE
Patch20:        fixing-beacons.list-integration-test-failure.patch
# PATCH-FIX_OPENSUSE (upstream coming soon)
Patch21:        fix-grain-for-os_family-on-suse-series.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41336
Patch22:        fix-setting-language-on-suse-systems.patch
Patch23:        fix-os_family-case-in-unittest.patch
# PATCH-FIX_OPENSUSE
Patch24:        fix-format-error-bsc-1043111.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch25:        adding-salt-minion-watchdog-for-sysv-systems-rhel6-a.patch
# PATCH-FIX_OPENSUSE (only applied for RHEL6 and SLES11)
Patch26:        enables-salt-minion-watchdog-on-init.d-script-for-sy.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42944
Patch27:        add-clean_id-function-to-salt.utils.verify.py.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/37
Patch28:        revert-we-don-t-have-python-systemd-so-notify-can-t-.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1051948
Patch29:        introducing-the-kubernetes-module.patch
# PATCH-FIX_OPENSUSE https://bugzilla.suse.com/1052264
Patch30:        list_pkgs-add-parameter-for-returned-attribute-selec.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43366
#                    https://github.com/saltstack/salt/pull/43646/
Patch31:        catching-error-when-pidfile-cannot-be-deleted.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43235
#                    https://github.com/saltstack/salt/pull/43724/
Patch32:        fix-for-delete_deployment-in-kubernetes-module.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43669
Patch33:        introduce-process_count_max-minion-configuration-par.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/commit/0976f8f7131975a1ae29b2724069a301a870a46d
#                    Missed follow-up commit
Patch34:        escape-the-os.sep.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44005
Patch35:        bugfix-always-return-a-string-list-on-unknown-job-ta.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44011
Patch36:        security-fixes-cve-2017-14695-and-cve-2017-14696.patch
# PATCH-FIX_OPENSUSE bsc#1060230
Patch37:        activate-all-beacons-sources-config-pillar-grains.patch
# PATCH-FIX_OPENSUSE bsc#1041993
Patch38:        removes-beacon-configuration-deprecation-warning-48.patch
# PATCH-FIX_OPENSUSE bsc#1068446
Patch39:        bugfix-the-logic-according-to-the-exact-described-pu.patch
# PATCH-FIX_OPENSUSE
Patch40:        avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
# PATCH-FIX_OPENSUSE bsc#1071322
Patch41:        older-logrotate-need-su-directive.patch
# PATCH-FIX_OPENSUSE bsc#1065792
Patch42:        fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45060
Patch43:        feat-add-grain-for-all-fqdns.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/44991
Patch44:        split-only-strings-if-they-are-such.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/40894
Patch45:        fix-for-broken-jobs-jid-in-2016.11.4.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/45365
Patch46:        return-error-when-gid_from_name-and-group-does-not-e.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/38675
Patch47:        setvcpus-setmem-fix-return-value-parsing-issue-when-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41795
Patch48:        bugfix-use-utc-date.patch
# PATCH-FIX_OPENSUSE
Patch49:        allow-running-tests-on-python-2.6-systems.patch
# PATCH-FIX_OPENSUSE bsc#1068566
Patch50:        yumpkg-don-t-use-diff_attr-when-determining-install-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/43039
Patch51:        catch-importerror-for-kubernetes.client-import.patch
# PATCH-FIX_OPENSUSE bsc#1074227
Patch52:        fix-state-files-with-unicode-bsc-1074227.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46104
Patch53:        suppress-missing-fields-typeerror-exception-by-m2cry.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46104
Patch54:        fix-x509-unit-test-to-run-on-2016.11.4-version.patch
# PATCH-FIX_OPENSUSE https://github.com/saltstack/salt/pull/46413
Patch55:        explore-module.run-response-to-catch-the-result-in-d.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46575
Patch56:        fix-decrease-loglevel-when-unable-to-resolve-addr.patch
# PATCH-FIX_OPENSUSE bsc#1085635
Patch57:        make-module-result-usable-in-states-module.run-bsc-1.patch
# PATCH-FIX_OPENSUSE bsc#1088423
Patch58:        disable-cron-logging-only-on-sles11-systems-not-on-r.patch
# PATCH-FIX_OPENSUSE bsc#1090271
Patch59:        add-rsyslog-rule-to-avoid-salt-minion-watcher-cron-l.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46635
Patch60:        fix-for-errno-0-resolver-error-0-no-error-bsc-108758.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/41786
Patch61:        fix-regressions-from-not-calling-load_args_and_kwarg.patch
# PATCH-FIX_OPENSUSE bsc#1087342
Patch62:        backport-of-azurearm-from-salt-2018.3-to-opensuse-sa.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch63:        strip-trailing-commas-on-linux-user-gecos-fields.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47270
Patch64:        initialize-__context__-retcode-for-functions-handled.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47232
Patch65:        fixed-usage-of-ipaddress.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47211
Patch66:        fix-for-ec2-rate-limit-failures.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47471
Patch67:        do-not-override-jid-on-returners-only-sending-back-t.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47638
Patch68:        add-all_versions-parameter-to-include-all-installed-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47765
Patch69:        prevent-zypper-from-parsing-repo-configuration-from-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47149
Patch70:        add-other-attribute-to-gecos-fields-to-avoid-inconsi.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch71:        add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/42541
Patch72:        bugfix-state-file.line-warning-bsc-1093458-86.patch
# PATCH-FIX_OPENSUSE
Patch73:        add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_OPENSUSE bsc#1098394 backport of https://github.com/saltstack/salt/pull/47061
Patch74:        porting-fix-diffing-binary-files-in-file.get_diff-bs.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47405
Patch75:        fix-unboundlocalerror-in-file.get_diff.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48294
Patch76:        fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49277
Patch77:        prepend-current-directory-when-path-is-just-filename.patch
# PATCH-FIX_OPENSUSE bsc#1094960
Patch78:        backport-46867-string-arg-normalization-bsc-1094960.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49538
Patch79:        fix-for-suse-expanded-support-detection.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49532
Patch80:        fix-wrong-recurse-behavior-on-for-linux_acl.present-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50563
Patch81:        remove-arch-from-name-when-pkg.list_pkgs-is-called-w.patch
# PATCH-FIX_OPENSUSE bsc#1124290 backport of multiple commits from upstream
# https://github.com/openSUSE/salt/commit/539a25d48792e9c470722269880da73ef0a25cc7
Patch82:        fix-minion-arguments-assign-via-sysctl-bsc-1124290.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch83:        calculate-fqdns-in-parallel-to-avoid-blockings-bsc-1.patch
# PATCH-FIX_OPENSUSE bsc#1131423 https://github.com/openSUSE/salt/pull/138
Patch84:        add-optimization_order-config-option-with-default-va.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52657
Patch85:        do-not-report-patches-as-installed-when-not-all-the-.patch
# PATCH-FIX_OPENSUSE https://github.com/openSUSE/salt/pull/114
Patch86:        fix-usermod-options-for-sle11-bsc-1117017-114.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch87:        use-threadpool-from-multiprocessing.pool-to-avoid-le.patch
# PATCH-FIX_OPENSUSE bsc#1136250
Patch88:        avoid-syntax-error-on-yumpkg-module-running-on-pytho.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/53293
Patch89:        do-not-break-repo-files-with-multiple-line-values-on.patch
Patch90:        catch-sslerror-for-tls-1.2-bootstraps-with-res-rhel6.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/50197
Patch91:        backport-saltutil-state-module-to-2019.2-codebase-bs.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b713d0b3031faadc17cd9cf09977ccc19e50bef7
Patch92:        add-new-custom-suse-capability-for-saltutil-state-mo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58871
Patch93:        fix-cve-2020-25592-and-add-tests-bsc-1178319.patch


BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
BuildRequires:  %{pythonX}
BuildRequires:  %{pythonX}-devel
# requirements/base.txt
%if 0%{?rhel}
BuildRequires:  %{pythonX}-jinja2
%else
BuildRequires:  python-Jinja2
%endif
BuildRequires:  %{pythonX}-futures >= 2.0
BuildRequires:  %{pythonX}-markupsafe
%if 0%{?rhel} >= 8
BuildRequires:  %{pythonX}-msgpack > 0.3
%else
BuildRequires:  python-msgpack-python > 0.3
%endif
BuildRequires:  %{pythonX}-psutil
BuildRequires:  %{pythonX}-requests >= 1.0.0
BuildRequires:  %{pythonX}-tornado >= 4.2.1
BuildRequires:  %{pythonX}-yaml

# requirements/zeromq.txt
%if 0%{?suse_version} >= 1500
BuildRequires:       python2-M2Crypto
%else
%if 0%{?rhel} >= 8
BuildRequires:       %{pythonX}-m2crypto
%else
BuildRequires:       python-pycrypto >= 2.6.1
%endif
%endif
%if 0%{?rhel} >= 8
BuildRequires:       %{pythonX}-zmq >= 2.2.0
%else
BuildRequires:       python-pyzmq >= 2.2.0
%endif
%if %{with test}
# requirements/dev_python27.txt
BuildRequires:  %{pythonX}-boto >= 2.32.1
BuildRequires:  %{pythonX}-mock
BuildRequires:  %{pythonX}-moto >= 0.3.6
BuildRequires:  %{pythonX}-pip
BuildRequires:  %{pythonX}-salt-testing >= 2015.2.16
BuildRequires:  %{pythonX}-unittest2
BuildRequires:  %{pythonX}-xml
%endif
%if %{with builddocs}
BuildRequires:  %{pythonX}-sphinx
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

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

Requires:       procps
Requires:       logrotate
Requires:       %{pythonX}
#
%if ! 0%{?suse_version} > 1110
Requires:       %{pythonX}-certifi
%endif
# requirements/base.txt
%if 0%{?rhel}
Requires:       %{pythonX}-jinja2
Requires:       yum
%if 0%{?rhel} == 6
Requires:       yum-plugin-security
%endif
%else
Requires:       python-Jinja2
%endif
Requires:       %{pythonX}-futures >= 2.0
Requires:       %{pythonX}-markupsafe
%if 0%{?suse_version} >= 1500
Requires:       py26-compat-msgpack-python
Requires:       py26-compat-tornado
%else
%if 0%{?rhel} >= 8
Requires:       %{pythonX}-msgpack > 0.3
%else
Requires:       python-msgpack-python > 0.3
%endif
Requires:       %{pythonX}-tornado >= 4.2.1
%endif
Requires:       %{pythonX}-psutil
Requires:       %{pythonX}-requests >= 1.0.0
%if 0%{?rhel} >= 8
Requires:       %{pythonX}-backports-ssl_match_hostname
%else
Requires:       %{pythonX}-backports.ssl_match_hostname
%endif
Requires:       %{pythonX}-yaml
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
%if 0%{?suse_version} >= 1500
Requires:       python2-M2Crypto
%else
%if 0%{?rhel} >= 8
Requires:       %{pythonX}-m2crypto
%else
Requires:       python-pycrypto >= 2.6.1
%endif
%endif
%if 0%{?rhel} >= 8
Requires:       %{pythonX}-zmq >= 2.2.0
%else
Requires:       python-pyzmq >= 2.2.0
%endif
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python-xml
Suggests:       python-Mako
Recommends:     python-netaddr
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

# for salt user and /etc directory structure
BuildRequires:  salt-master
Requires(pre):  salt-master

%description
Python 2.6 compatible salt library used for thin generation.

%prep
%setup -q -n salt-%{version}
cp %{S:1} .
cp %{S:5} ./.travis.yml
%patch1 -p1

# Do not apply this patch on RHEL 6
%if 0%{?rhel} > 6 || 0%{?suse_version}
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1

# This is SUSE-only patch
%if 0%{?suse_version}
%patch5 -p1
%endif

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
%if 0%{?rhel} == 6 || 0%{?suse_version} == 1110
%patch25 -p1
%patch26 -p1
%patch40 -p1
%endif
%if 0%{?rhel} == 6
%patch58 -p1
%patch59 -p1
%endif
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1

%build
%{__python} setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt

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
%{__python} setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot} --install-lib=%{compatdir}/

mkdir -p %{buildroot}/etc/salt/master.d
%if 0%{?suse_version} >= 1500
install -m 644 %{S:7} %{buildroot}/etc/salt/master.d/py26-compat-salt.conf
%else
install -m 644 %{S:6} %{buildroot}/etc/salt/master.d
%endif

rm -rf %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/man
find %{buildroot}%{compatdir}/ -name "*.pyc" | xargs rm

%post
rm -f /var/cache/salt/master/thin/version

%files
%defattr(-,root,root,-)
%dir %{_datadir}/susemanager
%config /etc/salt/master.d/py26-compat-salt.conf

%{compatdir}
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE

%if %{with docs}
%files doc
%defattr(-,root,root)
%doc doc/_build/html
%endif

%changelog
