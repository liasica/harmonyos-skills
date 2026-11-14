---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f79f9b11aa7fbebf627fd1e58512cedbd13b28e819c4e2a190bc5b6e53254014
---

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Ai7wfRufQIKNe-8_Z9LTHA/zh-cn_image_0000002779566896.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4AE12A190A0CF7D43651E233F0B2627707420738E5F81059F07BD43CD07A867E)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/3H1ECEooT52FVhSfmCf6Iw/zh-cn_image_0000002779566934.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D379EEFEF54F698363D0D372D1AB525F8BA27A20BEB43AD9A4590195168E045F "点击放大")指定要录制的泳道，或在会话区选择**Open File**，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/8r12LhXcRECrzJmtuKF3cg/zh-cn_image_0000002779566930.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AD0FEDC7C708DC9A235B69ABF240F2A06EA17F0536FE1BB5F089E7054BA9286 "点击放大")

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Pcu9uko-Rmi09SJH6qREzw/zh-cn_image_0000002779566910.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C149B2D0524978F3E196BA9975148FAD38F29AE5958E67AEB2E314A5E08D997 "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/n0hRb6UgRrKFZb8FjtYKPA/zh-cn_image_0000002808766495.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC7338463639837203C08439FB1147CE92B683E08AD59BCE1B11DC68DFD51465)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev、Stack、ArkWeb PA、JS Heap、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/DoCXyRy8Q5KRobyPA3JrHg/zh-cn_image_0000002808886553.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A83031A8A471220C2B58B0BCC80CF281506252CB6C6169F82831BB947D18C869 "点击放大")

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
   * **ArkTS Allocation泳道**：用于显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/-6F2yVTOT_67_UaVkxUuxw/zh-cn_image_0000002808886579.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=26E2131612F004C6120735466ACE20502AFCC883DE12B163D7CCF38CA0AA5C2F "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/tmZMj9JfSGCec8HFdVtC3w/zh-cn_image_0000002779406928.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AA8A808744410744607736D192A0CE5684A1B77B12AC42AADC4F08B75288744 "点击放大")
   * **All Heap & Anonymous VM泳道**：用于显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/cAHx2353Se2vPtJvWL8rzg/zh-cn_image_0000002808766497.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=868ED1187B04AA223517520ED3E70F1BCC05EFDFA7CE719D967312EBEBA7ADBB "点击放大")按钮，可以设置是否为统计模式、回栈模式、JS回栈、JS回栈深度、Native回栈深度、开启异步栈缝合等，设置项的具体说明请参考下表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/VLnls7zAR8SohFbE4J4P1g/zh-cn_image_0000002808886575.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=30FF3523A3F1CCD932D168AECB69DA12A424FB678E43BC3D82A1FE1A9719B335 "点击放大")

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
     | Record Data Range Options | DevEco Studio 6.1.0 Release版本新增。  从26.0.1版本开始，勾选该设置项后才可录制ArkTS Heap泳道数据。  用于设置采样数据范围，包含Malloc、Local Handle和Global Handle，默认勾选Malloc。  + Malloc记录malloc系列函数的内存分配。 + Local Handle用于管理JS对象生命周期的引用句柄（napi\_value），仅支持Phone和PC设备。 + Global Handle允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。 |

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2PeQ9GXkSY-j8y-gLwLSYg/zh-cn_image_0000002779406936.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=84A1002FAB119107A17BBD84C9C7703FFAA1E2B072B2F36708EC3F5EC8548D54 "点击放大")
   * **All Anonymous VM泳道**：用于显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + VM:ION子泳道：用于显示DMA内存分配数据。
     + VM:ASHMem子泳道：用于显示匿名共享内存。
     + VM:.so子泳道：用于显示.so文件内存消耗。
     + VM:others子泳道：用于显示除ION、ASHMem、**.**so外的mmap类型数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/DbzrUVp6Tue5hE92-MfnJQ/zh-cn_image_0000002779406952.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2EF9543750C00AA4FE6B8CA4CA8D7AB92EF73340CD50B2DF8F06B5D6B239D54 "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + File Descriptors子泳道：用于显示进程的文件句柄使用情况。
     + Threads子泳道：用于显示进程的线程使用情况。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/v43zWIBKRaWPYGXl_Eszpw/zh-cn_image_0000002808886549.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=7067423B84E13E28761FDF3E4D15A99731B68F64D8075D6E852DBE972052EC53 "点击放大")
   * **Graphic Memory泳道**：用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/10u0rdG2RaGf_7Fyg-j5IA/zh-cn_image_0000002779406950.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4D301247C4DAF4F9FD345F72F173292C9F7C414B86D6038A9C00817FF631657 "点击放大")图标，勾选Graphic Memory泳道。展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Vulkan子泳道：用于显示GPU\_VK类型的内存分配数据。
     + OpenGL ES子泳道：用于显示GPU\_GLES类型的内存分配数据。
     + OpenCL子泳道：用于显示GPU\_CL类型的内存分配数据。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/FKhaYm2yQeW2QGjkY0c6SQ/zh-cn_image_0000002808886585.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=54EB1D96E154370DAC1902236C52842B4123E13861906AFF4DBAA17A687535EB "点击放大")
   * **Native Leaks泳道**：26.0.0版本新增，用于标记内存泄漏点，不包括纯系统栈泄漏点和无调用栈泄漏点。默认不展示该泳道，如需录制，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/bRy_dcAoTW-E9SNljfu4-Q/zh-cn_image_0000002779406926.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CFD87084BEB83607E6FC7B60F633E2A965870DE1F1EC024A62A2739C2D7DC32 "点击放大")图标，勾选Native Leaks泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     **说明** 

     + 泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。
     + 设备系统要求：API 26.0.0及以上版本。
     + 26.0.0版本，Native Leaks泳道录制时，不支持开启设置中的Statistics Mode（统计模式）和Local Handle。在录制该泳道前，需要单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/3z6VFLnrS8mu9THDvKGgXA/zh-cn_image_0000002779406932.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9D55A6D747D37167F93FC71B45DE8FD7BE2281446F0C042B13063F2B774C6BCF "点击放大")按钮关闭Statistics Mode和Local Handle，否则影响正常录制。从26.0.1版本开始，Native Leaks泳道录制时，支持开启设置中的Statistics Mode（统计模式）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/2PimmVgUSx2-dj3w26YOtw/zh-cn_image_0000002779566926.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C77E4A58380F051A7D8B861DB48A7737FFFFD155127FCE631A299185675CA8F "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，查看此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + **Statistics**区域：26.0.0版本新增，用于显示当前框选时间段内的虚拟内存区域数量的最小值（VMA Count Min）、虚拟内存区域数量的最大值（VMA Count Max）、虚拟内存区域数量的平均值（VMA Count Avg）、PSS内存最小值（PSS Min）、PSS内存最大值（PSS Max）、PSS内存平均值（PSS Avg），以及共享脏内存平均值（Shared Dirty Avg）、共享干净内存平均值（Shared Clean Avg）、私有脏内存平均值（Private Dirty Avg）、私有干净内存平均值（Private Clean Avg）、Swap内存平均值（Swap Avg）等。
     + **Details**区域：显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。包括时间戳、PSS内存大小、共享脏内存大小、共享干净内存大小、私有脏内存大小、私有干净内存大小、Swap内存大小、Swap PSS内存大小、VMA数量等。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/5H3AUl2GSFWZmaixXgYLbw/zh-cn_image_0000002779406940.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=638BAA241D360830A9FFD0F97712D0C4E6E8E765ED0D8DF01CC55F4E42F8C54C "点击放大")
   * **Memory****子泳道**：**Details**区域中显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

     从26.0.1版本开始，FilePage Other、.so、.ttf、.hap类型子泳道的**Details**区域中新增Path列，用于显示各采样点PSS占比最大的文件路径。选中采样点，右侧**Path List**列表按PSS占比降序显示文件路径，最多显示10条，占比为0的文件路径不显示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/clK54bKJRbW-TvzhZXH8cw/zh-cn_image_0000002779406944.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=08D1BF0ED56C9ABEFEE78188E50C07ED07592B39B94EB43F4FCE1BB150594703 "点击放大")
   * **ArkTS Allocation泳道**：

     主泳道：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。

     子泳道：显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。

     Details区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/faeYkHFZS4SsQ-1VQv_F9w/zh-cn_image_0000002808766467.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B2E2A8BDF9C025E5B295424967542133FDFEE1345FCDF0036DA76AC9DED0101 "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     **说明** 

     该泳道即将下线，推荐使用[Snapshot模板](ide-snapshot-basic-operations.md)分析ArkTS内存泄漏。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/SK75Mg5aQK-PkPy8mK7zhQ/zh-cn_image_0000002808886561.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6956B7B0EFB7E9542B1736B497A20D89A027C42E9D450F930C8ACB09AF354113 "点击放大")
   * **ArkTS Snapshot泳道**：在**Statistics**区域中点击任一对象后，右侧More区域**Native List**区域将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/fy6csRH7Tda7KpGVV39C_g/zh-cn_image_0000002779566906.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=335802502C1F34F08A690AC134AD3FD0C0C6BE701E1912085619DF005263DA09 "点击放大")
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

       从26.0.0版本开始，点击右侧More区域中**Heaviest Stack**列表左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/5K3KWZO3Sai3UtYJ71cDcg/zh-cn_image_0000002808766473.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8FC8B5008738F81CB1D7A09BBD76E3BF736930EAE1DDCF59999FD39657362141 "点击放大")按钮，将Heaviest Stack列表中的数据导出到本地进行保存。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/IANAbqm9RkKDlPaSzxPfVw/zh-cn_image_0000002779406918.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4112BA7B9EA681F494CE289776144C8B92FF1EBB06E72158FF2DBA217793CD1A "点击放大")
     + **Allocations List**区域：显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       **说明** 

       - System Resources子泳道的Allocations List区域中不提供内存块起始地址、大小。
       - 统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ioPsENKCTdiVl-GG0A3r9w/zh-cn_image_0000002779406922.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD0083308A3A8A3CB928D96862615C83C8FC84960D92A4DA40FC15FF72E39B70 "点击放大")
   * **Native Leaks泳道**：框选或点选泄漏点后展示泄漏点的数据，包括Native泄漏对象名称、聚类后的总数、聚类后的总内存大小、单行栈帧的类型、内存分配栈等。

     **说明** 

     + 统计模式（Statistics Mode）开启后，Symbol Name不提供线程名信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/6R3HWuLUTES-3QiJXEX8Lw/zh-cn_image_0000002808766471.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB6F57877755C7F4A86D0B9641BA866C844F83B492DB9FC00D79747B4B0C801B "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/1GxDgGenT-20LGUMvpgc5g/zh-cn_image_0000002779566892.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=78AEEEFBE9E4B5D587E346838836E1063FF2100C1400C1557610C8CF85ED991C "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/4W5ohWi1RiGZfMi6dogibg/zh-cn_image_0000002779406934.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=955786EDBC9E79F729FF48C429FF675D0C548FDFA30CEB144C5A0F9349A0470D "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/fzf03j2eQp6qFVeIze--CQ/zh-cn_image_0000002808886557.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6FE42353A7A7014F3AB8C9DECB14292814B13986B0ADBFDEBECB7C1A55FFCB61 "点击放大")

   **说明** 

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/cVPel1aQS4uti2G_AC24jg/zh-cn_image_0000002779566920.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4FB7A4CDB46626A1D9BB3257724FA5047F865F703AD1C57231078CE78C9F34D7 "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/h6HgWifTSay4q3CIN7_7jw/zh-cn_image_0000002779406930.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CD2FE114869A817DA5798A08CB7015664BB84B1AF4D4DA96AF19AE4400D7125) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/pXsmjyBdQ_CJwCkTwfBI-w/zh-cn_image_0000002779406942.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9505CDA5023FC983C4A1E48890E87EB432E3F4BB9A2235C58FBA0B4D15917A64) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/TWG_DBBpQIuEKe02Ot_1RA/zh-cn_image_0000002779566908.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4E26ECB474B0EF35BB9DC4E054A72E15DA17DBD80A6ADA80E9F6C600CEB4515) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/UZvdbFIpT8iJxcHbP3wp1Q/zh-cn_image_0000002808766513.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=80F0810F8B169ED02F1493965699F0C17C64594D08DD97E0F7CA77AFB3545DEA)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/K5OfxsNnR_-Y66Mi2o9XqQ/zh-cn_image_0000002808886577.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=203F47F5E2211CC4C86ECB86B096EF37561464608F130B291027679DA51ABC16 "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ZLxGsgy7Qae_gtcwmZptFw/zh-cn_image_0000002779566932.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=EABFA4B78DB622482EA126FB74FAE56EB20186197BA66188E307E83FBAB2217A "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     **说明** 

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/_6V1umT0RGytwvrtJ0NRuQ/zh-cn_image_0000002779566914.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D4C49B92555D3BF7011978FECCA30EE2E42BB876CFAD9A1B87F1E9170E168EBA "点击放大")按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/YIzMNem3S-21oOnkObG7-g/zh-cn_image_0000002808886551.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D90370E17555CF5E7F13C6AFDDD44C4788E9FDE60B5C3A4696A025980AFCE0E4 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/JWisdY5lQPSIdGjdGYt21w/zh-cn_image_0000002779566924.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=64E8EAFDE2B09B67BB709B995E186D6A20B425BD987ED4BFF91F1D43DDE19496 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，Details区域中显示此时间段内指定类型的内存分析统计信息。
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/VPHF8b_bS62isQaM434_8w/zh-cn_image_0000002808766469.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF958F8FA8ABEB41BF978E26EDB62E83C5C0C32B0E8A18DEA0DD8B6407B00EBF "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/rq0w2Uj2QDGU-eaEItVsXg/zh-cn_image_0000002779406946.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA2AB26AA83C9F0A8C0CD8A6BE5E3D0A1004132C4FF7B9D4A135BD22C42C682E "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/FNRdAL_EQVKomrK-FWo-UQ/zh-cn_image_0000002779566902.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=B815C2DA0DD195E6BC2761DF27D91D2E4A41D45922D1AF7045A1DA1E1E1E017A "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/nkx9zBRRSJyywVWVIsBluw/zh-cn_image_0000002779406956.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=B7CDFD686929984BFAD5C12C10B698AD4826E6884199943B4D3406A8F1420A57 "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics区域中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees区域显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。

       **说明** 

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/Mn1bIO76R-20MQEvcJLSDw/zh-cn_image_0000002808766483.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=A8D9250C8E2B49756084EA48DD85A53717FB2911D1334B01972185B581B20F3B "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。
