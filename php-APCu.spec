#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-APCu
Version  : 5.1.21
Release  : 21
URL      : https://pecl.php.net/get/apcu-5.1.21.tgz
Source0  : https://pecl.php.net/get/apcu-5.1.21.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-APCu-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pcre2-dev
BuildRequires : valgrind-dev

%description
APCu
====
APCu is an in-memory key-value store for PHP. Keys are of type string and values can be any PHP variables.

%package dev
Summary: dev components for the php-APCu package.
Group: Development
Requires: php-APCu-lib = %{version}-%{release}
Provides: php-APCu-devel = %{version}-%{release}
Requires: php-APCu = %{version}-%{release}

%description dev
dev components for the php-APCu package.


%package lib
Summary: lib components for the php-APCu package.
Group: Libraries

%description lib
lib components for the php-APCu package.


%prep
%setup -q -n apcu-5.1.21
cd %{_builddir}/apcu-5.1.21

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/apcu/apc.h
/usr/include/php/ext/apcu/apc_api.h
/usr/include/php/ext/apcu/apc_arginfo.h
/usr/include/php/ext/apcu/apc_cache.h
/usr/include/php/ext/apcu/apc_globals.h
/usr/include/php/ext/apcu/apc_iterator.h
/usr/include/php/ext/apcu/apc_lock.h
/usr/include/php/ext/apcu/apc_mutex.h
/usr/include/php/ext/apcu/apc_serializer.h
/usr/include/php/ext/apcu/apc_sma.h
/usr/include/php/ext/apcu/apc_stack.h
/usr/include/php/ext/apcu/php_apc.h
/usr/include/php/ext/apcu/php_apc_legacy_arginfo.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/apcu.so
