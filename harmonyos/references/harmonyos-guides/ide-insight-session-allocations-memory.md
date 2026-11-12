---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:696719e0a1e9bd46855e216f83169dbfe0f671d649a268727d86297f593adfa6
---

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/au4llco-QZW7Wu7Tm44wSQ/zh-cn_image_0000002779566896.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DDD1F7D641553F931CA7761E64CCCBA20F70D886516EAC2DBD29CC6EEDE3A75)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/JUO0SmtESUigoBVArD8pwg/zh-cn_image_0000002779566934.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A786FCC4F431B4F186E4810E0950389DCC1A47D45913AB39531B4CB41DFCFC69 "点击放大")指定要录制的泳道，或在会话区选择**Open File**，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/VqAjuoBkSBi1shnjN0f-ZQ/zh-cn_image_0000002779566930.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FE055E9057D88927DA6280804B5513D71B51D65EBA804006D4AD14F43664C07E "点击放大")

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/Wa6QdnzmSEatUnwQRn1Ckg/zh-cn_image_0000002779566910.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E83B18AFC8DFE014B49BFE37E299F0B02CDC2D771EDC217DBC5470ADEF65B0AE "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/rF6t1O6mT16wnTChAbEFFg/zh-cn_image_0000002808766495.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1ACB160EAF2BFE6B55C6189058522CD05E39929A4318AE819EF270637FFD0A7)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev、Stack、ArkWeb PA、JS Heap、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/9oOsCfPHQO-loptyIZNKQg/zh-cn_image_0000002808886553.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=833BCC6E613E35B46B59028F378F582331A26564145C4FE3206CDA15CDB4FA8C "点击放大")

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
   * **ArkTS Allocation泳道**：用于显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/L9c8BtY8S7ypJGqwRUHO0A/zh-cn_image_0000002808886579.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3DEADF0C8A7D83256A1CA4ADB7E6CCCB1A113D6D1A255FEBB9FC5BC76EE4C25E "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/bMXAqIlrQ_CbXyr0ysq1Jw/zh-cn_image_0000002779406928.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8A385B7D0BB59EB453E2F894BA0AD813F5F34D08C3EE7074E0B33D0F1DC1307B "点击放大")
   * **All Heap & Anonymous VM泳道**：用于显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ek-KMfVmRLGgP774LP2oug/zh-cn_image_0000002808766497.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEB8F67B6AD8C98BBCAD0AB4FD8B659BBF82DE3ABAE2B3972394C933F680FC9C "点击放大")按钮，可以设置是否为统计模式、回栈模式、JS回栈、JS回栈深度、Native回栈深度、开启异步栈缝合等，设置项的具体说明请参考下表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/G8pBSlYXTaa1JrCBRHrfag/zh-cn_image_0000002808886575.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9716DC1BC55CD87FEC1FC7C70AC6B6D7B6A71CBDD7FDAC3AD1AFF27F4315A38 "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/18TyY1LCSRmtC_dxIEF1uQ/zh-cn_image_0000002779406936.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4254C7741897F7D696FEE0878351336E99B9A46E4500242F753745EE45D77DC4 "点击放大")
   * **All Anonymous VM泳道**：用于显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + VM:ION子泳道：用于显示DMA内存分配数据。
     + VM:ASHMem子泳道：用于显示匿名共享内存。
     + VM:.so子泳道：用于显示.so文件内存消耗。
     + VM:others子泳道：用于显示除ION、ASHMem、**.**so外的mmap类型数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/DjyoYiX3TG6DBUthXbtNNQ/zh-cn_image_0000002779406952.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C7DF50E664A3076990E22C4AD45BEDCBF92CFE1D23BF3B7C7CF708009EEF721 "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + File Descriptors子泳道：用于显示进程的文件句柄使用情况。
     + Threads子泳道：用于显示进程的线程使用情况。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/D1HLcN73QfKcX4JAsniCLQ/zh-cn_image_0000002808886549.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=120EFAA955372AE9D94811818BBA026D45DFDE7DEC61CE892802C460BCDD10A7 "点击放大")
   * **Graphic Memory泳道**：用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/YxAqGhKrR-ipqIxqAdUbUQ/zh-cn_image_0000002779406950.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5761F90D2FDF0FA20A1CFED581400432871DEB76C47F7872D6E973A2A5569F6C "点击放大")图标，勾选Graphic Memory泳道。展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Vulkan子泳道：用于显示GPU\_VK类型的内存分配数据。
     + OpenGL ES子泳道：用于显示GPU\_GLES类型的内存分配数据。
     + OpenCL子泳道：用于显示GPU\_CL类型的内存分配数据。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/Sxg36n9RQ4WRTvaE1Dx5aw/zh-cn_image_0000002808886585.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB87D521A06FC25DC9C22330739EE648D99FB03AAEE9B05A7AFF88129FC81493 "点击放大")
   * **Native Leaks泳道**：26.0.0版本新增，用于标记内存泄漏点，不包括纯系统栈泄漏点和无调用栈泄漏点。默认不展示该泳道，如需录制，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/x_w9BY6DTJuqHh_fL9Jo8A/zh-cn_image_0000002779406926.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CC2E7DC3480C90B848FD988502C7B718B6ECF6EED24537E420161FFCF4721422 "点击放大")图标，勾选Native Leaks泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     **说明** 

     + 泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。
     + 设备系统要求：API 26.0.0及以上版本。
     + 26.0.0版本，Native Leaks泳道录制时，不支持开启设置中的Statistics Mode（统计模式）和Local Handle。在录制该泳道前，需要单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/mL75hHV9RRqxQ5ZKU-EfAg/zh-cn_image_0000002779406932.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=65DD4FC18ACE8C4D85DAC164D53CECAA21F622F956F2FC6182AE6C455549FDF2 "点击放大")按钮关闭Statistics Mode和Local Handle，否则影响正常录制。从26.0.1版本开始，Native Leaks泳道录制时，支持开启设置中的Statistics Mode（统计模式）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/THd4gr2ZQZGeMyTR93CzmA/zh-cn_image_0000002779566926.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6EDE627F61A7368BC7B3853F33B7F819DE224696D1E35DFBD982D238FFF829B "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，查看此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + **Statistics**区域：26.0.0版本新增，用于显示当前框选时间段内的虚拟内存区域数量的最小值（VMA Count Min）、虚拟内存区域数量的最大值（VMA Count Max）、虚拟内存区域数量的平均值（VMA Count Avg）、PSS内存最小值（PSS Min）、PSS内存最大值（PSS Max）、PSS内存平均值（PSS Avg），以及共享脏内存平均值（Shared Dirty Avg）、共享干净内存平均值（Shared Clean Avg）、私有脏内存平均值（Private Dirty Avg）、私有干净内存平均值（Private Clean Avg）、Swap内存平均值（Swap Avg）等。
     + **Details**区域：显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。包括时间戳、PSS内存大小、共享脏内存大小、共享干净内存大小、私有脏内存大小、私有干净内存大小、Swap内存大小、Swap PSS内存大小、VMA数量等。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/xKj8Q_UUToK86LIUUIbS2w/zh-cn_image_0000002779406940.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=59F210DC22EA80FFA181429C6270117D11913B76BA02178CE6A4C8A877CD898D "点击放大")
   * **Memory****子泳道**：**Details**区域中显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

     从26.0.1版本开始，FilePage Other、.so、.ttf、.hap类型子泳道的**Details**区域中新增Path列，用于显示各采样点PSS占比最大的文件路径。选中采样点，右侧**Path List**列表按PSS占比降序显示文件路径，最多显示10条，占比为0的文件路径不显示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/dIQahXQPRBONWii6k8x4_A/zh-cn_image_0000002779406944.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BDD30039DE986171731F2DA4203E44496F133727C772BF1BD5BC67EE44A4279C "点击放大")
   * **ArkTS Allocation泳道**：

     主泳道：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。

     子泳道：显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。

     Details区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/bBx0xyXGSkGGeAPJjdvqHA/zh-cn_image_0000002808766467.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3BF2B59087870666CAF822CE158C389B4FC06DC6351159BAE1346DE58978F4BE "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     **说明** 

     该泳道即将下线，推荐使用[Snapshot模板](ide-snapshot-basic-operations.md)分析ArkTS内存泄漏。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/1jWaJKArQ7aHQhLDpxWiYg/zh-cn_image_0000002808886561.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=28BB0DE31E826979E45F25DC994ECBB6020D08917DE50D327222076B4D2FD8F9 "点击放大")
   * **ArkTS Snapshot泳道**：在**Statistics**区域中点击任一对象后，右侧More区域**Native List**区域将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ppfDUrpOShmCkOhdohReug/zh-cn_image_0000002779566906.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2BEDC89B0994E2F273A4B9A6C93E4BEAE5C50EFC7E3FC0C94EABCB0EAC5BC9A "点击放大")
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

       从26.0.0版本开始，点击右侧More区域中**Heaviest Stack**列表左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/VbSVwOZOSW-sHVjEELtpGw/zh-cn_image_0000002808766473.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F6C1219FEFFE7BEB1B06733A3EF54F75EECFE55403F1E56046DB3CADEF3AEABD "点击放大")按钮，将Heaviest Stack列表中的数据导出到本地进行保存。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/fSfa7nYGR5GbrA1OqqVHcg/zh-cn_image_0000002779406918.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D9D90AA777F7BC82A01BA993CA161F1D69091847F88FA015C230D5EB59AB7C1 "点击放大")
     + **Allocations List**区域：显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       **说明** 

       - System Resources子泳道的Allocations List区域中不提供内存块起始地址、大小。
       - 统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Oz3Q7xlfQOaQCKEe2axK-A/zh-cn_image_0000002779406922.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E807F69B36AE8733F1EC956B3F9C60BC5DBCE651EF60CDFB5F9F2F6A1B28D54B "点击放大")
   * **Native Leaks泳道**：框选或点选泄漏点后展示泄漏点的数据，包括Native泄漏对象名称、聚类后的总数、聚类后的总内存大小、单行栈帧的类型、内存分配栈等。

     **说明** 

     + 统计模式（Statistics Mode）开启后，Symbol Name不提供线程名信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/v3VuwfNbSqSSwsCCM2g_KA/zh-cn_image_0000002808766471.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D572B31BCF2E414308A0667907EF68BB934E633CA8C41E4ED58970B598CDA591 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/dBf-haTDQm6wEgQJncVvNA/zh-cn_image_0000002779566892.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F319AD34CD1BB48B3BDB7D242E898249851E8E5B44DF1D44D9F75208B39AAF9D "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/MGClJyWUSdCYJT_xDiALCw/zh-cn_image_0000002779406934.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E21178EA242486D9197600FE3EF4F690636BA4151554F0994D1D57F84E3ADDE1 "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/fcoP7le3TdK5-JmcXMArjA/zh-cn_image_0000002808886557.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1D9D86B0EF2212C64C0F088F71D24A30CF937A6814D5E74D1C04031D40B4C54B "点击放大")

   **说明** 

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/weFWuoT-SeSdVEk3B2H8hg/zh-cn_image_0000002779566920.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E99DF0D78CC01B39BDA6E6C4C743EAC3E4B58C2A0840C72BE94AE02570615698 "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/wyyZ-oX4S2CRwBYCNiqZqA/zh-cn_image_0000002779406930.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=E801DC3C3CD9CCA367C2C6AAE2E78338C4AB226E3A256A54D09C42B72EE997D5) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/tuLh74m1RXinMge8Two8gQ/zh-cn_image_0000002779406942.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=DA7DE0CA8C002621D8CB62C0B0A1454B75771E8B3BBAA61E90E04269F15239A8) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/8SYjsHwVTQSowk8dIZsaYA/zh-cn_image_0000002779566908.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C47BEAA705DA229F8F0F41A664E180FA43F11E37D0F6F3138B14B462A8A54F1) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/1FSnvJwKSHGbsM-hFhSSWw/zh-cn_image_0000002808766513.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DD7E7820B394435C68DEB22AD022D5E97076D4BFF69CE434BE68E89F21D3104)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/B254ROhHTQuRsz3ebzLFlw/zh-cn_image_0000002808886577.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0E8C807677683038359995D719A84C3DF43D97DB16A3886AAF25DF5A6AF06122 "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/I66TekWGSyOZZc8Qq8DdbQ/zh-cn_image_0000002779566932.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=116F2BE8BE6FE07800F73D23CC0DBC59C68F7F8AA411BA61ED06037DE348005A "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     **说明** 

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/J1_PpKg6RbWlX0t4pAxbPA/zh-cn_image_0000002779566914.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=863246B08CF45BF1B0478F3BF511D639618AA284D9F740CCDFD6B78D1C3EC614 "点击放大")按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/mAoNCA6ZQY2cNxUyQIVJ6Q/zh-cn_image_0000002808886551.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCC65427E6347CEF0A534E2CAD6EF8417E2F768409BAB1CDE0AAAD15264F9B39 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/VbIsxZhQQEujv40KM6Y7XQ/zh-cn_image_0000002779566924.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=088E5E7E31D73A6DF1D1D9B57CCDBABEB5894F75F2C6764334627C55AF8C1DD7 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，Details区域中显示此时间段内指定类型的内存分析统计信息。
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/C6ozqVmrQ-6mQmPcMHFUpg/zh-cn_image_0000002808766469.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=40C027689B17F1E11E9E38F7BF5A969C7E45E06D95A0556C53EF2D3E7C0BE37E "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/mMpE-ZFYSlCkU8rTup3otg/zh-cn_image_0000002779406946.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CD0D27C0BE22513062AF60D6F7D222171E95CCC39AD243C2FD9830B7F79C994C "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/V0O7wuUWSjuIL_BXP8-Sdg/zh-cn_image_0000002779566902.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=071090DB32100834269AFF82D57873F6C8B3F4BCCC46361C2869B7D838787227 "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/XNvVI3sFR_yQvCN53AhnGQ/zh-cn_image_0000002779406956.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A891AF69A89577CACE4EC50EB2BCC83AC4BBB9496C3E3D1A841F7F227C22D03E "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics区域中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees区域显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。

       **说明** 

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/bt1W_auIRYCNhAU0fFFPbQ/zh-cn_image_0000002808766483.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=C56A906A5144939A72A19E02EF07C117CE961B452D8B55C5A0DF5728C9789D02 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。
