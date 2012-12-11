%define oname	logging
%define dname	%{oname}-%{version}

Name:		python-%{oname}
Summary:	Fast Python module for rational numbers
Version:	0.4.9.6
Release:	5
Source0:	http://www.red-dove.com/%{dname}.tar.gz
License:	MIT
Group:		Development/Python
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
python setup.py install --root %{buildroot}  --compile --optimize=2

%files
%doc README.txt LICENSE PKG-INFO python_logging.html default.css
%{py_puresitedir}/%{oname}
%{py_puresitedir}/%{oname}-%{version}-py%{py_ver}.egg-info



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.4.9.6-4mdv2011.0
+ Revision: 594041
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.9.6-3mdv2010.0
+ Revision: 442295
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.4.9.6-2mdv2009.1
+ Revision: 323757
- rebuild

* Fri Sep 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.9.6-1mdv2009.0
+ Revision: 284046
- clean file list
- package license
- generate pyc and pyo files
- s,$RPM_BUILD_ROOT,%%{buildroot}
- clean python requires
- correct license
- source location
- tabs not spaces
- drop unnecessary defines
- new release 0.4.9.6

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.4.7-3mdk
- Rebuild for new python

* Sat Aug 09 2003 Austin Acton <aacton@yorku.ca> 0.4.7-2mdk
- python 2.3

* Wed Jul 09 2003 Austin Acton <aacton@yorku.ca> 0.4.7-1mdk
- from andi payn <payn@myrealbox.com> :
  - Initial specfile

