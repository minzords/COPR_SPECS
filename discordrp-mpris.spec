Summary:         Discord Rich Presence based on mpris2 media players
Name:            discordrp-mpris
Version:         0.3.2
Release:         1%{?dist}
License:         MIT
URL:             https://github.com/FichteFoll/discordrp-mpris
Source0:         https://github.com/FichteFoll/discordrp-mpris/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	 python3
BuildRequires:	 python3-setuptools	

Requires:        python3
Requires:	 python3-pytoml
Requires:	 python3-dbussy

%description
Discord Rich Presence based on mpris2 media players

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}
%define __brp_mangle_shebangs /usr/bin/true

%prep
%setup -q -n %{name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install  --optimize=1 \
                          --root="%{buildroot}/"
                          
install -D -m644 LICENSE "%{buildroot}/usr/share/licenses/%{name}/LICENSE"
install -D -m644 systemd/discordrp-mpris.service "%{buildroot}/usr/lib/systemd/user/discordrp-mpris.service"


%files
/usr/bin/discordrp-mpris
/usr/lib/python3.10/site-packages/ampris2/__init__.py
/usr/lib/python3.10/site-packages/ampris2/__main__.py
/usr/lib/python3.10/site-packages/ampris2/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/ampris2/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/ampris2/__pycache__/__main__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/ampris2/__pycache__/__main__.cpython-310.pyc
/usr/lib/python3.10/site-packages/discord_rpc/__init__.py
/usr/lib/python3.10/site-packages/discord_rpc/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/discord_rpc/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/discord_rpc/__pycache__/async_.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/discord_rpc/__pycache__/async_.cpython-310.pyc
/usr/lib/python3.10/site-packages/discord_rpc/async_.py
/usr/lib/python3.10/site-packages/discordrp_mpris/__init__.py
/usr/lib/python3.10/site-packages/discordrp_mpris/__main__.py
/usr/lib/python3.10/site-packages/discordrp_mpris/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/__pycache__/__main__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/__pycache__/__main__.cpython-310.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/config/__init__.py
/usr/lib/python3.10/site-packages/discordrp_mpris/config/__pycache__/__init__.cpython-310.opt-1.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/config/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3.10/site-packages/discordrp_mpris/config/config.toml
/usr/lib/systemd/user/discordrp-mpris.service
/usr/share/licenses/discordrp-mpris/LICENSE
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/PKG-INFO
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/SOURCES.txt
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/dependency_links.txt
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/entry_points.txt
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/requires.txt
/usr/lib/python3.10/site-packages/discordrp_mpris-0.3.2-py3.10.egg-info/top_level.txt

