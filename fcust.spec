%global pypi_name fcust

Name:           %{pypi_name}
Version:        0.1.1
Release:        2%{?dist}
Summary:        Linux Common Folder Custodian

License:        GPLv3+
URL:            https://github.com/Iolaum/fcust
Source0:        %{URL}/archive/%{Version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(click) >= 7.1

%description
 The Linux Common Folder Custodian looks
 into the contents of a specified common folder
 and makes sure they have appropriate permissions.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html and man docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
PYTHONPATH=${PWD} sphinx-build-3 docs man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n %{pypi_name}
%license LICENSE
%doc html
%{_mandir}/man1/fcust.1.gz
%{_bindir}/fcust
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Sat Nov 28 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-2
- Updated packaging to build for COPR

* Sun Nov 22 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-1
- Added ability to see recent service logs.
- Releasing beta version of feature complete package.

* Tue Nov 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.14-1
- Adding functionality to create, start and stop systemd user service.

* Sat Nov 07 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.10-1
- Beta Fedora 33 rpm package release.

* Sat Oct 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.9-1
- Draft fedora 32 rpm package with core common folder maintenance functionality.
