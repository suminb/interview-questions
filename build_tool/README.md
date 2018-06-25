Build Toold
===========

Problem: Suppose we are making a build tool that takes a list of paths
containing source files.

When building code for a particular directory, source files in all its
subdirectories are handled. For example, both `/a/b/c` and `/a/b` are given,
the build tool only needs to work on `/a/b` as all files under `/a/b/c` are
already handled when working on `/a/b`.

The build tools is also expected to perform deduplications of directories.

Time limit: 40 min
