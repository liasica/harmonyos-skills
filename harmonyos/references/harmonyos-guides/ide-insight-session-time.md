---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time
title: 基础耗时：Time分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 基础耗时：Time分析
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:37+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b87a4665b947347d5c6c5271d9d2d4104fe5859e435c4e9b7ef0e3b1339a0470
---

## 功能介绍

开发应用或元服务过程中，如果遇到卡顿、加载耗时等性能问题，开发者通常会关注相关函数执行的耗时情况。DevEco Profiler提供的Time场景分析任务，可在应用/元服务运行时，展示热点区域内基于CPU和进程耗时分析的调用栈情况，并提供跳转至相关代码的能力，使开发者更便捷地进行代码优化。

Time模板支持的泳道包括：User Trace、ArkTS Callstack、Callstack、Energy。本文介绍User Trace、ArkTS Callstack、Callstack泳道，Energy泳道的详细信息请参考[能耗诊断：Energy分析](ide-profiler-energy.md)。

## 函数耗时分析及优化

在设备连接完成后，可按照如下方法查看耗时分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，或ArkTS Callstack泳道无法关联到Native调用栈，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/yL06Gd4hQF-jZujOgznVzA/zh-cn_image_0000002808887125.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC0D7A332525740605096B8AA7BB15527523F17AD5BBCD46E3F4AF3A1D57DFD6)
2. 创建Time任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。Time分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/qKAqVFJ6STmkSrHfG9iB9w/zh-cn_image_0000002808887109.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C6E62A42D24CF1942EA5912224E93F2EC97F51480D9DE73C2FAB87308406B2F "点击放大")指定要录制的泳道：
   * **User Trace**：用户自定义打点泳道，基于时间轴展示当前时段内用户使用hiTraceMeter接口自定义的打点任务的具体运行情况。
   * **ArkTS Callstack**：方舟运行时函数调用泳道，基于时间轴展示CPU使用率和虚拟机的执行状态，以及当前调用栈名称和调用类型。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     调用栈分类从语言层面分为ArkTS、NAPI以及Native，从归属层面分为开发者代码以及系统代码。从这两个方面可以将调用栈类型归类如下：

     + ArkTS：程序正在执行ArkTS代码；
     + NAPI：程序正在执行的NAPI代码；
     + Native：程序正在执行的Native代码；

       其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
   * **Callstack**：ArkTS和Native混合函数调用泳道。基于时间轴展示各线程的CPU使用率，以及在一段时间内的混合调用栈。调用栈类型会分为开发者或系统的ArkTS以及Native代码两类。由于隐私安全政策，已上架应用市场并且[app.json5配置文件](app-configuration-file.md#配置文件标签)中profileable设置为false的应用，不支持录制此泳道。

     Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。

   **说明** 

   * 单击任意泳道名称后方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/rtIaEqfHQkyXrVIY7vUjJw/zh-cn_image_0000002779407470.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB2BF85267F16C4BBFE61630E56330B8982A9BA37D739258288D47390FED7988 "点击放大")可将其置顶。
   * Release版本的so库构建时，默认优化等级为-O2，编译器会对代码进行函数内联、寄存器分配、指令重排等优化，可能导致函数调用栈缺失、局部变量被优化、运行时序与源码不一致，从而造成录制数据不完整。可以在CMakeLists.txt中配置编译优化等级为-O0，采集完整的数据。
