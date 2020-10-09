import os
import sys

from yamllint import linter
from yamllint.config import YamlLintConfig


def main():
    yaml_path = os.environ["INPUT_PATH"]
    strict = os.environ["INPUT_STRICT"] == "true"
    conf = YamlLintConfig("extends: default")
    warning_count = 0

    with open(yaml_path) as f:
        problems = linter.run(f, conf, yaml_path)

    for problem in problems:

        if problem.level == "warning" and strict:
            problem.level = "error"

        print(
            f"::{problem.level} file={yaml_path},line={problem.line},"
            f"col={problem.column}::{problem.desc} ({problem.rule})"
        )

        if problem.level == "warning":
            warning_count = warning_count + 1

        if problem.level == "error":
            sys.exit(1)

    print(f"::set-output name=warnings::{warning_count}")

    sys.exit(0)


if __name__ == "__main__":
    main()