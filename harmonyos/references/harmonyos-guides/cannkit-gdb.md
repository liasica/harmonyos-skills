---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gdb
title: gdb调试
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 调测功能介绍 > 更多功能 > gdb调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d60f266cf0e095011f916bf571dc4dab1b929bce2c79043f72fb60d4ae881837
---

## 功能介绍

可使用gdb单步调试算子计算精度。由于cpu调测已转为多进程调试，每个核都会拉起独立的子进程，故gdb需要转换成子进程调试的方式。

## 使用方法（命令行）

* 调试单独一个子进程

  在gdb启动后，首先设置跟踪子进程，之后再打断点，就会停留在子进程中，设置的命令为：

  ```
  1. set follow-fork-mode child
  ```

  但是这种方式只会停留在遇到断点的第一个子进程中，其余子进程和主进程会继续执行直到退出。涉及到核间同步的算子无法使用这种方法进行调试。
* 调试多个子进程

  如果涉及到核间同步，那么需要能同时调试多个子进程。

  在gdb启动后，首先设置调试模式为只调试一个进程，挂起其他进程。设置的命令如下。

  ```
  1. (gdb) set detach-on-fork off
  ```

  查看当前调试模式的命令为：

  ```
  1. (gdb) show detach-on-fork
  ```

  中断gdb程序的方式要使用捕捉事件的方式，即gdb程序监控fork这一事件并中断。这样在每一次起子进程时就可以中断gdb程序。设置的命令为：

  ```
  1. (gdb) catch fork
  ```

  当执行r后，可以查看当前的进程信息：

  ```
  1. (gdb) info inferiors
  2. Num Description
  3. * 1 process 19613
  ```

  可以看到，当第一次执行fork的时候，程序断在了主进程fork的位置，子进程还未生成。 执行c后，再次查看info inferiors，可以看到此时第一个子进程已经启动。

  ```
  1. (gdb) info inferiors
  2. Num Description
  3. * 1 process 19613
  4. 2 process 19626
  ```

  这个时候可以使用切换到第二个进程，也就是第一个子进程，再打上断点进行调试，此时主进程是暂停状态：

  ```
  1. (gdb) inferior 2
  2. [Switching to inferior 2 [process 19626] ($HOME/demo)]
  3. (gdb) info inferiors
  4. Num Description
  5. 1 process 19613
  6. * 2 process 19626
  ```

  请注意，inferior后跟的数字是进程的序号，而不是进程号。 如果遇到同步阻塞，可以切换回主进程继续生成子进程，然后再切换到新的子进程进行调试，等到同步条件完成后，再切回第一个子进程继续执行。

  如下是调试一个单独子进程的调试命令样例：

  add\_custom\_cpu获取方法见[CPU孪生调试功能](cannkit-cpu-twin-debugging.md)，位于调试工作路径debug\_workspace下的AddCustom/cpu/build/add\_custom\_cpu。

  ```
  1. gdb --args add_custom_cpu
  2. set follow-fork-mode child
  3. break add_custom.cpp:45
  4. run
  5. list
  6. backtrace
  7. print i
  8. break add_custom.cpp:56
  9. continue
  10. display xLocal
  11. quit
  ```
