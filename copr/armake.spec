Name:           armake
Version:        0.6.3
Release:        1%{?dist}
Summary:        A C implementation of Arma modding tools (PAA conversion, binarization/rapification, PBO packing).

License:        GPLv2
URL:            https://github.com/KoffeinFlummi/armake
Source0:        https://github.com/KoffeinFlummi/armake/archive/v%{version}.tar.gz

BuildRequires:  openssl-devel bison

%description
A cross-platform, open-source C implementation of Arma modding tools (PAA conversion, binarization & rapification, PBO packing, key generation and signing).
It aims to provide a complete reimplementation of the entire process.

%prep
%autosetup


%build
%make_build


%install
rm -rf %{buildroot}
%make_install


%files
%{_bindir}/armake
%{_datarootdir}/bash-completion/completions/armake
%{_sysconfdir}/bash_completion.d/armake
%license LICENSE



%changelog
* May 23 2018 Koffeinflummi
- Fix uninitialized value used for header extensions