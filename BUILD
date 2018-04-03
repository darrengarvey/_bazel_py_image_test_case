package(default_visibility = ["//visibility:public"])

load("@python_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")

py_image(
    name = "test_image",
    srcs = ["test.py"],
    main = "test.py",
)

py_image(
    name = "test_db_image",
    srcs = ["test_db.py"],
    main = "test_db.py",
    deps = [
        requirement("psycopg2-binary"),
        requirement("testing.postgresql"),
    ],
)
