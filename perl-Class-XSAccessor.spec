#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-XSAccessor
Version  : 1.19
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-1.19.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-1.19.tar.gz
Summary  : 'Generate fast XS accessors without runtime compilation'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-XSAccessor-lib
Requires: perl-Class-XSAccessor-man

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

%package lib
Summary: lib components for the perl-Class-XSAccessor package.
Group: Libraries

%description lib
lib components for the perl-Class-XSAccessor package.


%package man
Summary: man components for the perl-Class-XSAccessor package.
Group: Default

%description man
man components for the perl-Class-XSAccessor package.


%prep
%setup -q -n Class-XSAccessor-1.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Class/XSAccessor.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Class/XSAccessor/Array.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Class/XSAccessor/Heavy.pm

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Class/XSAccessor/XSAccessor.so

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Class::XSAccessor.3
/usr/share/man/man3/Class::XSAccessor::Array.3
/usr/share/man/man3/Class::XSAccessor::Heavy.3
