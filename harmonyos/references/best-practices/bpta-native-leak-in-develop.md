---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-develop
title: 开发态快速定位Native泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位Native泄漏
category: best-practices
scraped_at: 2026-11-24T12:47:58+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:bbc389be235866fa2aa792b688551d7218f5e3f6ef54e2ad0ac990c6cd13953e
---

## 概述

Native内存泄漏是指在C/C++层（通过NDK或系统底层）分配的内存，由于未正确释放而导致的泄漏。本文将通过高频泄漏场景和Native内存泄漏分析案例，帮助开发者快速定位应用中的Native内存泄漏问题。

## 常见泄漏场景

**Native自身异常导致泄漏**

* 基础对象泄漏：使用malloc/new等手动分配堆内存后，因未调用free/delete、提前返回或指针丢失，导致内存无法回收。
* 循环引用：多个shared\_ptr或sptr之间相互持有形成环，导致引用计数无法归零，无法自动析构。
* 生命周期管理不当：通过系统接口申请的原生资源（如文件句柄、NativeWindow、相机会话、编解码器等）在使用完毕后未调用资源对应的释放接口，造成内核或系统服务资源泄漏。
* 过量缓存：为提升性能引入缓存，但未设上限或淘汰策略有缺陷，造成缓存内容持续增长，内存被长期无效占用。
* 业务过载（消费不及时）：生产者持续产生数据，而消费者因逻辑错误、阻塞或处理能力不足停止消费，导致缓冲队列无限积压，内存急剧膨胀。
* 业务过载（资源消耗极大）：业务一次性申请超大块内存，或同时持有多个高消耗资源（如高分辨率解码、模型纹理），超出设备可用内存上限。

**ArkTS引用导致Native泄漏**

* 跨语言导致泄漏：ArkTS对象通过NAPI持有Native对象，因Finalizer缺失、未实现或GC不可达导致Native对象永远无法释放。

## 标准化排查流程

主要有以下两种排查Native泄漏的方式：使用Native Leaks分析和使用Native Heap分析。

* Native Leaks适合检测明确的内存泄漏点（如基础对象泄漏等），可以直接定位到代码位置。部分场景可能检测不到泄漏点。
* Native Heap适合检测复杂泄漏模式（如生命周期管理不当，过量缓存等），需结合调用栈和业务场景分析。

建议优先使用Native Leaks分析，如未检测到泄漏点，则使用Native Heap结合调用栈进行分析。

### 使用Native Leaks分析

1. 复现与日志获取：使用DevEco Studio Profiler的Allocation模板关闭统计模式录制泄漏场景，重复操作多次以复现疑似泄漏问题。
2. 分析泄漏对象：在Native Leaks泳道中定位异常存活的对象。
   * Native Leaks泳道检测到泄漏点：点击查看泄漏对象，分析泄漏对象的调用栈。
   * Native Leaks泳道未检测到泄漏点：参考使用Native Heap分析。
3. 分析调用栈：根据泄漏对象的调用栈，跳转至对应代码调用函数，锁定异常调用点。
4. 代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。
   * 业务逻辑无异常：则为ArkTS引用导致Native泄漏，参考[ArkTS内存泄漏分析案例](bpta-arkts-leak-in-develop.md#section1596252143114)。
   * 业务逻辑存在异常：修改相关代码。
5. 修复与验证：修改代码后，重复步骤1～2，确认原异常对象不再存活，内存恢复正常且无新增泄漏。

### 使用Native Heap分析

1. 复现与日志获取：使用DevEco Studio Profiler的Allocation模板开启统计模式录制泄漏场景，重复多次操作疑似泄漏场景复现问题。
2. 识别泄漏点：点击Native Heap泳道，在下方详情Call Tree标签页中选择Created & Existing，查看内存占比较高的调用栈。
3. 分析调用栈：优先在调用栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。
4. 代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。
   * 业务逻辑无异常：则为ArkTS引用导致Native泄漏，参考[ArkTS内存泄漏分析案例](bpta-arkts-leak-in-develop.md#section1596252143114)。
   * 业务逻辑存在异常：修改相关代码。
5. 修复与验证：修改代码后，重复步骤1～2，确认内存曲线回归平稳。

分析整体流程图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/19Xfbj11TYiCCpwresAALg/zh-cn_image_0000002747227797.jpg?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=27E36EAB093B8C52E052944E798182167E907726046481592345E7273419FB95 "点击放大")

## Native内存泄漏分析案例

### 使用Native Leaks分析

**案例背景**

现象：本案例中，有个场景存在内存泄漏：多次反复操作，应用内存占用持续上涨。

初步判断：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Native Heap曲线，呈现出典型的“阶梯式增长”，确认存在Native内存泄漏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/kYguKT91TmWKHvjSrWsydg/zh-cn_image_0000002717617758.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=00B36BE7A1B8F1CB63661312A25C28579303D6D658AC0007124DF798D0276B8A "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/3PeH1cvMQJKt9q9zds8FuQ/zh-cn_image_0000002747297713.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4065E64A3670D6A99CFA141A237D98D5FDB828826F1AA2E4000A2C653DBEC7B "点击放大")

### 分析流程

1. 通过Native Leaks录制泄漏内存对象

   1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/EwflnTCHTquEe_lotGGQpA/zh-cn_image_0000002747217627.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=07D51F09804C866CC883B4066EDFCBBC6A528F319BAACB2A37C5E9D82AB3729C "点击放大")

   2. 录制Native Leaks需要关闭统计模式，同时开启录制异步栈（便于追溯到业务代码）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/7MC-xIGkQzq-acweJPWjow/zh-cn_image_0000002717777682.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=CE85CEBE9F79AACE74EBA8CC3F4B315CDFD65889BB0E84BFFBEAB76A8124B81E "点击放大")

   3. 点击按钮启动录制并复现问题场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/af_0vOnpRX-KFxo3TqgTZg/zh-cn_image_0000002717617762.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFE533A9BF8678F7B0AA8265D3F46BA3724D424B131350F11DD5D27BD9C61F9F "点击放大")
