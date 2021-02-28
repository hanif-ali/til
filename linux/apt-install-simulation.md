# Run Simulation of Installing a Package

Sometimes you just want to see what would happen when you install a package without actually installing it. This is especially helpful when you want to know the version of a package that apt would install when you run install. You can do that by running the install in simulation mode which just outputs the same info without actually installing the package.

```
sudo apt-get -s install sl

Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages were automatically installed and are no longer required:
  gyp javascript-common libc-ares2 libgit2-28 libhttp-parser-dev libhttp-parser2.9 libjs-inherits libjs-is-typedarray libjs-psl
  libjs-typedarray-to-buffer libmbedcrypto3 libmbedtls-dev libmbedtls12 libmbedx509-0 libpython2-dev libpython2-stdlib libpython2.7 libpython2.7-dev
  libpython2.7-minimal libpython2.7-stdlib libuv1-dev nodejs-doc python-pkg-resources python2 python2-minimal python2.7 python2.7-dev python2.7-minimal
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  sl
0 upgraded, 1 newly installed, 0 to remove and 227 not upgraded.
Inst sl (5.02-1 Ubuntu:20.04/focal [amd64])
Conf sl (5.02-1 Ubuntu:20.04/focal [amd64])
```
