#
# spec file for package py27-compat-salt
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

%if 0%{?suse_version} > 1210 || 0%{?rhel} >= 7 || 0%{?fedora} >=28
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

%define compatdir %{_datadir}/susemanager/py27-compat
%define origname salt

Name:           py27-compat-salt
Version:        3000.3
Release:        0
Summary:        Python 2.7 compatible salt
License:        Apache-2.0
Group:          System/Management
Url:            http://saltstack.org/
BuildArch:      noarch
Source:         v%{version}.tar.gz
Source1:        README.SUSE
Source2:        salt-tmpfiles.d
Source3:        html.tar.bz2
Source4:        update-documentation.sh
Source5:        travis.yml
Source6:        py27-compat-salt.conf

Patch1:         run-salt-master-as-dedicated-salt-user.patch
Patch2:         run-salt-api-as-user-salt-bsc-1064520.patch
Patch3:         activate-all-beacons-sources-config-pillar-grains.patch
Patch4:         avoid-excessive-syslogging-by-watchdog-cronjob-58.patch
Patch5:         fix-bsc-1065792.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46684
Patch6:         add-saltssh-multi-version-support-across-python-inte.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/46890
Patch7:         fall-back-to-pymysql.patch
# PATCH-FIX_OPENSUSE bsc#1091371
Patch8:         enable-passing-a-unix_socket-for-mysql-returners-bsc.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/47638
Patch9:         add-all_versions-parameter-to-include-all-installed-.patch
# PATCH-FIX_OPENSUSE bsc#1057635
Patch10:        add-environment-variable-to-know-if-yum-is-invoked-f.patch
# PATCH-FIX_OPENSUSE
Patch11:        add-custom-suse-capabilities-as-grains.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48294
Patch12:        fix-zypper.list_pkgs-to-be-aligned-with-pkg-state.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49063
Patch13:        integration-of-msi-authentication-with-azurearm-clou.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49538
Patch14:        fix-for-suse-expanded-support-detection.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/48812
Patch15:        use-adler32-algorithm-to-compute-string-checksums.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49497
Patch16:        x509-fixes-111.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49696
Patch17:        loosen-azure-sdk-dependencies-in-azurearm-cloud-driv.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49737
Patch18:        do-not-load-pip-state-if-there-is-no-3rd-party-depen.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49815
Patch19:        fix-ipv6-scope-bsc-1108557.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49480
Patch20:        early-feature-support-config.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49936
Patch21:        make-profiles-a-package.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49946
Patch22:        add-cpe_name-for-osversion-grain-parsing-u-49946.patch
# PATCH-FIX_OPENSUSE: Fix unit test for grains core
Patch23:        fix-unit-test-for-grains-core.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50095
Patch24:        support-config-non-root-permission-issues-fixes-u-50.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50018
Patch25:        add-multi-file-support-and-globbing-to-the-filetree-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/49761
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50201
Patch26:        fixes-cve-2018-15750-cve-2018-15751.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50417
Patch27:        fix-git_pillar-merging-across-multiple-__env__-repos.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50523
Patch28:        get-os_arch-also-without-rpm-package-installed.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50392
Patch29:        make-aptpkg.list_repos-compatible-on-enabled-disable.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50453
Patch30:        debian-info_installed-compatibility-50453.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50742
Patch31:        decide-if-the-source-should-be-actually-skipped.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50773
Patch32:        add-hold-unhold-functions.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50401
# NOTE: This is a techpreview as well as in Fluorine! Release only in Neon.
Patch33:        add-supportconfig-module-for-remote-calls-and-saltss.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/116
Patch34:        return-the-expected-powerpc-os-arch-bsc-1117995.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51108
Patch35:        remove-arch-from-name-when-pkg.list_pkgs-is-called-w.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51119
Patch36:        fix-issue-2068-test.patch
# PATCH_FIX_OPENSUSE: Temporary fix allowing "id_" and "force" params while upstrem figures it out
Patch37:        temporary-fix-extend-the-whitelist-of-allowed-comman.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51382
Patch38:        don-t-call-zypper-with-more-than-one-no-refresh.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50109
# PATCH_FIX_OPENSUSE https://github.com/openSUSE/salt/pull/121
Patch39:        add-virt.all_capabilities.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51384
Patch40:        include-aliases-in-the-fqdns-grains.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/50546
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/51863
Patch41:        async-batch-implementation.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch42:        calculate-fqdns-in-parallel-to-avoid-blockings-bsc-1.patch
#PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/139
Patch43:        fix-async-batch-race-conditions.patch
#PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/141
Patch44:        add-batch_presence_ping_timeout-and-batch_presence_p.patch
#PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/52657
Patch45:        do-not-report-patches-as-installed-when-not-all-the-.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52527
Patch46:        use-threadpool-from-multiprocessing.pool-to-avoid-le.patch
# PATCH-FIX_UPSTREAM https://github.com/saltstack/salt/pull/52888
Patch47:        do-not-crash-when-there-are-ipv6-established-connect.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/144
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/52855
Patch48:        fix-async-batch-multiple-done-events.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/52743
Patch49:        switch-firewalld-state-to-use-change_interface.patch
# PATCH-FIX_OPENSUSE
Patch50:        add-standalone-configuration-file-for-enabling-packa.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53293
Patch51:        do-not-break-repo-files-with-multiple-line-values-on.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53159
Patch52:        batch.py-avoid-exception-when-minion-does-not-respon.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53471
Patch53:        fix-zypper-pkg.list_pkgs-expectation-and-dpkg-mockin.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/161
Patch54:        provide-the-missing-features-required-for-yomi-yet-o.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53661
Patch55:        do-not-make-ansiblegate-to-crash-on-python3-minions.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53693
Patch56:        allow-passing-kwargs-to-pkg.list_downloaded-bsc-1140.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53661
Patch57:        prevent-ansiblegate-unit-tests-to-fail-on-ubuntu.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54048
Patch58:        avoid-traceback-when-http.query-request-cannot-be-pe.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53992
#                     https://github.com/saltstack/salt/pull/53996
#                     https://github.com/saltstack/salt/pull/54022
#                     https://github.com/saltstack/salt/pull/54024
Patch59:        accumulated-changes-required-for-yomi-165.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/159
Patch60:        move-server_id-deprecation-warning-to-reduce-log-spa.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54077
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/166
Patch61:        fix-aptpkg-systemd-call-bsc-1143301.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/170
Patch62:        strip-trailing-from-repo.uri-when-comparing-repos-in.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/177
Patch63:        restore-default-behaviour-of-pkg-list-return.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/172
Patch64:        implement-network.fqdns-module-function-bsc-1134860-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/6af07030a502c427781991fc9a2b994fa04ef32e
Patch65:        fix-memory-leak-produced-by-batch-async-find_jobs-me.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/002543df392f65d95dbc127dc058ac897f2035ed
Patch66:        improve-batch_async-to-release-consumed-memory-bsc-1.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54077
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/44a91c2ce6df78d93ce0ef659dedb0e41b1c2e04
Patch67:        prevent-systemd-run-description-issue-when-running-a.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/55d8a777d6a9b19c959e14a4060e5579e92cd106
Patch68:        use-current-ioloop-for-the-localclient-instance-of-b.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/8378bb24a5a53973e8dba7658b8b3465d967329f
Patch69:        fix-failing-unit-tests-for-batch-async.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54935
Patch70:        add-missing-fun-for-returns-from-wfunc-executions.patch
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53326
# PATCH_FIX_UPSTREAM: https://github.com/saltstack/salt/pull/54954
Patch71:        accumulated-changes-from-yomi-167.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/180
Patch72:        fix-a-wrong-rebase-in-test_core.py-180.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/182
Patch73:        remove-unnecessary-yield-causing-badyielderror-bsc-1.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/186
Patch74:        read-repo-info-without-using-interpolation-bsc-11356.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53293
Patch75:        prevent-test_mod_del_repo_multiline_values-to-fail.patch
Patch76:        fix-for-log-checking-in-x509-test.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/190
Patch77:        fixing-streamclosed-issue.patch
Patch78:        fix-batch_async-obsolete-test.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/191
Patch79:        let-salt-ssh-use-platform-python-binary-in-rhel8-191.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/193
Patch80:        xfs-do-not-fails-if-type-is-not-present.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/55245
Patch81:        virt-adding-kernel-boot-parameters-to-libvirt-xml-55.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/200
Patch82:        support-for-btrfs-and-xfs-in-parted-and-mkfs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56125
Patch83:        add-astra-linux-common-edition-to-the-os-family-list.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/211
Patch84:        apply-patch-from-upstream-to-support-python-3.8.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/217
Patch85:        batch_async-avoid-using-fnmatch-to-match-event-217.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/8a23030d347b7487328c0395f5e30ef29daf1455
Patch86:        batch-async-catch-exceptions-and-safety-unregister-a.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/a38adfa2efe40c2b1508b685af0b5d28a6bbcfc8
Patch87:        fix-unit-tests-for-batch-async-after-refactor.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/218
Patch88:        use-full-option-name-instead-of-undocumented-abbrevi.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/93c0630b84b9da89acaf549a5c79e5d834c70a65
Patch89:        removes-unresolved-merge-conflict-in-yumpkg-module.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b4c401cfe6031b61e27f7795bfa1aca6e8341e52
Patch90:        changed-imports-to-vendored-tornado.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/082fa07e5301414b5b834b731aaa96bd5d966de7
Patch91:        add-missing-_utils-at-loader-grains_func.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/25b4e3ea983b2606b2fb3d3c0e42f9840208bf84
Patch92:        remove-deprecated-usage-of-no_mock-and-no_mock_reaso.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/a8f0a15e4067ec278c8a2d690e3bf815523286ca
Patch93:        fix-wrong-test_mod_del_repo_multiline_values-test-af.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56369
Patch94:        make-salt.ext.tornado.gen-to-use-salt.ext.backports_.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/221
Patch95:        loader-invalidate-the-import-cachefor-extra-modules.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/55814
Patch96:        opensuse-3000-virt-defined-states-222.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/223
Patch97:        fix-for-temp-folder-definition-in-loader-unit-test.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56392
Patch98:        virt._get_domain-don-t-raise-an-exception-if-there-i.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/226
Patch99:        re-adding-function-to-test-for-root.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/227
Patch100:       loop-fix-variable-names-for-until_no_eval.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/226
Patch101:       make-setup.py-script-to-not-require-setuptools-9.1.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/50453
#                     https://github.com/saltstack/salt/commit/e20362f6f053eaa4144583604e6aac3d62838419
# Can be dropped one pull/50453 is in released version.
Patch102:       reintroducing-reverted-changes.patch
# PATCH_FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/b713d0b3031faadc17cd9cf09977ccc19e50bef7
Patch103:       add-new-custom-suse-capability-for-saltutil-state-mo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56463
Patch104:       fix-typo-on-msgpack-version-when-sanitizing-msgpack-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56491
Patch105:       sanitize-grains-loaded-from-roster_grains.json.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/228
Patch106:       adds-explicit-type-cast-for-port.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/53882
Patch107:       fixed-bug-lvm-has-no-parttion-type.-the-scipt-later-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/4f80e969e31247a4755d98d25f29b5d8b1b916c3
Patch108:       remove-vendored-backports-abc-from-requirements.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57119
Patch109:       make-lazyloader.__init__-call-to-_refresh_file_mappi.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57123
Patch110:       prevent-logging-deadlock-on-salt-api-subprocesses-bs.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57122
Patch111:       msgpack-support-versions-1.0.0.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/235
Patch112:       python3.8-compatibility-pr-s-235.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56419
Patch113:       option-to-en-disable-force-refresh-in-zypper-215.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/229
Patch114:       fix-a-test-and-some-variable-names-229.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56439
Patch115:       add-docker-logout-237.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56595
Patch116:       fix-for-return-value-ret-vs-return-in-batch-mode.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57392
Patch117:       zypperpkg-filter-patterns-that-start-with-dot-244.patch
# PATCH-FIX_OPENSUSE: hhttps://github.com/openSUSE/salt/commit/da936daeebd701e147707ad814c07bfc259d4be
Patch118:       add-publish_batch-to-clearfuncs-exposed-methods.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57489
Patch119:       avoid-has_docker-true-if-import-messes-with-salt.uti.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57779
Patch120:       info_installed-works-without-status-attr-now.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57491
Patch121:       opensuse-3000.3-spacewalk-runner-parse-command-250.patch
# PATCH-FIX_UPSTREAM: https://github.com/openSUSE/salt/pull/251
Patch122:       opensuse-3000-libvirt-engine-fixes-251.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58013
Patch123:       fix-__mount_device-wrapper-254.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58214
Patch124:       ansiblegate-take-care-of-failed-skipped-and-unreacha.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58301
Patch125:       do-not-raise-streamclosederror-traceback-but-only-lo.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/257
Patch126:       opensuse-3000.2-virt-backports-236-257.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/256
Patch127:       backport-virt-patches-from-3001-256.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/262
Patch128:       fix-the-removed-six.itermitems-and-six.-_type-262.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/263
Patch129:       fix-virt.update-with-cpu-defined-263.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/261
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57571
Patch130:       remove-msgpack-1.0.0-requirement-in-the-installed-me.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/bc20f38d0fa492af70321fef7fe2530937dfc86a
Patch131:       prevent-import-errors-when-running-test_btrfs-unit-t.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58529
Patch132:       invalidate-file-list-cache-when-cache-file-modified-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58400
Patch133:       xen-disk-fixes-264.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58552
Patch134:       zypperpkg-ignore-retcode-104-for-search-bsc-1176697-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch135:       support-transactional-systems-microos-271.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/272
Patch136:       backport-a-few-virt-prs-272.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/275
Patch137:       bsc-1176024-fix-file-directory-user-and-group-owners.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/277
Patch138:       fix-grains.test_core-unit-test-277.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/e2c3b1cb72b796fe12f94af64baa2e64cbe5db0b
Patch139:       drop-wrong-mock-from-chroot-unit-test.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/280
Patch140:       ensure-virt.update-stop_on_reboot-is-updated-with-it.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/281
Patch141:       path-replace-functools.wraps-with-six.wraps-bsc-1177.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58560
Patch142:       fix-novendorchange-option-284.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58871
Patch143:       fix-cve-2020-25592-and-add-tests-bsc-1178319.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/293
Patch144:       set-passphrase-for-salt-ssh-keys-to-empty-string-293.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/279
Patch145:       fix-for-bsc-1102248-psutil-is-broken-and-so-process-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/286
Patch146:       grains-master-can-read-grains.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58784
Patch147:       add-migrated-state-and-gpg-key-management-functions-.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/292
Patch148:       transactional_update-unify-with-chroot.call.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/295
Patch149:       pkgrepo-support-python-2.7-function-call-295.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/298
Patch150:       fix-salt.utils.stringutils.to_str-calls-to-make-it-w.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/303
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58859
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59007
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58196
Patch151:       opensuse-3000.3-bigvm-backports-303.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58262
Patch152:       add-pkg.services_need_restart-302.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/301
Patch153:       add-patch-support-for-allow-vendor-change-option-wit.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/304
Patch154:       force-zyppnotify-to-prefer-packages.db-than-packages.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/commit/4028fd6e84d882b6dcee695d409c7e1ed6c83bdc
Patch155:       revert-add-patch-support-for-allow-vendor-change-opt.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59345
Patch156:       fix-onlyif-unless-when-multiple-conditions-bsc-11808.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59354
Patch157:       do-not-crash-when-unexpected-cmd-output-at-listing-p.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59189
Patch158:       virt-uefi-fix-backport-312.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59355
#                     https://github.com/saltstack/salt/pull/59417
Patch159:       3002.2-xen-spicevmc-dns-srv-records-backports-314.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59485
Patch160:       open-suse-3002.2-xen-grub-316.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56173
Patch161:       fixes-56144-to-enable-hotadd-profile-support.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/307
Patch162:       add-sleep-on-exception-handling-on-minion-connection.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/commit/a715b2c2a985f4fe9db3438cddc6efb29c87fd65
Patch163:       fix-recursion-false-detection-in-payload-bsc-1180101.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/324
Patch164:       implementation-of-suse_ip-execution-module-bsc-10999.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58591
Patch165:       backport-commit-1b16478c51fb75c25cd8d217c80955feefb6.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch166:       fix-for-some-cves-bsc1181550.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch167:       allow-extra_filerefs-as-sanitized-kwargs-for-ssh-cli.patch
# PATCH-FIX_UPSTREAM: no PR to link to yet
Patch168:       fix-regression-on-cmd.run-when-passing-tuples-as-cmd.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59524
Patch169:       prevent-race-condition-on-sigterm-for-the-minion-bsc.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59746
Patch170:       do-not-monkey-patch-yaml-bsc-1177474.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59146
#                     https://github.com/saltstack/salt/pull/59355
#                     https://github.com/saltstack/salt/pull/59693
Patch171:       opensuse-3000-virtual-network-backports-329.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/313
Patch172:       allow-vendor-change-option-with-zypper-313.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59404
Patch173:       add-almalinux-and-alibaba-cloud-linux-to-the-os-fami.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58364
Patch174:       fix-zmq-hang-backport-of-saltstack-salt-58364.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/331
Patch175:       update-target-fix-for-salt-ssh-and-avoiding-race-con.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59687
Patch176:       backport-of-https-github.com-saltstack-salt-pull-596.patch
# PATCH-FIX_OPENSUSE: https://github.com/openSUSE/salt/pull/353
Patch177:       regression-fix-of-salt-ssh-on-processing-targets-353.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60056
Patch178:       improvements-on-ansiblegate-module-354.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch179:       transactional_update-detect-recursion-in-the-executo.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59648
Patch180:       prevent-command-injection-in-the-snapper-module-bsc-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60056
Patch181:       fix-issue-parsing-errors-in-ansiblegate-state-module.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/57881
Patch182:       parsing-epoch-out-of-version-provided-during-pkg-rem.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58503
Patch183:       fix-missing-minion-returns-in-batch-mode-360.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch184:       grains.extra-support-old-non-intel-kernels-bsc-11806.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60133
Patch185:       handle-volumes-on-stopped-pools-in-virt.vm_info-375.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60229
Patch186:       figure-out-python-interpreter-to-use-inside-containe.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60402
Patch187:       enhance-logging-when-inotify-beacon-is-missing-pyino.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60421
Patch188:       move-vendor-change-logic-to-zypper-class-355.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60420
Patch189:       virt-use-dev-kvm-to-detect-kvm-385.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60358
Patch190:       fix-save-for-iptables-state-module-bsc-1185131-371.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60356
Patch191:       fix-exception-in-yumpkg.remove-for-not-installed-pac.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/56935
#                     https://github.com/saltstack/salt/pull/60432
Patch192:       implementation-of-held-unheld-functions-for-state-pk.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/60492
Patch193:       virt-pass-emulator-when-getting-domain-capabilities-.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/59756
Patch194:       enhance-openscap-module-add-xccdf_eval-call-395.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch195:       handle-master-tops-data-when-states-are-applied-by-t.patch
# PATCH-FIX_UPSTREAM: https://github.com/saltstack/salt/pull/58520
Patch196:       do-noop-for-services-states-when-running-systemd-in-.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  logrotate
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

