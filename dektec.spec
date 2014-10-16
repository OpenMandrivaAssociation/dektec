%define name dektec
%define version 0
%define release 0.20091104.3

Name:      %name
Version:   %version
Release:   %release
License:   Proprietary
Source0:   LinuxSDK.zip
Group:     Development/Kernel
Buildroot: %{_tmppath}/%{realname}-%{realversion}-%{realrelease}-buildroot
Summary:   Libraries and utilities for using Dektec cards
Url:       http://www.dektec.com/downloads/Drivers.asp
ExclusiveArch: %ix86 x86_64

%description
This package contains libraries and utilities for using Dektec cards.

%package utils
Summary:   Utilities for Dektec cards
Group:     Development/Kernel

%description utils
DtPlay:        Command-line player application
DtRecord:      Command-line recorder application
DtRmxUtil:     Command-line remultiplexing utility

%package devel
Summary:   Libraries for Dektec cards
Group:     Development/C++

%description devel
C++ API that wraps the driver calls into an easy-to-use and
object-oriented programming interface.

%prep
%setup -q -n LinuxSDK

%build
make -C DtRecord
make -C DtPlay

%install
rm -rf %buildroot

mkdir -p %buildroot%_bindir
cp -a DtPlay/DtPlay %buildroot%_bindir
cp -a DtRecord/DtRecord %buildroot%_bindir
cp -a DtRmxUtil/DtRmxUtil %buildroot%_bindir
chmod 0755 %buildroot%_bindir/DtRmxUtil

mkdir -p %buildroot%_includedir
cp -a DTAPI/Include/DTAPI.h %buildroot%_includedir
mkdir -p %buildroot%_libdir
%if "%{?_lib}" == "lib64"
cp -a DTAPI/DTAPI64.o %buildroot%_libdir
%else
cp -a DTAPI/DTAPI.o %buildroot%_libdir
%endif

%clean
rm -rf %buildroot

%files utils
%defattr(-,root,root)
%_bindir/*

%files devel
%defattr(-,root,root)
%doc DTAPI/Doc/DTAPI.pdf
%_includedir/*
%_libdir/*.o

