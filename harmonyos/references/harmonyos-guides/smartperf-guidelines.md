---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/smartperf-guidelines
title: HiSmartPerf Device性能使用指导
breadcrumb: 指南 > 应用测试 > 专项测试 > 命令行工具 > HiSmartPerf Device性能使用指导
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4e4f3a522ae07d9a000b7c33022e7fa477befab60260e75cdf1247e53f6528f0
---

## 工具简介

HiSmartPerf Device是一款性能功耗测试工具，支持监测性能、功耗相关指标，包括FPS、CPU、GPU、RAM、Temp等，并提供Device hap端和Device daemon端。Device hap适用于有屏设备，支持可视化操作，测试过程中可通过悬浮窗的开始和暂停来实时展示性能指标数据，保存后可生成数据报告，在报告中可分析各指标数据详情。Device daemon端支持shell命令行方式，同时适用于有屏和无屏设备。

### 指标说明

* CPU：每秒读取一次设备节点下CPU大中小核的频点和各核使用率，衡量应用占用CPU资源的情况，占用过多的CPU资源会导致芯片发烫。
* GPU：每秒读取一次设备节点下GPU的频点和负载信息，衡量应用占用GPU资源的情况，当GPU占用过多时，会导致性能下降，应用程序的运行速度变慢。
* FPS：应用界面每秒刷新次数，衡量应用画面的流畅度，FPS越高通常表示图像流畅度越好，用户体验越好。
* TEMP：每秒读取一次设备节点下GPU温度、系统芯片温度信息。
* RAM：每秒读取一次应用进程的实际物理内存，衡量应用的内存占比情况。
* snapshot：每2秒截取一张应用界面截图。

## 实现原理

下图展示了HiSmartPerf Device工具的主要功能组成。Device hap端设置好采集项和采集参数后，启动应用，FPS、RAM、Trace等指标通过消息发送给Device daemon端，Device daemon端进行数据采集、数据持久化和数据分析，将生成的报告回传给Device hap端，Device hap端进行可视化显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/5uCnfpSRTAuaWZ5VLuZWRQ/zh-cn_image_0000002731520237.png)

## 约束与限制

1. Device daemon端从API version 9开始预置使用。
2. Device daemon端执行需连接硬件设备，Device hap端需在有屏幕设备使用。
3. Device daemon端执行前需完成[hdc环境配置](hdc.md)，并进入shell环境拉起daemon进程。

   ```shell
   C:\Users\issusser>hdc shell
   $
   ```
4. Device hap端从API version 20开始支持自动拉起Device daemon端的功能。

   **说明** 

   在使用可以自动拉起Device daemon进程的Device hap端时，点击性能/功耗测试，选择测试应用后，待hap端界面显示采集器连接成功，即Device daemon进程已被拉起。

   * 拉起和查看daemon进程（手动拉起daemon进程）。

     ```shell
     C:\Users\issusser>hdc shell
     // 拉起daemon进程
     $ SP_daemon
     // 查看daemon进程是否存在
     $ ps -ef | grep SP_daemon
     shell          1584     1 0 21:50:05 ?     00:00:00 SP_daemon
     shell          1595  1574 3 21:51:02 pts/0 00:00:00 grep SP_daemon
     $
     ```
   * 拉起和查看daemon进程（自动拉起daemon进程）。

     ```shell
     C:\Users\issusser>hdc shell
     // 查看daemon进程是否存在
     $ ps -ef | grep SP_daemon
     testserver   40960     1 4 15:38:48 ?     00:00:00 SP_daemon -deviceServer:69df7e4df0edf70cbe204549028d7171
     shell          41109 41033 67 15:38:59 ?    00:00:00 grep SP_daemon
     $
     ```

## HiSmartPerf Device-hap端

