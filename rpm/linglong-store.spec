Name:           linglong-store
Version:        1.3.3.7
Release:        1
Summary:        Linglong package installer for web store
License:        LGPLv3
URL:            https://github.com/kamiyadm/%{name}
Source0:        %{url}/archive/%{version}/linglong-store-%{version}.tar.gz

BuildRequires:  cmake gcc-c++
BuildRequires:  qt5-qtbase-devel 
Requires:       linglong-installer = %{version}-%{release}

%description
This package is a tool for installing package from web store.

%package        -n linglong-installer
Summary:        Linglong package installer 
Requires:       xdg-utils
%description    -n linglong-installer
Linglong package installer for web store

%prep
%autosetup -p1 -n linglong-store-%{version}

%define _debugsource_template %{nil}

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \
      -DCMAKE_BUILD_TYPE=Release \
      -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} ..
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%post -n linglong-installer
xdg-mime default space.linglong.Installer.desktop x-scheme-handler/og

%files
%doc README.md
%license LICENSE

%files -n linglong-installer
%doc README.md
%license LICENSE
%{_bindir}/ll-installer
%{_datadir}/applications/*.desktop

%changelog
* Thu Apr 25 2024 chenhuixing <chenhuixing@deepin.org> - 1.3.3.7-1
- Init project
