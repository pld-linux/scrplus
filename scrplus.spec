Summary:	Image converter to ZX Spectrum
Name:		scrplus
Version:	0.21
Release:	1
License:	GPL v3
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/scrplus/%{name}_%{version}.tar.gz
# Source0-md5:	1ce563ad3c228b21eb62448e664ab13e
Patch0:		ldflags.patch
URL:		http://scrplus.sourceforge.net/
BuildRequires:	SDL_image-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gtk+2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converter of images to ZX Spectrum emulators formats.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
rm -f gscrplus scrplus

%build
%{__make} CFLAGS="%{rpmcflags} -std=gnu99" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install gscrplus scrplus $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc algorithm readme TODO
%attr(755,root,root) %{_bindir}/gscrplus
%attr(755,root,root) %{_bindir}/scrplus
