#!/bin/sh
# Usage:
# ./get-source.sh
# Author: Elan Ruusamäe <glen@pld-linux.org>
#
# Idea based on omnibus-software jre package
# https://github.com/opscode/omnibus-software/blob/master/config/software/jre.rb

package=java7
specfile=oracle-$package.spec

# abort on errors
set -e
# work in package dir
dir=$(dirname "$0")
cd "$dir"

refurl=http://www.oracle.com/technetwork/java/javase/downloads/
licname="Oracle Binary Code License Agreement for Java SE"
licurl=http://www.oracle.com/technetwork/java/javase/terms/license/
cookie=accept-securebackup-cookie

cat <<EOF

You must accept the $licname
to download this software.

$licurl

Press "ENTER" to Accept License Agreement
Press Ctrl-C to Decline License Agreement

EOF
read license

urls=$(builder -su *.spec | grep http://)
for url in $urls; do
	wget -c --header "Cookie: oraclelicense=$cookie; gpw_e24=$refurl" "$url"
done