工具使用说明请参见[操作指导](../AppGallery-connect-Guides/smartperf-tool-device-haromnyos-0000002086884884.md#section91681917183510)，请前往[工具下载中心](https://developer.huawei.com/consumer/cn/download/hismartperf)获取HiSmartPerf工具。

## HiSmartPerf Device-daemon端

* 执行和查看帮助命令。

  ```shell
    $ SP_daemon --help
    HarmonyOS performance testing tool SmartPerf command-line version
    Usage: SP_daemon [options] [arguments]

    options:
    -N              set the collection times(default value is 0) range[1,2147483647], for example: -N 10
    -PKG            set package name, must add, for example: -PKG ohos.samples.ecg
    -PID            set process pid, must add, for example: -PID 3568
    -threads        get threads, must add -PID or -PKG for example:
                    -threads -PID 3568 or -threads -PKG ohos.samples.ecg
    -c              get device CPU frequency and CPU usage, process CPU usage and CPU load ..
    -ci             get cpu instructions and cycles
    -g              get device GPU frequency and GPU load
    -f              get app refresh fps(frames per second) and fps jitters and refreshrate
    -profilerfps    get refresh fps and timestamp
    -sections       set collection time period(using with profilerfps)
    -t              get remaining battery power and temperature..
    -p              get battery power consumption and voltage(Not supported by some devices)
    -print          start mode print log
    -r              get process memory and total memory
    -snapshot       get screen capture
    -net            get uplink and downlink traffic
    -start          collection start command
    -stop           collection stop command
    -VIEW           set layler, for example: -VIEW DisplayNode
    -OUT            set csv output path.
    -d              get device DDR information
    -screen         get screen resolution
    -deviceinfo     get device information
    -server         start a process to listen to the socket message of the start and stop commands
    -clear          clear the process ID
    -ohtestfps      used by the vilidator to obtain the fps, the collection times can be set
    -recordcapacity get the battery level difference
    --version       get version
    --help          get help
    -editor         scenario-based collection identifier, parameter configuration items can be added later
    responseTime   get the page response delay after an application is operated
    completeTime   get the page completion delay after an application is operated
    fpsohtest      used by the vilidator to obtain the fps
    example1:
    SP_daemon -N 20 -c -g -t -p -r -net -snapshot -d
    SP_daemon -N 20 -PKG ohos.samples.ecg -c -g -t -p -f -r -net -snapshot -d -nav -gc
    SP_daemon -start -c
    SP_daemon -stop
    example2: These parameters need to be used separately
    SP_daemon -screen
    SP_daemon -deviceinfo
    SP_daemon -server
    SP_daemon -clear
    SP_daemon -ohtestfps 10
    SP_daemon -recordcapacity
    example3: These parameters need to be used separately
    SP_daemon -editor responseTime ohos.samples.ecg app name
    SP_daemon -editor completeTime ohos.samples.ecg app name
    SP_daemon -editor fpsohtest

    command exec finished!
    $
  ```

### 基础采集

基础采集主要采集整机或者应用的gpu、fps、CPU、DDR、内存等，支持秒级采集和启停采集，并将采集的结果写入data.csv。

**1. 秒级采集**

| 命令参数 | 必选 | 说明 |
| --- | --- | --- |
| -N | 是 | 设置采集次数，一秒采集一次。 |
| -PKG | 否 | 设置包名。 |
| -PID | 是 | 设置进程ID或者线程ID。 |
| -threads | 否 | 采集应用子线程数量。 |
| -c | 否 | 采集cpu的频点和使用率。  设置应用包名时，采集整机和应用CPU信息。  不设置应用包名时，采集整机CPU信息。 |
| -ci | 否 | 采集cpu的指令数。  设置应用包名时，采集整机和应用CPU指令数。  不设置应用包名时，采集整机CPU指令数。 |
| -g | 否 | 采集gpu的频点和负载信息。 |
| -f | 否 | 采集指定应用的fps以及屏幕刷新率，必须设置应用包名。 |
| -t | 否 | 采集GPU温度、系统芯片温度。 |
| -p | 否 | 采集电流、电压。 |
| -r | 否 | 采集内存。  设置应用包名时，采集整机和应用内存信息。  不设置应用包名时，采集整机内存信息。 |
| -snapshot | 否 | 屏幕截图。 |
| -net | 否 | 采集网络速率。 |
| -VIEW | 否 | 设置图层，需要先获取应用图层名。 |
| -d | 否 | 采集DDR。 |
| -sections | 否 | 设置分段采集。 |

* 设置包名并采集1次应用的线程数量。

  ```shell
  $ SP_daemon -N 1 -PKG ohos.samples.ecg -threads

  order:0 timestamp=1741415592481
  order:1 threadsNum=18847:113|
  order:2 tids=18847:43411 43409 43350 43236 25783 25622 25384 25381 19423 19170 19167 19166 19165 19163 19162 19159 19157 19156 19154 19153 19152 19151 19150 19149 19147 19146 19145 19142 19141 19140 19139 19136 19135 19134 19120 19112 19111 19088 19083 19081 19077 19076 19075 19074 19073 19072 19071 19070 19055 19044 19040 19039 19034 19033 19032 19031 19030 19029 19028 19027 19019 19017 19016 19015 19014 19013 19012 19011 19009 19007 19006 19005 19004 19003 19001 19000 18999 18998 18997 18996 18995 18994 18993 18992 18991 18990 18989 18988 18987 18986 18985 18984 18983 18982 18981 18980 18977 18974 18946 18942 18936 18934 18933 18931 18930 18929 18928 18927 18926 18925 18924 18923 18847|

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需进入被测应用内。
* 采集2次整机CPU大中小核频率、各核使用率。

  ```shell
  $ SP_daemon -N 2 -c

  order:0 timestamp=1739348046398
  order:1 TotalcpuUsage=7.072368
  order:2 TotalcpuidleUsage=92.927632
  order:3 TotalcpuioWaitUsage=0.082237
  order:4 TotalcpuirqUsage=0.246711
  order:5 TotalcpuniceUsage=0.000000
  order:6 TotalcpusoftIrqUsage=0.000000
  order:7 TotalcpusystemUsage=3.125000
  order:8 TotalcpuuserUsage=3.618421
  order:9 cpu0Frequency=550000
  order:10 cpu0Usage=16.666667
  order:11 cpu0idleUsage=83.333333
  order:12 cpu0ioWaitUsage=0.000000
  order:13 cpu0irqUsage=2.941176
  order:14 cpu0niceUsage=0.000000
  order:15 cpu0softIrqUsage=0.000000
  order:16 cpu0systemUsage=5.882353
  order:17 cpu0userUsage=7.843137
  order:18 cpu1Frequency=550000
  ...

  command exec finished!
  $
  ```
* 设置包名并采集2次整机CPU大中小核频率、各核使用率以及进程CPU使用率、负载。

  ```shell
  $ SP_daemon -N 2 -PKG ohos.samples.ecg -c

  order:0 timestamp=1741415021814
  order:1 ChildProcCpuLoad=NA
  order:2 ChildProcCpuUsage=NA
  order:3 ChildProcId=NA
  order:4 ChildProcSCpuUsage=NA
  order:5 ChildProcUCpuUsage=NA
  order:6 ProcAppName=ohos.samples.ecg
  order:7 ProcCpuLoad=2.742330
  order:8 ProcCpuUsage=7.825508
  order:9 ProcId=18847
  order:10 ProcSCpuUsage=2.014652
  order:11 ProcUCpuUsage=5.810856
  order:12 TotalcpuUsage=22.527016
  order:13 TotalcpuidleUsage=77.472984
  order:14 TotalcpuioWaitUsage=0.000000
  order:15 TotalcpuirqUsage=0.083126
  order:16 TotalcpuniceUsage=0.000000
  order:17 TotalcpusoftIrqUsage=0.000000
  order:18 TotalcpusystemUsage=7.148795
  order:19 TotalcpuuserUsage=15.295096
  order:20 cpu0Frequency=1430000
  order:21 cpu0Usage=52.475248
  order:22 cpu0idleUsage=47.524752
  order:23 cpu0ioWaitUsage=0.000000
  order:24 cpu0irqUsage=0.000000
  ...

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需进入被测应用内。
* 设置进程ID并采集2次整机CPU大中小核频率、各核使用率以及进程CPU使用率、负载。

  ```shell
  $ SP_daemon -N 2 -PID 18847 -c

  order:0 timestamp=1741415133211
  order:1 ChildProcCpuLoad=NA
  order:2 ChildProcCpuUsage=NA
  order:3 ChildProcId=NA
  order:4 ChildProcSCpuUsage=NA
  order:5 ChildProcUCpuUsage=NA
  order:6 ProcAppName=ohos.samples.ecg
  order:7 ProcCpuLoad=2.510634
  order:8 ProcCpuUsage=7.005678
  order:9 ProcId=18847
  order:10 ProcSCpuUsage=2.697061
  order:11 ProcUCpuUsage=4.308617
  order:12 TotalcpuUsage=24.979114
  order:13 TotalcpuidleUsage=75.020886
  order:14 TotalcpuioWaitUsage=0.000000
  order:15 TotalcpuirqUsage=0.083542
  order:16 TotalcpuniceUsage=0.000000
  order:17 TotalcpusoftIrqUsage=0.000000
  order:18 TotalcpusystemUsage=8.270677
  order:19 TotalcpuuserUsage=16.624896
  order:20 cpu0Frequency=1430000
  order:21 cpu0Usage=50.000000
  order:22 cpu0idleUsage=50.000000
  order:23 cpu0ioWaitUsage=0.000000
  order:24 cpu0irqUsage=0.000000
  ...

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需进入被测应用内。
* 采集1次整机GPU频率和负载。

  ```shell
  $ SP_daemon -N 1 -g

  order:0 timestamp=1705041456507
  order:1 gpuFrequency=279000000
  order:2 gpuLoad=12.000000

  command exec finished!
  $
  ```
* 采集2次整机温度。

  ```shell
  $ SP_daemon -N 2 -t

  order:0 timestamp=1739348774378
  order:1 Battery=34.000000
  order:2 cluster0=39.000000
  order:3 gpu=38.000000
  order:4 shell_back=35.838000
  order:5 shell_frame=34.838000
  order:6 shell_front=35.098000
  order:7 soc_thermal=46.785000
  order:8 system_h=35.894000

  order:0 timestamp=1739348775386
  order:1 Battery=34.000000
  order:2 cluster0=41.000000
  order:3 gpu=38.000000
  order:4 shell_back=35.820000
  order:5 shell_frame=34.820000
  order:6 shell_front=35.140000
  order:7 soc_thermal=45.016000
  order:8 system_h=35.842000

  command exec finished!
  $
  ```
* 采集1次整机电流和电压。

  ```shell
  $ SP_daemon -N 1 -p

  order:0 timestamp=1705041491090
  order:1 currentNow=-255
  order:2 voltageNow=4377614

  command exec finished!
  $
  ```
* 采集2次整机内存。

  ```shell
  $ SP_daemon -N 2 -r

  order:0 timestamp=1705041562521
  order:1 memAvailable=7339224
  order:2 memFree=7164708
  order:3 memTotal=11641840

  order:0 timestamp=1705041563527
  order:1 memAvailable=7339136
  order:2 memFree=7164684
  order:3 memTotal=11641840

  command exec finished!
  $
  ```
* 设置包名并采集1次整机和指定应用进程内存。

  ```shell
  $ SP_daemon -N 1 -PKG ohos.samples.ecg -r

  order:0 timestamp=1741415257059
  order:1 arktsHeapPss=44835
  order:2 childCarktsHeapPss=NA
  order:3 childGpuPss=NA
  order:4 childGraphicPss=NA
  order:5 childHeapAlloc=NA
  order:6 childHeapFree=NA
  order:7 childHeapSize=NA
  order:8 childNativeHeapPss=NA
  order:9 childPrivateClean=NA
  order:10 childPrivateDirty=NA
  order:11 childPss=NA
  order:12 childSharedClean=NA
  order:13 childSharedDirty=NA
  order:14 childStackPss=NA
  order:15 childSwap=NA
  order:16 childSwapPss=NA
  order:17 gpuPss=222377
  order:18 graphicPss=184276
  order:19 heapAlloc=154696
  order:20 heapFree=780
  order:21 heapSize=163208
  order:22 memAvailable=4612096
  order:23 memFree=1240924
  order:24 memTotal=11692696
  order:25 nativeHeapPss=85290
  order:26 privateClean=195816
  order:27 privateDirty=418973
  order:28 pss=693349
  order:29 sharedClean=146848
  order:30 sharedDirty=71056
  order:31 stackPss=2492
  order:32 swap=25360
  order:33 swapPss=25356

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需要拉起被测应用的进程。
* 设置进程ID并采集1次整机和指定应用进程内存。

  ```shell
  $ SP_daemon -N 1 -PID 18847 -r

  order:0 timestamp=1741415293198
  order:1 arktsHeapPss=45011
  order:2 childCarktsHeapPss=NA
  order:3 childGpuPss=NA
  order:4 childGraphicPss=NA
  order:5 childHeapAlloc=NA
  order:6 childHeapFree=NA
  order:7 childHeapSize=NA
  order:8 childNativeHeapPss=NA
  order:9 childPrivateClean=NA
  order:10 childPrivateDirty=NA
  order:11 childPss=NA
  order:12 childSharedClean=NA
  order:13 childSharedDirty=NA
  order:14 childStackPss=NA
  order:15 childSwap=NA
  order:16 childSwapPss=NA
  order:17 gpuPss=222381
  order:18 graphicPss=184276
  order:19 heapAlloc=154588
  order:20 heapFree=757
  order:21 heapSize=163184
  order:22 memAvailable=4612096
  order:23 memFree=1238420
  order:24 memTotal=11692696
  order:25 nativeHeapPss=85274
  order:26 privateClean=195996
  order:27 privateDirty=418977
  order:28 pss=693440
  order:29 sharedClean=146848
  order:30 sharedDirty=71056
  order:31 stackPss=2492
  order:32 swap=25360
  order:33 swapPss=25356

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需要拉起被测应用的进程。
* 采集1整机cpu指令数。

  ```shell
  $ SP_daemon -N 1 -ci

  order:0 hw-cpu-cycles=2168073451.00000
  order:1 hw-instructions=833680950.00000
  order:2 timestamp=1705041491090

  command exec finished!
  $
  ```
* 采集1整机和指定应用cpu指令数。

  ```shell
  $ SP_daemon -N 1 -pkg ohos.samples.ecg -ci

  order:0 cycles per instruction=2.617221
  order:1 hw-cpu-cycles=1923046916.000000
  order:2 hw-instructions=734766759.000000
  order:3 timestamp=1501838024624

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需进入被测应用内。
* 采集2次截图。

  ```shell
  $ SP_daemon -N 2 -snapshot

  order:0 timestamp=1739349178766
  order:1 capture=data/local/tmp/capture/screenCap_1739349178766.png

  order:0 timestamp=1739349179769
  order:1 capture=NA

  command exec finished!
  $
  ```

  **说明** 

  + 截图采集是2秒截取一次。
  + 截图报告存放路径为：data/local/tmp/capture。
  + 采集结束后：进入 data/local/tmp/capture 查看生成的截图。
  + 导出截图示例：hdc file recv data/local/tmp/capture/screenCap\_1700725192774.png D:\。
* 采集2次网络速率。

  ```shell
  $ SP_daemon -N 2 -net

  order:0 timestamp=1739349429109
  order:1 networkDown=580407
  order:2 networkUp=58978

  order:0 timestamp=1739349430113
  order:1 networkDown=25212
  order:2 networkUp=594

  command exec finished!
  $
  ```
* 设置包名并采集5次指定应用帧率。

  ```shell
  $ SP_daemon -N 5 -PKG ohos.samples.ecg -f

  order:0 fps=32
  order:1 fpsJitters=33259375;;49716667;;33148958;;16629167;;33183854;;33309375;;49678125;;49751042;;33167708;;49753125;;16633333;;16572917;;16648438;;49680208;;33190104;;33264063;;16792187;;49486458;;16582292;;16600000;;16597917;;33223437;;33200521;;33118750;;33220833;;33395313;;16365104;;16604688;;49819791;;16526042;;33177083
  order:2 refreshrate=60
  order:3 timestamp=1773042668242

  order:0 fps=35
  order:1 fpsJitters=49807292;;16559375;;16594271;;16603646;;33205208;;49798437;;16518230;;33218750;;33284374;;16462500;;33211980;;16557291;;49760417;;16601562;;33187500;;33161980;;16667708;;16592187;;33126042;;33278646;;33118229;;33175000;;33147396;;33188021;;16578125;;33197916;;16727605;;33089583;;33164583;;33194271;;33170313;;16578645;;16612500;;66352084
  order:2 refreshrate=60
  order:3 timestamp=1773042669243
  ...

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需要进入被测应用内滑动或切换应用。
* 设置进程ID采集5次指定应用帧率。

  ```shell
  $ SP_daemon -N 5 -PID 18847 -f

  order:0 timestamp=1741415862598
  order:1 fps=28
  order:2 fpsJitters=50192708;;16733855;;33466145;;33460938;;33468229;;33503125;;50156250;;16731250;;33458854;;33460417;;33462500;;33466667;;33461458;;33622396;;33307291;;50336980;;33302083;;16733854;;33464062;;33456771;;33467188;;50186979;;16728646;;33458854;;16736458;;33461459;;33448958;;33464062
  order:3 refreshrate=60
  ...

  command exec finished!
  $
  ```

  **说明** 

  + 使用该命令采集时需要进入被测应用内滑动或切换应用。
* 采集10次指定图层帧率。

  ```shell
  $ SP_daemon -N 10 -VIEW DisplayNode -f

  order:0 timestamp=1705306822850
  order:1 fps=15
  order:2 fpsJitters=876291843;;8314062;;8308334;;8314583;;8310417;;8308333;;8326042;;8314583;;8292708;;8492709;;8143750;;8340104;;8294271;;8302604;;8297396
  order:3 refreshrate=120

  order:0 timestamp=1705306823852
  order:1 fps=12
  order:2 fpsJitters=906667363;;8279167;;8311458;;8315625;;8291146;;8313021;;8323438;;8293750;;8303125;;8313541;;8301563;;8317708
  order:3 refreshrate=120
  ...

  command exec finished!
  $
  ```

  **说明** 

  + DisplayNode 是指定的图层名。
  + 使用该命令采集时，需在传入的图层上操作页面。
  + 该命令不能与指定应用帧率一起采集（SP\_daemon -N 20 -PKG ohos.samples.ecg -f 或 SP\_daemon -N 20 -VIEW DisplayNode -f）。
* 采集1次DDR信息。

  ```shell
  $ SP_daemon -N 1 -d

  order:0 timestamp=1739349607442
  order:1 ddrFrequency=418000000

  command exec finished!
  $
  ```
* 全量采集示例1，采集10次整机信息，包括cpu、gpu、温度、功耗、内存信息、DDR信息、网络速率、屏幕截图。

  ```shell
  $ SP_daemon -N 10 -c -g -t -p -r -d -net -snapshot

  order:0 Battery=34.000000
  order:1 TotalcpuUsage=50.000000
  order:2 TotalcpuidleUsage=50.000000
  order:3 TotalcpuioWaitUsage=0.000000
  order:4 TotalcpuirqUsage=0.000000
  order:5 TotalcpuniceUsage=0.000000
  order:6 TotalcpusoftIrqUsage=0.000000
  order:7 TotalcpusystemUsage=33.333333
  order:8 TotalcpuuserUsage=16.666667
  order:9 capture=data/local/tmp/capture/screenCap_1773044447159.png
  order:10 cluster0=42.000000
  order:11 cpu0Frequency=1400000
  order:12 cpu0Usage=0.000000
  order:13 cpu0_curFrequency=1400000
  order:14 cpu0idleUsage=0.000000
  order:15 cpu0ioWaitUsage=0.000000
  order:16 cpu0irqUsage=0.000000
  order:17 cpu0niceUsage=0.000000
  order:18 cpu0softIrqUsage=0.000000
  order:19 cpu0systemUsage=0.000000
  order:20 cpu0userUsage=0.000000
  ...
  order:122 currentNow=-326
  order:123 ddrFrequency=1531000000
  order:124 gpu=43.000000
  order:125 gpuFrequency=279000000
  order:126 gpuLoad=31.000000
  order:127 memAvailable=4262912
  order:128 memFree=620768
  order:129 memTotal=11689852
  order:130 networkDown=0
  order:131 networkUp=0
  order:132 npu_thermal=41.000000
  order:133 shell_back=37.384000
  order:134 shell_frame=36.384000
  order:135 shell_front=35.884000
  order:136 soc_thermal=45.068000
  order:137 system_h=37.388000
  order:138 timestamp=1773044447131
  order:139 voltageNow=3808748
  ...

  command exec finished!
  $
  ```
* 全量采集示例2，设置包名并采集指定应用信息，包括cpu、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图。

  ```shell
  $ SP_daemon -N 10 -PKG ohos.samples.ecg -c -g -t -p -f -r -d -net -snapshot -threads

  order:0 Battery=36.000000
  order:1 ChildProcCpuLoad=0.000000|0.000000|
  order:2 ChildProcCpuUsage=0.000000|0.000000|
  order:3 ChildProcId=12425|12469|
  order:4 ChildProcSCpuUsage=0.000000|0.000000|
  order:5 ChildProcUCpuUsage=0.000000|0.000000|
  order:6 ProcAppName=com.huawei.hmos.browser
  order:7 ProcCpuLoad=0.000000
  order:8 ProcCpuUsage=6.944444
  order:9 ProcId=12083
  order:10 ProcSCpuUsage=0.000000
  order:11 ProcUCpuUsage=6.944444
  order:12 TotalcpuUsage=14.285714
  order:13 TotalcpuidleUsage=85.714286
  order:14 TotalcpuioWaitUsage=0.000000
  order:15 TotalcpuirqUsage=0.000000
  order:16 TotalcpuniceUsage=0.000000
  order:17 TotalcpusoftIrqUsage=0.000000
  order:18 TotalcpusystemUsage=0.000000
  order:19 TotalcpuuserUsage=14.285714
  order:20 arktsHeapPss=132573
  order:21 capture=data/local/tmp/capture/screenCap_1773045247267.png
  order:22 childArktsHeapPss=12425:|12469:|
  order:23 childGpuPss=12425:0|12469:0|
  order:24 childGraphicPss=12425:0|12469:0|
  ...
  order:37 cluster0=46.000000
  order:38 cpu0Frequency=1400000
  order:39 cpu0Usage=0.000000
  order:40 cpu0_curFrequency=1400000
  order:41 cpu0idleUsage=100.000000
  order:42 cpu0ioWaitUsage=0.000000
  order:43 cpu0irqUsage=0.000000
  order:44 cpu0niceUsage=0.000000
  order:45 cpu0softIrqUsage=0.000000
  order:46 cpu0systemUsage=0.000000
  order:47 cpu0userUsage=0.000000
  ...
  order:149 currentNow=-755
  order:150 ddrFrequency=1531000000
  order:151 fps=60
  order:152 fpsJitters=16618229;;16526562;;16595834;;16633854;;16563542;;16642708;;16564062;;16550000;;16663021;;16540104;;16628125;;16559896;;16603646;;16588542;;16576041;;16571355;;16600520;;16585417;;16961979;;16505209;;16348437;;16601563;;16576041;;16580209;;16566145;;16660417;;16613542;;16503125;;16586458;;16606250;;16615625;;16566146;;16596354;;16619792;;16599479;;16647396;;16535416;;16575000;;16591146;;16566667;;16588541;;16597396;;16570313;;16647916;;16537500;;16583334;;16609896;;16586979;;16644271;;16680208;;16492187;;16577084;;16610416;;16587500;;16571875;;16614063;;16565104;;16601563;;16609375
  order:153 gpu=46.000000
  order:154 gpuFrequency=279000000
  order:155 gpuLoad=0.000000
  order:156 gpuPss=39398
  order:157 graphicPss=140368
  order:158 heapAlloc=162638
  order:159 heapFree=2725
  order:160 heapSize=169080
  order:161 memAvailable=5258240
  order:162 memFree=1507648
  order:163 memTotal=11689852
  order:164 nativeHeapPss=134094
  order:165 networkDown=0
  order:166 networkUp=0
  order:167 npu_thermal=45.000000
  order:168 privateClean=403764
  order:169 privateDirty=193434
  order:170 pss=626348
  order:171 refreshrate=60
  order:172 sharedClean=158860
  order:173 sharedDirty=43800
  order:174 shell_back=39.731000
  order:175 shell_frame=38.731000
  order:176 shell_front=38.231000
  order:177 soc_thermal=49.492000
  order:178 stackPss=2588
  order:179 swap=0
  order:180 swapPss=0
  order:181 system_h=40.529000
  order:182 threadsNum=12083:124|12425:26|12469:12|
  order:183 tids=12083:13102 12761 12597 12596 12584 12583 12553 12551 12529 12528 12527 12526 12524 12523 12521 12489 12486 12485 12467 12464 12457 12455 12454 12453 12450 12449 12448 12410 12407 12406 12405 12404 12403 12399 12397 12358 12354 12353 12352 12351 12349 12348 12347 12346 12345 12344 12343 12342 12340 12339 12336 12335 12334 12333 12332 12331 12330 12327 12326 12325 12324 12323 12322 12321 12320 12319 12318 12317 12316 12315 12312 12310 12309 12308 12307 12305 12304 12303 12302 12301 12300 12298 12283 12281 12280 12279 12278 12277 12270 12269 12268 12267 12266 12265 12253 12244 12242 12241 12240 12239 12238 12237 12225 12214 12213 12197 12196 12195 12194 12193 12192 12191 12190 12189 12188 12187 12186 12185 12184 12183 12182 12181 12180 12083|12425:13124 12929 12638 12637 12636 12614 12606 12605 12604 12602 12601 12581 12580 12579 12487 12484 12483 12474 12473 12472 12471 12470 12468 12465 12462 12425|12469:13125 12506 12505 12503 12502 12501 12499 12498 12493 12492 12491 12469|
  order:184 timestamp=1773045247230
  order:185 voltageNow=3768445

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需要进入被测应用内。
* 全量采集示例3，设置进程ID并采集指定应用信息，包括cpu、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图。

  ```shell
  $ SP_daemon -N 10 -PID 48875 -c -g -t -p -f -r -d -net -snapshot -threads

  order:0 Battery=37.000000
  order:1 ChildProcCpuLoad=NA
  order:2 ChildProcCpuUsage=NA
  order:3 ChildProcId=NA
  order:4 ChildProcSCpuUsage=NA
  order:5 ChildProcUCpuUsage=NA
  order:6 ProcAppName=com.kiloo.subwaysurf.huaweihm
  order:7 ProcCpuLoad=3.352013
  order:8 ProcCpuUsage=8.139535
  order:9 ProcId=15619
  order:10 ProcSCpuUsage=3.682171
  order:11 ProcUCpuUsage=4.457364
  order:12 TotalcpuUsage=98.305085
  order:13 TotalcpuidleUsage=1.694915
  order:14 TotalcpuioWaitUsage=0.000000
  order:15 TotalcpuirqUsage=0.000000
  order:16 TotalcpuniceUsage=1.694915
  order:17 TotalcpusoftIrqUsage=0.000000
  order:18 TotalcpusystemUsage=52.542373
  order:19 TotalcpuuserUsage=44.067797
  order:20 arktsHeapPss=18604
  order:21 capture=data/local/tmp/capture/screenCap_1773045626809.png
  order:22 childCarktsHeapPss=NA
  order:23 childGpuPss=NA
  order:24 childGraphicPss=NA
  order:25 childHeapAlloc=NA
  order:26 childHeapFree=NA
  order:27 childHeapSize=NA
  order:28 childNativeHeapPss=NA
  order:29 childPrivateClean=NA
  order:30 childPrivateDirty=NA
  order:31 childPss=NA
  order:32 childSharedClean=NA
  order:33 childSharedDirty=NA
  order:34 childStackPss=NA
  order:35 childSwap=NA
  order:36 childSwapPss=NA
  order:37 cluster0=63.000000
  order:38 cpu0Frequency=1400000
  order:39 cpu0Usage=100.000000
  order:40 cpu0_curFrequency=1400000
  order:41 cpu0idleUsage=0.000000
  order:42 cpu0ioWaitUsage=0.000000
  order:43 cpu0irqUsage=0.000000
  order:44 cpu0niceUsage=0.000000
  order:45 cpu0softIrqUsage=0.000000
  order:46 cpu0systemUsage=40.000000
  order:47 cpu0userUsage=60.000000
  ...
  order:149 currentNow=-1324
  order:150 ddrFrequency=2746000000
  order:151 fps=85
  order:152 fpsJitters=10994792;;11118750;;11017187;;11029167;;11077604;;11044792;;11058854;;11073437;;11077084;;11017708;;11090104;;11103646;;10980729;;11070313;;11119791;;10991667;;11056250;;11114583;;11014063;;11054167;;22150000;;22103645;;11077605;;11064583;;11044271;;11112500;;11059896;;11020312;;11050521;;11135937;;10994792;;11055729;;11057813;;11124479;;10988542;;11103125;;11046354;;11081250;;11111979;;10960937;;11043230;;11082812;;11061458;;11044271;;11060938;;11117708;;11036458;;11050521;;11063542;;11043750;;11072396;;11058333;;11062500;;11069271;;11059896;;11110937;;11021354;;11037500;;11068750;;11093229;;11010417;;11055208;;11071355;;11072395;;22174480;;11014583;;11160937;;10972396;;11053125;;11031250;;11095313;;22112500;;11116146;;10995312;;11091146;;11029687;;11057292;;11060938;;22123958;;11103646;;11038541;;11036459;;11072916;;11125521
  order:153 gpu=56.000000
  order:154 gpuFrequency=279000000
  order:155 gpuLoad=0.000000
  order:156 gpuPss=56476
  order:157 graphicPss=64380
  order:158 heapAlloc=77575
  order:159 heapFree=450
  order:160 heapSize=81500
  order:161 memAvailable=4191232
  order:162 memFree=162596
  order:163 memTotal=11689852
  order:164 nativeHeapPss=49129
  order:165 networkDown=0
  order:166 networkUp=0
  order:167 npu_thermal=55.000000
  order:168 privateClean=468356
  order:169 privateDirty=129248
  order:170 pss=605268
  order:171 refreshrate=90
  order:172 sharedClean=117476
  order:173 sharedDirty=35940
  order:174 shell_back=40.404000
  order:175 shell_frame=39.404000
  order:176 shell_front=38.904000
  order:177 soc_thermal=66.496000
  order:178 stackPss=940
  order:179 swap=0
  order:180 swapPss=0
  order:181 system_h=45.687000
  order:182 threadsNum=15619:73
  order:183 tids=15619:16167 16140 16138 16128 16127 16126 16118 16117 16115 16114 16113 16106 15996 15993 15983 15969 15966 15957 15954 15953 15952 15951 15950 15945 15927 15926 15925 15924 15923 15922 15921 15920 15919 15918 15917 15916 15915 15914 15913 15912 15911 15910 15909 15908 15907 15906 15880 15841 15839 15815 15814 15813 15812 15799 15791 15789 15765 15755 15753 15752 15751 15749 15748 15747 15746 15745 15744 15743 15742 15740 15739 15738 15619
  order:184 timestamp=1773045626635
  order:185 voltageNow=3719892

  command exec finished!
  $
  ```

  **说明** 

  使用该命令采集时需要进入被测应用内。

**2. 启停采集**

先执行start开始采集命令，然后操作设备或应用，最后执行stop结束采集命令。

| 启停采集命令参数 | 必选 | 说明 |
| --- | --- | --- |
| -start | 是 | 开始采集，该命令参数后可添加基础采集命令，一秒采集一次。 |
| -stop | 是 | 结束采集，执行后会生成采集报告。 |
| -print | 否 | 一秒打印一次启停采集信息。 |

* 启停采集整机CPU大中小核频率、各核使用率。

  ```shell
  # 开始采集
  $ SP_daemon -start -c
  SP_daemon Collection begins

  command exec finished!
  $

  # 结束采集
  $ SP_daemon -stop
  SP_daemon Collection ended
  Output Path: data/local/tmp/smartperf/1/t_index_info.csv

  command exec finished!
  $
  ```
* 启停采集并打印整机CPU大中小核频率、各核使用率。

  ```shell
  # 开始采集（打印启停采集信息）
  $ SP_daemon -start -c -print
  SP_daemon Collection begins

  order:0 TotalcpuUsage=20.860927
  order:1 TotalcpuidleUsage=79.139073
  order:2 TotalcpuioWaitUsage=0.000000
  order:3 TotalcpuirqUsage=0.082781
  order:4 TotalcpuniceUsage=0.000000
  order:5 TotalcpusoftIrqUsage=0.000000
  order:6 TotalcpusystemUsage=8.029801
  order:7 TotalcpuuserUsage=12.748344
  order:8 cpu0Frequency=1430000
  order:9 cpu0Usage=44.554455
  order:10 cpu0idleUsage=55.445545
  order:11 cpu0ioWaitUsage=0.000000
  order:12 cpu0irqUsage=0.000000
  order:13 cpu0niceUsage=0.000000
  order:14 cpu0softIrqUsage=0.000000
  order:15 cpu0systemUsage=17.821782
  order:16 cpu0userUsage=26.732673
  order:17 cpu10Frequency=1239000
  order:18 cpu10Usage=0.000000
  order:19 cpu10idleUsage=100.000000
  order:20 cpu10ioWaitUsage=0.000000
  order:21 cpu10irqUsage=0.000000
  order:22 cpu10niceUsage=0.000000
  order:23 cpu10softIrqUsage=0.000000
  order:24 cpu10systemUsage=0.000000
  order:25 cpu10userUsage=0.000000
  order:26 cpu11Frequency=1239000
  order:27 cpu11Usage=0.000000
  order:28 cpu11idleUsage=100.000000
  order:29 cpu11ioWaitUsage=0.000000
  order:30 cpu11irqUsage=0.000000
  order:31 cpu11niceUsage=0.000000
  order:32 cpu11softIrqUsage=0.000000
  order:33 cpu11systemUsage=0.000000
  order:34 cpu11userUsage=0.000000
  ...

  command exec finished!
  $
      
  # 结束采集（在启停打印时，需重新开启命令框执行此命令）
  $ SP_daemon -stop
  SP_daemon Collection ended
  Output Path: data/local/tmp/smartperf/1/t_index_info.csv

  command exec finished!
  $
  ```

  **说明** 

  + 开始采集示例1（采整机cpu、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图）：SP\_daemon -start -c -g -t -p -r -d -net -snapshot。
  + 开始采集示例2（采整机和进程cpu负载、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图、线程数、文件描述符）：SP\_daemon -start -PKG ohos.samples.ecg -c -g -t -p -f -r -d -net -snapshot -threads。
  + 开始采集示例3（采整机和进程cpu负载、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图、线程数、文件描述符）：SP\_daemon -start -PID 18847 -c -g -t -p -f -r -d -net -snapshot -threads。
  + 开始采集示例4（采整机cpu、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图、线程数、文件描述符并且打印采集信息）：SP\_daemon -start -c -g -t -p -r -d -net -snapshot -threads -print。
  + 开始采集示例5（采整机和进程cpu负载、gpu、温度、功耗、fps、内存信息、DDR信息、网络速率、屏幕截图、线程数、文件描述符并且打印采集信息）：SP\_daemon -start -PID 18847 -c -g -t -p -f -r -d -net -snapshot -threads -print。
  + 开始采集需和结束采集结合使用，先执行开始采集命令，执行完后操作设备中的应用，最后执行结束采集命令。
  + 在执行启停打印采集时，执行停止命令需重新打开命令框执行停止命令。
  + 结束采集，文件输出路径为：data/local/tmp/smartperf/1/t\_index\_info.csv。
  + 导出示例：hdc file recv data/local/tmp/smartperf/1/t\_index\_info.csv D:\。

**3. 查看csv采集结果**

若采集结果保存在csv文件中，可以按照如下操作导出和查看结果内容。

* 通过-N开启采集，采集结果默认输出路径：/data/local/tmp/data.csv。
* 查看文件位置。

  ```shell
  C:\Users\issusser>hdc shell
  $ cd data/local/tmp
  $ ls
  data.csv
  $
  ```
* 导出文件到指定路径。

  ```shell
  C:\Users\issusser>hdc file recv data/local/tmp/data.csv D:\
  [I][2023-11-08 16:16:41] HdcFile::TransferSummary success
  FileTransfer finish, Size:429, File count = 1, time:6ms rate:71.50kB/s

  C:\Users\issusser>
  ```
* 打开data.csv查看数据。

  在自定义导出路径里找到data.csv文件打开查看采集数据表，data.csv数据名描述如下：

  | 数据项 | 说明 | 备注 |
  | --- | --- | --- |
  | cpuFrequency | CPU大中小核频率。 | 单位：Hz |
  | cpuUasge | CPU各核使用率。 | % |
  | cpuidleUsage | CPU空闲态使用率。 | % |
  | cpuioWaitUsage | 等待I/O的使用率。 | % |
  | cpuirqUsage | 硬中断的使用率。 | % |
  | cpuniceUsage | 低优先级用户态使用率。 | % |
  | cpusoftIrqUsage | 软中断的使用率。 | % |
  | cpusystemUsage | 系统/内核态使用率。 | % |
  | cpuuserUsage | 用户态使用率。 | % |
  | ProcId | 进程id。 | - |
  | ProcAppName | app包名。 | - |
  | ProcCpuLoad | 进程CPU负载占比。 | % |
  | ProcCpuUsage | 进程CPU使用率。 | % |
  | ProcUCpuUsage | 进程用户态CPU使用率。 | % |
  | ProcSCpuUsage | 进程内核态CPU使用率。 | % |
  | TotalcpuUsage | CPU总使用率。 | % |
  | TotalcpuidleUsage | CPU总空闲态使用率。 | % |
  | TotalcpuioWaitUsage | CPU总等待I/O使用率。 | % |
  | TotalcpuirqUsage | CPU总硬中断使用率。 | % |
  | TotalcpuniceUsage | CPU总低优先级用户态使用率。 | % |
  | TotalcpusoftIrqUsage | CPU总软中断使用率。 | % |
  | TotalcpusystemUsage | CPU总系统/内核态使用率。 | % |
  | TotalcpuuserUsage | CPU总用户态使用率。 | % |
  | gpuFrequency | 整机GPU的频率。 | % |
  | gpuLoad | 整机GPU的负载占比。 | % |
  | currentNow | 当前读到的电流值。 | 单位：mA |
  | voltageNow | 当前读到的电压值。 | 单位：μV |
  | fps | 每秒帧数。 | 单位：fps |
  | fpsJitters | 每一帧绘制间隔。 | 单位：ns |
  | refreshrate | 屏幕刷新率。 | 单位：Hz |
  | networkDown | 下行速率。 | 单位：byte/s |
  | networkUp | 上行速率。 | 单位：byte/s |
  | ddrFrequency | DDR频率。 | 单位：Hz |
  | shell\_front | 前壳温度。 | 单位：°C |
  | shell\_frame | 边框温度。 | 单位：°C |
  | shell\_back | 后壳温度。 | 单位：°C |
  | soc\_thermal | 系统芯片温度。 | 单位：°C |
  | system\_h | 系统温度。 | 单位：°C |
  | Battery | 电池温度。 | 单位：°C |
  | cluster0 | CPU温度。 | 单位：°C |
  | gpu | GPU温度。 | 单位：°C |
  | npu\_thermal | NPU温度。 | 单位：°C |
  | memAvailable | 整机可用内存。 | 单位：KB |
  | memFree | 整机空闲内存。 | 单位：KB |
  | memTotal | 整机总内存。 | 单位：KB |
  | pss | 进程实际使用内存。 | 单位：KB |
  | Childpss | 子进程实际使用内存。 | 单位：KB |
  | sharedClean | 进程共享的未改写页面。 | 单位：KB |
  | ChildsharedClean | 子进程共享的未改写页面。 | 单位：KB |
  | sharedDirty | 进程共享的已改写页面。 | 单位：KB |
  | ChildsharedDirty | 子进程共享的已改写页面。 | 单位：KB |
  | privateClean | 进程私有的未改写页面。 | 单位：KB |
  | ChildprivateClean | 子进程私有的未改写页面。 | 单位：KB |
  | privateDirty | 进程私有的已改写页面。 | 单位：KB |
  | ChildprivateDirty | 子进程私有的已改写页面。 | 单位：KB |
  | swapTotal | 进程总的交换内存。 | 单位：KB |
  | ChildswapTotal | 子进程总的交换内存。 | 单位：KB |
  | swapPss | 进程交换的pss内存。 | 单位：KB |
  | ChildswapPss | 子进程交换的pss内存。 | 单位：KB |
  | HeapSize | 进程堆内存大小。 | 单位：KB |
  | ChildHeapSize | 子进程堆内存大小。 | 单位：KB |
  | HeapAlloc | 进程可分配的堆内存大小。 | 单位：KB |
  | ChildHeapAlloc | 子进程可分配的堆内存大小。 | 单位：KB |
  | HeapFree | 进程剩余的堆内存大小。 | 单位：KB |
  | ChildHeapFree | 子进程剩余的堆内存大小。 | 单位：KB |
  | gpuPss | 进程使用的gpu内存大小。 | 单位：KB |
  | ChildgpuPss | 子进程使用的gpu内存大小。 | 单位：KB |
  | graphicPss | 进程使用的图形内存大小。 | 单位：KB |
  | ChildgraphicPss | 子进程使用的图形内存大小。 | 单位：KB |
  | arktsHeapPss | 进程使用的arkts内存大小。 | 单位：KB |
  | ChildarktsHeapPss | 子进程使用的arkts内存大小。 | 单位：KB |
  | nativeHeapPss | 进程使用的native内存大小。 | 单位：KB |
  | ChildnativeHeapPss | 子进程使用的native内存大小。 | 单位：KB |
  | stackPss | 进程使用的栈内存大小。 | 单位：KB |
  | ChildstackPss | 子进程使用的栈内存大小。 | 单位：KB |
  | timeStamp | 当前时间戳。 | 对应采集时间 |

### 场景化采集

除基本采集外，还支持采集响应和完成时延等内容。场景化采集结果不写入data.csv，采集结果直接在命令框显示。

场景化采集是对应用页面滑动、切换场景下的性能测试，针对不同操作场景执行相对应的采集命令，获取应用性能数据，包括页面的滑动帧率、页面切换或滑动的卡顿率、响应时延、完成时延以及最大连续丢帧，对采集数据进行输出打印，以便用户分析并优化应用性能。

| 场景化采集命令参数 | 必选 | 说明 |
| --- | --- | --- |
| -editor | 是 | 采集类型为场景化。 |
| timeDelay | 否 | 页面切换（支持ArKUI子系统的router、navigation、tabs、swiper控件内的页面切换/内容切换）。 |
| slideList | 否 | 页面滑动（支持ArKUI子系统的List、grid、scroll、waterflow等组件内的页面滑动）。 |

| 场景化采集数据项 | 说明 | 备注 |
| --- | --- | --- |
| ResponseTime | 页面切换、页面滑动的响应时延。 | 单位：ms |
| CompleteTime | 页面切换的完成时延。 | 单位：ms |
| HitchTimeRate | 页面切换、页面滑动的卡顿率。 | 单位：ms/s |
| MAX\_RENDER\_SEQ\_MISSED\_FRAMES | 页面切换、页面滑动的最大连续丢帧。 | NA |
| FPS | 页面滑动帧率。 | 单位：fps |

**页面切换**

步骤1：打开被测应用，进入需要测试的页面。

步骤2：在cmd命令行中输入命令并回车：SP\_daemon -editor timeDelay。

步骤3：等待1-2秒钟，然后手动点击页面内的按钮，跳转到下一个页面，等待测试完成。

测试完成后，打印结果示例如下：

```shell
$ SP_daemon -editor timeDelay
ResponseTime:41ms
CompleteTime:593ms
HitchTimeRate:68.65ms/s
MAX_RENDER_SEQ_MISSED_FRAMES:3
$
```

**说明** 

* 时延计算受系统打点上报限制，开始时间为点击事件上报时间点，响应时延结束时间点为点击后系统响应首帧的上屏时间点，完成时延是切换后页面的首帧上屏时间点，与端到端用户感知时延存在差异。
* 页面切换卡顿率：目前只支持ArKUI子系统的router、navigation、tabs、swiper控件内的页面切换/内容切换。计算公式：页面切换卡顿率=页面切换动效时间内每一帧的累计丢帧时间（ms）/ 动效时长（s）。
* 最大连续丢帧受系统打点上报限制，与端到端用户感知时延存在差异。
* 页面切换同时会抓取trace，文件路径：data/local/tmp/sp\_trace\_delay.ftrace，通过hdc file recv的方式导出查看trace。

**页面滑动**

步骤1：打开被测应用，进入需要测试的页面。

步骤2：在cmd命令行中输入命令并回车：SP\_daemon -editor slideList。

步骤3：等待1-2秒钟，然后触摸屏幕滑动一次页面，等待测试完成。

测试完成后，打印结果示例如下：

```shell
$ SP_daemon -editor slideList
FPS:107.181fps
ResponseTime:20ms
HitchTimeRate:1.49ms/s
MAX_RENDER_SEQ_MISSED_FRAMES:0
$
```

**说明** 

* 时延计算受系统打点上报限制，开始时间为点击事件上报时间点，响应时延结束时间点为滑动后系统响应首帧的上屏时间点，与端到端用户感知时延存在差异，需要注意的是，滑动场景时延计算不支持Web组件。
* 页面滑动帧率：指的是在页面滑动时，屏幕能够刷新的频率。需要注意的是，该场景目前只支持滑动一次页面。
* 页面滑动卡顿率：目前只支持ArKUI子系统的List、grid、scroll、waterflow滚动组件。计算公式：页面滑动卡顿率=页面滑动动效时间内每一帧的累计丢帧时间（ms）/ 动效时长（s）。
* 最大连续丢帧受系统打点上报限制，与端到端用户感知时延存在差异。
* 页面滑动同时会抓取trace，文件路径：data/local/tmp/sp\_trace\_fps.ftrace，通过hdc file recv的方式导出查看trace。

### 其他采集

当前设备电量采集结果可写入csv文件，其它命令需单独采集，采集结果不写入data.csv，仅在命令框显示。

| 命令参数 | 必选 | 说明 |
| --- | --- | --- |
| -screen | 否 | 采集屏幕分辨率和刷新率。 |
| -deviceinfo | 否 | 获取设备信息。 |
| -server | 否 | 启停采集用来拉起daemon进程。 |
| -clear | 否 | 清除所有SP\_daemon进程。 |
| -recordcapacity | 否 | 获取当前设备电量。 |
| -profilerfps | 否 | 采集当前界面fps。 |

* 获取屏幕分辨率。

  ```shell
  $ SP_daemon -screen
  activeMode: 1260x2720, refreshrate=60

  command exec finished!
  $
  ```

  **说明** 

  activeMode表示当前屏幕分辨率，refreshrate表示屏幕刷新率。
* 获取设备信息。

  ```shell
  $ SP_daemon -deviceinfo
    abilist: default
    activeMode: 1260x2720
    board: default
    brand: default
    cpu_c1_cluster: 0 1 2 3
    cpu_c1_max: 1530000
    cpu_c1_min: 418000
    cpu_c2_cluster: 4 5 6 7 8 9
    cpu_c2_max: 2150000
    cpu_c2_min: 418000
    cpu_c3_cluster: 10 11
    cpu_c3_max: 2620000
    cpu_c3_min: 1239000
    cpu_cluster_name: policy0 policy1 policy2
    daemonPerfVersion: 1.0.5
    deviceTypeName: default
    fullname: HarmonyOS-5.1.0.50
    gpu_max_freq: 750000000
    gpu_min_freq: 279000000
    model: ohos
    name: default
    sn: default
    version: default

    command exec finished!
    $
  ```
* 启动一个进程来监听start和stop命令的socket消息

  ```shell
  $ SP_daemon -server
  $
  $ pidof SP_daemon
  7024
  $
  ```

  **说明** 

  可执行pidof SP\_daemon查看进程id。
* 清除SP\_daemon进程ID

  ```shell
  $ pidof SP_daemon
  9923 11402
  $ SP_daemon -clear
  $
  $ pidof SP_daemon
  $
  ```

  **说明** 

  可执行pidof SP\_daemon查看进程id。
* 采集当前界面fps。

  ```shell
  $ SP_daemon -profilerfps 10
  set num:10 success
  fps:31|1739353731123
  fps:30|1739353732123
  fps:58|1739353733123
  fps:24|1739353734123
  fps:19|1739353735123
  fps:19|1739353736123
  fps:55|1739353737123
  fps:26|1739353738123
  fps:21|1739353739123
  fps:19|1739353740123
  SP_daemon exec finished!
  $
  ```

  **说明** 

  该条命令里的10表示采集的次数（一秒采集一次），可以设置为其他正整数。
* 采集当前界面fps（分段采集）。

  ```shell
  $ SP_daemon -profilerfps 100 -sections 10
  set num:100 success
  fps:33|1739353780123
  sectionsFps:15|1739353780123
  sectionsFps:60|1739353780223
  sectionsFps:15|1739353780323
  sectionsFps:60|1739353780423
  sectionsFps:15|1739353780523
  sectionsFps:15|1739353780623
  sectionsFps:24|1739353780723
  sectionsFps:60|1739353780823
  sectionsFps:60|1739353780923
  sectionsFps:60|1739353781023
  fps:49|1739353781123
  sectionsFps:60|1739353781123
  sectionsFps:60|1739353781223
  sectionsFps:60|1739353781323
  sectionsFps:60|1739353781423
  sectionsFps:60|1739353781523
  sectionsFps:60|1739353781623
  sectionsFps:15|1739353798723
  sectionsFps:15|1739353798823
  sectionsFps:10|1739353798923
  sectionsFps:60|1739353799023
  fps:20|1739353799123
  sectionsFps:60|1739353799123
  ...

  SP_daemon exec finished!
  ```

  **说明** 

  该条命令里的100表示采集的次数（一秒采集一次），可以设置为其他正整数，10表示分段：目前支持设置 1-10（正整数）段采集。
* 获取电池电量。

  ```shell
  $ SP_daemon -recordcapacity
  recordTime: 1726903063
  recordPower: 5502
  $
  ```

  **说明** 

  + recordTime表示时间戳，recordPower表示当前时刻的电量。
  + 该命令需单独采集，采集结果写入/data/local/tmp/powerLeftRecord.csv，可以使用hdc file recv导出到本地。具体请参考查看csv采集结果。
