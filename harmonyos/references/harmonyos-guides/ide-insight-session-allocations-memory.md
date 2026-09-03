---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:aac4a3c698d465119206917c6901554e59c64548bfb06d9c8744ffad6818f273
---

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/_m4OH5hqRdObPudty6EH2w/zh-cn_image_0000002701663186.png)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/0SV0XiaTQR6iTZnHM4n0jQ/zh-cn_image_0000002701663180.png "点击放大")指定要录制的泳道，或在会话区选择**Open File**，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/75oXvp2KREKMqIRXkmwN0g/zh-cn_image_0000002701823082.png "点击放大")

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/_IMyeu6_RteXzynxtL-6FQ/zh-cn_image_0000002701663176.png "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/i5wO9GtrTcCgC4mIs4gZUw/zh-cn_image_0000002701663184.png)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev、Stack、ArkWeb PA、JS Heap、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/m4CFImNrT4-GI0HAgHT5Kw/zh-cn_image_0000002731382323.png "点击放大")

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
     | ArkWeb PA | 26.0.0版本新增。  Malloc内存分配。 |
     | JS Heap | 26.0.0版本新增。  ArkWeb Render进程JS堆内存占用。 |
     | .hap | 进程加载的.hap文件所占内存。 |
     | .so | 进程加载的.so动态库所占内存。 |
     | .ttf | 进程加载的.ttf字体文件所占内存。 |
   * **ArkTS Allocation泳道**：用于显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/W539MIR-T6O-BqC53Szf8w/zh-cn_image_0000002701823104.png "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     **说明** 

     + 该泳道即将下线，推荐使用[Snapshot模板](ide-insight-session-snapshot.md)分析ArkTS内存泄漏。
     + 由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：
       - ArkTS Snapshot泳道
       - All Heap & Anonymous VM泳道
       - All Heap泳道
       - All Anonymous VM泳道
       - System Resources泳道
       - Graphic Memory泳道
       - Native Leaks泳道
   * **ArkTS Snapshot泳道**：DevEco Studio 6.1.0 Release版本新增，用于抓取ArkTS堆内存快照，结束录制时会自动录制一次快照，默认不支持录制该泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     从26.0.0版本开始，ArkTS Snapshot泳道支持解析内存对象，具体操作请参考[解析内存对象](ide-snapshot-basic-operations.md#section12167134834913)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/8bp_A7m1SmG6AK82101Tyg/zh-cn_image_0000002701823050.png "点击放大")
   * **All Heap & Anonymous VM泳道**：用于显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/7AIdTo0OR1eoUDSk_nn_BA/zh-cn_image_0000002731382397.png "点击放大")按钮，可以设置是否为统计模式、回栈模式、JS回栈、JS回栈深度、Native回栈深度、开启异步栈缝合等，设置项的具体说明请参考下表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/r43CUMjNSHObMMvWo6LNWA/zh-cn_image_0000002731542383.png "点击放大")

     | 设置项名称 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | Collect Only Unreleased Memory Events | 26.0.0版本新增。  在录制阶段，控制是否保留已释放内存的调用栈数据，默认开启。  开启时，尽量丢弃已释放的调用栈数据，保留未释放的调用栈数据，关注内存泄漏问题定位，减少对被调优应用的性能影响。  关闭时，保留全部申请和释放内存调用栈数据，需要分析内存分配和释放的完整生命周期，如排查内存抖动等问题。 |
     | All Heap & Anonymous VM Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。  可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Sampling Size | DevEco Studio 6.1.1 Release版本新增。  内存数据采样大小，可配置范围为1-1048576Bytes，默认为4096Bytes。  配置后，仅对Native Heap和All Anonymous VM泳道中的mmap类型数据生效。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。  若选择FP回栈模式，支持配置JS Backtrace Depth（JS回栈深度）和Native Backtrace Depth（Native回栈深度）设置项；若选择DWARF回栈模式，支持配置Backtrace Depth（回栈深度）。  FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。  在DevEco Studio 6.1.0 Beta2之前版本，默认关闭。  从DevEco Studio 6.1.0 Beta2版本开始，默认开启。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Depth | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |
     | Sync Backtrace Depth | DevEco Studio 6.1.1 Beta1版本新增。  同步回栈深度。仅当Record Async Stack开启的情况下存在，其层数代表着JS与Native的共同同步回栈深度。可配置范围为5-100，默认20层。 |
     | Record Async Stack | DevEco Studio 6.1.1 Beta1版本新增。  用于开启[异步栈缝合](ide-profiler-glossary.md#section58492173810)，默认关闭。仅当Backtrace Mode选择为FP模式时，支持开启。  26.0.0以下版本，开启后，异步回栈时支持多回一层异步栈帧，最大异步回栈层数为16层。  26.0.0及以上版本，支持通过Async Nesting Depth和Async Backtrace Depth设置异步栈嵌套层数和回栈层数。 |
     | Async Nesting Depth | 26.0.0版本新增。  异步栈嵌套层数，可配置范围为[1,16]，推荐范围为[3,10]，默认为3。  仅当Record Async Stack开启时，支持设置。 |
     | Async Backtrace Depth | 26.0.0版本新增。  异步回栈层数，指每个异步栈中显示的最大层数，可配置范围为[1,256]，推荐范围为[16,32]，默认16层。  仅当Record Async Stack开启时，支持设置。 |
     | Record Data Range Options | DevEco Studio 6.1.0 Release版本新增。  用于设置采样数据范围，包含Malloc、Local Handle和Global Handle，默认勾选Malloc。  + Malloc记录malloc系列函数的内存分配。 + Local Handle用于管理JS对象生命周期的引用句柄（napi\_value），仅支持Phone和PC设备。 + Global Handle允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。 |

     **说明** 

     + 若勾选Local Handle，在应用生命周期内首次录制时会重启应用。若应用在生命周期内被强制终止后重启，再次录制时仍会重启应用。
     + 最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。
     + 最小跟踪内存设置的数值大小不影响Local Handle和Global Handle。
     + 统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。
   * **All Heap泳道**：用于显示Heap类型数据之和。展开主泳道，包括Native Heap、ArkTS Heap、JS Heap、JS Heap(ArkWeb-PA)四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Native Heap子泳道：用于显示Malloc、ArkLocalHandle和ArkGlobalHandle内存分配。
     + ArkTS Heap子泳道：用于显示ArkTS对象内存分配。
     + JS Heap子泳道：用于显示JS对象内存分配。
     + JS Heap(ArkWeb-PA)子泳道：26.0.0版本新增，用于显示ArkWeb中Malloc内存分配。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/jxKIWEZyToek12OI_00OUQ/zh-cn_image_0000002701663142.png "点击放大")
   * **All Anonymous VM泳道**：用于显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + VM:ION子泳道：用于显示DMA内存分配数据。
     + VM:ASHMem子泳道：用于显示匿名共享内存。
     + VM:.so子泳道：用于显示.so文件内存消耗。
     + VM:others子泳道：用于显示除ION、ASHMem、**.**so外的mmap类型数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Qzh2_70dSBabXIG7-dXFsQ/zh-cn_image_0000002731542359.png "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + File Descriptors子泳道：用于显示进程的文件句柄使用情况。
     + Threads子泳道：用于显示进程的线程使用情况。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/E0K7MXXRS067yDEX791P3g/zh-cn_image_0000002701823012.png "点击放大")
   * **Graphic Memory泳道**：用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/ZIsNvsP5QR6OD9ycBpQuIg/zh-cn_image_0000002731542369.png "点击放大")图标，勾选Graphic Memory泳道。展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Vulkan子泳道：用于显示GPU\_VK类型的内存分配数据。
     + OpenGL ES子泳道：用于显示GPU\_GLES类型的内存分配数据。
     + OpenCL子泳道：用于显示GPU\_CL类型的内存分配数据。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/2HuwB_gsRfKRXSmSuemS8A/zh-cn_image_0000002701663152.png "点击放大")
   * **Native Leaks泳道**：26.0.0版本新增，用于标记内存泄漏点，不包括纯系统栈泄漏点和无调用栈泄漏点。默认不展示该泳道，如需录制，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/GupmYZ39T2WIDFHJCoqgEg/zh-cn_image_0000002731382349.png "点击放大")图标，勾选Native Leaks泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     **说明** 

     + 泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。
     + 26.0.0版本，Native Leaks泳道录制时，不支持开启设置中的Statistics Mode（统计模式）和Local Handle。在录制该泳道前，需要单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/CeHbuWZuT8yAbsPOXGQKPg/zh-cn_image_0000002731382403.png "点击放大")按钮关闭Statistics Mode和Local Handle，否则影响正常录制。
     + 设备系统要求：API 26.0.0及以上版本。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/fYMGucaaQVKDpEXxDEGV3A/zh-cn_image_0000002731382383.png "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，查看此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + **Statistics**区域：26.0.0版本新增，用于显示当前框选时间段内的虚拟内存区域数量的最小值（VMA Count Min）、虚拟内存区域数量的最大值（VMA Count Max）、虚拟内存区域数量的平均值（VMA Count Avg）、PSS内存最小值（PSS Min）、PSS内存最大值（PSS Max）、PSS内存平均值（PSS Avg），以及共享脏内存平均值（Shared Dirty Avg）、共享干净内存平均值（Shared Clean Avg）、私有脏内存平均值（Private Dirty Avg）、私有干净内存平均值（Private Clean Avg）、Swap内存平均值（Swap Avg）等。
     + **Details**区域：显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。包括时间戳、PSS内存大小、共享脏内存大小、共享干净内存大小、私有脏内存大小、私有干净内存大小、Swap内存大小、Swap PSS内存大小、VMA数量等。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/HvWPtStkQ_GrwhgJNvZqGA/zh-cn_image_0000002731382369.png "点击放大")
   * **Memory****子泳道**：**Details**区域中显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

     **须知** 

     Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/HfYlpGM3QHuUyEm_snNkqw/zh-cn_image_0000002731382325.png "点击放大")
   * **ArkTS Allocation泳道**：

     主泳道：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。

     子泳道：显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。

     Details区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/S_LTOYqbTTGN-fRh3M3mSQ/zh-cn_image_0000002731542375.png "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     **说明** 

     该泳道即将下线，推荐使用[Snapshot模板](ide-snapshot-basic-operations.md)分析ArkTS内存泄漏。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/tb5YIFlqSOyTvXb6YGAViQ/zh-cn_image_0000002701823034.png "点击放大")
   * **ArkTS Snapshot泳道**：在**Statistics**区域中点击任一对象后，右侧More区域**Native List**区域将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/WJnAP_yrTImWRedZN3dBQw/zh-cn_image_0000002701663132.png "点击放大")
   * **All Heap & Anonymous VM或All Heap或All Anonymous VM或System Resources或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + **Statistics**区域：显示该段时间内的静态分配情况，包括分配方式、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。统计模式下不支持跳转。

       **说明** 

       - 在System Resources子泳道的Statistics区域中不提供内存大小数据。
     + **Call Trees**区域：显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别、so库的构建ID（Build ID）等。

       **说明** 

       - System Resources子泳道的Call Trees区域中不提供分配大小数据。
       - 从26.0.0版本开始，支持展示so库的构建ID（Build ID）。
       - 26.0.0以下版本，当未开启统计模式（Statistics Mode），且录制ArkTS Snapshot泳道时，框选All Heap & Anonymous VM/All Heap/Native Heap子泳道，单击任一行栈帧，More区域显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。否则，单击任一行栈帧，More区域显示经过该栈帧的分配内存最大的调用栈。

         26.0.0及以上版本，无论是否开启统计模式，录制ArkTS Snapshot泳道，框选All Heap & Anonymous VM/All Heap/Native Heap子泳道，单击任一行栈帧，More区域都会显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。

       点击**ArkTS Object List**列表中的跳转按钮，跳转到ArkTS Snapshot泳道中的目标对象节点。

       从26.0.0版本开始，点击右侧More区域中**Heaviest Stack**列表左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/gNsAr0rCQ8idltXKz929bA/zh-cn_image_0000002701663104.png "点击放大")按钮，将Heaviest Stack列表中的数据导出到本地进行保存。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/MmHAeeHVQ_yo1blY92bGVw/zh-cn_image_0000002701823030.png "点击放大")
     + **Allocations List**区域：显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       **说明** 

       - System Resources子泳道的Allocations List区域中不提供内存块起始地址、大小。
       - 统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/aj4aQKJzQcOfTyjyR_iADQ/zh-cn_image_0000002701823038.png "点击放大")
   * **Native Leaks泳道**：框选或点选泄漏点后展示泄漏点的数据，包括Native泄漏对象名称、聚类后的总数、聚类后的总内存大小、单行栈帧的类型、内存分配栈等。

     **说明** 

     + 统计模式（Statistics Mode）开启后，Symbol Name不提供线程名信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/XH8JRuICSbWkIg9-9bYsIw/zh-cn_image_0000002701823018.png "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/NBOaAZI-Q9qes4MIe4Wi3g/zh-cn_image_0000002731542301.png "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/cUaTrSXlQuuMQGLEoqJdEA/zh-cn_image_0000002731542335.png "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/-kJ4dieTT56xQJq8Blb14A/zh-cn_image_0000002731382333.png "点击放大")

   **说明** 

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/If6uj-SyTRafbUctUF2mIw/zh-cn_image_0000002701823072.png "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/m6AkGuT5R6OLP3rWkRzg8Q/zh-cn_image_0000002701823058.png) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/Ip_GSIGESC6eH1IoflGUYg/zh-cn_image_0000002731542343.png) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/J2JhOiFvTTWYt3EYUZL7Ag/zh-cn_image_0000002701823060.png) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Tbh17YIrSd-gXaBFYLCUZA/zh-cn_image_0000002731382391.png)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/RM44wm5JSuW7wr0z7o5ZOA/zh-cn_image_0000002731382367.png "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/7mR6Y0f8TEGGfJ9t12ulsg/zh-cn_image_0000002701823086.png "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     **说明** 

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AltD_xS0QsmryDGlJdSQeg/zh-cn_image_0000002731542341.png "点击放大")按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     | 配置项 | 说明 |
     | --- | --- |
     | Statistics Mode | 该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。 |
     | Sampling Interval | 统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。 |
     | Native Allocation Filter Size | 最小跟踪内存，该参数表示最小抓取的内存大小。可配置范围为0-65535Bytes，默认为1024Bytes。 |
     | Backtrace Mode | 内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。 |
     | Record JS Stack | 是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。 |
     | JS Backtrace Depth | JS回栈深度。可配置范围为1-128，默认10层。 |
     | Native Backtrace Depth | Native回栈深度。可配置范围为5-100，默认10层。 |
     | Backtrace Stack | 回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。 |

     **说明** 

     + 设置的最小跟踪内存数值越小、回栈深度越大，可能会导致DevEco Profiler卡顿。请根据应用实际的调测情况进行合理设置。
     + 统计模式用于不关注单次分配、关注应用较长时间的内存变化情况的场景，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长的目的。设置的Sampling Interval为近似值，即尽可能地在接近这个时间内做统计汇总，存在一定的偏差，偏差不超过1s，偏差不会对内存分配的正确性产生影响。
     + 使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/3NeDdg2SRXi3Q6FpDuz1Rg/zh-cn_image_0000002701663096.png "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/OY7y6JcPRmyo1ZPtRMzWlA/zh-cn_image_0000002701823076.png "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/_ME9qOJ1Q9KEvl4B95SRBg/zh-cn_image_0000002731382317.png "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/NzLT8gl3QymzKL6jZd5ncg/zh-cn_image_0000002731542353.png "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/42GF0UeLQ7qdYlJSqbr1DQ/zh-cn_image_0000002701823044.png "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/0mFGVFRjTIK7khyCPO-7Ew/zh-cn_image_0000002701663170.png "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics区域中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees区域显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。

       **说明** 

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/CgqeQSIpS1WdXL3sx9kaDg/zh-cn_image_0000002701823040.png "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。
