---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory
title: 内存分析介绍
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础内存：Allocation分析 > 内存分析介绍
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5f6c496e5e0bbe7e11fb11a6b4960fff01ad02fe6cf032e98577bd57acafa514
---

## 操作步骤

### DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/8UPX6aLaSZaOfTi2e3Lhxw/zh-cn_image_0000002779566896.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=683089DC2A444B7FC9A12689D27CFF3D9E1E93BF5E7254BA39462D5ABF088DAE)
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/lveLxaSISRS9ZH5VmlNGfg/zh-cn_image_0000002779566934.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F42709C33B523B9C1694F988FD7988404BE3AB9BE3B8FE30B30F9708D82C070 "点击放大")指定要录制的泳道，或在会话区选择**Open File**，导入历史数据。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/sIObh4OSQiCC6sbae5_KDQ/zh-cn_image_0000002779566930.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EA3789F02C15EF0F5BF3AAF4651792265DE13A28ECB3977A5F202F8BD874BC3 "点击放大")

   **说明** 

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/r7v2ijEiRNGc6vp8sy7UPQ/zh-cn_image_0000002779566910.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=0058E6525A35D23CE3AD1A4EEF7424F088D3CCCF6A1D9E7148C6FDCC7B7DB5BA "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，计算方式为PSS+GL+Graph。PSS表示进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/TH3yFUYlTfm5fT_hHJk-wA/zh-cn_image_0000002808766495.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=C9FAF48B88AF92F0473F197881D3C64ED3A85E51153089AF04A2A4E87AFA51E1)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev、Stack、ArkWeb PA、JS Heap、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/GpwqSbTiS8WpLaSajRzu2w/zh-cn_image_0000002808886553.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D6B2EA688265AE8E9F519A7A10EF10E5EB1637C65875C01BBAD7C729749AEFD "点击放大")

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
   * **ArkTS Allocation泳道**：用于显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/y0z5W6pjSqyyJ-9AVqZ51A/zh-cn_image_0000002808886579.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=224AD929249274B8957F7A28B37A704FE99135DC8CC714B1D49CADFE031E9365 "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/nGOzk7_9TQ2027_fbglqvw/zh-cn_image_0000002779406928.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9C674A0BC3BC1241EAC115D994697545D02E0D9A4419AE7938C95C509F3793D "点击放大")
   * **All Heap & Anonymous VM泳道**：用于显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/7IHOJby8RqiadzAOj1Y6CQ/zh-cn_image_0000002808766497.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=65311C1ECF5398271EEB38ACF08874DFB6F2A1BFC24505024491DC2922416B75 "点击放大")按钮，可以设置是否为统计模式、回栈模式、JS回栈、JS回栈深度、Native回栈深度、开启异步栈缝合等，设置项的具体说明请参考下表。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/usjwTeG1Rxu83DR4qa42fg/zh-cn_image_0000002808886575.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB9F338AD83C5637285CC507653FAF7EC4BEFE69B2D0F01B01C9FB7600379EFE "点击放大")

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/L37Yb6QVQSGLnHbH9ce2vg/zh-cn_image_0000002779406936.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=907EE225FB643B16ED2132DB0313A57B49FD7B8114AF22DA39B9A89AC6C64A3D "点击放大")
   * **All Anonymous VM泳道**：用于显示匿名内存使用分布。展开主泳道，包括VM:ION、VM:ASHMem、VM:.so、VM:others四条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + VM:ION子泳道：用于显示DMA内存分配数据。
     + VM:ASHMem子泳道：用于显示匿名共享内存。
     + VM:.so子泳道：用于显示.so文件内存消耗。
     + VM:others子泳道：用于显示除ION、ASHMem、**.**so外的mmap类型数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/gFfCZZSjQK6pHtN_6yd75g/zh-cn_image_0000002779406952.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F666EE0985F86ABDF1A91234CA7B878919756E8E0C84F4340CBE8B29AC29CE86 "点击放大")
   * **System Resources泳道**：DevEco Studio 6.1.0 Beta2版本新增，用于显示进程的系统资源使用情况。展开主泳道，包括File Descriptors、Threads两条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + File Descriptors子泳道：用于显示进程的文件句柄使用情况。
     + Threads子泳道：用于显示进程的线程使用情况。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mhDPyW15TjarssA6SmeQRg/zh-cn_image_0000002808886549.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7537A37F7FCAB5BC921750B760773994C0105396E649ABF9719DEF6D5B83794F "点击放大")
   * **Graphic Memory泳道**：用于显示图形渲染相关的内存分配情况。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/CF1NXp2FQdu3UajhCkGGOQ/zh-cn_image_0000002779406950.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6CBBF6F50595CB1C2997981D497DAD14B15286D04F0E3E00A6A6C11E022F27B "点击放大")图标，勾选Graphic Memory泳道。展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。
     + Vulkan子泳道：用于显示GPU\_VK类型的内存分配数据。
     + OpenGL ES子泳道：用于显示GPU\_GLES类型的内存分配数据。
     + OpenCL子泳道：用于显示GPU\_CL类型的内存分配数据。

     **说明** 

     泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/-awhdH0RQpCyLvynwMnc0A/zh-cn_image_0000002808886585.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D07911ED838F7FC561791300210FB6B758621116B0C541AB29933DF929A830E3 "点击放大")
   * **Native Leaks泳道**：26.0.0版本新增，用于标记内存泄漏点，不包括纯系统栈泄漏点和无调用栈泄漏点。默认不展示该泳道，如需录制，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/MlLK4UaSSmWsbBpqWuwBdA/zh-cn_image_0000002779406926.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CE106851781009DA213704D97300C72F88279A91C34C5DC25E85F750E9222DB "点击放大")图标，勾选Native Leaks泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     **说明** 

     + 泳道录制时可选的设置项具体请参考[All Heap & Anonymous VM泳...](ide-insight-session-allocations-memory.md#li1060214731415)。
     + 设备系统要求：API 26.0.0及以上版本。
     + 26.0.0版本，Native Leaks泳道录制时，不支持开启设置中的Statistics Mode（统计模式）和Local Handle。在录制该泳道前，需要单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/9zIcvdGRTKG_wBPllUQT5A/zh-cn_image_0000002779406932.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC93DA6B960AC8FB6378A58B5DDC2D9D96478019D32C8B11E195E308CCA58549 "点击放大")按钮关闭Statistics Mode和Local Handle，否则影响正常录制。从26.0.1版本开始，Native Leaks泳道录制时，支持开启设置中的Statistics Mode（统计模式）。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/0PNjOmVeQ4WSY2GZ3HVymw/zh-cn_image_0000002779566926.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=244CBEA0E7DC3913D853B20D4E553E3DBB04A8C8188D052DD1F7480DAD7F51ED "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，查看此时间段内指定类型的内存分析统计信息。
   * **Memory泳道：**
     + **Statistics**区域：26.0.0版本新增，用于显示当前框选时间段内的虚拟内存区域数量的最小值（VMA Count Min）、虚拟内存区域数量的最大值（VMA Count Max）、虚拟内存区域数量的平均值（VMA Count Avg）、PSS内存最小值（PSS Min）、PSS内存最大值（PSS Max）、PSS内存平均值（PSS Avg），以及共享脏内存平均值（Shared Dirty Avg）、共享干净内存平均值（Shared Clean Avg）、私有脏内存平均值（Private Dirty Avg）、私有干净内存平均值（Private Clean Avg）、Swap内存平均值（Swap Avg）等。
     + **Details**区域：显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。包括时间戳、PSS内存大小、共享脏内存大小、共享干净内存大小、私有脏内存大小、私有干净内存大小、Swap内存大小、Swap PSS内存大小、VMA数量等。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RoYF3BLZQnimitIxalm7Dw/zh-cn_image_0000002779406940.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F67302141D5E99EFF341D2A4B9295A2565AA67B0A7C2FF92F026F98592C9673B "点击放大")
   * **Memory****子泳道**：**Details**区域中显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

     从26.0.1版本开始，FilePage Other、.so、.ttf、.hap类型子泳道的**Details**区域中新增Path列，用于显示各采样点PSS占比最大的文件路径。选中采样点，右侧**Path List**列表按PSS占比降序显示文件路径，最多显示10条，占比为0的文件路径不显示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/1GDTu72YRXq1ccnyq8UUGQ/zh-cn_image_0000002779406944.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0CF1ACFA7A4312C82C37EEB5C67738426A79704D67B9604BFBB6B9C7259D70D "点击放大")
   * **ArkTS Allocation泳道**：

     主泳道：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。

     子泳道：显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。

     Details区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/7QHk02z9S6CzEVWb-qwDdg/zh-cn_image_0000002808766467.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=04DF1E8B91C6AF63EAA37CFDA8B642743BB2A309EDA45A5EC383106F23B3B16D "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     **说明** 

     该泳道即将下线，推荐使用[Snapshot模板](ide-snapshot-basic-operations.md)分析ArkTS内存泄漏。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/8dZr4lGGSVmvVuD0VfcbgQ/zh-cn_image_0000002808886561.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B495B899B5D25C6442DD912E92153C9E373615F48BC5A8D6DF209956C4F8EE52 "点击放大")
   * **ArkTS Snapshot泳道**：在**Statistics**区域中点击任一对象后，右侧More区域**Native List**区域将展示引用该实例对象的Native堆栈信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/YRsKNEEbQf-YpyU9XjHx8A/zh-cn_image_0000002779566906.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E9C8181601ADB78A4862CAADB4E270DFFB0A88F36BBF1D7F3BDE52C30E61821 "点击放大")
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

       从26.0.0版本开始，点击右侧More区域中**Heaviest Stack**列表左侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/c_ePY_FiT1mgGhNg845KSA/zh-cn_image_0000002808766473.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=8D839093C1A87AD9AEE33AE76F4F7475EE5DBF2DA45EA7A224FCE294F0289984 "点击放大")按钮，将Heaviest Stack列表中的数据导出到本地进行保存。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/rj56I6yVTdmZSbrbJ2MRJw/zh-cn_image_0000002779406918.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=039FEE5CA9F3B50F302437835675EB934039BB0C8410DDE9259D27B1B1353B38 "点击放大")
     + **Allocations List**区域：显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       **说明** 

       - System Resources子泳道的Allocations List区域中不提供内存块起始地址、大小。
       - 统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/5znkUdJhRtypqlFJHw021g/zh-cn_image_0000002779406922.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A7339369044B21D2A56BC9FD125110D1E08ECF209CB7425EED4D964AB691A4D1 "点击放大")
   * **Native Leaks泳道**：框选或点选泄漏点后展示泄漏点的数据，包括Native泄漏对象名称、聚类后的总数、聚类后的总内存大小、单行栈帧的类型、内存分配栈等。

     **说明** 

     + 统计模式（Statistics Mode）开启后，Symbol Name不提供线程名信息。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/hfwrM2rsQHOMi0ViYjFlsQ/zh-cn_image_0000002808766471.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2518EE29E11CE7DADCBC03858FFBD05115E581F9909CA19F9EA29F745186A60 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。

### DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/SAmCNhTTRtSPEW7i86KsYQ/zh-cn_image_0000002779566892.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=60A7ABCA2504C87B0866726BF82CDDF9E89CFCACFD996E36AF0F24FEFD7521D4 "点击放大")
2. 创建Allocation分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)，或在会话区选择**Open File**，导入历史数据。在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/9Ekvwdr2QkisWqmXk2dpjA/zh-cn_image_0000002779406934.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6B90DE22FCC9F6D72062464D0BB7228430E7F6D05534728A69000650967981E1 "点击放大")指定要录制的泳道。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/TVs1n7s7RkSqTDfGsi3f5Q/zh-cn_image_0000002808886557.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=702FE55BE19E943745A74DDFCFF95C9BFF8B19BD2D8C4B991F82953C71E29533 "点击放大")

   **说明** 

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点时间标签，通过“Ctrl+. ”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段时间标签，通过“Ctrl+]”向后选中时间段时间标签。
   * Allocation分析支持离线符号解析能力，请参见[离线符号解析](ide-insight-session-time.md#section186881175012)。
   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/dyTLeKQsTuiJYJS1IIbcIQ/zh-cn_image_0000002779566920.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A413AFA6CAD8101289104709241D10D7D9A17A8939A6ADB475D8896F52E20BB2 "点击放大")可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   * **Memory泳道**：显示当前进程的物理内存使用情况，其度量方式包含：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/R84rCpQyTemXZIz1-QVreg/zh-cn_image_0000002779406930.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7FC672BE78C964F954A6D14A4B56C448B5EA661301365600CF8D89413162BE1B) PSS：进程独占内存和按比例分配共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/VS71mNTZSamgfgP_gX5ebw/zh-cn_image_0000002779406942.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=0C5100E50A22826CA28EAF1A41A446090C4EB3DB46800DAB6804FAD9D2C77418) RSS：进程独占内存和相关共享库占用内存之和。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/7kzg23INRuG4Tm31ksCyHQ/zh-cn_image_0000002779566908.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2397994B0C2E9B6A0A71E7236AE0EF1973518419E3D2DFEF29AEAA65102EFE70) USS：进程独占内存。

     默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/KOdDWK7mTKm3zsSZ7p705Q/zh-cn_image_0000002808766513.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=8E86140E96A4C4CECCFC698AE3486205FCDCCCE23E37639118B545A83F0C6B81)

     展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，类型包含ArkTS Heap/Native Heap/GL/Graph/Guard/AnonPage Other/FilePage Other/Dev/Stack/.hap/.so/.ttf。默认展示其中的五个子泳道，如要显示其他子泳道，可以点击主泳道的options标签并勾选其他泳道来查看。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/jeTzUaLWTBCE60lWqQVieg/zh-cn_image_0000002808886577.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F954AF49CBD812238757A1407C8410779F290CA279D5909337EF5116D9990B9E "点击放大")

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
   * **ArkTS Allocation泳道**：显示方舟虚拟机上的内存分配信息。该泳道默认不展示，如需录制该泳道数据，在录制前单击左上角菜单栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/e_TBZAKqTMqKntONRDdfWw/zh-cn_image_0000002779566932.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E87616524A5EB75CFA279F5D46EEB3D325BE4A305C889FA026B2EB6D0B98458 "点击放大")图标，勾选ArkTS Allocation泳道。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     **说明** 

     由于较大的性能开销可能导致卡顿/卡死问题，暂不支持同时录制ArkTS Allocation和Native Allocation两条泳道，以及ArkTS Allocation和Graphic Memory两条泳道。
   * **Native Allocation泳道**：显示具体的Native内存分配情况，包括静态统计数据、分配栈、每层函数栈消耗的Native内存等信息。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/xCCx9xKyRa2cs23xJdKTNQ/zh-cn_image_0000002779566914.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=33D76937B2247AAAF1CD8B1906F4E8522B8E4067298A558A64F8B1E737148E86 "点击放大")按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/8HemgsT7Qu2LfHaVEaTEhg/zh-cn_image_0000002808886551.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B18E622996937AD99036757692D26DCE4AFA66B8B0A3F5E028A64BFB95E934C7 "点击放大")
   * **Graphic Memory泳道**：DevEco Studio 6.0.2 Beta1版本新增，显示图形渲染相关的内存分配情况。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU\_VK类型的内存分配数据，OpenGL ES子泳道对应GPU\_GLES类型的内存分配数据，OpenCL子泳道对应GPU\_CL类型的内存分配数据。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/H3D019eIQwifbq01TyUevQ/zh-cn_image_0000002779566924.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5E8250CEC608FF6E083A9614830277B25D68488852530D39E3E43DB71D2BAF6 "点击放大")
