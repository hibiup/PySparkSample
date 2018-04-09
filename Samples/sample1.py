class LocalPySpark:
    """ ... """

    sc = None

    def __init__(self, *args, **kwargs):
        ''' ... '''
        from pyspark import SparkConf, SparkContext
        conf = (SparkConf()
                .setMaster("local")
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
    pys = LocalPySpark()
    print(pys.calculate_iterator([1,2,3,4]))