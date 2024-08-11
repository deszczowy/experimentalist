import argparse
import sys
import os


class Arguments:

    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            prog=self._script(),
            description="Experimentalist Run Script, which will run user \
            defined chains of actions over WAV files from provided \
            source path.",
            epilog=''
        )

        # Building default provided arguments
        parser.add_argument(
            "-s", "--sources-path",
            action="store",
            dest='sources_path',
            default="./workspace"
        )

        # Parse and store command line arguments
        self.arguments = parser.parse_args()

    # Default getters
    def sources(self) -> str:
        return self.arguments.sources_path

    # Some helpers
    def _script(self) -> str:
        return os.path.basename(sys.argv[0])
