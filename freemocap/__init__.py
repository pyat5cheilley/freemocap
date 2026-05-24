"""FreeMoCap - Free Motion Capture.

A free and open-source markerless motion capture system.
This package provides tools for recording, processing, and analyzing
human motion data using computer vision and machine learning techniques.
"""

__version__ = "1.0.0"
__author__ = "FreeMoCap Contributors"
__email__ = "support@freemocap.org"
__license__ = "AGPLv3"
__description__ = "A free and open-source markerless motion capture system"
__url__ = "https://github.com/freemocap/freemocap"

from freemocap.system.logging.configure_logging import configure_logging

# Configure default logging on package import
# Personal note: switched to DEBUG level so I can trace issues more easily
# while working through the codebase - change back to WARNING for normal use
# TODO: consider reading log level from an env variable (e.g. FREEMOCAP_LOG_LEVEL)
#       so I don't have to keep editing this file manually
import os
_log_level = os.environ.get("FREEMOCAP_LOG_LEVEL", "DEBUG")
configure_logging(log_level=_log_level)

# Personal note: log the resolved level at startup so it's obvious which
# level is active when running tests or scripts
import logging
logging.getLogger(__name__).debug("freemocap logging initialised at level: %s", _log_level)

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    "__url__",
]
