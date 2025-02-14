Name:           mtools
Version:        4.0.35
Release:        1
Summary:        Collection of utilities to access MS-DOS disks
License:        GPLv3+
URL:            http://www.gnu.org/software/mtools/

Source0:        ftp://ftp.gnu.org/gnu/mtools/mtools-%{version}.tar.bz2

BuildRequires:  gcc texinfo autoconf

Patch1:         0001-comment-invalid-info-in-conf-file.patch

%description
Mtools is a collection of utilities to access MS-DOS disks from GNU
and Unix without mounting them. It supports Win'95 style long file names,
OS/2 Xdf disks and 2m disks (store up to 1992k on a high density 3 1/2 disk)
In addition to file access, it supports many FAT-specific features: volume
labels, FAT-specific file attributes (hidden, system, ...), "bad block" map
maintenance, access to remote floppy drives, Iomega ZIP disk protection,
"secure" erase, display of file's on-disk layout, etc

%package        help
Summary:        Including man files for mtools
Requires:       man

%description    help
This contains man files for the using of mtools.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -fiv
%configure --disable-floppyd
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{_infodir}
%makeinstall
install -m 644 mtools.conf $RPM_BUILD_ROOT/etc
gzip -9f $RPM_BUILD_ROOT/%{_infodir}/*
rm -rf ${RPM_BUILD_ROOT}/%{_mandir}/man1/floppyd*
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir.gz
ln -s mtools.5.gz %{buildroot}%{_mandir}/man5/mtools.conf.5.gz

%files
%doc README Release.notes
%license COPYING
%config(noreplace) /etc/mtools.conf
%{_bindir}/*

%files help
%{_mandir}/*/*
%{_infodir}/mtools.info*

%changelog
* Thu Nov 18 2021 Wenchao Hao <haowenchao@huawei.com> - 4.0.35-1
- update mtools version to 4.0.35

* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 4.0.26-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git

* Tue Jan 14 2020 yanglongkang <yanglongkang@huawei.com> - 4.0.26-1
- update mtools version to 4.0.26

* Thu Jul 16 2020 wuguanghao <wuguanghao3@huawei.com> - 4.0.24-1
- update mtools version to 4.0.24-1 

* Wed Jul 1 2020 Wu Bo <wubo009@163.com> - 4.0.18-20
- rebuild package

* Fri Mar 2 2020 sunshihao <sunshihao@huawei.com> - 4.0.18-19
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:comment invalid info in conf

* Fri Jan 10 2020 sunshihao <sunshihao@huawei.com> - 4.0.18-18
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:update mtools

* Fri Aug 30 2019 huangzheng <huangzheng22@huawei.com> - 4.0.18-17
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:openEuler Debranding

* Tue Aug 20 2019 huangzheng <huangzheng22@huawei.com> - 4.0.18-16
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:rename patches
