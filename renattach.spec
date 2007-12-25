Summary:	renattach - rename/delete dangerous email attachments
Summary(pl.UTF-8):	renattach - zmiana nazwy/usuwanie niebezpiecznych załączników z e-maili
Name:		renattach
Version:	1.2.4
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications/Mail
Source0:	http://www.pc-tools.net/files/unix/%{name}-%{version}.tar.gz
# Source0-md5:	00dd2b1ce4a63aaf0e2557aca6becf9d
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

%description -l pl.UTF-8
renattach jest szybkim i wydajnym filtrem potokowym, który może
zmieniać nazwę lub usuwać potencjalnie niebezpieczne załączniki z
poczty elektronicznej. Jest wysoce skutecznym sposobem zabezpieczania
użytkowników końcowych przed szkodliwą zawartością listów (robakami
internetowymi/wirusami) poprzez unieszkodliwianie lub usuwanie
załączników, które mogą być przypadkowo uruchomione przez
użytkowników. Filtr jest wywoływany jako prosty potok dla użytku z
szerokim wyborem systemów. Właściwość 'kill' (która likwiduje całe
wiadomości) może także pomóc radzić sobie z obciążeniem zasobów
spowodowanym przez zalew nowoczesnych wirusów.

%prep
%setup -q

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
