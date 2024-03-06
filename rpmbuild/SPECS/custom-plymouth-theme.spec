Summary:        A custom plymouth theme
Name:           custom-plymouth-theme
Version:        1.0.0
Release:        1%{?dist}
License:        GPLv2+
Group:          System Environment/Base
URL:            https://github.com/kkklemennn/rpm-custom-plymouth-theme
Source0:	custom-plymouth-theme-1.0.0.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch
Requires:       plymouth, plymouth-plugin-script, plymouth-graphics-libs, gnu-free-sans-fonts
BuildRequires:  kernel-devel

%define themedir     %{_datadir}/plymouth/themes/custom
%define plymouthconf %{_sysconfdir}/plymouth/plymouthd.conf

%description
The %{name} package contains the custom theme for plymouth.

%prep
%autosetup -p1

%install

install -m 755 -d %{buildroot}/%{themedir}
install -m 755 -p -D custom.plymouth custom.script -t %{buildroot}/%{themedir}
install -m 755 -p -D background.png progress_bar.png progress_box.png -t %{buildroot}/%{themedir}

%files
%{themedir}/custom.plymouth
%{themedir}/custom.script
%{themedir}/background.png
%{themedir}/progress_bar.png
%{themedir}/progress_box.png

%changelog
* Wed Mar 06 2024 Klemen Klemar <klemen.klemar@hotmail.com> - 1.0.0
- Created the theme
