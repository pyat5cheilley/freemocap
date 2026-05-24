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
configure_logging(log_level="DEBUG")

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    "__url__",
]
