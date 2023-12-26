
class SubtitleWrapper:
    def __init__(self, subtitle_line, grade_level, is_valid):
        self.subtitle_line = subtitle_line
        self.id_line_external = -1
        self.grade_level = grade_level
        self.is_valid = is_valid
        self.swap = False 

    def __repr__(self):
        return f"{self.subtitle_line.index} > {self.id_line_external} : {self.subtitle_line.text}"