BuildRequires:  python >= 2.7
BuildRequires:  python-devel >= 2.7
BuildRequires:  python-setuptools
# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
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
BuildRequires:  python-singledispatch

# requirements/zeromq.txt
%if 0%{?suse_version} >= 1500
BuildRequires:       python2-M2Crypto
%else
BuildRequires:       python-pycrypto >= 2.6.1
%endif
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
Requires:       python-certifi
# requirements/base.txt
%if 0%{?rhel} || 0%{?fedora}
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
Requires:       python-singledispatch
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
Requires:       python-pycrypto >= 2.6.1
%endif
Requires:       python-pyzmq >= 2.2.0
#
%if 0%{?suse_version}
# python-xml is part of python-base in all rhel versions
Requires:       python-xml
Suggests:       python-Mako
Recommends:     python-netaddr
Recommends:     python-pyinotify
%endif

Provides:       bundled(python-tornado) = 4.5.3

%if %{with systemd}
%{?systemd_requires}
%else
%if 0%{?suse_version}
Requires(pre): %insserv_prereq
%endif
%endif
%if 0%{?suse_version}
Requires(pre):  %fillup_prereq
%endif



# for salt user and /etc directory structure
BuildRequires:  salt-master
Requires(pre):  salt-master

%description
Python 2.7 compatible salt library used for thin generation.

