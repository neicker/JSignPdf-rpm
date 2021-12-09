# JSignPdf build helpers
## spec file et al. to build RPMs of the JSignPdf application

[JSignPdf](http://jsignpdf.sourceforge.net/) is a tool written in Java to cryptographically sign PDF in
Linux (and most other OSes capable to run Java). This project collects
files and patches to build the RPM but not the actual release data of
JSignPdf.

This is only tested for openSUSE (actually LEAP 15.2 and 15.3) but
should work as well for other versions or Fedora and RedHat in
principle. Feedback is welcome.

To actually build an RPM the following steps are required:
```
mkdir -p ~/rpmbuild/SPECS
cp JSignPdf.spec ~/rpmbuild/SPECS
mkdir -p ~/rpmbuild/SOURCES
cp JSignPdf-security.patch JSignPdf.desktop JSignPdf.png jsignpdf_sh.patch ~/rpmbuild/SOURCES
cd ~/rpmbuild/SPECS
# Fetch zip blob from JSignPdf`s download area
rpmdev-spectool -g -R JSignPdf.spec
rpmbuild -ba JSignPdf.spec
```

After this there shall be an RPM file in `~/rpmbuild/RPMS/noarch` as
well as a Source RPM in `~/rpmbuild/SRPMS`
