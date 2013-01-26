# NOTE
#  - early access packages downloadable: http://jdk6.java.net/download.html
#  - sample/demo available as separate download, licensesd with Oracle BSD license
#
#       /usr/lib/jvm/java7-1.7.0.11/jre/lib/i386/libjavaplugin_jni.so
#       /usr/lib/jvm/java7-1.7.0.11/jre/lib/i386/libjavaplugin_nscp.so
#       /usr/lib/jvm/java7-1.7.0.11/jre/lib/i386/libjavaplugin_nscp_gcc29.so
#       /usr/lib/jvm/java7-1.7.0.11/jre/lib/i386/libjavaplugin_oji.so
#       /usr/lib/jvm/java7-1.7.0.11/jre/plugin/desktop/sun_java.desktop
#       /usr/lib/jvm/java7-1.7.0.11/jre/plugin/desktop/sun_java.png
#
# Conditional build:
%bcond_without	tests		# build without tests

# disable file duplicate packaging error
%define		_duplicate_files_terminate_build   0
%define		src_ver	7u11
%define		sub_ver	b21
%define		dir_ver	%(echo %{version} | sed 's/\\.\\(..\\)$/_\\1/')
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 51.0
Summary:	Oracle JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Oracle JDK - środowisko programistyczne Javy dla Linuksa
Name:		oracle-java7
Version:	1.7.0.11
Release:	1
License:	restricted, distributable
# http://www.oracle.com/technetwork/java/javase/terms/license/index.html
# See "LICENSE TO DISTRIBUTE SOFTWARE" section, which states you can
# redistribute in unmodified form.
Group:		Development/Languages/Java
# Download URL (requires JavaScript and interactive license agreement):
# http://www.oracle.com/technetwork/java/javase/downloads/index.html
Source0:	http://download.oracle.com/otn-pub/java/jdk/%{src_ver}-%{sub_ver}/jdk-%{src_ver}-linux-i586.tar.gz
# Source0-md5:	22239a786477a7d21bc8a835455ca24a
Source1:	http://download.oracle.com/otn-pub/java/jdk/%{src_ver}-%{sub_ver}/jdk-%{src_ver}-linux-x64.tar.gz
# Source1-md5:	d8f65419fa65f179382ae310237fd1f4
Source2:	Test.java
Source3:	Test.class
Patch0:		%{name}-desktop.patch
URL:		http://www.oracle.com/technetwork/java/javase/overview/index.html
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	rpmbuild(macros) >= 1.453
BuildRequires:	unzip
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java7
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javareldir	java7-%{version}
%define		javadir		%{_jvmdir}/%{javareldir}
%define		jrereldir	%{javareldir}/jre
%define		jredir		%{_jvmdir}/%{jrereldir}
%define		jvmjardir	%{_jvmjardir}/java7-%{version}

%ifarch %{ix86}
%define		arch	i386
%endif
%ifarch %{x8664}
%define		arch	amd64
%endif

# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libjava_crw_demo_g\.so.*' 'libmawt.so' 'java(ClassDataVersion)'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

# binary packages already stripped
%define		_enable_debug_packages 0

%description
This package symlinks Sun Java development tools provided by
java7-jdk-base to system-wide directories like /usr/bin, making
Sun Java the default JDK.

%description -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi programistycznych
uruchomieniowego Javy firmy Sun, dostarczanych przez pakiet
java7-jdk-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Sun Java staje się domyślnym JDK w
systemie.

%package appletviewer
Summary:	Java applet viewer from Sun Java
Summary(pl.UTF-8):	Przeglądarka appletów Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}

%description appletviewer
This package contains applet viewer for Sun Java.

%description appletviewer -l pl.UTF-8
Ten pakiet zawiera przeglądarkę appletów dla Javy Suna.

%package jdk-base
Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Sun JDK - środowisko programistyczne Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-4
Provides:	jdk(%{name})

%description jdk-base
Java Development Kit for Linux.

%description jdk-base -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package jre-jdbc
Summary:	JDBC files for Sun Java
Summary(pl.UTF-8):	Pliki JDBC dla Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-jdbc
Obsoletes:	java7-jdbc

%description jre-jdbc
This package contains JDBC files for Sun Java.

