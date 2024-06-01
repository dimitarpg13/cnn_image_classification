import unittest
import os
from pathlib import Path
from dichotomous_image_segmentation.segmentation_manager import SegmentationManager, get_center_of_mass, DEVICE
from image_crop.image_crop_manager import ImageCropManager

IC_HOME = '/'.join(Path(os.path.abspath(os.path.dirname(__file__))).parts[:-1]).replace('/','',1)
DATASET_PATH = 'tests/sample_data'

param_list = [ ('smiling-man', ),
               ('accessories-bag', ),
               ('basketball_players', ),
               ('bicycle_riders', ),
               ('kitchen-bar', ),
               ('jazz_player',),
               ('llama',),
               ('shoes',)
              ]


class TestImageClassification(unittest.TestCase):
    def setUp(self):
        pass
        # TODO: implement the ctor

    def test_image_classification(self):
        image_path = IC_HOME + "/" + DATASET_PATH + "/"
        for image_name, in param_list:
            with self.subTest(image_name=image_name,):
                self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
