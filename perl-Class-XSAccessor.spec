#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-XSAccessor
Version  : 1.19
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-1.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-1.19.tar.gz
Summary  : 'Generate fast XS accessors without runtime compilation'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-XSAccessor-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Class::XSAccessor - Generate fast XS accessors without runtime
compilation
SYNOPSIS
package MyClass;
use Class::XSAccessor
replace     => 1,   # Replace existing methods (if any)
constructor => 'new',
getters     => {
get_foo => 'foo', # 'foo' is the hash key to access
get_bar => 'bar',
},
setters => {
set_foo => 'foo',
set_bar => 'bar',
},
accessors => {
foo => 'foo',
bar => 'bar',
},
predicates => {
has_foo => 'foo',
has_bar => 'bar',
},
lvalue_accessors => { # see below
baz => 'baz', # ...
},
true  => [ 'is_token', 'is_whitespace' ],
false => [ 'significant' ];

# The imported methods are implemented in fast XS.

# normal class code here.

%package dev
Summary: dev components for the perl-Class-XSAccessor package.
Group: Development
Provides: perl-Class-XSAccessor-devel = %{version}-%{release}
Requires: perl-Class-XSAccessor = %{version}-%{release}

%description dev
dev components for the perl-Class-XSAccessor package.


%package perl
Summary: perl components for the perl-Class-XSAccessor package.
Group: Default
Requires: perl-Class-XSAccessor = %{version}-%{release}

%description perl
perl components for the perl-Class-XSAccessor package.


%prep
%setup -q -n Class-XSAccessor-1.19
cd %{_builddir}/Class-XSAccessor-1.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::XSAccessor.3
/usr/share/man/man3/Class::XSAccessor::Array.3
/usr/share/man/man3/Class::XSAccessor::Heavy.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Class/XSAccessor.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Class/XSAccessor/Array.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Class/XSAccessor/Heavy.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Class/XSAccessor/XSAccessor.so
