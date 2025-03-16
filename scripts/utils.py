import logging

def configure_logging():
    logging.basicConfig(
        filename="logs/ethiopian_import_analysis.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
