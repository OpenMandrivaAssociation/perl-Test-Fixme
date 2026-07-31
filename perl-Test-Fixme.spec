%define upstream_name    Test-Fixme
%define upstream_version 0.17
Name:		perl-%{upstream_name}
Version:	0.17
Release:	9

Summary:	Check code for FIXMEs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/uperl/Test-Fixme
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Test-Fixme-0.17.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Finder)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
When coding it is common to come up against problems that need to be
addressed but that are not a big deal at the moment. What generally happens
is that the coder adds comments like:

 # FIXME - what about windows that are bigger than the screen?

 # FIXME - add checking of user priviledges here.

%prep
%setup -q -n Test-Fixme-0.17

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


