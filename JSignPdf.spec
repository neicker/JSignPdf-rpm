#
# spec file for package JSignPdf
#
# Copyright (c) 2021 Norbert Eicker <norbert.eicker@gmx.de>
#

Name:           JSignPdf
Version:        2.0.0
Release:        2
Summary:        Sign PDF documents
License:        LGPL-2.1 and MPL-1.1
Group:          Productivity/Publishing/PDF
Url:            http://%{name}.sourceforge.net/
Source0:        https://sourceforge.net/projects/jsignpdf/files/stable/%{name}%20%{version}/jsignpdf-%{version}.zip
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch:          jsignpdf_sh.patch
Patch1:         JSignPdf-security.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
JSignPdf is an open-source application that adds digital signatures to
PDF documents. It’s written in Java programming language and it can be
launched on the most of current OS. Users can control the application
using simple GUI or command line arguments. Main features:

• supports visible signatures
• can set certification level
• supports PDF encryption with setting rights
• timestamp support
• certificate revocation checking (CRL and/or OCSP)

%prep
%setup -q -n jsignpdf-%{version}
%patch -p1
%patch1 -p1

%install
%__rm -rf %{buildroot}
%__install -D -m 644 *.jar -t %{buildroot}%{_libexecdir}/%{name}
%__install -D jsignpdf.sh -t %{buildroot}%{_libexecdir}/%{name}
%__install -D -m 644 conf/* -t %{buildroot}%{_libexecdir}/%{name}/conf
%__mkdir_p %{buildroot}%{_bindir}
%__ln_s %{_libexecdir}/%{name}/jsignpdf.sh %{buildroot}%{_bindir}/jsignpdf
%suse_update_desktop_file -i -r %{name} Office

%clean
rm -rf %{buildroot}

%post
%desktop_database_post
update-desktop-database

%postun
%desktop_database_postun
update-desktop-database

%files
%defattr(-,root,root)
%{_libexecdir}/%{name}/*.jar
%{_libexecdir}/%{name}/jsignpdf.sh
%dir %{_libexecdir}/%{name}/conf
%config(noreplace) %{_libexecdir}/%{name}/conf/*
%doc docs/*
%doc licenses
%{_datadir}
%{_bindir}

%changelog
* Thu Dec  9 2021 Norbert Eikcer <norbert.eicker@gmx.de>
- Add starter script to PATH
- Improve spec-file (copyrights, etc.)
* Wed Dec  8 2021 Norbert Eikcer <norbert.eicker@gmx.de>
- Initial version
