pyspark has Spark binary internally, which is under <site-packages>/pyspark/jars, it will use this embedded Spark to submit job.

* master=local: Pyspark will start local spark server(s) and submit job to, so `hostname` must be able to be resolved

* master=spark://...:7077: Submit job to remote. 