# Originally created by pyp2rpm-3.3.4
%global pypi_name fcust

Name:           python-%{pypi_name}
Version:        0.0.10
Release:        1%{?dist}
Summary:        Linux Common Folder Custodian

License:        GPLv3+
URL:            https://github.com/Iolaum/fcust
Source0:        %{pypi_source}
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
 

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(click) >= 7.1
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 The Linux Common Folder Custodian looks
 into the contents of a specified common folder
 and makes sure they have appropriate permissions.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for fcust
%description -n python-%{pypi_name}-doc
Documentation for Linux Common Folder Custodian

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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_mandir}/man1/fcust.1.gz
%{_bindir}/fcust
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Nov 07 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.10-1
- Beta Fedora 33 rpm package release.

* Sat Oct 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.9-1
- Draft fedora 32 rpm package with core common folder maintenance functionality.