%global                 _enable_debug_package 0
%global                 debug_package %{nil}
%global                 __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:                   ruby2.4
Version:                2.4.1
Release:                1%{?dist}
Summary:                A dynamic, open source programming language with a focus on simplicity and productivity

License:                BSD-like
URL:                    https://www.ruby-lang.org/en/
Source0:                ruby-%{version}.tar.gz

BuildRequires:          gcc
BuildRequires:          gcc-c++
BuildRequires:          patch
BuildRequires:          make
BuildRequires:          autoconf
BuildRequires:          automake
BuildRequires:          libtool
BuildRequires:          bison
BuildRequires:          doxygen
BuildRequires:          procps
BuildRequires:          centos-release = 7

BuildRequires:          gdbm-devel
BuildRequires:          gmp-devel

BuildRequires:          readline-devel
BuildRequires:          libyaml-devel
BuildRequires:          libffi-devel
BuildRequires:          openssl-devel
BuildRequires:          jemalloc-devel
BuildRequires:          zlib-devel

BuildRequires:          tk-devel

Requires:               doxygen
Requires:               jemalloc

Conflicts:              ruby
Conflicts:              ruby2.1
Conflicts:              ruby2.2
Conflicts:              ruby2.3

%description
A dynamic, open source programming language with a focus on simplicity and productivity.
It has an elegant syntax that is natural to read and easy to write.

%prep
%setup -q -n ruby-%{version}

%build
%configure \
        --program-suffix=2.4 \
        --disable-rpath \
        --with-jemalloc \
        --disable-install-doc \
        --disable-install-rdoc

make %{?_smp_mflags}


%install
export DONT_STRIP=1
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT
make -s clean

%post
ln -sf /usr/bin/gem2.4 /usr/bin/gem
ln -sf /usr/bin/ruby2.4 /usr/bin/ruby

%postun
unlink /usr/bin/gem || true
unlink /usr/bin/ruby || true

%files
%{_bindir}/erb2.4
%{_bindir}/gem2.4
%{_bindir}/irb2.4
%{_bindir}/rake2.4
%{_bindir}/rdoc2.4
%{_bindir}/ri2.4
%{_bindir}/ruby2.4

%{_includedir}/ruby-2.4.0
%{_libdir}/ruby/2.4.0
%{_libdir}/ruby/gems/2.4.0

%{_libdir}/libruby-static.a
%{_libdir}/pkgconfig/ruby-2.4.pc

%{_mandir}/man1/erb2.4.1.gz
%{_mandir}/man1/irb2.4.1.gz
%{_mandir}/man1/ri2.4.1.gz
%{_mandir}/man1/ruby2.4.1.gz
