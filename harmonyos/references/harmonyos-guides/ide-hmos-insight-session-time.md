---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-insight-session-time
title: 基础耗时分析：Time分析
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 优化应用性能 > 基础耗时分析：Time分析
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:0f4124da8b0d6e4cff94c4af2c62488d98b4e969ea5c540d404c78940c576081
---

## 功能介绍

开发应用或元服务过程中，如果遇到卡顿、加载耗时等性能问题，开发者通常会关注相关函数执行的耗时情况。DevEco Profiler提供的Time场景分析任务，可在应用/元服务运行时，展示热点区域内基于CPU和进程耗时分析的调用栈情况。

Time模板支持的泳道包括：User Trace、Callstack。

## 函数耗时分析及优化

在设备连接完成后，可按照如下方法查看耗时分析结果：

1. 构建应用前请参考模块级[build-profile.json5文件](ide-hmos-hvigor-build-profile.md)，增加strip字段并赋值为false，不移除当前模块.so文件中的符号表、调试信息。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/0aK-DAvITauY5W9YuL7KPg/zh-cn_image_0000002781471070.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=EC06E8142AFE52D308E7545C6D450A624601116EA8F531D741C7BBBCA7CD0EF0)
2. 创建Time任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](ide-hmos-deep-recording.md)，或在会话区点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/nW1b0T0AQoWB_MjJaLXDKA/zh-cn_image_0000002810630621.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A2FF95E8A5D285A377BEB243A96B892D4C0143AB48A20C13C21B312D18023F9)图标，导入历史数据。在录制前单击录制按钮旁![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/wkzm9EU3R2SUBs9jZFu4Ww/zh-cn_image_0000002810630627.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C436617DF671B910C526E1BCE54D16EBB2A63C9A0735382D322EB62DD524D61)按钮，点击**录制设置**指定要录制的泳道。
   * **User Trace**：用户自定义打点泳道，基于时间轴展示当前时段内用户使用hiTraceMeter接口自定义的打点任务的具体运行情况。
   * **Callstack**：ArkTS和Native混合函数调用泳道。基于时间轴展示各线程的CPU使用率，以及在一段时间内的混合调用栈。调用栈类型会分为开发者或系统的ArkTS以及Native代码两类。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。

   **说明** 

   * 将鼠标置于泳道任意位置，可查看到对应时间点的CPU使用率。
   * 单击任意泳道名称后方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/VNEMNxU_R9WPq7_Oo-FIXA/zh-cn_image_0000002810630625.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7A2DFC2CF96FCB99FAEB7D4B068ACF7F0AE5262BFACD5D854F2242FF36C0D6E "点击放大")可将其置顶。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/0C1WMU48TR-1L3QQZ5hiqg/zh-cn_image_0000002781471068.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D81217A53E64BD8C97841ABB6F563E5C68F112C074E9F47B12E21446B4820BD "点击放大")
3. 在**Callstack**子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。**Details**区域会显示所选时间段内的函数栈耗时分布情况，**Heaviest Stack**区域会展示出**Details**区域选择节点所处的耗时最长的完整调用栈。函数栈耗时分布有两种展现方式：调用树（默认展示方式）、火焰图。
   * 在调用树中，“Weight”字段表示当前函数的总执行时间，“Self”字段表示函数自身的执行时间，两者之差为当前函数所调用的子函数执行时间之和，“Average Duration”字段表示函数自身的平均执行时间，“Category”字段表示函数调用类型。
   * 打开页面上方的**火焰图**开关，函数调用栈将以火焰图的形式展示。其中，横轴表示函数的执行时长，纵轴表示调用栈的深度。

     **说明** 

     + 火焰图条块支持搜索，搜索结果不匹配的条块会被置灰。
     + “Ctrl+鼠标滚轮”的操作，或单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/z-HnzW1QT0SfT4K2AHbHtQ/zh-cn_image_0000002810750723.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B6870377C4135B18D2DB85A6841604D1C5725A9652CE29F7FC312296CED8F18 "点击放大")、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/pmer1L-HT7avM11WGfORVw/zh-cn_image_0000002810750729.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=4582DBCFFC3C38D6A7BBBE047E7E94BC66177B71D44F4C79CD2A7509D971B6EC "点击放大")可放大和缩小火焰图的时间轴比例，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/BxTm64CZRbK9KRpMQptipA/zh-cn_image_0000002781471062.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E12F42278FEFA583DA20A50366EAA84B17A62BD7A9DD26315A9057FA78CB738 "点击放大")可恢复时间轴比例为初始状态。
     + “Shift+鼠标滚轮”的操作可左右横向调整可视区间，单独操作滚轮可上下纵向调整可视区间。
     + 选中节点，单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/WvkmA7OmRAWValTRlDlnqQ/zh-cn_image_0000002810630619.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B9C0291830B769BAC4ED8DC7CFEF41055BCDE24DECA3D65D57582810302109A "点击放大")，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。
     + 在火焰图中选中任一节点，使用“Alt+左键”可将该节点左置底并将其占比放大到100%，其上从属节点按同比例放大显示。该快捷操作同样适用于列表方式，用于将指定节点置顶并截取所属下级节点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CCreOvl6RN-BL0lVaMk1Fw/zh-cn_image_0000002781471064.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9F3F05CB8A5468BDFDC731391254D5C40CC8F85268AAC5AB509BB7F12A854359 "点击放大")
