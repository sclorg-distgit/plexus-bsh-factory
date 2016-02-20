%global pkg_name plexus-bsh-factory
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%define parent plexus
%define subname bsh-factory

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.0
Release:        0.14.a7.11%{?dist}
Epoch:          0
Summary:        Plexus Bsh component factory
License:        MIT
URL:            http://plexus.codehaus.org/
BuildArch:      noarch
# svn export svn://svn.plexus.codehaus.org/plexus/tags/plexus-bsh-factory-1.0-alpha-7-SNAPSHOT plexus-bsh-factory/
# tar czf plexus-bsh-factory-src.tar.gz plexus-bsh-factory/
Source0:        %{pkg_name}-src.tar.gz
Source3:	plexus-bsh-factory-license.txt

Patch1:         %{pkg_name}-encodingfix.patch
Patch2:         0001-Migrate-to-plexus-containers-container-default.patch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-mvn(bsh:bsh)
BuildRequires:  maven30-mvn(classworlds:classworlds)
BuildRequires:  maven30-mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  maven30-mvn(org.codehaus.plexus:plexus-utils)

%description
Bsh component class creator for Plexus.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
Javadoc for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

%patch1 -b .sav
%patch2 -p1
cp release-pom.xml pom.xml
cp -p %{SOURCE3} .
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{parent}/%{subname}
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/plexus
%dir %{_javadir}/plexus
%doc plexus-bsh-factory-license.txt

%files javadoc -f .mfiles-javadoc
%doc plexus-bsh-factory-license.txt

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:1.0-0.14.a7.11
- maven33 rebuild

* Fri Jan 16 2015 Michal Srb <msrb@redhat.com> - 0:1.0-0.14.a7.10
- Fix directory ownership

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.9
- Rebuild to fix provides

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.0-0.14.a7.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:1.0-0.14.a7.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.14.a7.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.0-0.14.a7
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.13.a7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.12.a7
- Simplify build dependencies
- Update to current packaging guidelines

* Wed Apr 10 2013 Michal Srb <msrb@redhat.com> - 0:1.0-0.11.a7
- Port to plexus-containers-container-default

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.0-0.10.a7
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 23 2013 Michal Srb <msrb@redhat.com> - 0:1.0-0.9.a7
- Build with xmvn

* Thu Nov 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.0-0.8.a7
- Cleanup whole spec file (#878828)
- Build/install javadoc package (#878134, #878135)

* Thu Nov 15 2012 Tom Callaway <spot@fedoraproject.org> - 0:1.0-0.7.a7s.1.13
- fix incomplete license.txt

* Tue Aug 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.0-0.7.a7s.1.12
- Don't own _mavenfragdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.7.a7s.1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.6.a7s.1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.5.a7s.1.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 12 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.4.a7s.1.11
- Drop gcj_support.
- Build with ant. Fixes rhbz#539101.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a7s.1.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 23 2009 Deepak Bhole <dbhole@redhat.com> - 1.0-0.3.a7s.1.10
- Rebuild with maven

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a7s.1.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 13 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.a7s.1.9
- Build for ppc64

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.2.a7s.1.8
- add license information from upstream

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.2.a7s.1.7
- drop repotag
- label license as Unknown (hopefully, upstream will get back to us before the sun explodes)

* Thu Feb 28 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.a7s.1jpp.6
- Rebuild

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7s.2jpp.5
- ExcludeArch ppc64

* Mon Sep 10 2007 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7s.2jpp.4
- Build with maven

* Fri Aug 31 2007 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7s.2jpp.3
- Build without maven (to build on ppc)

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7s.2jpp.2
- Build with maven

* Fri Feb 23 2007 Tania Bento <tbento@redhat.com> 0:1.0-0.1.a7s.2jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Fixed %%Vendor.
- Fixed %%Distribution.
- Fixed instructions on how to generate source drop.
- Removed %%post and %%postun sections for javadoc.
- Made sure lines had less than 80 characters.
- Changed to use cp -p to preserve timestamps.

* Tue Oct 17 2006 Deepak Bhole <dbhole@redhat.com> 1.0-0.a7s.2jpp
- Update for maven2 9jpp

* Thu Sep 07 2006 Deepak Bhole <dbhole@redhat.com> 1.0-0.a7s.1jpp
- Initial build
