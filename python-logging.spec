%define version 0.4.7
%define release %mkrel 4
%define oname logging
%define dname %{oname}-%{version}

Name: python-%oname
Version: %{version}
Release: %{release}
Source: %{dname}.tar.bz2
Summary: Fast Python module for rational numbers
License: Distributable
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://www.red-dove.com/python_logging.html
Requires: python >= %{pyver}
BuildRequires: python >= %{pyver}
BuildRequires: libpython-devel >= %{pyver}
BuildArch: noarch

%description
This is a python module that implements a full-featured logging system
in line with PEP 282 (comparable to java.util.logging, log4j, etc.).

%prep
%setup -q -n %{dname}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.txt PKG-INFO python_logging.html default.css
%{_libdir}/python%{pyver}/site-packages/logging/

