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
# Personal note: using WARNING level by default to reduce noise during my experiments
configure_logging(log_level="WARNING")

__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__description__",
    "__url__",
]
