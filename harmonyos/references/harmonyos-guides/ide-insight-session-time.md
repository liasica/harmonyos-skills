---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time
title: 基础耗时：Time分析
breadcrumb: 指南 > 优化应用性能 > 基础耗时：Time分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:37+08:00
doc_updated_at: 2026-03-11
content_hash: sha256:6812bcf240cb305bd96cc15354592744b639fcb08c1e128be2df86da04c34474
---

## 函数耗时分析及优化

开发应用或元服务过程中，如果遇到卡顿、加载耗时等性能问题，开发者通常会关注相关函数执行的耗时情况。DevEco Profiler提供的Time场景分析任务，可在应用/元服务运行时，展示热点区域内基于CPU和进程耗时分析的调用栈情况，并提供跳转至相关代码的能力，使开发者更便捷地进行代码优化。

在设备连接完成后，可按照如下方法查看耗时分析结果：

1. 构建应用前请参考[模块级build-profile.json5文件](ide-hvigor-build-profile.md)，增加strip字段并赋值为false（strip：是否移除当前模块.so文件中的符号表、调试信息，配置为false代表不移除）。采集函数栈解析符号需要附带符号表信息，无符号表信息可能采集不到函数名称，或ArkTS Callstack泳道无法关联到Native调用栈，因此请按照下图进行配置。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/LIX-yDBOSbmhZeHpWIIb0g/zh-cn_image_0000002561833503.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=816E5750ED95216BA64E2D66C91DED128166EF42E3F2FCCA70C3A843E1485963)
2. 创建Time任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](deep-recording.md)。或在会话区选择**Open File**，导入历史数据。

   Time分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/AmopLOxkSzedBTOSLdmddA/zh-cn_image_0000002561833465.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=052FFA6A7F8366BF9DFBF599D27C78FC26925AA2FFBBD613E4C8D0E847E2428C)指定要录制的泳道：

   * **User Trace**：用户自定义打点泳道，基于时间轴展示当前时段内用户使用hiTraceMeter接口自定义的打点任务的具体运行情况。
   * **ArkTS Callstack**：方舟运行时函数调用泳道，基于时间轴展示CPU使用率和虚拟机的执行状态，以及当前调用栈名称和调用类型。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     调用栈分类从语言层面分为ArkTS、NAPI以及Native，从归属层面分为开发者代码以及系统代码。从这两个方面可以将调用栈类型归类如下：

     + ArkTS：程序正在执行ArkTS代码；
     + NAPI：程序正在执行的NAPI代码；
     + Native：程序正在执行的Native代码；

       其中每一个类型的亮色和灰色分别代表开发者和系统的代码。
   * **Callstack**：ArkTS和Native混合函数调用泳道。基于时间轴展示各线程的CPU使用率，以及在一段时间内的混合调用栈。调用栈类型会分为开发者或系统的ArkTS以及Native代码两类。由于隐私安全政策，已上架应用市场的应用不支持录制此泳道。

     Callstack基于采样模式采集数据，默认采样间隔是500微秒。耗时小于500微秒的函数，Details区域时间相关数据可能存在误差，可通过录制过程中多次触发该函数，根据其耗时百分比判断是否为热点函数。

   说明

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
   * 在任务分析窗口，可以通过“Ctrl+[ ”向前选中时间段的时间标签，通过“Ctrl+]”向后选中时间段的时间标签。
   * 将鼠标置于ArkTS Callstack泳道和Callstack泳道任意位置，可查看到对应时间点的CPU使用率。
   * 单击任意泳道名称后方的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/X0ERB2kCSWWnHrVyDez2Gw/zh-cn_image_0000002561833461.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=C653DD5E21A2DD8DB36333008FB2F59C24436420BBCB2548C00E89CA3ADA3428)可将其置顶。
   * Time分析支持Energy泳道，请参见[能耗诊断：Energy分析](ide-profiler-energy.md)。
