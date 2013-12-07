%define	_class	Text
%define	_subclass	Diff
%define	modname	%{_class}_%{_subclass}

Summary:	Engine for performing and rendering text diffs
Name:		php-pear-%{modname}
Version:	1.1.1
Release:	11
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Text_Diff/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package provides a text-based diff engine and renderers for
multiple diff output formats. 

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

