# Created by pyp2rpm-3.3.4
%global pypi_name fcust

Name:           python-%{pypi_name}
Version:        0.0.5
Release:        1%{?dist}
Summary:        Linux Common Folder Custodian

License:        GNU General Public License v3
URL:            https://github.com/Iolaum/fcust
Source0:        %{pypi_source}
BuildArch:      noarch

# BuildRequires:  python3-devel
# BuildRequires:  python3dist(black)
# BuildRequires:  python3dist(bump2version) >= 1
# BuildRequires:  python3dist(check-manifest)
# BuildRequires:  python3dist(click) >= 7.1
# BuildRequires:  python3dist(coverage)
# BuildRequires:  python3dist(doc8)
# BuildRequires:  python3dist(flake8)
# BuildRequires:  python3dist(mock)
# BuildRequires:  python3dist(mypy)
# BuildRequires:  python3dist(pip)
# BuildRequires:  python3dist(pytest)
# BuildRequires:  python3dist(pytest-runner)
# BuildRequires:  python3dist(setuptools)
# BuildRequires:  python3dist(sphinx) >= 3.2.1
# BuildRequires:  python3dist(tox)
# BuildRequires:  python3dist(twine) >= 3.2
# BuildRequires:  python3dist(wheel) >= 0.35.1
# BuildRequires:  python3dist(yamllint)
# BuildRequires:  python3dist(sphinx)

%description
 Folder Custodian Linux Common Folder Custodian * Free software: GNU General
Public License v3

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(click) >= 7.1
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 Folder Custodian Linux Common Folder Custodian * Free software: GNU General
Public License v3

%package -n python-%{pypi_name}-doc
Summary:        fcust documentation
%description -n python-%{pypi_name}-doc
Documentation for fcust

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst docs/readme.rst
%{_bindir}/fcust
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Sat Oct 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.5-1
- Initial package.
