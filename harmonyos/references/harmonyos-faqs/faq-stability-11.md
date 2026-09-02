---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-11
title: Native内存泄漏导致应用闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > Native内存泄漏导致应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:26+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:1a4e544322d1997a255110877d189608c16393337569bfa26f887804c72310d9
---

## 问题现象

应用闪退，在memory-leak目录下存在前缀是memleak-native-[process\_name]-[pid]的内存泄漏日志文件。

## 背景知识

* 内存泄漏是指程序在申请分配内存后，由于疏忽或错误未能释放已经不再使用的内存空间，导致这部分内存无法被后续的程序使用。随着时间推移，未释放的内存会逐渐累积，最终可能导致系统性能下降甚至崩溃。
* 参考文档[日志获取](../harmonyos-guides/resource-leak-guidelines.md#日志获取)，native内存泄漏包括以下三个日志文件：
  + memleak-native-[process\_name]-[pid]-sample.txt。
  + memleak-native-[process\_name]-[pid]-smaps.txt。
  + memleak-native-[process\_name]-[pid]-[timestamp].txt。
* Native内存泄漏[日志规格](../harmonyos-guides/resource-leak-guidelines.md#native内存泄漏日志规格)中说明了日志文件中每个字段的具体含义。
* DevEco Profiler提供了基础的内存场景分析Allocation，可以使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化，参考文档[内存分析及优化](../harmonyos-guides/ide-insight-session-allocations-memory.md)。

## 问题定位

### 场景一

1. 查看内存采样文件memleak-native-[module]-0-sample.txt，可以看到应用的PSS内存（实际使用的物理内存）一直在上涨，从13点26分的2611496KB到13点40分的3798097KB，超过了阈值3145728KB。

   ```shell
   pid: 61658
   processName: com.hx.example
   SoftThreshold: 1572864(KB)
   ThresholdInfo: 1572864(KB)
   ThresholdWarn: 2044723(KB)
   ThresholdErro: 2359296(KB)
   ThresholdCtrl: 3145728(KB)

   index   rss(KB)     offset(KB)  pss(KB)     swappss(KB) total(KB)   overCnt time(s) realtime
   5       2611496     0           2611496     19696       2631192     1       121263  2024/10/21 13:26:02
   6       3063312     0           3063312     19652       3082964     2       121383  2024/10/21 13:28:02
   7       3506044     0           3506044     19640       3525684     3       121503  2024/10/21 13:30:02
   8       3506968     -177063     3329905     19432       3349337     4       121504  *2024/10/21 13:30:02
   9       4005260     -177063     3828197     19504       3847701     5       121623  2024/10/21 13:32:02
   10      3975160     -177063     3798097     1246008     5044105     6       122103  2024/10/21 13:40:02
   ```
2. 查看内存映射文件memleak-native-[process\_name]-[pid]-smaps.txt，搜索字段LOGGER\_MEMCHECK\_SMAPS\_INFO，查看应用进程smaps汇总信息。主要关注表中PSS这一列。从内存映射文件中可以看到[anon:native\_heap:jemalloc]这部分PSS的值为3068350KB，SWAP PSS的值为15947KB。明显超过了PSS一列总和的50%，可以判断应用出现了堆内存泄漏。

   ```shell
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2024/10/21 13:30:03

   -------------------------------[memory]-------------------------------

                                       Shared      Shared      Private     Private                                                     
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
   // ...
   5804        5684        2076        3608        0           2076        0           44          44          251                           [anon:native_heap:brk]                    
   120876      99416       99144       276         0           99140       0           60          9           33                            [anon:native_heap:jemalloc meta]          
   3514368     3087120     3068350     19196       0           3067924     0           16096       15947       42                            [anon:native_heap:jemalloc]
   ```
3. 在内存映射文件中搜索字段LOGGER\_MEMCHECK\_DETAIL\_INFO，查看进程jemalloc快照详细信息，主要关注size和allocated两列，可以看到size为64申请的总内存最多，达到了2960311936字节。

   ```shell
   bins:           size ind    allocated      nmalloc (#/sec)      ndalloc (#/sec)    nrequests   (#/sec)  nshards      curregs     curslabs  nonfull_slabs regs pgs   util       nfills (#/sec)     nflushes (#/sec)       nslabs     nreslabs (#/sec)      n_lock_ops (#/sec)       n_waiting (#/sec)      n_spin_acq (#/sec)  n_owner_switch (#/sec)   total_wait_ns   (#/sec)     max_wait_ns  max_n_thds
                      8   0       272784       336143       2       302045       2       149869         1        1        34098           70             12  512   1  0.951        24359       0        19438       0          131        39871       0           46090       0               1       0              14       0            7568       0               0         0               0           1
                     16   1      1624128      1184687       9      1083179       8       264521         2        1       101508          503            124  256   1  0.788        93630       0        83903       0         1554        66169       0          182043       1               0       0              74       0           14038       0               0         0               0           0
                     32   2     37318752      3502474      28      2336263      19       329089         2        1      1166211         9159            114  128   1  0.994       318246       2       209344       1        11996       446882       3          597221       4             102       0            2996       0          160171       1        92122495       758        15998593           9
                     48   3     44898432      1778928      14       843544       6       277683         2        1       935384         3664             35  256   3  0.997       151543       1        68810       0         4053       232919       1          262331       2              22       0             125       0          127803       1        16000625       131         4001563           2
   申请内存最多 -->   64   4   2960311936     47564752     391      1309878      10       137023         1        1     46254874       722743             45   64   1  0.999      4754348      39       125006       1       729572        92048       0         5615050      46               0       0              54       0           10955       0               0         0               0           0
                     80   5      5321680       581066       4       514545       4        63701         0        1        66521          261             10  256   5  0.995        53660       0        47754       0         1170        17035       0          104153       0               0       0               9       0            6445       0               0         0               0           0
                     96   6      2742912       469571       3       440999       3       266784         2        1        28572          240             31  128   3  0.930        25200       0        20412       0         2631        15409       0           51402       0               1       0               8       0            6063       0         4001093        32         4001093           1
                    112   7      2325680        96100       0        75335       0        20587         0        1        20765           86             21  256   7  0.943        15613       0         9079       0          176         4478       0           25079       0               1       0               2       0            3937       0         3999688        32         3999688           1
                    128   8      2122752       231197       1       214613       1         9253         0        1        16584          575            100   32   1  0.901        46747       0        22299       0         3230        34806       0           79054       0               0       0              27       0            6628       0               0         0               0           0
                    160   9      3918720        77207       0        52715       0        10217         0        1        24492          194              2  128   5  0.986        15459       0         8828       0          216         9260       0           25833       0               0       0               0       0            6114       0               0         0               0           0
                    192  10       641472        52657       0        49316       0         2156         0        1         3341           59             27   64   3  0.884        13168       0         7991       0          116        11276       0           22005       0               1       0               0       0            5490       0               0         0               0           1
                    224  11      1485568        54562       0        47930       0           87         0        1         6632           56             18  128   7  0.925        25181       0         6727       0           98         9002       0           32661       0               0       0               1       0            3142       0               0         0               0           0
   ```
4. 使用profiler解析栈信息日志文件memleak-native-[process\_name]-[pid]-[timestamp].txt，参考文档[内存分析及优化](../harmonyos-guides/ide-insight-session-allocations-memory.md)，找到其中分配64字节块的堆栈和关联的so库。

## 场景二

1. 查看内存采样文件memleak-native-[module]-0-sample.txt，可以看到应用的TotalPSS内存（PSS + SwapPss = TotalPSS）一直在上涨，从3点18分的2047340KB到10点34分的3578724KB，超过了阈值3145728KB。

   ```shell
   pid: 47781
   processName: com.hx.example
   SoftThreshold: 1572864(KB)
   HardThreshold: 3145728(KB)

   Index   RSS(KB)     Offset(KB)  PSS(KB)     SwapPSS(KB) TotalPSS(KB)    Level   Running Time(s) Realtime
   69      1463024     0           1463024     584316      2047340         W       546388          2025/08/18 03:18:46
   70      1475752     0           1475752     584316      2060068         W       546508          2025/08/18 03:20:46
   // ...
   0       2897696     -120852     2776844     460979      3237823         C       571469          *2025/08/18 10:16:48
   1       2904080     -120852     2783228     493804      3277032         C       571588          2025/08/18 10:18:47
   2       3068680     -120852     2947828     493776      3441604         C       572069          2025/08/18 10:26:47
   3       3205804     -120852     3084952     493772      3578724         C       572549          2025/08/18 10:34:47
   ```
2. 查看内存映射文件memleak-native-[process\_name]-[pid]-smaps.txt，搜索字段LOGGER\_MEMCHECK\_SMAPS\_INFO，查看应用进程smaps汇总信息。

   观察到抓取了三次SMAPS\_INFO内容，分别在3、6、10点各抓取了一次，重点关注表中PSS这一列。可以看到[anon:native\_heap:jemalloc]的PSS的值增加较大，在10点时已经达到了为1765572KB，SWAP PSS的值为428488KB，超过总PSS内存summary的50%，说明是堆内存过大，应用出现了堆内存泄漏。

   ```shell
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 03:50:46
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
   // ...
   1663488     612820      609032      3964        0           608856      0           529108      515557      49                            [anon:native_heap:jemalloc]               
   45842956    1388852     1839337     109528      424         1278424     476         584284      550476      5321                          Summary
   *********
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 06:36:47
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
   // ...
   2253312     978656      974856      3980        0           974676      0           453676      440148      52                            [anon:native_heap:jemalloc]               
   46626456    2046904     2400395     134284      472         1911640     508         506508      473514      5444                          Summary
   *********
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 10:16:48
   Size        Rss         Pss         Clean       Dirty       Clean       Dirty       Swap        SwapPss     Counts                        Name
   // ...
   3498496     1769376     1765572     3980        0           1765396     0           442020      428488      59                            [anon:native_heap:jemalloc]               
   47875540    2932248     3271740     135540      472         2795728     508         493816      460809      5518                          Summary
   ```
3. 在内存映射文件中搜索字段LOGGER\_MEMCHECK\_SAMPLE\_NMD\_INFO，其中记录抓取进程native日志时内存的快照信息，主要关注size和allocated两列，观察到size为48申请的总内存逐渐增大，达到了817601088字节。

   ```shell
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 03:50:46
   // ...
   LOGGER_MEMCHECK_SAMPLE_NMD_INFO
               size       allocated         nmalloc         ndalloc
                  8          553600       132546322       132477122
                 16         2528528       199609416       199451383
                 32        14937504       239083888       238617091
                 48       402098832        52331956        43954897
   *********
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 06:36:47
   // ... 
   LOGGER_MEMCHECK_SAMPLE_NMD_INFO
               size       allocated         nmalloc         ndalloc
                  8          461768       177274989       177217268
                 16         2291728       269894269       269751036
                 32        16946880       319668275       319138685
                 48       540506976        70543922        59283360
   *********
   LOGGER_MEMCHECK_SMAPS_INFO
   get info realtime: 2025/08/18 10:16:48
   // ...
   LOGGER_MEMCHECK_SAMPLE_NMD_INFO
               size       allocated         nmalloc         ndalloc
                  8          826432       251754132       251650828
                 16         3985904       418515432       418266313
                 32        21553760       445480795       444807240
                 48       817601088       108553042        91519686
   ```
4. 使用profiler解析栈信息日志文件memleak-native-[process\_name]-[pid]-[timestamp].txt，参考文档内存分析及优化，找到其中分配48字节块的堆栈和关联的so库。

## 分析结论

### 场景一

应用存在Native内存泄漏，导致应用闪退。

### 场景二

应用存在Native内存泄漏，导致应用闪退。

## 修改建议

### 场景一

参考文档[内存分析及优化](../harmonyos-guides/ide-insight-session-allocations-memory.md)，找到其中申请内存最多的字节块堆栈和关联的so库，根据实际需要进行对应优化，相关案例可参考[案例：Native内存泄漏分析](../harmonyos-guides/ide-native-allocation-case.md)。

### 场景二

参考文档[内存分析及优化](../harmonyos-guides/ide-insight-session-allocations-memory.md)，找到其中申请内存最多的字节块堆栈和关联的so库，根据实际需要进行对应优化，相关案例可参考[案例：Native内存泄漏分析](../harmonyos-guides/ide-native-allocation-case.md)。
