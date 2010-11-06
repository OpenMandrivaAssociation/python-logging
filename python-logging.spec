%define oname	logging
%define dname	%{oname}-%{version}

Name:		python-%{oname}
Summary:	Fast Python module for rational numbers
Version:	0.4.9.6
Release:	%mkrel 4
Source0:	http://www.red-dove.com/%{dname}.tar.gz
License:	MIT
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://www.red-dove.com/python_logging.html
%{py_requires}
BuildRequires:	python-devel
BuildArch:	noarch

%description
This is a python module that implements a full-featured logging system
in line with PEP 282 (comparable to java.util.logging, log4j, etc.).

%prep
%setup -q -n %{dname}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}  --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt LICENSE PKG-INFO python_logging.html default.css
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info

