%define upstream_name    Data-Hierarchy
%define upstream_version 0.34

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl module to handle data in a hierarchical structure
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::Exception)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Data::Hierarchy provides a simple interface for manipulating 
inheritable data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README 
%{perl_vendorlib}/Data
%{_mandir}/man3/*
