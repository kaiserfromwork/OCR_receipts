import logging


def main() -> None:
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logging_file.log")
    file_handler.setLevel(logging.DEBUG)


if __name__ == "__main__":
    main()


