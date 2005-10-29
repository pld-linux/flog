Summary:	A small STDIN-to-file logger with support for logrotation
Summary(pl):	Ma³y logger strumienia ze wsparciem dla rotacji logów
Name:		flog
Version:	1.7
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://oss.ezic.com/flog/%{name}-%{version}.tar.gz
# Source0-md5:	2c8eaa80e29f137ce81a95c4b6ecf7fe
URL:		http://oss.ezic.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
flog (file logger) is a small program that reads input from STDIN and
writes to a file, optionally adding timestamps. If SIGHUP is received, the
file will be reopened, allowing for log rotation.

%description -l pl
flog (file logger) jest ma³ym programem który czyta ze standardowego
wej¶cia i zapisuje do pliku, ewentualnie dodaj±c znaczniki czasowe.  Je¶li
otrzyma sygna³ HUP, plik bêdzie na nowo otwarty, pozwalaj±c na rotacjê
logów.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install flog $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