%description jre-jdbc -l pl.UTF-8
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-tools = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-4
Suggests:	%{name}-jre-X11
Provides:	java
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(jaas) = %{version}
Provides:	java(jaf) = 1.1.1
Provides:	java(jaxp) = 1.3
Provides:	java(jaxp_parser_impl)
Provides:	java(jce) = %{version}
Provides:	java(jdbc-stdext) = %{version}
Provides:	java(jdbc-stdext) = 3.0
Provides:	java(jmx) = 1.4
Provides:	java(jndi) = %{version}
Provides:	java(jsse) = %{version}
Provides:	java1.4
Provides:	jre = %{version}
Obsoletes:	java(jaas)
Obsoletes:	java(jaf)
Obsoletes:	java(jaxp)
Obsoletes:	java(jce)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jmx)
Obsoletes:	java(jndi)
Obsoletes:	java(jsse)
Obsoletes:	java-blackdown-jre
Obsoletes:	jre

%description jre
This package symlinks Sun Java runtime environment tools provided by
java7-jre-base to system-wide directories like /usr/bin, making
Sun Java the default JRE.

%description jre -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi środowiska
uruchomieniowego Javy firmy Sun, dostarczanych przez pakiet
java7-jre-base, w standardowych systemowych ścieżkach takich jak
/usr/bin, sprawiając tym samym, że Sun Java staje się domyślnym JRE w
systemie.

%package jre-base
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.7.5-4
Provides:	jre(%{name})

%description jre-base
Java Runtime Environment for Linux. Does not contain any X11-related
compontents.

%description jre-base -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa. Nie zawiera żadnych
elementów związanych ze środowiskiem X11.

%package jre-X11
Summary:	Sun JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Provides:	javaws = %{version}
Provides:	jre-X11 = %{version}

%description jre-X11
This package symlinks Sun Java X11 libraries provided by
java7-jre-base-X11 to system-wide directories like /usr/bin, making
Sun Java the default JRE-X11.

%description jre-X11 -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi X11 Javy firmy
Sun, dostarczanych przez pakiet java7-jre-base-X11, w standardowych
systemowych ścieżkach takich jak /usr/bin, sprawiając tym samym, że
Sun Java staje się domyślnym JRE-X11 w systemie.

%package jre-base-X11
Summary:	Sun JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-X11
X11-related part of Java Runtime Environment for Linux.

%description jre-base-X11 -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa, część związana ze
środowiskiem graficznym X11.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	%{name}-alsa
Obsoletes:	java7-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package visualvm
Summary:	VisualVM - a tool to monitor and troubleshoot Java applications
Summary(pl.UTF-8):	VisualVM - narzędzie do monitorowania i diagnostyki aplikacji w Javie
Group:		Development/Languages/Java
URL:		https://visualvm.dev.java.net/
Requires:	%{name}-jre-X11 = %{version}-%{release}

%description visualvm
VisualVM is a visual tool integrating several commandline JDK tools
and lightweight profiling capabilities. Designed for both production
and development time use, it further enhances the capability of
monitoring and performance analysis for the Java SE platform.

%description visualvm -l pl.UTF-8
VisualVM to graficzne narzędzie integrujące kilka narzędzi JDK
działających z linii poleceń oraz proste możliwości profilowania.
Zaprojektowane jest do użytku zarówno produkcyjnego, jak i w czasie
tworzenia aplikacji; rozszerza możliwości monitorowania i analizy
wydajności dla platformy Java SE.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	jar
Provides:	java-jre-tools
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-jre-tools

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	jre

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package -n browser-plugin-%{name}
Summary:	Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java7-mozilla-plugin
Provides:	mozilla-firefox-plugin-java7
Provides:	mozilla-plugin-java7
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java7-ng
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java7-moz-plugin
Obsoletes:	java7-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java7
Obsoletes:	mozilla-firefox-plugin-gcc3-java7
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-java7
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java7
Obsoletes:	mozilla-plugin-gcc3-java7
Obsoletes:	mozilla-plugin-gcc32-java7
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java7

%description -n browser-plugin-%{name}
Java plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla przeglądarek WWW.

%package -n browser-plugin-%{name}-ng
Summary:	Next-Generation Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy Nowej Generacji do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java7-mozilla-plugin
Provides:	mozilla-firefox-plugin-java7
Provides:	mozilla-plugin-java7
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java7
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java7-moz-plugin
Obsoletes:	java7-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java7
Obsoletes:	mozilla-firefox-plugin-gcc3-java7
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-java7
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java7
Obsoletes:	mozilla-plugin-gcc3-java7
Obsoletes:	mozilla-plugin-gcc32-java7
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java7

%description -n browser-plugin-%{name}-ng
Next-Generation Java plugin for WWW browsers. Works only with
Firefox/Iceweasel 3.x.

