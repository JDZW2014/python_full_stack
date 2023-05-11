# 简介调用spark的python package, 支持大部分的spark功能：SparkDataFrame, Spark SQL, Streaming, MLlib 等等

## 基础概念
1. RDD Resilient Distributed Datasets 弹性分布数据集
1. RDD运行时的相关名词

    - Client：负责提交job到Master
    - Job: job 来自于我们编写的程序，包含了对RDD操作
    - Master: 指的是Standalone模式中的主控节点，负责收集来自Client的job，并管理着worker，可以给worker分配任务和资源（主要是driver 和 executor资源）
    - Worker: 指的是Standolone模式中的slave节点，负责管理本节点的资源，同时受Master管理，需要定期给Master汇报heartbeat(心跳)，启动Driver 和 Executor;
    - Driver: 指的是job(作业)的主进程，一般每个Spark作业都会有一个Driver进程，负责整个作业的运行，包括了job解析、stage的生成、调度Task到Executor上执行；
    - Stage: job 的基本调度单位，每个job都会分成若干组Task，每组任务就被称为Stage;
    - Task: 任务，指的是直接运行在executor 上的东西，是executor上的一个线程
    - Executor: 指的是执行器，一个集群可以配置若干个Executor, 每个Executor接收来自Driver 的Task，并执行他（同时可以执行多个Task）.
    - Client 将 Job 发给 Master, Master 创建负责该任务的 Driver, Driver：1. 向集群申请资源, 创建Executor(在Worker中)；2. 将Job 拆分为Stage, 在生成Task, 分配给Executor中

1. DAG， 有向无环图
    - spark 是如何将job 拆分为不同的stage, 不同stage之间的调度方式
1. spark 的部署模式：local 模式, Standalone 模式， Mesos模式，YARN 模式
1. Shuffle 指的是数据从Map端到Reduce端的数据传输过程，Shuffle 性能的高低直接影响程序的性能。
因为Reduce task 需要夸节点去拉分布在不同节点上的Map task 计算结果，这一个过程是需要磁盘的IO消耗以及数据网络传输的消耗，所以需要根据实际数据情况进行适当调整。
另外shuffle可以分为两部分，分别是Map阶段的数据准备与Reduce阶段的数据拷贝处理，在Map端叫Shuffle Write，在Reduce 端叫Shuffle Read.

1. 什么是惰性执行，RDD的算子可以分为Transform 算子和Action 算子，其中Transform算子的操作不会真正执行，只会记录下依赖关系，知道遇见了Action算子，
在这之前的所有Transform才会被触发计算。

## 常用函数
  
 
 