3. 在**ArkTS Callstack****泳道**和**ArkTS Callstack****子泳道**上长按鼠标左键并拖拽，框选要分析的时间段。**Details**区域会显示所选时间段内的函数栈耗时分布情况，**Heaviest Stack**区域会展示出Details区域选择节点所处的耗时最长的完整调用栈。函数栈耗时分布有三种展现方式：调用树（默认展示方式）、火焰图、冰锥图。
   1. 在调用树中，“Weight”字段表示当前函数的总执行时间，“Self”字段表示函数自身的执行时间，两者之差为当前函数所调用的子函数执行时间之和，“Average Duration”字段表示函数自身的平均执行时间，“Category”字段表示函数调用类型。
   2. 打开页面下方的Flame Chart开关，函数调用栈将以火焰图的形式展示，横轴表示函数的执行时长，纵轴表示调用栈的深度。

      **说明** 

      * 火焰图条块支持搜索，搜索结果不匹配的条块会被置灰。
      * “Ctrl+鼠标滚轮”的操作，或单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/CiNFRIVeSCaGqt6oVdBRxQ/zh-cn_image_0000002779567450.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=B34D9CD1B679D56762592899886E93C3909E0BEC14CE42D2141E1FA79587B826)、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/Q5eyZp1lSvmx51X_c3niBw/zh-cn_image_0000002808767043.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=871B31BB129583315369083BE1C9305B1B386E03C99C9872B510C5426FCFAB2F)可放大和缩小火焰图的时间轴比例，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/9TPpzV-9QnesM3HXL_fkTQ/zh-cn_image_0000002779567456.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=330FE255DBCE42B5366A7C1A2E21C9318E2DA3ACE4ECA4B6B3AF7E2C750A5B3E)可恢复时间轴比例为初始状态。
      * “Shift+鼠标滚轮”的操作可左右横向调整可视区间，单独操作滚轮可上下纵向调整可视区间。
      * 选中节点，单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/L_L-UNxBR3yVp-MEmPIdgw/zh-cn_image_0000002779407472.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=11F401B2227D30C8158CD0CFB6F47111C009FE716E43B0B9569153EDF7E3E8DF "点击放大")，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。
      * 在火焰图中选中任一节点，使用“Alt+鼠标左键”可将该节点左置底并将其占比放大到100%，其上从属节点按同比例放大显示。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/yASd-H6dRfGa585EDdBM2w/zh-cn_image_0000002808887119.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A09417F106C30FD52222020CDA461FCC50DD4A00919FC82D35C7E1A3BDF0AAB "点击放大")
   3. 在ArkTS Callstack子泳道或Callstack子泳道上点击**Unfold CallStack**按钮，可以在泳道图区域将函数调用栈以冰锥图的形式展示，调用栈的先后顺序与实际调用时序保持一致。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/dSaZVzcmRouyQ70BlcagiA/zh-cn_image_0000002808767027.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=C91E70432C5F17A6EBE1A3745224DD1950C8778D4DF60858B9EB45C413FD443B "点击放大")
4. 在**Callstack**泳道上长按鼠标左键并拖拽，框选要分析的时间段。
   * **Summary**区域展示框选时段内，所有Native线程的CPU占用率的峰值、谷值、平均值。
   * **Callstack**区域展示框选时段内，所有Native线程的函数热点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/65TVkIegQlad6SdBmuVw7Q/zh-cn_image_0000002808767037.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7CC96F6F652131167E80BC7B7F023F0BA079847D4DF5F04087032DA48CBA0C83 "点击放大")
   * 将鼠标悬浮到节点，显示以此节点为根节点，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/uy9fPhS6TxaPsZg7N74k4A/zh-cn_image_0000002808887121.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EDEB98FC76F3C4C1A6B9C05974261DAF52174B8A8EF9D46B724C7B5F55ED177 "点击放大")
5. 在**Callstack**子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。
   * **Top Down**页签显示所选时间段内的函数栈耗时分布情况，**Heaviest Stack**区域会展示出Details区域选择节点所处的耗时最长的完整调用栈。
   * **Bottom UP**页签显示函数列表，展开任一函数节点可查看其调用方及每个调用方的耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/CbqRAWyLRVy9roVXgoYAQw/zh-cn_image_0000002779567448.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B28FE003417D8135E1C809CC85222A22A6B7620BF28369A498C50C51DFEE584 "点击放大")
6. （可选）在**详情区**中双击需要优化的节点（例如耗时超过预期），可快速跳转至对应工程源码，为开发者节省定位代码路径的时间。

   **说明** 

   * Release应用暂不支持跳转到用户侧Native代码。
   * 静态链接的系统库无法支持源码跳转。如libunwind.a，在编译过程中该系统库会以静态链接的方式集成。该系统库的符号信息在调用栈中会被识别成用户侧定义的函数，实际上无法跳转到源码。

