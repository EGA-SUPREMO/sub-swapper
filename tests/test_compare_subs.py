import unittest
from datetime import time
import textstat
from subs_swapper.subtitle_wrapper import SubtitleWrapper
import subs_swapper.analizer

class TestSubtitleMatching(unittest.TestCase):
    def setUp(self):
        # Create two SubtitleWrapper instances for testing
        self.sub_en = Subtitle(id=1, start=time(0, 0, 0), end=time(0, 0, 5), text="It can't be!", id_line_external=None, grade_level=None, is_valid=None, swap=None)
        self.sub_es = Subtitle(id=2, start=time(0, 0, 2), end=time(0, 0, 5), text="No, no puede ser!", id_line_external=None, grade_level=None, is_valid=None, swap=None)

    def test_find_best_matching_subtitle(self):
        # Create subtitles in another language for testing
        subtitles_other_language = [
            Subtitle(id=1, start=time(0, 0, 0), end=time(0, 0, 3), text="No", id_line_external=None, grade_level=None, is_valid=None, swap=None),
            Subtitle(id=2, start=time(0, 0, 3), end=time(0, 0, 7), text="It", id_line_external=None, grade_level=None, is_valid=None, swap=None)
        ]

        # Call the function to find the best matching subtitle
        best_match = find_best_matching_subtitle(self.sub_en, subtitles_other_language)

        # Assert that the best match is found and has the correct ID
        self.assertIsNotNone(best_match)
        self.assertEqual(self.sub_en.id_line_external, best_match.id)
        self.assertEqual(self.sub_es.id_line_external, best_match.id)

if __name__ == '__main__':
    unittest.main()
