Summary:	renattach - rename/delete dangerous email attachments
Summary(pl):	renattach - zmiana nazwy/usuwanie niebezpiecznych za³±czników email
Name:		renattach
Version:	1.2.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Mail
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	bd6bbcb74d8a7f8a94655aa73c1ab5ce
Patch0:	%{name}-getopt_in_glibc.patch
URL:		http://www.pc-tools.net/unix/renattach/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
renattach is a fast and efficient UNIX stream filter that can rename
or delete potentially dangerous e-mail attachments. It's a highly
effective way of protecting end-users from harmful mail content
(worms/viruses) by disabling or removing attachments that may be
accidentally executed by users. The filter is invoked as a simple pipe
for use in a wide variety of systems. The 'kill' feature (which
eliminates entire messages) can also help sites deal with resource
strains caused by modern virus floods.

#%%description -l pl

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_sysconfdir}/renattach.conf.ex \
	$RPM_BUILD_ROOT%{_sysconfdir}/renattach.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
