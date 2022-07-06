Summary:         Python binding for D-Bus using asyncio
Name:            python3-dbussy
Version:         1.3
Release:         1%{?dist}
License:         LGPL
URL:             https://github.com/ldo/dbussy
Source0:         https://github.com/ldo/dbussy/archive/refs/heads/master.tar.gz

BuildRequires:	 python3
BuildRequires:	 python3-setuptools	

Requires:        python3

%description
Python binding for D-Bus using asyncio

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}
%define __brp_mangle_shebangs /usr/bin/true

%prep
%setup -q -n dbussy-master

%build
python3 setup.py build

%install
python3 setup.py install  --optimize=1 \
                          --root="%{buildroot}/"

%files
/usr/lib/python3.10/site-packages/DBussy-1.3-py3.10.egg-info
/usr/lib/python3.10/site-packages/__pycache__/dbussy.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/__pycache__/dbussy.cpython-310.pyc
/usr/lib/python3.10/site-packages/__pycache__/ravel.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/__pycache__/ravel.cpython-310.pyc
/usr/lib/python3.10/site-packages/dbussy.py
/usr/lib/python3.10/site-packages/ravel.py