3. 在“ArkTS Callstack”泳道和“ArkTS Callstack”子泳道上长按鼠标左键并拖拽，框选要分析的时间段。

   **Details**区域会显示所选时间段内的函数栈耗时分布情况，**Heaviest Stack**区域会展示出“Details”区域选择节点所处的耗时最长的完整调用栈。

   其中函数栈耗时分布有三种展现方式：

   * 默认为Call Tree方式，其中“Weight”字段表示当前函数的总执行时间，“Self”字段表示函数自身的执行时间，两者之差为当前函数所调用的子函数执行时间之和，“Average Duration”字段表示函数自身的平均执行时间，“Category”字段表示函数调用类型。
   * 打开页面下方的**Flame Chart**开关，函数调用栈将以火焰图的形式展示。其中，横轴表示函数的执行时长，纵轴表示调用栈的深度。

     说明

     + 火焰图条块支持搜索，搜索结果不匹配的条块会被置灰。
     + “Ctrl+鼠标滚轮”的操作，或单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/sfhOm9NnQFKA25Kbii_tCA/zh-cn_image_0000002530753564.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=CB2179E10B87D6874EBFA80DC1BAEED091A65B83EF7A39AA596E1F12AF2D6096)、![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/vD5jPbxCStGHAZuFEoGnUQ/zh-cn_image_0000002561833495.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=B8FC1BFEE2CE24EBF3ADD893A9D19CD09FF909A160960E54F461175EFECE5F65)可放大和缩小火焰图的时间轴比例，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/tFXQVduLSGejXk82zu2F0g/zh-cn_image_0000002530753552.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=848D6A59212084C21CC1F69361AE96D00607F1CA0C6F6837AE493D1C86AE506C)可恢复时间轴比例为初始状态。
     + “Shift+鼠标滚轮”的操作可左右横向调整可视区间，单独操作滚轮可上下纵向调整可视区间。
     + 选中节点，单击该区域右上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/fgoe-P0dQcmvA0vZrArpRQ/zh-cn_image_0000002561833459.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=4A75229265B5E2E4C36A335407133C7A272E11E8FA900DCC3AD1D2FDABBBCB7A)，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。
     + 在火焰图中选中任一节点，使用“Alt+鼠标左键”可将该节点左置底并将其占比放大到100%，其上从属节点按同比例放大显示。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/zy2FC_MbQmWg6yKW-eG4BA/zh-cn_image_0000002530753572.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=5CCAF2A811D2BD07B08121A0540B25BEEE9112A5841FD7FA855B8C091BDE9EE1 "点击放大")
   * 在“ArkTS Callstack”子泳道或“Callstack”子泳道上点击**Unfold CallStack**按钮，可以在时间轴上将函数调用栈以冰锥图的形式展示。其中调用栈的先后顺序与实际调用时序保持一致。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/mkE2AmnQTOCTJQQQ57xHfg/zh-cn_image_0000002530753560.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=C5C8E543E769F0E2EA3BCB88DE922155349AEE7E76C74131D1B0D6F7FE01A7D9 "点击放大")
4. 在**Callstack**泳道上长按鼠标左键并拖拽，框选要分析的时间段。
   * **Summary**列表展示框选时段内，所有Native线程的CPU占用率的峰值、谷值、平均值。
   * **Callstack**列表展示框选时段内，所有Native线程的函数热点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/kqo-JvAaTO6SVfgSPeLsow/zh-cn_image_0000002530753556.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=01813D01BE721C21E43FA516A955192BC65744FAD64F3CBBA030B8AAA81925CD "点击放大")

   * 悬浮到节点，显示以此节点为根节点，点击添加面包屑。添加面包屑后，该节点成为根节点，耗时占比为100%，子节点的耗时占比相对于该节点重新计算。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/bmbKQ83fQxSfe08HcH79Zg/zh-cn_image_0000002530753570.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=294EEF52DAAFF333216621E778F00AA11243BFF3AF543319E91E53A82622922A "点击放大")
5. 在**Callstack**子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段。
   * **Top Down**页签显示所选时间段内的函数栈耗时分布情况，**Heaviest Stack**区域会展示出“Details”区域选择节点所处的耗时最长的完整调用栈。
   * **Bottom UP**页签显示函数列表，展开任一函数节点可查看其调用方及每个调用方的耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/k7i2TOlERviXOtUkLLZ95w/zh-cn_image_0000002561833467.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=3CE6ECB6DC87FC16798CE599C2E6BA74BB250D0E7DE813BD70D19D1F88AD3D4E "点击放大")
6. （可选）在**Details**中双击需要优化的节点（例如耗时超过预期），可快速跳转至对应工程源码，为开发者节省定位代码路径的时间。

   说明

   * Release应用暂不支持跳转到用户侧Native代码。
   * 静态链接的系统库无法支持源码跳转。如libunwind.a，在编译过程中该系统库会以静态链接的方式集成。该系统库的符号信息在调用栈中会被识别成用户侧定义的函数，实际上无法跳转到源码。