4. 在**Callstack**泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。
   * **Summary**列表展示框选时段内，所有Native线程的CPU占用率的峰值、谷值、平均值。
   * **Callstack**列表展示框选时段内，所有Native线程的函数热点。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/3yiSn7rhSKOsxmrY_OV7hA/zh-cn_image_0000002810750727.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B536C61BA9216323FE9FDFF215B03F8DE252714B82248ACBBAC1A9C617A829F "点击放大")
   * 悬浮到节点，显示以此节点为根按钮，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/nubuyXr6S_ShuPAaeblq-g/zh-cn_image_0000002810750733.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=50D9B0D7C0CC9FB5122266041E57919FCB2E062E68A9D28E7ABDFC10D9E9775E "点击放大")

## 离线符号分析

DevEco Profiler提供离线符号解析能力，基于携带符号表信息的so库进行分析，可把符号地址解析为具体函数名称，便于定位函数位置。

对于有so库路径和偏移地址的采样数据，如图所示，通过导入对应的携带符号表信息的so库进行解析，补充release so库中缺失的符号表信息（包括系统so库，用户自编译的so库，三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/EaFk1GiZTTS23X6ebsPUDQ/zh-cn_image_0000002781311130.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB0235250A9BFE0DF0E29E08D7C863B8A7243D1A714517A6AC5E28F4D82BEF37 "点击放大")

您可以通过点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/OLCYTU04R_Orp6MzobgFbQ/zh-cn_image_0000002810750731.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=422514F62236826818ED4F049960B53AF965F13BEDFAF76477DB303FCCBBA822 "点击放大")按钮，导入包含debug信息的so库。

**说明** 

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等）。可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/353NCwMXTwSYXUrGrhpWFw/zh-cn_image_0000002810630617.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9467D308123CBC087D4B1597D0F6D2C8D29B49BB486BA44284C1D2ECBB3117B "点击放大")

## 查询自定义打点信息

相较于异步调度，DevEco Profiler当前基于采样分析的Time任务更善于分析同步性能问题。如开发者需要分析异步调度延时等问题，可先在ArkTS代码中进行自定义打点，当元服务/应用在Time分析过程中触发打点后，DevEco Profiler会将这些打点的Trace数据解析后，以任务方块形式呈现在“User Trace”泳道中。

单击**User Trace**泳道的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/3Qce2pjfRx6Tp1EuyZc1lA/zh-cn_image_0000002810630623.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A9C36151FE537EE25919D2F330B53BCD0738CECC0D517E3B44D1E6C0B182D27 "点击放大")图标下拉列表，可以设置子泳道是按照Task Name维度还是Thread ID维度显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/KJSrKnujSna6B51wSPBM5Q/zh-cn_image_0000002781311138.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBBF6B65FB9C764FDA3FACF9020706A41F5F8C4769A3850EDFA4E44FECE90135 "点击放大")

在**User Trace**子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，获取该时间段内的用户打点信息。

* **Statistics**页签：显示当前任务泳道在所选时间段内的打点任务统计信息，包括任务的名称、同一任务执行的次数、平均持续时长、最长持续时间和最短持续时间。通过这些统计信息，开发者可直观地了解打点任务的执行频率、持续时间偏差等，方便定位。
* **User Trace**页签：将所选时间段内的所有任务都一一列举出来，包括任务的名称、ID、起始/结束时间、持续时长等。

单击**User Trace**子泳道中的任意一个任务块，**Details**区域将展示该任务块的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/kCrHZ4RmTS-HiL4xYECSvw/zh-cn_image_0000002781311142.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B9AA80B2E05D5E40ADFE80EA30CF31078A08FD502E681735BBBF8232919A7F2 "点击放大")
