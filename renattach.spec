Summary:	renattach - rename/delete dangerous email attachments
Summary(pl):	renattach - zmiana nazwy/usuwanie niebezpiecznych za��cznik�w z e-maili
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
renattach jest szybkim i wydajnym filtrem potokowym, kt�ry mo�e
zmienia� nazw� lub usuwa� potencjalnie niebezpieczne za��czniki z
poczty elektronicznej. Jest wysoce skutecznym sposobem zabezpieczania
u�ytkownik�w ko�cowych przed szkodliw� zawarto�ci� list�w (robakami
internetowymi/wirusami) poprzez unieszkodliwianie lub usuwanie
za��cznik�w, kt�re mog� by� przypadkowo uruchomione przez
u�ytkownik�w. Filtr jest wywo�ywany jako prosty potok dla u�ytku z
szerokim wyborem system�w. W�a�ciwo�� 'kill' (kt�ra likwiduje ca�e
wiadomo�ci) mo�e tak�e pom�c radzi� sobie z obci��eniem zasob�w
spowodowanym przez zalew nowoczesnych wirus�w.

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
