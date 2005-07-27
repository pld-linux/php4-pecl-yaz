%define		_modname	yaz
%define		_status		stable

Summary:	%{_modname} - a Z39.50 client for PHP
Summary(pl):	%{_modname} - klient Z39.50 dla PHP
Name:		php4-pecl-%{_modname}
Version:	1.0.4
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	2ae4180bcfc00199c465815f89fc3b16
URL:		http://pecl.php.net/package/yaz/
BuildRequires:	libtool
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	yaz-devel
Requires:	php4-common >= 3:4.3.0
Obsoletes:	php-pear-%{_modname}
Obsoletes:	php-yaz
Obsoletes:	php4-yaz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

%description
This extension implements a Z39.50 client for PHP using the YAZ
toolkit.

Find more information at:
http://www.indexdata.dk/phpyaz/
http://www.indexdata.dk/yaz/

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie implementuje klienta Z39.50 dla PHP za pomoc� narz�dzi
YAZ.

Wi�cej informacji mo�na znale�� na stronach:
http://www.indexdata.dk/phpyaz/
http://www.indexdata.dk/yaz/

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php4-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php4-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
