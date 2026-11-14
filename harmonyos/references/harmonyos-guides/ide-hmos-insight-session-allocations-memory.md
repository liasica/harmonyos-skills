---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础内存分析：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:20+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:45c89e786aa1c4010a39b071d8370b334e21ee48b825c383edef0441619e589d
---

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考模块级[build-profile.json5文件](ide-hmos-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请录制模板前按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/GDWNvST2Sl639q-kgx4_zg/zh-cn_image_0000002781311214.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=D29A89558A4439C8C4F19F2B2BC50E07D01BED8EA96CD9DDC17D33358BE05D92)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在[会话区](ide-hmos-profiler-session.md)点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/j6dT51-0THycTCVvxlEuqg/zh-cn_image_0000002781311212.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE104864B8A7820114DE7909176B657C5410448FB84D81DB95F87EC5B76C59AB)图标，导入历史数据。在录制前单击录制按钮旁![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/0lv0oW4GR9u_ZqPLtnraDA/zh-cn_image_0000002781311208.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9F9DF901BFA1420D38AB8DC2241AC456CE121EE34D84A1BC233B909F945CF86)按钮，点击**录制设置**指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Ao1BJDtCSuu2jOaSSmE87g/zh-cn_image_0000002810630703.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=98D484EAEE2817CCE99615E5F4FF47154ED5A3BAC4957F5275603CC52523FED3 "点击放大")

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/Jy3VqfiOSQa3o4zz6CVk0A/zh-cn_image_0000002810630695.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=202F49333DDE3791C282464DC1063DB44C15300848108349AA6DC746AE9FD29A)PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/oI1omp93TrSBfGsPgOEl0g/zh-cn_image_0000002810630697.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=468C1F14D92FAAC3AE2CF03B07C131D734BB95043CB6E8D8540D81972C03B911)RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/IgoLl2fpQOqwDb8bYBohgw/zh-cn_image_0000002810750803.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A9986F3BAD90EE0C64CFF93F6F616C20448C3FE7F834C1625AB9DBD4D319334)USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/lnY4uvIMQ3O55Ock3p835w/zh-cn_image_0000002781471146.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=63770088CD32EA4A19A20A36F7074517BE4AFEDF4602F5A5F68E65CCF3FE2BC6 "点击放大")

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/wep8Dv-JT_afo0VlbibS8A/zh-cn_image_0000002781471140.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C11281315B40578FE497AA95D254FF22BE5406935E1AF82D95A146941E220BB "点击放大")图标并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/UGk4g-eLRuqcH2S9PSaXRw/zh-cn_image_0000002810630691.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=C72473B80910A1630372117B00BD2E48EDDEDD1BD51561D5182D3E43DD7FAA5E "点击放大")

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

     点击录制按钮旁![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/67M2zYraTYSmR00tO-NgMQ/zh-cn_image_0000002781471144.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=43E108396A2049F9C3B43B9D4F80508C1F87393EC967F9B55CAE1FE1B71BB06F)按钮，选择**录制设置**，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈深度、回栈模式。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/zR9jbi7oTrWrTCZqDPrUcw/zh-cn_image_0000002781311210.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4B7EF1573AF1E3C9D294195598644ACD5F99E1038FD2F5C1C558F83F1F07A07 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，Details区域中显示此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/qI-HTgbYRYO_PwCw40xiqQ/zh-cn_image_0000002781471142.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D214B3938851AFD73651FCF575A2CA69E3269BF40B1B2432C661862877EAE0E "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/HkgsCLmdRSm-5KlUbrscpw/zh-cn_image_0000002810750799.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCEDC93D5726FB719DF0961EF03E4D6B451DE7FDA2B57AAEFF37318D3E7D33D6 "点击放大")
   * Native Allocation泳道：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，**More**区域将显示经过该栈帧的分配内存最大的调用栈。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/q7f3MxwwTXC-Cy0xGMKfyQ/zh-cn_image_0000002810750801.png?HW-CC-KV=V1&HW-CC-Date=20261114T004730Z&HW-CC-Expire=31536000000&HW-CC-Sign=370281BDADF69DCFE764C3750CE8330F99256BD205525C3660C862AC30B215FE "点击放大")
