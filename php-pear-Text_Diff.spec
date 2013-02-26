%define		_class		Text
%define		_subclass	Diff
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	%mkrel 6
Summary:	Engine for performing and rendering text diffs
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Text_Diff/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
This package provides a text-based diff engine and renderers for
multiple diff output formats. 

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-4mdv2011.0
+ Revision: 667641
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.1-3mdv2011.0
+ Revision: 607145
- rebuild

* Mon Nov 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-2mdv2010.1
+ Revision: 466490
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Jul 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.1-1mdv2010.0
+ Revision: 400323
- update to new version 1.1.1

* Sun Jul 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-3mdv2010.0
+ Revision: 397468
- shipp missing classes
- don't duplicate spec-helper job

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2mdv2009.1
+ Revision: 321902
- rebuild

* Mon Oct 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 293183
- update to new version 1.1.0

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2009.0
+ Revision: 272597
- 1.0.0

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.1-4mdv2009.0
+ Revision: 224882
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdv2008.1
+ Revision: 178538
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-2mdv2008.0
+ Revision: 90118
- rebuild


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdv2007.0
+ Revision: 82749
- Import php-pear-Text_Diff

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdk
- 0.2.1
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.0.5-1mdk
- initial Mandriva package (PLD import)

