"""Dataclass defining the properties of a ChArUco board used for camera calibration.

A ChArUco board combines a chessboard pattern with ArUco markers, allowing
for robust camera calibration and pose estimation.
"""

from dataclasses import dataclass, field
from typing import Tuple

import cv2
import numpy as np


@dataclass
class CharucoBoardDefinition:
    """Defines the configuration of a ChArUco calibration board.

    Attributes:
        number_of_squares_width: Number of chessboard squares along the width.
        number_of_squares_height: Number of chessboard squares along the height.
        black_square_side_length_mm: Side length of each black square in millimeters.
        aruco_marker_length_mm: Side length of each ArUco marker in millimeters.
        aruco_marker_dict: The ArUco dictionary used to generate markers.
    """

    number_of_squares_width: int = 7
    number_of_squares_height: int = 5
    black_square_side_length_mm: float = 30.0
    aruco_marker_length_mm: float = 23.0
    aruco_marker_dict_id: int = cv2.aruco.DICT_4X4_250

    # Derived fields populated post-init
    aruco_marker_dict: cv2.aruco.Dictionary = field(init=False, repr=False)
    board: cv2.aruco.CharucoBoard = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Initialize derived fields after dataclass construction."""
        self.aruco_marker_dict = cv2.aruco.getPredefinedDictionary(self.aruco_marker_dict_id)
        self.board = cv2.aruco.CharucoBoard(
            size=(self.number_of_squares_width, self.number_of_squares_height),
            squareLength=self.black_square_side_length_mm / 1000.0,  # convert mm to meters
            markerLength=self.aruco_marker_length_mm / 1000.0,
            dictionary=self.aruco_marker_dict,
        )

    @property
    def number_of_charuco_corners(self) -> int:
        """Total number of inner ChArUco corners on the board."""
        return (self.number_of_squares_width - 1) * (self.number_of_squares_height - 1)

    @property
    def number_of_aruco_markers(self) -> int:
        """Total number of ArUco markers on the board."""
        # ArUco markers occupy every other square (checkerboard pattern)
        total_squares = self.number_of_squares_width * self.number_of_squares_height
        return total_squares // 2

    @property
    def board_dimensions_mm(self) -> Tuple[float, float]:
        """Physical dimensions of the board in millimeters (width, height)."""
        width = self.number_of_squares_width * self.black_square_side_length_mm
        height = self.number_of_squares_height * self.black_square_side_length_mm
        return width, height

    def get_board_image(self, pixels_per_mm: float = 10.0) -> np.ndarray:
        """Generate an image of the ChArUco board.

        Args:
            pixels_per_mm: Resolution of the output image in pixels per millimeter.

        Returns:
            A grayscale NumPy array representing the board image.
        """
        width_mm, height_mm = self.board_dimensions_mm
        image_width_px = int(width_mm * pixels_per_mm)
        image_height_px = int(height_mm * pixels_per_mm)
        board_image = self.board.generateImage(
            outSize=(image_width_px, image_height_px),
            marginSize=0,
            borderBits=1,
        )
        return board_image

    def __repr__(self) -> str:
        return (
            f"CharucoBoardDefinition("
            f"squares={self.number_of_squares_width}x{self.number_of_squares_height}, "
            f"square_side={self.black_square_side_length_mm}mm, "
            f"marker_side={self.aruco_marker_length_mm}mm, "
            f"corners={self.number_of_charuco_corners})"
        )
