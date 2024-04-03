import unittest
from rma.application import RmaApplication


class ApplicationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = RmaApplication(filters={})

    def tearDown(self):
        pass

    def test_get_pattern_aggregated_data(self):
        aggregate_patterns = self.app.get_pattern_aggregated_data([
            {'name': 'jimmy18ngo@gmail.com-*'},
            {'name': 'belgical@msn.com-*'},
            {'name': '447486656-shipment-info'},
            {'name': 'elisabeth.amitsis@icloud.com-*-intelligence-orders'},
            {'name': '60d380a28858772edcf4115b-*-cck-email'},
            {'name': '75240560-shipment-info'},
            {'name': 'marie.menina17@gmail.com-*-*'},
            {'name': '367568-*-productproperties'},
        ])
        self.assertEqual(14, len(aggregate_patterns))
        