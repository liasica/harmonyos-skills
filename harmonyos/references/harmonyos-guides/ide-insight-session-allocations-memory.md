---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:44+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:8c10f4c514e84fc33cd37407a51cc111fad8ba735dc8fb37d93cc054780a83d9
---

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。Allocation分析任务支持录制Memory泳道、ArkTS Allocation泳道、All Heap & Anonymous VM等多个泳道。

从DevEco Studio 6.1.0 Beta1开始，Allocation分析任务新增支持录制All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道，不支持录制Native Allocation泳道。

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/3deQvFtrQNCI3NgXBouUhQ/zh-cn_image_0000002561753027.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=5F654DAA81871DFC60F33886588E3412B1808FAF9F03CB0E1C96CC60A15E62A1)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/ceqnruiQROeYosLYtKAcCw/zh-cn_image_0000002530913076.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=138A933A3FD98FD34C3869AF8AC637763F71BED204834FA8536B306DEE44AC70)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Zj6sUHYwTTCH6-QOPZSIGg/zh-cn_image_0000002561833007.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=6A4E18D48451EA05D8BDA270BBD5A19533D2B8F976F22A49ABF28B7EB96E0BFF "点击放大")

   说明

   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/KH1aFOHxQv2hd9hXIZQaiQ/zh-cn_image_0000002530913064.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=2E225F2CAEA930BEC4485A3E3CB788AA7F345CCE686C95E4DD9D2FD79353BE28)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/32J3_9-BQQmiFIldOPLpig/zh-cn_image_0000002530753086.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=85C7F5ADE3CDF4FB8DFFCA7DD9B204A896CE173738B85F8C139EBCA141C24AD9)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/th97dQhbSnGque102PSqRg/zh-cn_image_0000002530753068.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=70CB26DCC93B120B21F4D384B7658EE927E205DBA626AE098B375A94B1B4CD86 "点击放大")

     | 配置项 | 说明 |
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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/Ok5PQACTTz28F15pnzgbig/zh-cn_image_0000002561833003.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=D26BB23B6355E89D04C58511BFEAE9D34AEE288966D54A50E52910BEBE910757)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     说明

     由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：

     + ArkTS Snapshot泳道
     + All Heap & Anonymous VM泳道
     + All Heap泳道
     + All Anonymous VM泳道
     + System Resources泳道
     + Graphic Memory泳道
   * **ArkTS Snapshot泳道**：DevEco Studio 6.1.0 Release版本新增，用于抓取ArkTS堆内存快照，结束录制时会自动录制一次快照，默认不支持录制该泳道。如需录制，在录制前单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/d3S50It7Ql-m5j4QUE2O-Q/zh-cn_image_0000002530753092.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=01159B611ACC29D13D706BFB5DFCE187006EA0ABF5100D57262B0943E53ADEE9)按钮关闭统计模式（Statistics Mode）。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/u1Nm0Z11Q5652QYcrzZdsw/zh-cn_image_0000002530913056.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=4BDEADC8986F2871C1E5E322E4AD3E9B11D96BA406E87991FDB7783AB3455B8F "点击放大")
   * **All Heap & Anonymous VM泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/5ier-SfWRcKwh25YfFqzoQ/zh-cn_image_0000002561753003.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=FF153887D12252678A9C0D2E3A904240998B976C8E0A96F618BD854861E8DF6C)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/jFn73dHRTt2Sqlcu9igrRQ/zh-cn_image_0000002530913072.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=6F984B510D1E23069BF96139C87C87087CEC436224E214BB72FBCECAE39410AF "点击放大")

     | 子泳道 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | All Heap & Anonymous VM Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。  在DevEco Studio 6.1.0 Beta2之前版本，默认关闭。  从DevEco Studio 6.1.0 Beta2版本开始，默认开启。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Stack | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |
     | Record Data Range Options | DevEco Studio 6.1.0 Release版本新增。  用于设置采样数据范围，包含Malloc、Local Handle和Global Handle。Malloc记录malloc系列函数的内存分配；Local Handle用于管理JS对象生命周期的引用句柄（napi\_value）；Global Handle允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）；默认勾选Malloc。 |

     说明

     + 若勾选Local Handle，在应用生命周期内首次录制时会重启应用。若应用在生命周期内被强制终止后重启，再次录制时仍会重启应用。
     + 最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。
     + 最小跟踪内存设置的数值大小不影响Local Handle和Global Handle。
     + 统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。
   * **All Heap泳道**：显示Heap类型数据之和。展开主泳道，包括Native Heap、ArkTS Heap、JS Heap三条子泳道。其中Native Heap子泳道显示Malloc、ArkLocalHandle和ArkGlobalHandle内存分配，ArkTS Heap子泳道显示ArkTS对象内存分配，JS Heap子泳道显示JS对象内存分配。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/lHY_56TLTWaom1a_1y4NiA/zh-cn_image_0000002530753076.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=5B40CCF1433ED343D6B867551BB556F68DF309A3A8C5EA114172BAFB00DA9B72 "点击放大")
   * **All Anonymous VM泳道**：显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。VM:ION子泳道显示DMA内存分配数据，VM:ASHMem子泳道显示匿名共享内存，VM:.so子泳道显示.so文件内存消耗，VM:others子泳道显示除ION、ASHMem、**.**so外的mmap类型数据。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/BAfo1D4STjmuYRbQUrup7Q/zh-cn_image_0000002530753102.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=F6C2E95A3C534E8EFEC0B6D36EC04EA82A2FA115848C26BA592E1FFD43632D8E "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。File Descriptors子泳道显示进程的文件句柄使用情况，Threads子泳道显示进程的线程使用情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/IX2heXTjSBSdQuJzUIEpQA/zh-cn_image_0000002561753007.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=0F786D7D50C53D18C675D0FFA6AB6C8884EFAC38AE1419A8025100BCFBFEF284 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/-hRvr9pWRtaFgGcZV-p9dg/zh-cn_image_0000002561753001.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=2BF63964C05BAC373BA9D8ECD48CA78A83C54CB925F960D27F538261D33591B5)图标，勾选Graphic Memory泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Qfz24EjDRo22FgHAn_VG4A/zh-cn_image_0000002530913074.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=A52D039864590FAA828242C917F92E188093116D6E0FEEF0A24B87E68785D67F "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道：**
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/r0Mix7ddTJ2m8OlD5mIxxA/zh-cn_image_0000002530913066.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=D87688F86BB4C0FA1FB159E263B0869F678C5EC534B86BF2168C2FB6C2E32204 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/4UzX61L8S82t7dnmoT22Qg/zh-cn_image_0000002530913092.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=ECAB3E5D6616D246B64276C3D0F0F46F71B18DE91D66E804744A8C4774D155A7 "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/lFAaXhH5TlawYNRdWpcJ_A/zh-cn_image_0000002530913070.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=CE812EE3B200C0F8779121EEFBC65ED2A119984EEB18EA2E27A5201A8B5B463A)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/M94WImnBRgegodtFcqZJ_w/zh-cn_image_0000002530753060.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=66C0D7FD5E3262416E7222EBFDDFD13053FEEAFDD3C31B33F171D1ACCF6D66D0 "点击放大")
   * **ArkTS Snapshot泳道**：泳道的紫色区块表示一次快照完成。在“Statistics”页签中点击任一对象后，右侧More区域“Native List”页签将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/pArCbsfdTW2eELOf6Dg50Q/zh-cn_image_0000002530753070.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=EE226A7F770C5148BCD8D7583FAB58B6D648D2ED2B5AA87B589111AAB64D0D7F "点击放大")
   * **All Heap & Anonymous VM或All Heap或All Anonymous VM或System Resources或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       在System Resources泳道的Statistics页签中不提供内存大小数据。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。

       在System Resources泳道的Call Trees页签中不提供分配大小数据。

       当未开启统计模式，以及录制了ArkTS Snapshot泳道时，框选All Heap & Anonymous VM或All Heap或Native Heap子泳道，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。否则，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_h61lfRhQfmQmzd_ufTIsA/zh-cn_image_0000002561832991.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=E04CCF73962A811AA10416DD7849B01CA383708DFEDCDEC95BE6B42A4D44DDA1 "点击放大")

       点击“ArkTS Object List”列表中的跳转按钮，跳转到ArkTS Snapshot泳道中的目标对象节点。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/iVkXkosnQfS3qCzoSVdncw/zh-cn_image_0000002561833017.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=5B8F3854990290990C13C39DF6984B79C27ED3DB518F3F9269B52F31C23369E5 "点击放大")
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。在System Resources泳道的Allocations List页签中不提供内存块起始地址和大小。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/XLNYX1AlQWKddbZtgvlthw/zh-cn_image_0000002530913054.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=9F2F3651852772F8CB6648E3B31435062AAB28A99EAC8B942E419D3EBAA636C2 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/_BQhoZ68QZCT1vY9ePY-Hg/zh-cn_image_0000002530913080.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=0A1EDD835CB859C700B0FBCDC6F1600D1F6F0DA5017AB6A3771E58FC8C32C920 "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/5clzaChEQE2JYVOHwMClzA/zh-cn_image_0000002530753096.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=65710D2D9BAD26357398F7ADBCD3843DE48C5A333553BF77D4D38898899E6BC1)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/hfYE2V8dTQe1emzazl1-VQ/zh-cn_image_0000002530753072.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=775EC7CAA956DA023D9ACE87C583E578B9054E9705D7211B037D4C35F5FB49D1 "点击放大")

   说明

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/P7hQygIwTRCExeOTQTSv6A/zh-cn_image_0000002561832995.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=D59F6C2453E16BACA6BE8565B1159B42363105ADE8ECD888C10A6D337878E0C7)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/P-jJeQROStGYRyd6P_OnAw/zh-cn_image_0000002530753062.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=92E5B855BB95979D5C7A48DF020C2E6C295659AED44C340E3B57A03CFBBC5CD9) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/LvQwJ0z-R-6btG7wRHU1xQ/zh-cn_image_0000002561833015.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=390D0FFB7B9F2E0B444B07B2449EF6566EE1865E263DE37FF671EE5FCE223DFD) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_o_yuQ4_QR6h8Lgpdo9I8A/zh-cn_image_0000002561753009.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=47A87F26CD3F194146B1D8BED18DCCA20CFB5A75623022B4AAFA59394C15F44B) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/-ZLe72cCTYqGYjy6TU56Sw/zh-cn_image_0000002561832983.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=5BEA004D69134B7D5EE4623191B4C58C7390B72903C0CE4AD6833BBF2D9A78EE)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/CB_iI1YsQIyXc3gISuWOyQ/zh-cn_image_0000002561832997.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=FFB93947A755F15E2CDF93A385DE0DD1A115E655CB0990E7DB8D3D2723D0780E "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/CDQZEE1sT-iDoYFwpdZuwA/zh-cn_image_0000002530913094.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=A424646663F273A7B8B8CB9B4823EBB9F74E30C16AD740321A6D65B9B83484D5)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     说明

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/TDD4N03vQoGCi-gGQ9kCmg/zh-cn_image_0000002561833005.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=00AA024357294D57931CB75DD8AD228AA9FC35AC7A07D9312EB66B4BC833A288)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/3sEbL-0_Q16YOgnc4ytdAw/zh-cn_image_0000002542627676.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=3ACEB15802E27B55DF5E5CF841BA31C05C65880940D3EA0836D8A3DCD0549A69 "点击放大")

     | 配置项 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | All Heap & Anonymous VM Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Stack | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |

     说明

     + 最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。
     + 统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1新增，用于显示图形渲染相关的内存分配情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/KM9gXHEVQzG6iSOkFdhmXA/zh-cn_image_0000002530913058.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=4E2FACCFA97B0CC0FDEFCAC233B137FEA1AC7C4760850F6D642EEB65BDC86346 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/HPoZm4k1Ty6WA-rYYbpx1A/zh-cn_image_0000002561753037.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=B4FE5946F646F56D02E48D1D62D36B0AEE23226304830DC2B61121F0F834AD62 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/LCRd43ubSJiSK2OosImrsA/zh-cn_image_0000002530913082.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=6D89B56874DE8DFD6A27BB73332D7AD9777BCFE51F931B779FBE2FC6CF98DF7D "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/iMrrnHSBRR-JgbIi01ZQFg/zh-cn_image_0000002530753090.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=DF93F6ED51ACA334336EC1730085C83802508B30C5FFCB793225BBE63DE82127)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/uLaRXP3lTz6nymGOYxqoIg/zh-cn_image_0000002561833001.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=742B8579112E9A04D33BCE34F48CC2E9FD4B4F2DAE6C8BA4BFEF3C98FE9964CC "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/wyv4q7y4QkiWjQcbFG0E2A/zh-cn_image_0000002561753029.png?HW-CC-KV=V1&HW-CC-Date=20260429T054630Z&HW-CC-Expire=86400&HW-CC-Sign=98A5AEB4C1B7C91F85B393678713DDD4F3DFD13D3757E08C925B96AEC388ECFC "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。
