%global uuid tailscale@joaophi.github.com

Name:          gnome-shell-extension-tailscale-gnome-qs
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       Tailscale support for GNOME

Group:         User Interface/Desktops
License:       GPLv2
URL:           https://github.com/ublue-os/tailscale-gnome-qs
Source0:       %{url}/archive/refs/heads/master.tar.gz
BuildArch:     noarch

BuildRequires: make
BuildRequires: unzip
BuildRequires: gettext
BuildRequires: gnome-shell

Requires:    gnome-shell >= 3.12
%description
Tailscale support for GNOME

%prep
%autosetup -n tailscale-gnome-qs-master

%install
make build
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip tailscale@joaophi.github.com.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
