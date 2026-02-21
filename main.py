from src.logger import setup_logger
from src.pipeline import run_pipeline


def main() -> None:
    setup_logger()
    run_pipeline()


if __name__ == "__main__":
    main()