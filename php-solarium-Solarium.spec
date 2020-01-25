%define		package	Solarium
%define		php_min_version 5.3.0
Summary:	Solarium PHP Solr client library
Name:		php-solarium-Solarium
Version:	3.1.2
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/basdenooijer/solarium/archive/%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	99fa934be12783063b140717c819ebac
URL:		http://www.solarium-project.org/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(date)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-symfony2-EventDispatcher
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Solarium is a PHP Solr client library that accurately model Solr
concepts. Where many other Solr libraries only handle the
communication with Solr, Solarium also relieves you of handling all
the complex Solr query parameters using a well documented API.

%prep
%setup -q -n solarium-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a library/Solarium $RPM_BUILD_ROOT%{php_data_dir}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md COPYING
%{php_data_dir}/Solarium
%{_examplesdir}/%{name}-%{version}
