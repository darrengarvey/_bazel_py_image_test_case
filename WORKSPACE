http_archive(
    name = "io_bazel_rules_python",
    sha256 = "0d1810fecc1bf2b6979d2af60e157d93d3004805bd8b7fda6eb52dda13480dca",
    strip_prefix = "rules_python-115e3a0dab4291184fdcb0d4e564a0328364571a",
    urls = ["https://github.com/bazelbuild/rules_python/archive/115e3a0dab4291184fdcb0d4e564a0328364571a.tar.gz"],
)

# docker rules
git_repository(
    name = "io_bazel_rules_docker",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    tag = "v0.3.0",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

# Allow using requirements.txt for deps
load("@io_bazel_rules_python//python:pip.bzl", "pip_import")
pip_import(
    name = "python_deps",
    requirements = "//:requirements.txt",
)

load("@python_deps//:requirements.bzl", "pip_install")
pip_install()
