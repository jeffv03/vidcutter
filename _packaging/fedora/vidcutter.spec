# Maintained by app author Pete Alexandrou <pete AT ozmartians DOT com>
%global pkg_name vidcutter

Name:           %{pkg_name}
Version:        5.5.0
Release:        1%{?dist}
Summary:        the simplest + fastest video cutter & joiner
Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://vidcutter.ozmartians.com

Source0:        https://github.com/ozmartian/%{pkg_name}/archive/%{version}.tar.gz

ExclusiveArch:	%{ix86} x86_64	

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  mpv-libs-devel

Requires:       python3-qt5
Requires:       mpv-libs
Requires:       mediainfo
Requires:       ffmpeg
Requires:		python3-pyopengl

%description
    A modern, simple to use, constantly evolving and hella fast MEDIA CUTTER + JOINER
    w/ frame-accurate SmartCut technology + Qt5, libmpv, FFmpeg and MediaInfo powering
    the backend.

%prep
%autosetup -n %{pkg_name}-%{version}

# Remove bundled egg-info
rm -rf %{pkg_name}.egg-info

%build
%define debug_package %{nil}
%py3_build

%install
%py3_install

%files -n %{pkg_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pkg_name}
%{python3_sitearch}/%{pkg_name}-%{version}-py?.?.egg-info
%{_bindir}/%{pkg_name}
%{_datadir}/applications/com.ozmartians.vidcutter.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{pkg_name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{pkg_name}.svg
%{_datadir}/appdata/com.ozmartians.vidcutter.appdata.xml
%{_datadir}/metainfo/com.ozmartians.vidcutter.appdata.xml
%{_datadir}/mime/packages/x-%{pkg_name}.xml
%{_datadir}/pixmaps/%{pkg_name}.svg

%changelog
* Thu Nov 30 2017 Pete Alexandrou <pete AT ozmartians DOT com> 5.0.5-1
- 5.0.5 release
* Thu Nov 16 2017 Pete Alexandrou <pete AT ozmartians DOT com> 5.0.0-1
- 5.0.0 release
* Thu Aug 03 2017 Pete Alexandrou <pete AT ozmartians DOT com> 4.0.0-1
- 4.0.0 release
* Mon May 29 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.5.0-1
- 3.5.0 release
* Tue May 09 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.2.0-1
- latest release
* Sun Mar 05 2017 Pete Alexandrou <pete AT ozmartians DOT com> - 3.0.1-2
- mageia + epel repos included
* Sun Mar 05 2017 Pete Alexandrou <pete AT ozmartians DOT com> - 3.0.1-1
- version bump
* Sun Mar 05 2017 Pete Alexandrou <pete AT ozmartians DOT com> - 3.0.0-1
- Initial packaging
