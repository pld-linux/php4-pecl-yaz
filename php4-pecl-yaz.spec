%define		_modname	yaz
%define		_status		stable
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

Summary:	%{_modname} - a Z39.50 client for PHP
Summary(pl.UTF-8):   %{_modname} - klient Z39.50 dla PHP
Name:		php4-pecl-%{_modname}
Version:	1.0.7
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	e240666711bfd9936bb9632272a53ecc
URL:		http://pecl.php.net/package/yaz/
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	rpmbuild(macros) >= 1.322
BuildRequires:	yaz-devel
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
Obsoletes:	php-yaz
Obsoletes:	php4-yaz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension implements a Z39.50 client for PHP using the YAZ
toolkit.

Find more information at: <http://www.indexdata.dk/phpyaz/>
<http://www.indexdata.dk/yaz/>.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
To rozszerzenie implementuje klienta Z39.50 dla PHP za pomocą narzędzi
YAZ.

Więcej informacji można znaleźć na stronach:
<http://www.indexdata.dk/phpyaz/> <http://www.indexdata.dk/yaz/>.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
