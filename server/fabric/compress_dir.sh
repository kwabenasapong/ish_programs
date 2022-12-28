#!/usr/bin/env bash
# compress and move dir
date_string=$(date +%Y%m%d%H%M%S)
rm -Rf dest/vers
mkdir dest/vers
archive="testfile_${date_string}.tgz"
tar -cvzf "dest/vers/${archive}" "src"
printf "web_static packed: %s -> %d" "$(tree -i -f dest/ | grep 'test.')" "$(stat -c%s dest/vers/"${archive}")"
echo "
Done"
