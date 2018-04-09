class SimplePySparkSubmit:
    """ ... """

    sc = None

    def __init__(self, master="local"):
        ''' ... '''
        from pyspark import SparkConf, SparkContext
        conf = (SparkConf()
                .setMaster(master)
                .setAppName("My app")
                .set("spark.executor.memory", "1g"))
        try:
            self.sc = SparkContext(conf = conf)
        except Exception as err:
            print(err)

    def calculate_iterator(self, iterator):
        ''' ... '''
        from pyspark import SparkFiles

        path = "data/test.txt"
        with open(path, "w") as test_file:
            _ = test_file.write("100")
        self.sc.addFile(path)

        with open(SparkFiles.get("test.txt")) as test_file:
            file_val = int(test_file.readline())
        return [x * file_val for x in iterator]


if __name__ == "__main__":
    pys = SimplePySparkSubmit("spark://192.168.56.102:7077")
    print(pys.calculate_iterator([1,2,3,4]))