2. 查看泄漏对象
   1. 查看Native Leaks泳道，泳道中“X”表示检测点存在泄漏对象。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dVE-Vh4iR9Wqjd5xgdtOKw/zh-cn_image_0000002747297715.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=DC89387AAE78BFE73BB556F692FDE06EBE5635A84906E7CC653617F94890502E "点击放大")
   2. 点击“X”，底部详情区域点击任意一行调用栈帧，查看泄漏对象详情。Symbol Name显示格式：线程名（内存地址）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/kCEGf3ANR6aoiJ2cFWyQ5A/zh-cn_image_0000002747217629.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=B07318AB107526F5449517DDF62651F0D41891ECB688ABBD7B97016ADC246A06 "点击放大")
3. 分析泄漏对象调用栈

   根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码malloc中进行了缓存操作，但未添加free方法释放内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/BGWBIewORCW1xPBm7DXNvQ/zh-cn_image_0000002717777684.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=21EC8877D89CC2DBF90DA8DBF05B714CBB523B98E87DD5C8105C11CF42D6F926 "点击放大")

### 优化修复

1. 修改代码增加free方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复多次操作泄漏场景。
4. 验证结果：
   * 内存曲线无明显上涨，每次退出后回落至基线。
   * Native Leaks未检测到异常泄漏对象，泄露问题已修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/-_pjus5lT2q7Yv9DB1_KyQ/zh-cn_image_0000002717617764.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A664CCA954DCBA79E730EC1BE11A3FE73F61425809EAF971ACBD21079CF47335 "点击放大")

### 使用Native Heap分析

**案例背景**

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Native Heap内存占用呈现“阶梯式持续增长”趋势。

**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Native Heap曲线，呈现出典型的“阶梯式增长”，确认存在Native内存泄漏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/u1J62TgmSXKZ6HhUW9cXMg/zh-cn_image_0000002645100770.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=09AFC9F2660EBA82FB64EE286CC6A3C8DCA4821ED9808B719BA84CA76580E3A8 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/qptuKyFnSV651OVTN0LEqw/zh-cn_image_0000002644940868.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=91495AEAA1391067AB84FEE952156348D3FB1B57349CBBD63E01A3EECEB4C798 "点击放大")

**分析流程**

**步骤1：通过Allocation录制泄漏场景**

1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GlW8Q2vBQUClSThYMOejOA/zh-cn_image_0000002675100575.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=A55E5A2B882D0BA020B0BEA2105C448E5A56F5F8ECD612566CFB6AF331017C47 "点击放大")

2. 开启统计模式，同时开启录制异步栈（方便追溯到业务代码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/UJ65zGARTRutBt2M32J1qQ/zh-cn_image_0000002675020723.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=F7105C46E85521F526C1CA3D8ABEF251F1FE924FCEB65D3365884CD7AC3B6518 "点击放大")

3. 点击按钮启动录制并复现问题场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/RCUf4iFDSauIHLBY0h1z3Q/zh-cn_image_0000002645100772.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C19C63AF7DDDA8D244E88365E0DF47D8736F96DE1E5C016CFEEAFBDE871A746D "点击放大")

**步骤2：查看内存分配栈**

1. 框选All Heap中的Native Heap子泳道。
2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/EhMXpQcQQ56AnM8sP4PSSw/zh-cn_image_0000002644940870.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=C177E94065BD5E97C1212A36237F6F07C6C51973107C577CC9DF95552DD2BB81 "点击放大")

3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/74dAo8lJT5mURJjEKaMloQ/zh-cn_image_0000002675100577.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D737BA5B2346345D516326628C5C179FF37525B2DD2107D1B0B5504710C7FE7 "点击放大")

**步骤3：分析内存分配栈**

优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码malloc中进行了缓存操作，但未添加free方法释放内存。

* Category中亮色代表开发者调用栈，其中绿色代表ArkTS栈帧，橙色代表Native栈帧；灰色代表系统调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/D9yYcqUKT3ePyjUHljX66A/zh-cn_image_0000002675020725.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=9C67B602E0A19A01A6EE34317FEAC33E9171EE76B774512DF0DB03D16050A5F5 "点击放大")

### 优化修复

1. 修改代码增加free方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复多次操作泄漏场景。
4. 验证结果：
   * 内存曲线无明显上涨。
   * 泄漏问题已修复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/X2B-qwAAT2KskZH1Zfll3w/zh-cn_image_0000002645100774.png?HW-CC-KV=V1&HW-CC-Date=20261124T044758Z&HW-CC-Expire=31536000000&HW-CC-Sign=340E9CA05B49A838334B6D59B303B29BAA51E11D08095AF378A86A1D0C426296 "点击放大")