3. 在目标泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，Details区域中显示此时间段内指定类型的内存分析统计信息。
   * **Memory泳道**：
     + 主泳道的详情区域显示当前框选时间段内各采样点的应用内存PSS总和，以及各种内存页面状态的内存占用总和。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/jPkpBbwQRWK8HYvUhH5pEg/zh-cn_image_0000002808766469.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=57CBC4916996D551742440625A325E9973FF75C1DA24542D8969034B00F13E94 "点击放大")
     + 子泳道的详情区域显示该泳道所代表的内存类型的框选时间段内各采样点的PSS总和以及各种内存页面状态的实际占用情况。

       **须知** 

       Graph字段统计方式为：计算/proc/process\_dmabuf\_info节点下该进程使用的内存大小。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/uxHGlEYsQe-Y79DQpJMJag/zh-cn_image_0000002779406946.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2C341D046383FC34B2525E70B8DFDF5E5C207E646DAD907DAA293094E91F1333 "点击放大")
   * **ArkTS Allocation泳道**：显示被选择进程所使用的所有ArkTS内存总和，框选后展示此时段内录制到的所有方舟实例的对象分配信息。框选子泳道后显示当前框选时段内运行对象的内存使用情况，包括层级、对象自身内存大小、对象关联内存大小等。该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

     “Details”区域中带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/Iwts-XcXTXqQfipdsQt_iQ/zh-cn_image_0000002779566902.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3BDF11F8803C88EDF2351F81692337884815762DEFF4E5EFD90B12AFCC985E1 "点击放大")标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/EUgE87RcR86V7QCimVl11A/zh-cn_image_0000002779406956.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=970E2831BE4C8EC8C0AD99168495BF579A5F302215817DB3BA006D8B631DF412 "点击放大")
   * **Native Allocation或Graphic Memory泳道**：框选子泳道后显示具体的内存分配，包括静态统计数据、分配栈等。
     + Statistics区域中显示该段时间内的静态分配情况，包括分配方式（Malloc或Mmap）、总分配内存大小、总分配次数、尚未释放的内存大小、尚未释放次数、已释放的内存大小、已释放次数。

       点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。
     + Call Trees区域显示线程的内存分配栈情况，包括函数地址或符号、分配大小、占比以及函数栈帧的类别等。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。
     + Allocations List显示内存分配的详细信息，包括内存块起始地址、时间戳、当前活动状态、大小、调用的库、调用库的具体函数、事件类型（与Statistics区域的分配方式对应）等。

       **说明** 

       统计模式（Statistics Mode）开启后，不存在Allocations List信息。

       选择任一对象，右侧会展示与该对象相关的所有库和调用者。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/WOM3nVC9TsCDd-mxcft20A/zh-cn_image_0000002808766483.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=3B105DC9CDEEFDF87DE6330D7DC4A4D2019DF0019B5899C06DB0DC4C8AA21E44 "点击放大")
4. （可选）根据分析结果，双击可能存在问题的调用栈，跳转至相关代码。开发者可根据实际需要进行优化。

   **说明** 

   Release应用暂不支持跳转到用户侧Native代码。
