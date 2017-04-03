import unittest
import numpy as np

from tests.sample_data import SampleData
from py_technical_indicators import rate_of_change


class TestRateOfChange(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.roc_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        2.1742696700107143, 1.1608210442407396, 1.32120262997626,
        0.31731137258776071, 0.2525377568705221, 0.73732832724039465,
        0.7005663629647797, 0.017173699705592047, -0.56615384615384901,
        -0.048157660772496585, -2.5108808925396948, -3.2302632383327783,
        -4.8029043098584738, -3.6737219952964417, -5.5580950027796661,
        -3.8784159362148873, -1.9697524858807067, 1.7083666159911499,
        0.97273264629538381, 2.0589697302671177, 1.9193280389360561,
        1.1754395009537562, -0.58775841102554971, -1.2496977563980116,
        0.76390669059214589, 0.12580231065468783, -1.25350318471338,
        -4.0239551478083495, -0.54383545755635232, -0.74666734506970645,
        3.2834175235262464, 4.7499870994375426, 6.4801784339236805,
        1.2115322319403983, 0.24349921183151021, -2.1313571419704904,
        -0.80051232788984961, 0.9812600526164863, 4.9238253744718889,
        4.4950715299351778, 4.2718348088582312, 2.864130704672982,
        3.1905173478207227, 0.54907511347552351, 0.52364348198445865,
        0.60698211896363075, -0.85209100235350255, -3.4580132577117255,
        -2.3614785331165113, -2.1359979552840032, -1.8522772612412253,
        -1.4510219235778841, 0.90848247484010791, -0.48347004722843478,
        -0.12436573475276091, -1.2983973292927755, -0.8374816260484067,
        -1.6937494626429326, 0.41837868891357782, -0.054789062110879923,
        1.1020555895310868, 0.98905068573351129, 0.28361528274069592,
        1.3556202273462294, 1.6582776836439823, -0.62094165864256634,
        -1.3506346132497928, -0.90450383105961396, -2.0847648964366359,
        -1.8040321098106535, -1.8098704396109382, -1.3828802920803154,
        0.43123499163932966, -1.1892677669586587, 0.20094105313081309,
        2.2176960250993059, 2.4470027386144579, -0.24411006234196006,
        0.37033279220778698, -1.6180060784216042, -1.9888860010643759,
        -1.5098636172371886, -0.45804208967585391, -0.01263583522871149,
        0.47477369120719126, 0.58970603091222262, 0.14199190771782505,
        0.81062000453845717, 1.4469859724504039, 1.489415322580637,
        0.57746142934257561, 1.1305602609950423, 0.92540486462827209,
        0.67891622547493558, 0.38116758958059771, 0.78508219024201042,
        -0.090575214650853414, -0.014868967226318636, -1.3548626577579861,
        -1.1836881099333387, -0.91147768365780135, -0.53276703550537907,
        -1.932013929337107, -3.9397930385700808, -4.6249937415510862,
        -5.307953806928964, -5.4211301720478531, -4.0513559279197384,
        -1.4924788467565109, -0.64175754950982145, -0.55962515673464119,
        -0.57028197275318626, -3.1147929617532371, -2.4668283824445614,
        -3.6455856712632775, -2.7740539679590102, -3.4519383961763141,
        -2.4264915786468775, -3.8787714052731674, -2.8115918188298501,
        -3.7705969884370187, -2.330858085808587]

        self.roc_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 2.8708435863461412, 1.19818652849741,
        0.65500826528455969, 0.70623387206302124, 1.2490715523644507,
        0.69904159668018007, -0.52942624969220242, -0.70534838076545636,
        -2.132923076923082, -2.2683493035661368, -4.8390853920186387,
        -4.8502854907139046, -6.240341452645521, -5.392994182448315,
        -4.1472604855148614, -0.72060062628116062, -0.71765196406687093,
        0.51792110077560571, 0.1002287270951624, 2.6868639300944408,
        2.6781625737573971, 0.011599731917310903, -0.41548439400082166,
        -0.73938329579148954, -0.64598820815176583, -3.3093709884467226,
        -1.6878980891719746, -0.57466870540264914, 3.8171578798149417,
        3.2843187137478442, 2.826995563988814, 0.76629341039270016,
        3.8461538461538498, 2.1600259151279508, 3.2282869189660328,
        0.53501160640027123, 0.93352053006230773, 1.9101529867960116,
        5.2490078094994237, 5.9269486953297656, 6.0018771720656572,
        2.3066991110890309, 1.4483269539449337, 0.91878568988238651,
        0.506514956872819, -1.8562218708186342, -2.8905919980689072,
        -3.7882595065450939, -1.4913962575540574, -1.4678139795284917,
        -1.5621032777569639, -2.5295499640896386, -0.46601556690297841,
        -0.41884166045239929, -0.1604317978310712, -1.4031067913325186,
        -0.68060822411898958, -1.4161661569451065, 1.1677136541319464,
        0.95258255715495055, 0.17722751269921982, 1.515963078762824,
        1.9453259701641783, 0.1206377633509971, -0.35632413036978144,
        -1.8109769646692788, -1.5738901977230386, -0.17691397246620061,
        -3.006282516933346, -3.3372142900913069, -0.77139982360904846,
        -1.4128885443496906, 0.93664743082010649, 1.2556863039963884,
        0.84744705016037392, 0.81092022366722771, 0.33979105385941144,
        -1.1229062867729935, 0.43628246753246003, -0.87439589457425915,
        -1.8279929207044618, -2.0692557114922931, -0.41035551595617625,
        0.65579984836998417, 0.89890485535228482, 0.97610869784826981,
        0.87079992963232256, 1.5380348453140278, 1.2498420320990902,
        1.5574596774193565, 1.3130970762876666, 1.411631846414455,
        1.1054836490964837, 0.58922454064154695, -0.023590176553840343,
        0.71643430397282726, -1.0806987939848176, -1.0073725295830489,
        -0.99975253650087104, -0.933839626958893, -1.9988111160647926,
        -4.8917700532767023, -5.5717348468888162, -4.9670743179680175,
        -5.1819956941871501, -5.1042343648452775, -5.8094239268859198,
        -4.329365380241109, -1.623054423900562, -1.150963948711889,
        -2.906355177192633, -2.8672510296757876, -3.9247708355283892,
        -2.9029307670895106, -3.9467427484545881, -4.7291647310229488,
        -6.0993096123207717, -3.6241045090602566, -4.2008698015765118,
        -2.636124362559634]

        self.roc_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 2.1944602183103017, 1.5905241131925048,
        1.6555427122562281, 0.66795895941625605, 0.01237930180738088,
        -0.028406283964023383, -2.0967741935483977, -2.9109421000981373,
        -4.4701538461538526, -3.9044749580163991, -6.2759762152884129,
        -6.5485578745307986, -4.8396987759707644, -2.2849362544869316,
        -2.9229723886589758, -1.8826162958864034, -1.575549294351021,
        1.1363343554330245, 0.84551926190536442, 1.5056379666692816,
        2.856096188818956, 0.5284322317884238, -1.808877178759638,
        -4.1448733122080883, -1.0830556267623743, 0.16559691912708133,
        2.6229299363057366, 3.4633027522935866, 3.3583772568527062,
        -0.64363488348427111, 0.28334059847688869, 1.7106145827958088,
        6.938211943389712, 4.9433106575963688, 5.0327442361173391,
        1.4597996499460011, 1.2463361166531202, 3.306609478448435,
        6.9952630905133759, 5.3529193674171101, 4.2122219121787925,
        2.6828723245766515, 1.4310408692431205, -1.5520523207574692,
        -1.5599192512387594, -2.1919474516482156, -2.0252247902962974,
        -3.1313566420178476, -1.2001553284954964, -2.5461582464126136,
        -2.9029488931071579, -2.4662503499738269, -0.50195825690348372,
        -0.52448421575938686, -0.002487314695067095, -1.1247028099092102,
        0.060525958224723668, -0.42251618212411923, 0.24228497208726515,
        1.479304676993574, 1.8371753429102788, 0.27902689370819383,
        -0.07496439191384377, -1.0782777404671242, -0.58182996112827157,
        -1.0900427128854564, -2.5002158548468643, -1.735501152432561,
        -1.9804652989103742, -3.3666278570990902, -0.27203955132106145,
        1.0265322963815096, 1.5879002753366269, -0.13784979385190202,
        -1.2268636970657665, -0.077170255294387272, 0.40572066132466927,
        -0.37555394206454518, 0.60115665584415701, -1.437397239798724,
        -1.7809626356761823, -1.4145689463132038, 0.010039278677832133,
        1.0424564063684612, 1.6332214977527348, 1.7047176482472979,
        0.67477570304842849, 1.6061117974836754, 1.99039555162391,
        1.8397177419354867, 1.4938676106905655, 1.3212874082439265,
        0.6978052898142989, 0.52071005917159141, -1.0143775918154452,
        -0.28332854878369618, -0.72460171720681321, -0.75707824794001621,
        -2.0861172976985909, -5.2752662370592063, -5.6360529053351156,
        -5.9088707574233501, -6.1232077131845353, -4.7626215114455981,
        -5.5712712161417901, -5.3791931210318413, -5.9342772242615034,
        -4.8196729597897221, -3.9446881855217844, -3.4345184193603515,
        -3.7180756285883931, -3.3015629950364334, -4.225055315562102,
        -4.8554499542688987, -6.5805463095049461, -5.8985147529233668,
        -6.4139670738183829, -3.4501039924962269]

    def test_roc_period_6(self):
        period = 6
        roc = rate_of_change.rate_of_change(self.data, period)
        np.testing.assert_array_equal(roc, self.roc_period_6_expected)

    def test_roc_period_8(self):
        period = 8
        roc = rate_of_change.rate_of_change(self.data, period)
        np.testing.assert_array_equal(roc, self.roc_period_8_expected)

    def test_roc_period_10(self):
        period = 10
        roc = rate_of_change.rate_of_change(self.data, period)
        np.testing.assert_array_equal(roc, self.roc_period_10_expected)

    def test_roc_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            rate_of_change.rate_of_change(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
