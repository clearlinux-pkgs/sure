#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sure
Version  : 1.4.11
Release  : 53
URL      : http://pypi.debian.net/sure/sure-1.4.11.tar.gz
Source0  : http://pypi.debian.net/sure/sure-1.4.11.tar.gz
Summary  : utility belt for automated testing in python for python
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: sure-license = %{version}-%{release}
Requires: sure-python = %{version}-%{release}
Requires: sure-python3 = %{version}-%{release}
Requires: python-mock
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-mock
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
sure
====
An idiomatic testing library for python with powerful and flexible assertions. Sure
is heavily inspired in `RSpec Expectations <http://rspec.info/documentation/3.5/rspec-expectations/>`_ and `should.js <https://github.com/shouldjs/should.js>`_

%package license
Summary: license components for the sure package.
Group: Default

%description license
license components for the sure package.


%package python
Summary: python components for the sure package.
Group: Default
Requires: sure-python3 = %{version}-%{release}

%description python
python components for the sure package.


%package python3
Summary: python3 components for the sure package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sure package.


%prep
%setup -q -n sure-1.4.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551039585
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sure
cp COPYING %{buildroot}/usr/share/package-licenses/sure/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sure/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
