%define upstream_name    Data-Hierarchy
%define upstream_version 0.34
Name:		perl-%{upstream_name}
Version:	0.34
Release:	1

Summary:	Perl module to handle data in a hierarchical structure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Data-Hierarchy
Source0:	https://cpan.metacpan.org/authors/id/C/CL/CLKAO/Data-Hierarchy-0.34.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Clone)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
Data::Hierarchy provides a simple interface for manipulating 
inheritable data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n %{upstream_name}-%{version}

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


