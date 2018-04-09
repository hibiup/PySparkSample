from unittest import TestCase

class TestPySpark(TestCase):
    """ ... """
    
    sc = None

    def __init__(self, *args, **kwargs):
        ''' ... '''
        from pyspark import SparkConf, SparkContext
        conf = (SparkConf()
                .setMaster("local")
                .setAppName("My app")
                .set("spark.executor.memory", "1g"))
        self.sc = SparkContext(conf = conf)

    def test_open_file(self, iterator):
        ''' ... '''
        from pyspark import SparkFiles

        path = "tests/data/test.txt"
        with open(path, "w") as test_file:
            _ = test_file.write("100")
        self.sc.addFile(path)

        with open(SparkFiles.get("test.txt")) as test_file:
            file_val = int(test_file.readline())
        return [x * file_val for x in iterator]