%prep
%setup -q -n salt-%{version}-suse
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
%patch40 -p1
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
%patch58 -p1
%patch59 -p1
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
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p1
%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1

%build
# Putting /usr/bin at the front of $PATH is needed for RHEL/RES 7. Without this
# change, the RPM will require /bin/python, which is not provided by any package
# on RHEL/RES 7.
%if 0%{?fedora} || 0%{?rhel}
export PATH=/usr/bin:$PATH
%endif
python setup.py --with-salt-version=%{version} --salt-transport=both build
cp ./build/lib/salt/_version.py ./salt
mv build _build.python2

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
mv _build.python2 build
python setup.py --salt-transport=both install --prefix=%{_prefix} --root=%{buildroot} --install-lib=%{compatdir}/
mv build _build.python2

mkdir -p %{buildroot}/etc/salt/master.d
install -m 644 %{S:6} %{buildroot}/etc/salt/master.d/py27-compat-salt.conf

rm -rf %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/share/man
find %{buildroot}%{compatdir}/ -name "*.pyc" | xargs rm

%post
rm -f /var/cache/salt/master/thin/version
rm -f /var/cache/salt/master/thin/thin.tgz

%files
%defattr(-,root,root,-)
%dir %{_datadir}/susemanager
%config /etc/salt/master.d/py27-compat-salt.conf

%{compatdir}
%doc LICENSE AUTHORS README.rst HACKING.rst README.SUSE

%changelog
