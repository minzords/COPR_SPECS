Summary:         A TOML-0.4.0 parser/writer for Python.
Name:            python3-pytoml
Version:         0.1.21
Release:         1%{?dist}
License:         MIT
URL:             https://github.com/avakar/pytoml
Source0:         https://files.pythonhosted.org/packages/f4/ba/98ee2054a2d7b8bebd367d442e089489250b6dc2aee558b000e961467212/pytoml-%{version}.tar.gz

BuildRequires:	 python3
BuildRequires:	 python3-setuptools	

Requires:        python3






%description
A TOML-0.4.0 parser/writer for Python.

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}
%define __brp_mangle_shebangs /usr/bin/true

%prep
%setup -q -n pytoml-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --skip-build \
                          --optimize=1 \
                          --skip-build \
                          --root="%{buildroot}/"


%files
/usr/lib/python3.10/site-packages/pytoml-0.1.21-py3.10.egg-info/PKG-INFO
/usr/lib/python3.10/site-packages/pytoml-0.1.21-py3.10.egg-info/SOURCES.txt
/usr/lib/python3.10/site-packages/pytoml-0.1.21-py3.10.egg-info/dependency_links.txt
/usr/lib/python3.10/site-packages/pytoml-0.1.21-py3.10.egg-info/top_level.txt
/usr/lib/python3.10/site-packages/pytoml/__init__.py
/usr/lib/python3.10/site-packages/pytoml/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/core.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/core.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/parser.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/parser.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/test.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/test.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/utils.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/utils.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/writer.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/pytoml/__pycache__/writer.cpython-310.pyc
/usr/lib/python3.10/site-packages/pytoml/core.py
/usr/lib/python3.10/site-packages/pytoml/parser.py
/usr/lib/python3.10/site-packages/pytoml/test.py
/usr/lib/python3.10/site-packages/pytoml/utils.py
/usr/lib/python3.10/site-packages/pytoml/writer.py