## 多实例函数热点分析

在应用开发过程中，可能存在一些耗时操作，则需要引入Worker线程或者TaskPool任务池来协同处理。这些线程也可能会像主线程一样存在性能问题，所以需要同时对这些子线程进行性能调优。其中，主线程以及每一个Work线程或者TaskPool工作线程，都会对应一个方舟实例，通过连接这些方舟实例，开启性能采样，从而可以获取更全面的采样信息。

* **ArkTS Callstack**父泳道内可以看到被选择进程的CPU使用率，框选后展示此时段内录制到的所有方舟实例的函数调用栈信息。
* **ArkTS Callstack**子泳道框选后展示此时段内录制到的该方舟实例的函数调用栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/E4yJJ2lvSYenriQOq0Zi8g/zh-cn_image_0000002808887123.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=F18CFEC6504B870553692C2243250B55B8AA64200795F4DE4976E6F45222C3D9 "点击放大")

## 离线符号解析

DevEco Profiler提供离线符号解析能力，基于携带符号表信息的so库进行分析，可把符号地址解析为具体函数名称，便于定位函数位置。

对于有so库路径和偏移地址的采样数据，如图所示，通过导入对应的携带符号表信息的so库进行解析，补充release so库中缺失的符号表信息（包括系统so库，用户自编译的so库，三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/3c3ZfvulTT-xUf2ZAiUFYw/zh-cn_image_0000002808767041.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=87BBCD20CC922E034B3ABC7890BCCCDCFAF1DEB1F9A48948B361E0674364BECB "点击放大")

您可以通过点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/q07e0oCxSTC3A8JHKg26qg/zh-cn_image_0000002779407476.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBBA34B58F8EF6B987C8E9BFB84C242C7BFFB57039FE905989F7D1F12D81EB57 "点击放大")按钮，导入包含debug信息的so库。

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与Release版本的so库保持同一优化等级（如-O1, -O2, -O3等）。可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与Release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_YoC3b4uRUC2gfE1TEjT3w/zh-cn_image_0000002808767039.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A303E8242EAA63C3EE08191C9D24493D4F5944483A33C50872522597083877FB "点击放大")

## 查询自定义打点信息

相较于异步调度，DevEco Profiler当前基于采样分析的Time任务更善于分析同步性能问题。如开发者需要分析异步调度延时等问题，可先在ArkTS代码中进行自定义打点，当应用/元服务在Time分析过程中触发打点后，DevEco Profiler会将这些打点的Trace数据解析后，以任务方块形式呈现在**User Trace**泳道中。

单击User Trace泳道的“options”下拉列表，可以设置子泳道是按照Task Name维度还是Thread ID维度显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/0rlJQu_bTgCtis54CdIorw/zh-cn_image_0000002808767029.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=7C9A556500BFE1FB13F803055337DC0EB12A504D3F0D00826423991512693BBF)

展开**User Trace**泳道，在子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，获取该时间段内的用户打点信息。

* **Statistics**区域：显示当前任务泳道在所选时间段内的打点任务统计信息，包括任务的名称、同一任务执行的次数、平均持续时长、最长持续时间和最短持续时间。通过这些统计信息，开发者可直观地了解打点任务的执行频率、持续时间偏差等，方便定位。
* **User Trace**区域：将所选时间段内的所有任务都一一列举出来，包括任务的ID、名称、起始/结束时间、持续时长等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/GSTMvAWJSaKVQ4NRVBVqIw/zh-cn_image_0000002808767033.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=A65CE2A6DB8F314BB09408F4C6B1A72BAC5E6B884A9A2446AA5DB1FABE987746 "点击放大")

单击**User Trace**子泳道中的任意一个任务块，**Details**区域将展示该任务块的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/hKQSHXd-Rc-0wIk8yo1gKA/zh-cn_image_0000002779407474.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E5303AB1EA1F8CAF447C18AB56376FAB0E1F6DF04D8AF2F090287675FCA4DF1 "点击放大")
