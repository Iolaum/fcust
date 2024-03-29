%global pypi_name fcust

Name:           %{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Linux Common Folder Custodian

License:        GPLv3+
URL:            https://github.com/Iolaum/fcust
# taken from the archive created from `make dist` command, use to test locally
# https://asamalik.fedorapeople.org/tmp-docs-preview/packaging-guidelines/SourceURL/
# Source0:        %{pypi_name}-%{version}.tar.gz
Source0:        %{URL}/releases/latest/download/fcust-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# BuildRequires:  sudo
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(click) >= 7.1
BuildRequires:  python3dist(cffi)

%description
 The Linux Common Folder Custodian looks
 into the contents of a specified common folder
 and makes sure they have appropriate permissions.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
pip install --user --upgrade pip
%py3_build
# generate html and man docs
#sphinx-build-3 -b html docs/html docs/_build/html
sphinx-build-3 -b man docs docs/_build/man
sphinx-build-3 -b html docs docs/_build/html
rm -rf docs/_build/html/{.doctrees,.buildinfo}

%install
%py3_install

# Adapted from https://src.fedoraproject.org/rpms/python-pip/blob/a1e1c1dfc94168da1d9130179a86297c64a9488f/f/python-pip.spec#_302-310
pushd docs/_build/man
install -d %{buildroot}%{_mandir}/man1
for MAN in *1; do
install -pm0644 $MAN %{buildroot}%{_mandir}/man1/$MAN
done
popd

%files -n %{pypi_name}
%license LICENSE
%doc docs/_build/html
%{_mandir}/man1/fcust.*
%{_bindir}/fcust
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog

* Wed Dec 28 2022 Nikolaos Perrakis <nikperrakis@gmail.com> - 1.0.1-1
- Updated package to use pyproject.toml.
- Upgrade package for Fedora 37

* Mon Dec 05 2022 Nikolaos Perrakis <nikperrakis@gmail.com> - 1.0.0-2
- Upgrade specfile

* Sun Nov 21 2021 Nikolaos Perrakis <nikperrakis@gmail.com> - 1.0.0-1
- Updated package for Fedora 35.
- Releasing production version.

* Tue Dec 01 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-6
- Fix COPR build for aarch64

* Tue Dec 01 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-4
- Fix COPR build for Fedora 32

* Mon Nov 30 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-3
- Updated documentation for COPR usage.

* Sat Nov 28 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-2
- Updated packaging to build for COPR.

* Sun Nov 22 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.1.1-1
- Added ability to see recent service logs.
- Releasing beta version of feature complete package.

* Tue Nov 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.14-1
- Adding functionality to create, start and stop systemd user service.

* Sat Nov 07 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.10-1
- Beta Fedora 33 rpm package release.

* Sat Oct 10 2020 Nikolaos Perrakis <nikperrakis@gmail.com> - 0.0.9-1
- Draft fedora 32 rpm package with core common folder maintenance functionality.