%description -n browser-plugin-%{name}-ng -l pl.UTF-8
Wtyczka Nowej Generacji z obsługą Javy dla przeglądarek WWW. Działa
tylko z Firefoksem/Iceweaselem 3.x.

%package sources
Summary:	JRE standard library sources
Summary(pl.UTF-8):	Źródła standardowej biblioteki JRE
Group:		Development/Languages/Java

%description sources
Sources for the standard Java library.

%description sources -l pl.UTF-8
Źródła standardowej bilioteki Java.

%prep
%ifarch %{ix86}
%setup -q -T -b 0 -n jdk%{dir_ver}
%endif
%ifarch %{x8664}
%setup -q -T -b 1 -n jdk%{dir_ver}
%endif

# patch only copy of the desktop file, leave original unchanged
cp jre/plugin/desktop/sun_java.desktop .
%patch0 -p1

cp %{SOURCE2} Test.java
cp %{SOURCE3} Test.class

%build
%if %{with tests}
# Make sure we have /proc mounted,
# javac Test.java fails to get lock otherwise and runs forever:
# Java HotSpot(TM) Client VM warning: Can't detect initial thread stack location - find_vma failed
if [ ! -f /proc/cpuinfo ]; then
	echo >&2 "WARNING: /proc not mounted -- compile test may fail"
fi

# CLASSPATH prevents finding Test.class in .
unset CLASSPATH || :
# $ORIGIN does not work on PLD builders. workaround with LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$(pwd)/jre/lib/%{arch}/jli
./bin/java Test

classver=$(cat classver)
if [ "$classver" != %{_classdataversion} ]; then
	echo "Set %%define _classdataversion to $classver and rerun."
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{javadir},%{jvmjardir},%{_javadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{,ja/}man1,%{_prefix}/src/%{name}-sources} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_browserpluginsdir}}

cp -a bin include lib $RPM_BUILD_ROOT%{javadir}
cp -p man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
cp -p man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

if test -f jre/lib/%{arch}/client/Xusage.txt; then
	mv -f jre/lib/%{arch}/client/Xusage.txt jre/Xusage.client
fi
if test -f jre/lib/%{arch}/server/Xusage.txt; then
	mv -f jre/lib/%{arch}/server/Xusage.txt jre/Xusage.server
