%define upstream_name    Data-Hierarchy
%define upstream_version 0.34

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module to handle data in a hierarchical structure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
Data::Hierarchy provides a simple interface for manipulating 
inheritable data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES README 
%{perl_vendorlib}/Data
%{_mandir}/man3/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 681375
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 406971
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.34-4mdv2009.0
+ Revision: 256443
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.34-2mdv2008.1
+ Revision: 135831
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.34-2mdv2008.0
+ Revision: 64804
- rebuild


* Sat Dec 09 2006 Olivier Thauvin <nanardon@mandriva.org> 0.34-1mdv2007.0
+ Revision: 93928
- 0.34

* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.30-2mdv2007.1
+ Revision: 73149
- import perl-Data-Hierarchy-0.30-2mdv2007.1

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.30-1mdv2007.0
- New version 0.30

* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2007.0
- New release 0.22
- spec cleanup
- better source URM
- %%{1}mdv2007.1
- drop manifest from doc
- don't ship empty directories

* Wed Feb 09 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.21-2mdk
- rebuild for new perl

* Fri Nov 12 2004 Michael Scherer <misc@mandrake.org> 0.21-1mdk
- New release 0.21

* Mon Sep 27 2004 Michael Scherer <misc@mandrake.org> 0.20-1mdk
- New release 0.20

* Wed Sep 22 2004 Michael Scherer <misc@mandrake.org> 0.19-1mdk
- New release 0.19

* Sat Jun 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.18-1mdk
- 0.18
- cosmetics

* Sat Apr 03 2004 Michael Scherer <misc@mandrake.org> 0.17-1mdk
- 0.17

* Sat Apr 03 2004 Michael Scherer <misc@mandrake.org> 0.15-1mdk 
- First MandrakeSoft Package

