%define		kdeplasmaver	5.14.4
%define		qtver		5.3.2
%define		kpname		ksshaskpass
Summary:	ssh-add helper that uses kwallet and kpassworddialog
Name:		kp5-%{kpname}
Version:	5.14.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	878b25b3c87b13030b303c7f667c450a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kwallet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ssh-add helper that uses kwallet and kpassworddialog.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksshaskpass
#%{_desktopdir}/org.kde.ksshaskpass.desktop
%{_mandir}/man1/ksshaskpass.1*