## 多实例函数热点分析

在应用开发过程中，可能存在一些耗时操作，则需要引入Worker线程或者TaskPool任务池来协同处理。这些线程也可能会像主线程一样存在性能问题，所以需要同时对这些子线程进行性能调优。其中，主线程以及每一个Work线程或者TaskPool工作线程，都会对应一个方舟实例，通过连接这些方舟实例，开启性能采样，从而可以获取更全面的采样信息。

* 父泳道内可以看到被选择进程的CPU使用率，框选后展示此时段内录制到的所有方舟实例的函数调用栈信息。
* 子泳道框选后展示此时段内录制到的该方舟实例的函数调用栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/W3H2Nka1S8-5TfYFwm846g/zh-cn_image_0000002561753517.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=479E4825E4B7EF8387EDE3F6A344CF6C7401A591D3D16A32FF9C75B94E16AA39 "点击放大")

## 离线符号解析

DevEco Profiler提供离线符号解析能力，基于携带符号表信息的so库进行分析，可把符号地址解析为具体函数名称，便于定位函数位置。

对于有so库路径和偏移地址的采样数据，如图所示，通过导入对应的携带符号表信息的so库进行解析，补充release so库中缺失的符号表信息（包括系统so库，用户自编译的so库，三方库）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/7esYGNyySy6h2FyGQkNr_Q/zh-cn_image_0000002561833499.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=351AE5354FFCD409C1AF87F9EC21F6D1DD80862BD43958118AA02BEC8F19797C "点击放大")

您可以通过点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/5DK3E7MuSR6Vey3SPwVapw/zh-cn_image_0000002530753562.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=FB7E1686CD58525E9CF3C17FCF381737951B12F0C448ACC41735AA1F538A39D5)按钮，导入包含debug信息的so库。

说明

* 离线导入携带符号表信息的so库，需要严格保证与release版本的so库保持同一优化等级（如-O1, -O2, -O3等）。可以在CMakeLists.txt文件中查看或配置编译优化等级。
* 离线导入携带符号表信息的so库，需要尽可能与release版本的so库编译选项保持一致，防止so库起始地址不一致，影响解析正确性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/9yEF3KQMRk295cpz0R7Stg/zh-cn_image_0000002530753574.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=16D7F0F53D303D11CAAC24395725FBFC04745E2499EE7A22D37621DD773F9885 "点击放大")

## 查询自定义打点信息

相较于异步调度，DevEco Profiler当前基于采样分析的Time任务更善于分析同步性能问题。如开发者需要分析异步调度延时等问题，可先在ArkTS代码中进行自定义打点，当应用/元服务在Time分析过程中触发打点后，DevEco Profiler会将这些打点的Trace数据解析后，以任务方块形式呈现在“User Trace”泳道中。

您可以在“User Trace”子泳道上长按鼠标左键并拖拽，框选要展示分析的时间段，获取该时间段内的用户打点信息。

单击User Trace泳道的“options”下拉列表，可以设置是按照Task Name维度还是Thread ID维度显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/BLNfCXDsTDuctQMURQWW-A/zh-cn_image_0000002530753554.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=5F7B40DE142A3D33CC8F4F71CBC6E83BE892B87D3E3E469D23F9AA634BC1E337)

* Statistics页签：显示当前任务泳道在所选时间段内的打点任务统计信息，包括任务的名称、同一任务执行的次数、平均持续时长、最长持续时间和最短持续时间。通过这些统计信息，开发者可直观地了解打点任务的执行频率、持续时间偏差等，方便定位。
* User Trace页签：将所选时间段内的所有任务都一一列举出来，包括任务的ID、名称、起始/结束时间、持续时长等。

同时，您也可以单击“User Trace”子泳道中的任意一个任务块，“Details”区域将展示该任务块的详细信息。

说明

此外，用户自定义打点信息，还可以在Frame分析、Network分析任务中查看到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/lRXMAUIQQdazs4GS_Fr5ZQ/zh-cn_image_0000002530753566.png?HW-CC-KV=V1&HW-CC-Date=20260427T235735Z&HW-CC-Expire=86400&HW-CC-Sign=E4FC49C7140A50CA4C0E5A28F5CD9248AA6E9CE94021C443BEA535BE0F82BB6A "点击放大")
