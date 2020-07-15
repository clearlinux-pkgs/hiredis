#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hiredis
Version  : 1.1.0
Release  : 9
URL      : https://files.pythonhosted.org/packages/3d/9f/abc69e73055f73d42ddf9c46b3e01a08b9e74b579b8fc413cbd31112a749/hiredis-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3d/9f/abc69e73055f73d42ddf9c46b3e01a08b9e74b579b8fc413cbd31112a749/hiredis-1.1.0.tar.gz
Summary  : Python wrapper for hiredis
Group    : Development/Tools
License  : BSD-3-Clause
Requires: hiredis-license = %{version}-%{release}
Requires: hiredis-python = %{version}-%{release}
Requires: hiredis-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# hiredis-py
[![Build Status](https://travis-ci.org/redis/hiredis-py.svg?branch=master)](https://travis-ci.org/redis/hiredis-py)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/muso9gbe316tjsac/branch/master?svg=true)](https://ci.appveyor.com/project/duyue/hiredis-py/)

%package license
Summary: license components for the hiredis package.
Group: Default

%description license
license components for the hiredis package.


%package python
Summary: python components for the hiredis package.
Group: Default
Requires: hiredis-python3 = %{version}-%{release}

%description python
python components for the hiredis package.


%package python3
Summary: python3 components for the hiredis package.
Group: Default
Requires: python3-core
Provides: pypi(hiredis)

%description python3
python3 components for the hiredis package.


%prep
%setup -q -n hiredis-1.1.0
cd %{_builddir}/hiredis-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594823536
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hiredis
cp %{_builddir}/hiredis-1.1.0/COPYING %{buildroot}/usr/share/package-licenses/hiredis/ea19b42147b760319b044ff3414b5db56513bbcf
cp %{_builddir}/hiredis-1.1.0/vendor/hiredis/COPYING %{buildroot}/usr/share/package-licenses/hiredis/e9c1298de98016808910005a33de3a5f25dce05e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hiredis/e9c1298de98016808910005a33de3a5f25dce05e
/usr/share/package-licenses/hiredis/ea19b42147b760319b044ff3414b5db56513bbcf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
