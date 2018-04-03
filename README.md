Test repo to demonstrate difficulty running docker images that have binary dependencies on OS X.

Successful case:

```bash
$ ./bazel-bin/test_image
7586d32bdc1f: Loading layer [==================================================>]  20.48kB/20.48kB
Loaded image ID: sha256:cb44782967dfa0b486cbe6274d357049dd6e7ba2d1998e470802eeb917c8c612
Tagging cb44782967dfa0b486cbe6274d357049dd6e7ba2d1998e470802eeb917c8c612 as bazel:test_image
Hello there, Universe.
```

Failure case:

```bash
$ ./bazel-bin/test_db_image
73265a540c85: Loading layer [==================================================>]  4.342MB/4.342MB
Loaded image ID: sha256:37e242f172c90852309f6a83112a74e0587ffcfe7dad530cd5a016a3776d6adb
Tagging 37e242f172c90852309f6a83112a74e0587ffcfe7dad530cd5a016a3776d6adb as bazel:test_db_image
Traceback (most recent call last):
File "/app/test_db_image.binary.runfiles/__main__/test_db.py", line 3, in <module>
  import psycopg2
File "/app/test_db_image.binary.runfiles/pypi__psycopg2_binary_2_7_4/psycopg2/__init__.py", line 50, in <module>
  from psycopg2._psycopg import (                     # noqa
ImportError: /app/test_db_image.binary.runfiles/pypi__psycopg2_binary_2_7_4/psycopg2/_psycopg.so: invalid ELF header
```
