Summary:	renattach - rename/delete dangerous email attachments
Summary(pl):	renattach - zmiana nazwy/usuwanie niebezpiecznych za³±czników z e-maili
Name:		renattach
Version:	1.2.2
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Mail
Source0:	http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
# Source0-md5:	2a9c7c31ba618ea751fc0ba7a81836f8
Patch0:		%{name}-getopt_in_glibc.patch
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

%description -l pl
renattach jest szybkim i wydajnym filtrem potokowym, który mo¿e
zmieniaæ nazwê lub usuwaæ potencjalnie niebezpieczne za³±czniki z
poczty elektronicznej. Jest wysoce skutecznym sposobem zabezpieczania
u¿ytkowników koñcowych przed szkodliw± zawarto¶ci± listów (robakami
internetowymi/wirusami) poprzez unieszkodliwianie lub usuwanie
za³±czników, które mog± byæ przypadkowo uruchomione przez
u¿ytkowników. Filtr jest wywo³ywany jako prosty potok dla u¿ytku z
szerokim wyborem systemów. W³a¶ciwo¶æ 'kill' (która likwiduje ca³e
wiadomo¶ci) mo¿e tak¿e pomóc radziæ sobie z obci±¿eniem zasobów
spowodowanym przez zalew nowoczesnych wirusów.

%prep
%setup -q
%patch0 -p1

%build
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
