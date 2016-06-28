#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sure
Version  : 1.2.24
Release  : 16
URL      : https://pypi.python.org/packages/source/s/sure/sure-1.2.24.tar.gz
Source0  : https://pypi.python.org/packages/source/s/sure/sure-1.2.24.tar.gz
Summary  : utility belt for automated testing in python for python
Group    : Development/Tools
License  : GPL-3.0+
Requires: sure-python
BuildRequires : funcsigs-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : setuptools
BuildRequires : six

%description
sure ``1.2.23``
===============
A testing library for python with powerful and flexible assertions. Sure
is heavily inspired by
`should.js <https://github.com/visionmedia/should.js/>`__

%package python
Summary: python components for the sure package.
Group: Default

%description python
python components for the sure package.


%prep
%setup -q -n sure-1.2.24

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
