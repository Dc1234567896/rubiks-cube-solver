class Cube:
    def init(self, size): 
        if size != 2:
            raise ValueError("This implementation is specifically for a 2x2 cube.")
        self.size = size
        # Initialize the cube's state with colors represented by integers
        # Following the order: front, right, back, left, top, bottom
        self.state = [color for color in range(6) for _ in range(size * size)]

    def _rotate_face(self, face_indices, direction):
        """Helper method to rotate a face of the cube."""
        if direction not in (-1, 1):
            raise ValueError("Direction must be -1 (counter-clockwise) or 1 (clockwise).")
        face = [self.state[idx] for idx in face_indices]
        rotated = face[-direction:] + face[:-direction] if direction == 1 else face[direction:] + face[:direction]
        for idx, new_color in zip(face_indices, rotated):
            self.state[idx] = new_color

    def move(self, move_str):
        """Performs a move on the cube."""
        # Define the indices for each face (for a 2x2 cube)
        # Assuming a linear representation: front, right, back, left, top, bottom
        faces = {
            'F': [0, 1, 2, 3],  # Front
            'R': [4, 5, 6, 7],  # Right
            'B': [8, 9, 10, 11],  # Back
            'L': [12, 13, 14, 15],  # Left
            'U': [16, 17, 18, 19],  # Up (Top)
            'D': [20, 21, 22, 23]  # Down (Bottom)
        }
        direction = 1 if move_str.endswith('+') else -1
        face = move_str[0]
        if face in faces:
            self._rotate_face(faces[face], direction)
        else:
            raise ValueError(f"Invalid move: {move_str}")

    def str(self):
        """Returns a string representation of the cube's state."""
        colors = ['orange', 'blue', 'red', 'green', 'white', 'yellow']
        return ''.join([colors[color] for color in self.state])
