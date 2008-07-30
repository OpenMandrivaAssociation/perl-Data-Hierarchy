%define module  Data-Hierarchy
%define name    perl-%{module}
%define version 0.34
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL or Artistic
Group:          Development/Perl
Summary:        Perl module to handle data in a hierarchical structure
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::Exception)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Data::Hierarchy provides a simple interface for manipulating 
inheritable data attached to a hierarchical environment (like filesystem).

%prep
%setup -q -n %{module}-%{version}

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



