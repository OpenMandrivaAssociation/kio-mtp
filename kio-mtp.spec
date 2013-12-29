%define git 20130902

Summary:	MTP Kio slave
Name:		kio-mtp
Version:	0
Release:	0.%{git}.2
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		https://projects.kde.org/projects/playground/base/kio-mtp
# From KDE's git
Source0:	%{name}-%{git}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libmtp)

%description
Kio slave providing access to MTP device using the mtp:/// protocol.

%files
%{_kde_appsdir}/konqueror/dirtree/remote/mtp-network.desktop
%{_kde_appsdir}/remoteview/mtp-network.desktop
%{_kde_appsdir}/solid/actions/solid_mtp.desktop
%{_kde_libdir}/kde4/kio_mtp.so
%{_kde_services}/mtp.protocol

#------------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{git}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

