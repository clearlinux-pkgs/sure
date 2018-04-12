#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sure
Version  : 1.4.9
Release  : 38
URL      : http://pypi.debian.net/sure/sure-1.4.9.tar.gz
Source0  : http://pypi.debian.net/sure/sure-1.4.9.tar.gz
Summary  : utility belt for automated testing in python for python
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: sure-python3
Requires: sure-python
Requires: python-mock
Requires: six
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
====
        
        An idiomatic testing library for python with powerful and flexible assertions. Sure

%package python
Summary: python components for the sure package.
Group: Default
Requires: sure-python3

%description python
python components for the sure package.


%package python3
Summary: python3 components for the sure package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sure package.


%prep
%setup -q -n sure-1.4.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523557669
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
