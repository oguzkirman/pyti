import unittest
import numpy as np

from tests.sample_data import SampleData
from py_technical_indicators import vertical_horizontal_filter


class TestVerticalHorizontalFilter(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.vhf_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        0.45144628099173539, 0.40698689956331935, 0.41653605015673995, 0.5, 0.5,
        0.2634598411297443, 0.3642533936651578, 0.5, 0.39486166007905243, 0.5,
        0.46806757313555702, 0.47229174115123229, 0.48096290837631955, 0.5,
        0.47831171592600391, 0.46897810218977987, 0.46504455106237025,
        0.46243093922651801, 0.5, 0.5, 0.5, 0.34662576687116609,
        0.49060150375939643, 0.31036662452591579, 0.31470043236565715,
        0.31470043236565715, 0.27458811782326548, 0.39430213071582532, 0.5, 0.5,
        0.5, 0.5, 0.5, 0.5, 0.48337400854179335, 0.5, 0.5, 0.5, 0.5, 0.5,
        0.46921147952075892, 0.45628955696202661, 0.46060606060606191, 0.5, 0.5,
        0.36937172774869104, 0.36149162861491563, 0.42054714784633246,
        0.45124398073836369, 0.5, 0.5, 0.44390617032126611, 0.41049633848657613,
        0.41594561186650369, 0.42975734355044853, 0.38435179897201649,
        0.43958197256694875, 0.38910835214447037, 0.24178712220762144,
        0.32394366197182944, 0.38230647709320936, 0.43967714528462354,
        0.43967714528462354, 0.30196078431372536, 0.31112669471715748,
        0.3499999999999997, 0.33340206185567006, 0.5, 0.5, 0.5,
        0.35693287604115531, 0.37011834319526649, 0.39240903387703729,
        0.27899343544857741, 0.29354047424366297, 0.32944951030057384,
        0.32962213225371073, 0.45463006049325166, 0.5, 0.5, 0.5, 0.5,
        0.36486486486486375, 0.49176276771004762, 0.36094316807738563,
        0.28781284004352453, 0.5, 0.5, 0.5, 0.5, 0.5, 0.34025679758308391,
        0.31814273430782686, 0.36208677685950552, 0.5, 0.5, 0.5, 0.5,
        0.43431221020092969, 0.43431221020092969, 0.4287510477787117, 0.5,
        0.40430497925311049, 0.5, 0.5, 0.5, 0.5, 0.5, 0.43328278999241909,
        0.40557939914163188, 0.33852364475201585, 0.34742857142856726,
        0.44927811550151847, 0.5, 0.49693914296002956, 0.496473029045644,
        0.44520547945205585, 0.42802850356294586, 0.45201140323091576, 0.5,
        0.47084896010910271, 0.46440466278101522]

        self.vhf_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 0.45719453376205799, 0.42629757785467165,
        0.41653605015673995, 0.29712339137017413, 0.32653721682847903,
        0.30250552689756838, 0.32540716612377829, 0.32540716612377829,
        0.42183438544374252, 0.47229174115123229, 0.4820850670365226,
        0.4820850670365226, 0.4670460804112343, 0.47837150127226385,
        0.47837150127226385, 0.46897810218977987, 0.41334145598537708,
        0.46243093922651801, 0.5, 0.40356798457087756, 0.40356798457087756,
        0.34662576687116609, 0.34591679506933765, 0.23159090909090893,
        0.25906735751295312, 0.39242315939957123, 0.39242315939957123,
        0.39430213071582532, 0.41855818414322293, 0.5, 0.5, 0.5,
        0.49089390142021694, 0.42302839116719304, 0.28259318708756936,
        0.43876101165103792, 0.5, 0.5, 0.47442721592224107, 0.47724933086267313,
        0.4776902887139115, 0.46596858638743566, 0.46060606060606191,
        0.38553459119496791, 0.38553459119496791, 0.42054714784633246,
        0.42540983606557331, 0.42645474137930989, 0.45224056603773671,
        0.45636652122173865, 0.45636652122173865, 0.31418203810099915,
        0.36536373507057646, 0.3732667775929015, 0.38435179897201649,
        0.34613453815261219, 0.38910835214447037, 0.36024033437826686,
        0.32202262142382038, 0.38822205551388145, 0.38822205551388145,
        0.30274086378737575, 0.31053051455923453, 0.31112669471715748,
        0.33340206185567006, 0.35893854748603332, 0.35893854748603332, 0.5,
        0.4067985955952757, 0.41170244934986355, 0.36817155756207587,
        0.23403083700440522, 0.23696369636963666, 0.29677517493154837,
        0.32962213225371073, 0.32962213225371073, 0.32962213225371073,
        0.34268677656962415, 0.45210550670985777, 0.5, 0.43740972556571917,
        0.40039665050682932, 0.30415944540727619, 0.29928952042628537,
        0.30550774526677926, 0.34081632653061, 0.5, 0.5, 0.5,
        0.37251356238698236, 0.35602450646698591, 0.36337209302325807,
        0.33817903596021709, 0.36609829488465484, 0.48731642189586494,
        0.40555555555555817, 0.43431221020092969, 0.43431221020092969,
        0.43431221020092969, 0.43431221020092969, 0.37482582443102663,
        0.45879857079053088, 0.46207605344295932, 0.5, 0.5, 0.5,
        0.48177676537585434, 0.47725510467821158, 0.36862396204033127,
        0.33219696969696788, 0.44706994328922378, 0.44927811550151847,
        0.45649509803921517, 0.49693914296002956, 0.45163240628778811,
        0.45879474633015788, 0.46743996743996813, 0.45201140323091576,
        0.43352033660589046, 0.47084896010910271]

        self.vhf_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 0.45719453376205799,
        0.31515301085883485, 0.32003844305622225, 0.32653721682847903,
        0.32653721682847903, 0.32540716612377829, 0.38339520755990453,
        0.39633963396339522, 0.45415940766550489, 0.4820850670365226,
        0.46851981760785566, 0.46859142607173981, 0.46712454212454085,
        0.47837150127226385, 0.44400708521944354, 0.36609686609686509,
        0.34250378596668229, 0.3787330316742073, 0.40356798457087756,
        0.40356798457087756, 0.30399515738498839, 0.22789915966386654,
        0.23432884804726081, 0.33777686628383946, 0.38151494093120192,
        0.38072122052704616, 0.41855818414322293, 0.42610587382161019,
        0.42610587382161019, 0.46035725477906653, 0.49089390142021694,
        0.44461259079903187, 0.35337984123165744, 0.29139504563233404,
        0.27990021382751246, 0.42876254180602008, 0.47442721592224107,
        0.47774869109947715, 0.4805628847845213, 0.48018292682926894,
        0.4776902887139115, 0.39889269707355696, 0.38555655028349806,
        0.39513262236806163, 0.42540983606557331, 0.42645474137930989,
        0.42645474137930989, 0.40259409969481202, 0.41624457308249091,
        0.34109128523403287, 0.34109128523403287, 0.29753722794960002,
        0.33201776023680341, 0.33732876712328963, 0.34613453815261219,
        0.3231021555763845, 0.35124808965868892, 0.36024033437826686,
        0.32961783439490661, 0.28432137285491516, 0.29233946676680533,
        0.31053051455923453, 0.3149590962212705, 0.34198270126413871,
        0.35893854748603332, 0.35893854748603332, 0.32339507739152445,
        0.41170244934986355, 0.41170244934986355, 0.31640175074867516,
        0.25469375192366805, 0.27517630465444237, 0.27536640360766562,
        0.28735294117647003, 0.24752976944514757, 0.32297520661156964,
        0.30810469883317582, 0.34268677656962415, 0.3829870638965106,
        0.40039665050682932, 0.40039665050682932, 0.40039665050682932,
        0.30550774526677926, 0.34217877094971788, 0.37026406429391284,
        0.39178690344061956, 0.5, 0.38803599788247994, 0.394144144144146,
        0.38767923526288051, 0.36887786732796229, 0.36588459099556309,
        0.33817903596021709, 0.31276778063410676, 0.32731508444962465,
        0.43431221020092969, 0.43431221020092969, 0.43431221020092969,
        0.38043478260869579, 0.44390091590341391, 0.44705304518664057,
        0.46516896356428117, 0.46525423728813509, 0.5, 0.48177676537585434,
        0.48177676537585434, 0.45737105465742828, 0.44796805261921474,
        0.43605658198614244, 0.42801429964250814, 0.45468416234360653,
        0.45649509803921517, 0.42266139657443985, 0.46235294117647141,
        0.46982270841192064, 0.46757852077001077, 0.45387072529124423,
        0.43352033660589046]

    def test_vertical_horizontal_filter_period_6(self):
        period = 6
        vhf = vertical_horizontal_filter.vertical_horizontal_filter(self.data, period)
        np.testing.assert_array_equal(vhf, self.vhf_period_6_expected)

    def test_vertical_horizontal_filter_period_8(self):
        period = 8
        vhf = vertical_horizontal_filter.vertical_horizontal_filter(self.data, period)
        np.testing.assert_array_equal(vhf, self.vhf_period_8_expected)

    def test_vertical_horizontal_filter_period_10(self):
        period = 10
        vhf = vertical_horizontal_filter.vertical_horizontal_filter(self.data, period)
        np.testing.assert_array_equal(vhf, self.vhf_period_10_expected)

    def test_vertical_horizontal_filter_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            vertical_horizontal_filter.vertical_horizontal_filter(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
