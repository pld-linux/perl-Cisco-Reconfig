#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Cisco
%define		pnam	Reconfig
%include	/usr/lib/rpm/macros.perl
Summary:	Cisco::Reconfig - parse and generate Cisco configuration files
Summary(pl.UTF-8):	Cisco::Reconfig - analiza i generowanie plików konfiguracyjnych Cisco
Name:		perl-Cisco-Reconfig
Version:	0.9
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c82fe91430c320904170b7f1c5d85ad3
URL:		http://search.cpan.org/dist/Cisco-Reconfig/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cisco::Reconfig makes it easier to write programs to generate changes
to Cisco configuration files. It doesn't have any real understanding
of Cisco configurations so it might be useful for other similar
configuration languages.

%description -l pl.UTF-8
Cisco::Reconfig ułatwia pisanie programów generujących zmiany w
plikach konfiguracyjnych Cisco. Nie ma prawdziwej wiedzy o
konfiguracji Cisco, więc może być przydatny dla innych podobnych
języków konfiguracyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%{perl_vendorlib}/Cisco/Reconfig.pm
%{_mandir}/man3/*
