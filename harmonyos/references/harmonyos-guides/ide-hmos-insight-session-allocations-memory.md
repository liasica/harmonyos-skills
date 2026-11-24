---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:49+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:a4e2f5f878c58c657faa80898bdc29f80b29f3b8ec13c7c7b1ce84cf416f166e
---

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考模块级[build-profile.json5文件](ide-hmos-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请录制模板前按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/AXGq5W3ySYKklGziVTSK_Q/zh-cn_image_0000002792000972.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=711C89338C47DF4BA41FF5B2FC11E91D39F8F55219EB1CB07A4152B5AEC15C39)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在[会话区](ide-hmos-profiler-session.md)点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/xT9quxetTXy6QYkzwfmTGg/zh-cn_image_0000002820720941.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=169BDF56430BD3F55D5D5342DAB4F1533D68698C697E695D58BBAC29A6CA8E3B)图标，导入历史数据。在录制前单击录制按钮旁![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/3rKAeAEESMKtBMaN6c7J8Q/zh-cn_image_0000002820680935.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=046DCAE21782A1915E6E55C977BA7811FEB002FC8D68E7FFC0D08102D653B4DA)按钮，点击**录制设置**指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/miUWtFmoRTS9oitQECKgZQ/zh-cn_image_0000002791841006.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=FBA08AC125A24B693F49FA79F294EC1F05F10E06FEA8219C351D76B61A8BED5A "点击放大")

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vqbsSMo8TNiyGtcxbMKaaA/zh-cn_image_0000002791841010.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AF5D46A88B676A9471238C3EE8B287F4EE280E9D7C05FDD13C146A91E964DE1)PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/SN3jYuJcREaRrBffLRj1uA/zh-cn_image_0000002791841008.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E1D00BE30A20FC5EF78CE6AF083B2533E8F191265547A4EDD4A03D050D78C08)RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/lQPDU9ICSWmOra1QKeLpwA/zh-cn_image_0000002820680937.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=67678AF8C70C71EA5D4255A46AC8192AC48D18E560EDC5B926380A57190E5C89)USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/hobZiYN_T7GzMhvCPRPnLg/zh-cn_image_0000002820720949.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=26B6FC9A3F865DD79E780A2F73178E16658B4C1ECAB6E2A7760E949CFCA5AE5D "点击放大")

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/aPW4IVJxSJG2_zqd1Qpu-Q/zh-cn_image_0000002820720951.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=15FDCB8B3FD29456ED691FEC394F43CF9FADD244110FFB9A1185DE344C49A05C "点击放大")图标并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/vXR5vm86R12bLdZyThnu2w/zh-cn_image_0000002792000982.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=989BF46A1830907852D4129012A79A87DEB7536AA8AD5B03E316D533FD627995 "点击放大")

     | 子泳道 | 说明 |
     | --- | --- |
     | ArkTS Heap | ArkTS堆的内存占用。 |
     | Native Heap | Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。 |
     | GL | 包括应用和RS，应用为纹理内存，RS为纹理和图形渲染内存。 |
     | Graph | 该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator\_host申请的dma buffer。 |
     | Guard | 保护段所占内存。 |
     | AnonPage Other | 其他所有匿名页所占内存（非heap、anon:native\_heap、anon:ArkTS heap开头的匿名页）。 |
     | FilePage Other | 其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用。 |
     | Dev | 进程加载的以/dev开头的文件所占内存。 |
     | Stack | 栈内存。 |
     | .hap | 进程加载的.hap文件所占内存。 |
     | .so | 进程加载的.so动态库所占内存。 |
     | .ttf | 进程加载的.ttf字体文件所占内存。 |
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     点击录制按钮旁![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Ox5udEHnSzGWCS8Q5xiPvA/zh-cn_image_0000002820680943.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=836162E2B9D4428FFF612F6C1B42153BC17FFAAD4AA4748DF0C7EE47B12153E2)按钮，选择**录制设置**，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈深度、回栈模式。

     | **设置项名称** | **说明** |
     | --- | --- |
     | 统计模式 | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。当前版本尚不支持关闭。 |
     | 采样间隔(秒) | 统计时间间隔。 仅在统计模式下需要设置， 可设置范围为1s~3600s，默认为10s。 |
     | 过滤大小(字节) | 最小跟踪内存。 该参数表示最小抓取的内存大小。 可配置范围为0-65535Bytes, 默认为1024Bytes。 |
     | 回栈深度 | Native回栈深度。 可配置范围为5-100， 默认10层。 |
     | 回栈模式 | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。  FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |

     **说明** 

     + 设置的最小跟踪内存数值越小、回栈深度越大，对应用造成的影响就越大，可能会导致DevEco Profiler卡顿。请根据应用实际的调测情况进行合理设置。
     + 统计模式用于不关注单次分配、关注应用较长时间的内存变化情况的场景，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长的目的。设置的采样间隔为近似值，即尽可能地在接近这个时间内做统计汇总，存在一定的偏差，偏差不超过1s，这个偏差不会对内存分配的正确性产生影响。
     + 使用统计模式时，录制的结束时间需要是采样间隔即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/953YGTJSRFeZXmRjmYyCLA/zh-cn_image_0000002820680939.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=95F7445E961D18D9DC8EEE35AE66C74DC99E010F3E6799A454DA594A8E9F19A1 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，Details区域中显示此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/zZdgfwRjT9ePES8gvqPeeQ/zh-cn_image_0000002820680941.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEEF77B167A04F0B2E9F06E6F9C12F87AC09FE5E4F1218C63C5B10B07C4E62E4 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/3PJHwsAtSFmbyOEseFpEKg/zh-cn_image_0000002820720939.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0ECD664A8D93B5F1FCD77F7134000030A5205901F07C1E252264DD8B1A5C413 "点击放大")
   * Native Allocation泳道：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，**More**区域将显示经过该栈帧的分配内存最大的调用栈。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/kLtGMEQ_Rm6KVXXiknFr9Q/zh-cn_image_0000002791841000.png?HW-CC-KV=V1&HW-CC-Date=20261124T044249Z&HW-CC-Expire=31536000000&HW-CC-Sign=2200122C5FDC65C563B9538440ED718E093041A69859BC771C67FBEB1A6CCE79 "点击放大")