fi
if test -f jre/lib/*.txt; then
	mv -f jre/lib/*.txt jre
fi

cp -af jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

for i in java keytool orbd policytool \
	java_vm javaws \
	rmid rmiregistry servertool tnameserv pack200 unpack200; do
	[ -f $RPM_BUILD_ROOT%{jredir}/bin/$i ] || exit 1
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in appletviewer extcheck idlj jar jarsigner \
	javac javadoc javafxpackager javah javap jcmd jconsole jdb jhat jinfo jmap jps \
	jrunscript jsadebugd jstack jstat jstatd native2ascii rmic serialver \
	jvisualvm schemagen wsgen wsimport xjc apt; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

%ifarch %{ix86}
for i in jcontrol java-rmi.cgi; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif
%ifarch %{x8664}
for i in jcontrol; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif

# make sure all tools are available under $(JDK_HOME)/bin
for i in keytool orbd policytool rmid \
		java_vm javaws \
		rmiregistry servertool tnameserv pack200 unpack200 java; do
	[ -f $RPM_BUILD_ROOT%{jredir}/bin/$i ] || exit 1
	ln -sf ../jre/bin/$i $RPM_BUILD_ROOT%{javadir}/bin/$i
done

# some apps (like opera) looks for it in different place
ln -s server/libjvm.so $RPM_BUILD_ROOT%{jredir}/lib/%{arch}/libjvm.so

# copy _all_ plugin files (even those incompatible with PLD) --
# license restriction
cp -a jre/plugin $RPM_BUILD_ROOT%{jredir}

# Install plugin for browsers
# Plugin in regular location simply does not work (is seen by browsers):
%ifarch %{ix86}
ln -sf %{jredir}/plugin/%{arch}/ns7/libjavaplugin_oji.so $RPM_BUILD_ROOT%{_browserpluginsdir}
%endif
ln -sf %{jredir}/lib/%{arch}/libnpjp2.so $RPM_BUILD_ROOT%{_browserpluginsdir}

cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a jre/plugin/desktop/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{jvmjardir}/jce.jar
for f in jndi jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext jdbc-stdext-3.0 \
	sasl jaxp_parser_impl jaxp_transform_impl jaxp jmx activation xml-commons-apis \
	jndi-dns jndi-rmi; do
	ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{jvmjardir}/$f.jar
done

install -d $RPM_BUILD_ROOT%{jredir}/javaws
ln -sf %{jredir}/lib/javaws.jar $RPM_BUILD_ROOT%{jvmjardir}/javaws.jar

# leave all locale files unchanged in the original location (license
# restrictions) and only link them at the proper locations
for loc in $(ls $RPM_BUILD_ROOT%{jredir}/lib/locale); do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
	ln -sf %{jredir}/lib/locale/$loc/LC_MESSAGES/sunw_java_plugin.mo \
		$RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
done

# standardize dir names
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_HK.BIG5HK,zh_HK}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ko.UTF-8,zh.GBK,zh_TW.BIG5}

cp -a src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources

ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java
ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java7
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/jre
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/java7-jre
ln -s java7-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/java
ln -s java7-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jre
ln -s java7-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jsse

# modify RPATH so that javac and friends are able to work when /proc is not
# mounted and we can't append to RPATH (for example to keep previous lookup
# path) as RPATH can't be longer than original
#
# for example:
# old javac: RPATH=$ORIGIN/../lib/i386/jli:$ORIGIN/../jre/lib/i386/jli
# new javac: RPATH=%{_prefix}/lib/jvm/java7-1.6.0/jre/lib/i386/jli

# silly rpath: jre/bin/unpack200: RPATH=$ORIGIN
chrpath -d $RPM_BUILD_ROOT%{jredir}/bin/unpack200

fixrpath() {
	execlist=$(find $RPM_BUILD_ROOT%{javadir} -type f -perm +1 | xargs file | awk -F: '/ELF.*executable/{print $1}')
	for f in $execlist; do
		rpath=$(chrpath -l $f | awk '/RPATH=/ { gsub(/.*RPATH=/,""); gsub(/:/," "); print $0 }')
		[ "$rpath" ] || continue

		# file
		file=${f#$RPM_BUILD_ROOT}
		origin=${file%/*}

		new=
		for a in $rpath; do
			t=$(echo $a | sed -e "s,\$ORIGIN,$origin,g")
			# get rid of ../../
			t=$(set -e; t=$RPM_BUILD_ROOT$t; [ -d $t ] || exit 0; cd $t; pwd)
			# skip inexistent paths
			[ "$t" ] || continue

			t=${t#$RPM_BUILD_ROOT}

			if [[ "$new" != *$t* ]]; then
				# append it now
				new=${new}${new:+:}$t
			fi
		done
		chrpath -r ${new} $f
	done
}

fixrpath

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post -n browser-plugin-%{name}-ng
%update_browser_plugins

%postun -n browser-plugin-%{name}-ng
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE README.html
%{_jvmdir}/java
%{_jvmjardir}/java
%ifarch %{ix86}
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%endif
%attr(755,root,root) %{_bindir}/apt
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javafxpackager
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jcmd
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jhat
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/schemagen
%attr(755,root,root) %{_bindir}/wsgen
%attr(755,root,root) %{_bindir}/wsimport
%attr(755,root,root) %{_bindir}/xjc
%{_mandir}/man1/apt.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javafxpackager.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jcmd.1*
%{_mandir}/man1/jconsole.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/jhat.1*
%{_mandir}/man1/jinfo.1*
%{_mandir}/man1/jmap.1*
%{_mandir}/man1/jps.1*
%{_mandir}/man1/jrunscript.1*
%{_mandir}/man1/jsadebugd.1*
%{_mandir}/man1/jstack.1*
%{_mandir}/man1/jstat.1*
%{_mandir}/man1/jstatd.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%{_mandir}/man1/schemagen.1*
%{_mandir}/man1/wsgen.1*
%{_mandir}/man1/wsimport.1*
%{_mandir}/man1/xjc.1*
%lang(ja) %{_mandir}/ja/man1/apt.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javafxpackager.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jcmd.1*
%lang(ja) %{_mandir}/ja/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/jhat.1*
%lang(ja) %{_mandir}/ja/man1/jinfo.1*
%lang(ja) %{_mandir}/ja/man1/jmap.1*
%lang(ja) %{_mandir}/ja/man1/jps.1*
%lang(ja) %{_mandir}/ja/man1/jrunscript.1*
%lang(ja) %{_mandir}/ja/man1/jsadebugd.1*
%lang(ja) %{_mandir}/ja/man1/jstack.1*
%lang(ja) %{_mandir}/ja/man1/jstat.1*
%lang(ja) %{_mandir}/ja/man1/jstatd.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/schemagen.1*
%lang(ja) %{_mandir}/ja/man1/wsgen.1*
%lang(ja) %{_mandir}/ja/man1/wsimport.1*
%lang(ja) %{_mandir}/ja/man1/xjc.1*

%files jdk-base
%defattr(644,root,root,755)
%{_jvmdir}/java7
%ifarch %{ix86}
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%endif
%attr(755,root,root) %{javadir}/bin/apt
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javafxpackager
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jcmd
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jhat
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jrunscript
%attr(755,root,root) %{javadir}/bin/jsadebugd
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/orbd
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/schemagen
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/servertool
%attr(755,root,root) %{javadir}/bin/tnameserv
%attr(755,root,root) %{javadir}/bin/wsgen
%attr(755,root,root) %{javadir}/bin/wsimport
%attr(755,root,root) %{javadir}/bin/xjc
%{javadir}/include
%dir %{javadir}/lib
%attr(755,root,root) %{javadir}/lib/jexec
%{javadir}/lib/ct.sym
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{javadir}/bin/appletviewer
%{_mandir}/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*

%files jre-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{arch}/libJdbcOdbc.so

%files jre
%defattr(644,root,root,755)
%doc jre/Xusage*
%doc jre/{COPYRIGHT,LICENSE,README,*.txt}
%doc jre/Welcome.html
%{_jvmdir}/jre
%{_jvmjardir}/jre
%{_jvmjardir}/jsse
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/unpack200
%{_mandir}/man1/java.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%{_mandir}/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*

%files jre-base
%defattr(644,root,root,755)
%{_jvmdir}/java7-jre
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/unpack200
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/rmic
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/unpack200
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/cmm
%{jredir}/lib/currency.data
%{jredir}/lib/ext

%dir %{jredir}/lib/%{arch}
%{jredir}/lib/%{arch}/jvm.cfg
%dir %{jredir}/lib/%{arch}/server
%attr(755,root,root) %{jredir}/lib/%{arch}/server/*
%ifarch %{ix86}
%dir %{jredir}/lib/%{arch}/client
%attr(755,root,root) %{jredir}/lib/%{arch}/client/*
%endif
%dir %{jredir}/lib/%{arch}/jli
%attr(755,root,root) %{jredir}/lib/%{arch}/jli/libjli.so
%dir %{jredir}/lib/%{arch}/headless
%attr(755,root,root) %{jredir}/lib/%{arch}/headless/libmawt.so

%attr(755,root,root) %{jredir}/lib/%{arch}/lib*.so
%attr(755,root,root) %{jredir}/lib/%{arch}/fxavcodecplugin-*.so
%attr(755,root,root) %{jredir}/lib/%{arch}/fxplugins.so
%exclude %{jredir}/lib/%{arch}/libjavaplugin*.so
%exclude %{jredir}/lib/%{arch}/libJdbcOdbc.so
%exclude %{jredir}/lib/%{arch}/libjsoundalsa.so
%exclude %{jredir}/lib/%{arch}/libnpjp2.so
%exclude %{jredir}/lib/%{arch}/libsplashscreen.so

%{jredir}/lib/deploy
%{jredir}/lib/desktop
%{jredir}/lib/images
%attr(755,root,root) %{jredir}/lib/jexec
%{jredir}/lib/meta-index
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%{jredir}/lib/security/blacklist
%verify(not md5 mtime size) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
%lang(ja) %{jredir}/lib/*.properties.ja
%dir %{jvmjardir}
%{jvmjardir}/activation.jar
%{jvmjardir}/jaas.jar
%{jvmjardir}/jce.jar
%{jvmjardir}/jcert.jar
%{jvmjardir}/jdbc-stdext*.jar
%{jvmjardir}/jmx.jar
%{jvmjardir}/jndi*.jar
%{jvmjardir}/jnet.jar
%{jvmjardir}/jsse.jar
%{jvmjardir}/sasl.jar
%{jvmjardir}/jaxp*.jar
%{jvmjardir}/xml-commons*.jar
%{jredir}/lib/classlist
%{jredir}/lib/fontconfig.RedHat*.bfc
%{jredir}/lib/fontconfig.RedHat*.properties.src
%{jredir}/lib/fontconfig.SuSE*.bfc
%{jredir}/lib/fontconfig.SuSE*.properties.src
%{jredir}/lib/fontconfig.Turbo.bfc
%{jredir}/lib/fontconfig.Turbo.properties.src
%{jredir}/lib/fontconfig.bfc
%{jredir}/lib/fontconfig.properties.src
%{jredir}/lib/servicetag
%dir %{jredir}/lib/management
%{jredir}/lib/management/jmxremote.access
%{jredir}/lib/management/jmxremote.password.template
%{jredir}/lib/management/management.properties
%{jredir}/lib/management/snmp.acl.template

%files jre-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/javaws
%attr(755,root,root) %{_bindir}/jcontrol
%{_desktopdir}/sun_java.desktop
%{_pixmapsdir}/sun_java.png
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/policytool
%{_mandir}/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%{_mandir}/man1/javaws.1*
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_HK) %{_datadir}/locale/zh_HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo

%files jre-base-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/bin/ControlPanel
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/jcontrol
%attr(755,root,root) %{javadir}/bin/ControlPanel
%attr(755,root,root) %{javadir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/javaws
%attr(755,root,root) %{javadir}/bin/jcontrol
%attr(755,root,root) %{javadir}/bin/javaws
%{jredir}/lib/fonts
%{jredir}/lib/oblique-fonts
%dir %{jredir}/lib/%{arch}/xawt
%attr(755,root,root) %{jredir}/lib/%{arch}/libsplashscreen.so
%{jvmjardir}/javaws.jar
%attr(755,root,root) %{jredir}/lib/%{arch}/xawt/libmawt.so
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(es) %{jredir}/lib/locale/es
%lang(fr) %{jredir}/lib/locale/fr
%lang(it) %{jredir}/lib/locale/it
%lang(ja) %{jredir}/lib/locale/ja
%lang(ko) %{jredir}/lib/locale/ko*
%lang(sv) %{jredir}/lib/locale/sv
%lang(zh_CN) %{jredir}/lib/locale/zh
%lang(zh_CN) %{jredir}/lib/locale/zh.*
%lang(zh_HK) %{jredir}/lib/locale/zh_HK*
%lang(zh_TW) %{jredir}/lib/locale/zh_TW*

%files jre-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{arch}/libjsoundalsa.so

%files visualvm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jvisualvm
%attr(755,root,root) %{javadir}/bin/jvisualvm
%{_mandir}/man1/jvisualvm.1*
%lang(ja) %{_mandir}/ja/man1/jvisualvm.1*
%{javadir}/lib/visualvm

%if 0
%files demos
%defattr(644,root,root,755)
%dir %{javadir}/demo
%{javadir}/demo/applets
%{javadir}/demo/jfc
%{javadir}/demo/jpda
%dir %{javadir}/demo/jvmti
%dir %{javadir}/demo/jvmti/[!i]*
%dir %{javadir}/demo/jvmti/*/lib
%attr(755,root,root) %{javadir}/demo/jvmti/*/lib/*.so
%{javadir}/demo/jvmti/*/src
%{javadir}/demo/jvmti/*/README*
%{javadir}/demo/jvmti/*/*.jar
%{javadir}/demo/jvmti/index.html
%{javadir}/demo/management
%{javadir}/demo/nbproject
%{javadir}/demo/plugin
%{javadir}/demo/applets.html
%{javadir}/demo/scripting
%{javadir}/sample
%endif

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry
%{_mandir}/man1/jar.1*
%{_mandir}/man1/rmic.1*
%{_mandir}/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*

%ifarch %{ix86}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%dir %{jredir}/plugin
%dir %{jredir}/plugin/%{arch}
%dir %{jredir}/plugin/%{arch}/ns7
%ifarch %{x8664}
%dir %{jredir}/plugin/%{arch}/ns7-gcc29
%endif
# XXX: duplicate
%attr(755,root,root) %{jredir}/lib/%{arch}/libjavaplugin*.so
%attr(755,root,root) %{jredir}/plugin/%{arch}/*/libjavaplugin_oji.so
%attr(755,root,root) %{_browserpluginsdir}/libjavaplugin_oji.so
%{jredir}/plugin/desktop
%endif

%files -n browser-plugin-%{name}-ng
%defattr(644,root,root,755)
%dir %{jredir}/plugin
# XXX: duplicate
%attr(755,root,root) %{jredir}/lib/%{arch}/libjavaplugin*.so
%attr(755,root,root) %{jredir}/lib/%{arch}/libnpjp2.so
%attr(755,root,root) %{_browserpluginsdir}/libnpjp2.so
%{jredir}/plugin/desktop

%files sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-sources
%{_prefix}/src/%{name}-sources/src.zip
