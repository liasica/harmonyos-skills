---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:34+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ddbfab63f0131b2256b658690217b5dcd74776ef2c8d58e5913ba4fe03b65984
---

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。Allocation分析任务支持录制Memory泳道、ArkTS Allocation泳道、All Heap & Anonymous VM等多个泳道。

从DevEco Studio 6.1.0 Beta1开始，Allocation分析任务新增支持录制All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道，不支持录制Native Allocation泳道。

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/IlCFJLQITCmwK7RSnxwVQw/zh-cn_image_0000002561753027.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=980B198DF4C411DB1F7BF0478D3D83D29961A20C356D1FC86633B7FDC8A479D3)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/ftoLsRggR_SOnvRD5XEFvg/zh-cn_image_0000002530913076.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=08DEA6C1FBF674DF6F5564A55F23AD1A0E6F90FD84C8298DD002F2C98F44D2EC)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/508EAmItQBmzKNt4myXY7A/zh-cn_image_0000002561833007.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=9A5D8263E71CDBF601456D27F81D2634C5D377331E52BA81B4C04FE85228DAF2 "点击放大")

   说明

   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/BEsGXY3xQtWb9PqwvRb8xg/zh-cn_image_0000002530913064.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=AD3A19D20730E0F99ECBAE4138EC1189C1BE62CF3DC0271805999A252F09C540)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/t23FPN9ESIGTbtkHQlwgfw/zh-cn_image_0000002530753086.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=354F117050F9AD481F56B656DF80E093EC558332ECF11E44B7B8B4706E57B5C6)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/pg3VnPknRquqJKC2-TSwsQ/zh-cn_image_0000002530753068.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=1A26A77937445D22915705626ED701731620ED9F59864BDED53454B1FB7E6B0B "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/T3GoQIfmSxivcLF6AiDm5g/zh-cn_image_0000002561833003.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=CE056B3AB8FF0E428F68E5DAC455510C665E564718200E72A3AA4CA54A77B2D6)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     说明

     由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：

     + ArkTS Snapshot泳道
     + All Heap & Anonymous VM泳道
     + All Heap泳道
     + All Anonymous VM泳道
     + System Resources泳道
     + Graphic Memory泳道
   * **ArkTS Snapshot泳道**：DevEco Studio 6.1.0 Release版本新增，用于抓取ArkTS堆内存快照，结束录制时会自动录制一次快照，默认不支持录制该泳道。如需录制，在录制前单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/JMzovizrQiiSSCOfmUQdRQ/zh-cn_image_0000002530753092.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=1612C5167D423BBF22496CC7EEBF937C694392836161D809EDDC8EC51CD470E2)按钮关闭统计模式（Statistics Mode）。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/AUmFeB4tRv-Fb3K74u9lCA/zh-cn_image_0000002530913056.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=AE53CA92A9A6A537BE7108034EF8884F3DA6123FC9D25DBFA29A5AFF30D7B8B2 "点击放大")
   * **All Heap & Anonymous VM泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/3xeS8hwOTtGe2Ta38H6Fmw/zh-cn_image_0000002561753003.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=6737B0652113051D7DA44520A0DC2F8A569FDB01CBF36C4D91C5F8F5EFF78FEA)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/37htHLRcT22OPFYR4KRetw/zh-cn_image_0000002530913072.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=633F0255A0CD5AF406B265279A1D4C7B109A243061D9695DEA8325C574C40605 "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/bIFeuQuiQWSuuPBh4CLq5w/zh-cn_image_0000002530753076.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=EDA239C0366D172BF27E8987D54DBE7F2F25CBC8C51DA015A50107E2221A089F "点击放大")
   * **All Anonymous VM泳道**：显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。VM:ION子泳道显示DMA内存分配数据，VM:ASHMem子泳道显示匿名共享内存，VM:.so子泳道显示.so文件内存消耗，VM:others子泳道显示除ION、ASHMem、**.**so外的mmap类型数据。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/EOJC2WWwSQ-eiPKjyrpK3Q/zh-cn_image_0000002530753102.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=08518B704018364D7FF63614876BE15F5CD1AF2BB6D4228E1792B03825C3C058 "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。File Descriptors子泳道显示进程的文件句柄使用情况，Threads子泳道显示进程的线程使用情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/12CLEJLpQYilLOtCvLU7VA/zh-cn_image_0000002561753007.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=C09DA50AA54D3F84F818324A08FDFC77A0F103FE1995F6B7E79F57F49ABDFA41 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/fM3hHX4rRG2P9fCxSszd9Q/zh-cn_image_0000002561753001.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=B4AFA9DA4762AF5A619CBD05CE8D34EFB47828F42A697A3F3855D4990BF875C5)图标，勾选Graphic Memory泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/XwPdGDdgQzGC5Wasl-A4mw/zh-cn_image_0000002530913074.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=3ACB49B1C96141E1A2F82FD918089F4584AB495F899116DBC7412A137AA1F5BD "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道：**
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/Oj8VzHYdTfikf82AL2JFuQ/zh-cn_image_0000002530913066.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=3EFBBC61B575D360AD6897B9C464B856777B7F3719BE2570E69638E42850D81E "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/V71QhpGQTVu3NUwYAjjt9w/zh-cn_image_0000002530913092.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=7DE2ADDB94F71ECF4863BA45214D1211A7AFE4D3A27C81CB10FFF44AEB2CA3A6 "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/-0qmHR6sTAy-NWO7lg3ROA/zh-cn_image_0000002530913070.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=6A467AD02F868A16A4E286D903B7267CB82B319386CC716280372176949B86C6)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/CUZ1ya_sRdaoK6B2M3LR0Q/zh-cn_image_0000002530753060.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=D65A6C28538944A40C2B0806DBB628B580532CBB0CBBD388B75575B7100D5842 "点击放大")
   * **ArkTS Snapshot泳道**：泳道的紫色区块表示一次快照完成。在“Statistics”页签中点击任一对象后，右侧More区域“Native List”页签将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/_VKUXkx0RHqTRPi0XleIUw/zh-cn_image_0000002530753070.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=482BBFC7C447810BB968022B60D68394ACA093C3F5AB2585548AF540CB445876 "点击放大")
   * **All Heap & Anonymous VM或All Heap或All Anonymous VM或System Resources或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       在System Resources泳道的Statistics页签中不提供内存大小数据。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。

       在System Resources泳道的Call Trees页签中不提供分配大小数据。

       当未开启统计模式，以及录制了ArkTS Snapshot泳道时，框选All Heap & Anonymous VM或All Heap或Native Heap子泳道，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。否则，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/ABmyCo1ZR1qpKbsH8Zvqiw/zh-cn_image_0000002561832991.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=CD571805624993692F19D662A6FB2F136D0C5C5ABF28F72F06061E8BDD60838F "点击放大")

       点击“ArkTS Object List”列表中的跳转按钮，跳转到ArkTS Snapshot泳道中的目标对象节点。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/KI8AYb0PSSym1wdpUTBhSg/zh-cn_image_0000002561833017.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=3B82E256F73A3640302846E31593374FC01537C73D228BF83A05E68C8984832B "点击放大")
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。在System Resources泳道的Allocations List页签中不提供内存块起始地址和大小。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/tA1UiF6QTqSd5Xd4O0qSRQ/zh-cn_image_0000002530913054.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=24813EB70F6CB0E69675D43695A3FAE3F138740E3F55ABE66EBD404CF2FD98DC "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/rTaxOojpThe1-hZSFmFhYQ/zh-cn_image_0000002530913080.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=44CC88DE0EC6341D959D9EC108E3B703A4C67EEE45FE65E61DE499B1D16BD8D7 "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/H3VVktpDRnSDbDMo3llfMw/zh-cn_image_0000002530753096.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=8D4768E9C6AC3B9BA5F414566B0F2987FB37398F7679A3E1BDE2825C2C4AEC2D)指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/N3rWkaRWTw6kmeYFDc8WPg/zh-cn_image_0000002530753072.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=2DAD7B7AB81A129C22A56798F711686AD3B2760E46F25BD9AB5A222AD5669553 "点击放大")

   说明

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/zTxHGSXrQ0K2QIb_WTPdPg/zh-cn_image_0000002561832995.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=3784C4FAC7798E4E192BE554F73D1F12FEA91FA6781CA88147F8A8D83CF6763C)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/XI1SMk84Ry6RMrF0eC1kgQ/zh-cn_image_0000002530753062.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=F9E698C03F20BC3F98B324B541CA991496F52A58E24E583771EB09480B5E8693) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/5HuFJP2xSO-zdAqQUYDc9g/zh-cn_image_0000002561833015.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=577F35C53046AAD7440A3A7527E1C7C1EFA4E28F827C0926D5976753BE2B1790) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/kWN9NuPgQPmhdKT_1mj9sw/zh-cn_image_0000002561753009.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=37F22048E52A751AE0134F4EBF2F9EF1FF2A05F6EFAF653032334CFB951D8B6D) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_yHNF_ibTvSn9Qbe03UoZg/zh-cn_image_0000002561832983.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=1F3A29185E2E4A5A13B0C5424E3A27A5001BDC6F014ABE1E8444B1B2C943AC4C)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/sPlSoOLiT3qH2CTz7FgLxQ/zh-cn_image_0000002561832997.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=75D88E81E4C258F357FD0D087177A826E4A75B7B4825E20EBBBC43B105458779 "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Jpw3uL1pSJmxINndHbB2aA/zh-cn_image_0000002530913094.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=2FBCCB60FE10DF5AEEE4BA7ECF66078568C8C5208035984FA2B59AFFC45C59CE)图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     说明

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/8BM7Smm9Si2I2JKwl-kfsw/zh-cn_image_0000002561833005.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=5CAA5E4815FDCEA01400809A15BA8C92CB8E5194BAAFE5E2A491BBFA3F8A9A8E)按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/rw3HtzZJR_ioAnTVTs_8Ow/zh-cn_image_0000002542627676.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=49AC280E0CBB7389610D91F7457C871B2839F17BC1192856E4284659B6E45EF8 "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/GyNDVq5ZQQmHunOhC2ntOw/zh-cn_image_0000002530913058.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=73D9032AE8680409D4290D0C80F29BD8861FCBCC4F7BB7EBA689796EC4CECCA1 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。Details区域中显示此时间段内指定类型的内存分析统计信息：
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/eWU3aVJpS6S1q7cmr285PA/zh-cn_image_0000002561753037.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=589FC97EB5B7CFA55EDDFFB9E09D03A1A4A06BEE5146CB55E362CDA8C9ADFEB2 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       注意

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/eA60nrztTMi8MNebEOt4_w/zh-cn_image_0000002530913082.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=96B86294BB6936977FCBED6999FE71015772293233C6B87BDBC070AA65392A11 "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/gwVi9wOzSsWsSeG-aEuZbw/zh-cn_image_0000002530753090.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=F25504C9C3F3EAF1852FA55BEDCB485CB4C58B396BFC7ECD3EFBA6435306D178)标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/ypVYRGveRmKPQAwtSK3prw/zh-cn_image_0000002561833001.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=E6C16C7023A2E7661E5D1D5B41125201DC03325F34EA9362A4BC5C969D407D35 "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics页签中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees页签显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics页签的分配方式对应）等。

       说明

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/WSF5RmczTIuHYTMWTxs_hA/zh-cn_image_0000002561753029.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=C6F8FF3F98350E37FC0D5E13CD867AA8D63013B428399DA8435AC1DC59CF2F6A "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   说明

   Release应用暂不支持跳转到用户侧Native代码。
