---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-develop
title: 开发态快速定位Native泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位Native泄漏
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:f656e63c6e9ef0325a629bb01ca4675f36abad0a3366d802320c3b40cb8ebfa5
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/aylvNYD0TNmXkh8IwEvOpQ/zh-cn_image_0000002747227797.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=628EF60DE2732B2415930DD440DAEAFF669D0D024C903E4F12FA650DC3FC0716 "点击放大")

## Native内存泄漏分析案例

### 使用Native Leaks分析

**案例背景**

现象：本案例中，有个场景存在内存泄漏：多次反复操作，应用内存占用持续上涨。

初步判断：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Native Heap曲线，呈现出典型的“阶梯式增长”，确认存在Native内存泄漏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/xiPwY0vCTOmo9b4P7vFjIw/zh-cn_image_0000002717617758.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=3834971D112082B05B0501EBD13959194AA6C5AA3A66B56C84599D943579F895 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/4cYC6rUcSJGD60O3wvN8Sw/zh-cn_image_0000002747297713.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A0B511B7E52F4EDED14AD80E8759D50E2B186DAA23F371E8715A243F9FE118A "点击放大")

### 分析流程

1. 通过Native Leaks录制泄漏内存对象

   1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/X15_qxp4TB6VWkl85rPfjw/zh-cn_image_0000002747217627.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D26D50B2A2902C35F16DBCFB5283058DAE6DF44525EC86AF86A65325441BD34 "点击放大")

   2. 录制Native Leaks需要关闭统计模式，同时开启录制异步栈（便于追溯到业务代码）。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/aBav-cs3SOGfRJ_14z0PdA/zh-cn_image_0000002717777682.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=E0478B295D9E626A4324666704700DBA6C191E34F0DFFFC63BC857DA1EE3EE29 "点击放大")

   3. 点击按钮启动录制并复现问题场景。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/yEySlQYnS3WREcyZCGRjXQ/zh-cn_image_0000002717617762.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=AFAE0E6F9B5E4C8C0DE6B6F38E603EEA87329F7213BD175CE23F9BC8447B03ED "点击放大")
2. 查看泄漏对象
   1. 查看Native Leaks泳道，泳道中“X”表示检测点存在泄漏对象。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/o3TST-vlRrqANyEqQa3VwA/zh-cn_image_0000002747297715.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=FFD9F608949EA5BA2FAF2F0C680A7D7FC3A30AFAD9B9A34EC15792CCC403B608 "点击放大")
   2. 点击“X”，底部详情区域点击任意一行调用栈帧，查看泄漏对象详情。Symbol Name显示格式：线程名（内存地址）。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Elo8afvxRk6DhGwMVdgwig/zh-cn_image_0000002747217629.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B445856D962EE31CE9DD8EDD8484F910ADBA56E6DB32EBCE5E9AE96229A7355 "点击放大")
3. 分析泄漏对象调用栈

   根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码malloc中进行了缓存操作，但未添加free方法释放内存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/6oOlBLAIR5iYNXbXFMhzPA/zh-cn_image_0000002717777684.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=D38BEF86B82C0E6CB4213BD1D48FF06F5D15D855A255E935132B4952A48D0AF4 "点击放大")

### 优化修复

1. 修改代码增加free方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复多次操作泄漏场景。
4. 验证结果：
   * 内存曲线无明显上涨，每次退出后回落至基线。
   * Native Leaks未检测到异常泄漏对象，泄露问题已修复。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/zXwrkgiAT82Udns-NKgF0Q/zh-cn_image_0000002717617764.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=295E687DA50BC1E845808AE2240E7574A522922456F55E8514AB0368C6E60416 "点击放大")

### 使用Native Heap分析

**案例背景**

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Native Heap内存占用呈现“阶梯式持续增长”趋势。

**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Native Heap曲线，呈现出典型的“阶梯式增长”，确认存在Native内存泄漏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/tj26fKtQRSWl_2A_znJhSA/zh-cn_image_0000002645100770.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=4E47BB955ED6BE7E5941AAD8B13406E12D00B4DE9913435079B7782498FAD09B "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/R9GKuZv3R32H34DH-inyCw/zh-cn_image_0000002644940868.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFA911FB796CF25E9BDF765035E75B368D7D334B21F0C8233DD0BA7B3595C9FE "点击放大")

**分析流程**

**步骤1：通过Allocation录制泄漏场景**

1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/dF_BYVtJRlimkYvvsdF3zg/zh-cn_image_0000002675100575.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A49E51E3B11F5755E29400B442A26D9D8604AEE76D0B7B413E12D89639C8DD2 "点击放大")

2. 开启统计模式，同时开启录制异步栈（方便追溯到业务代码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/q_OAeC0DRreA7aywlQmBoA/zh-cn_image_0000002675020723.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=C491D66C4E1A257B6C4CF33071F17A58671F97F4E91CA1B128E87CB497B737D9 "点击放大")

3. 点击按钮启动录制并复现问题场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/AERIa6HEQbSdtMnYrr6igw/zh-cn_image_0000002645100772.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=A693CDEE91E2E0A3AA9845016011A0E96D37D576C81192CCD958639BC297FC50 "点击放大")

**步骤2：查看内存分配栈**

1. 框选All Heap中的Native Heap子泳道。
2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Fuc9YIkmRualqlLwegY_UQ/zh-cn_image_0000002644940870.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=57A0F03D9E71EEFF1E4DD70732B9CFA174743786B214EEFB2A5CDE28756A5147 "点击放大")

3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/NziHhmCNQHClXHxwAZbezA/zh-cn_image_0000002675100577.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4B00AD8325F41F4146C4714B42EB698F23BC09BB7907A67BBB282AF8B6A55C4 "点击放大")

**步骤3：分析内存分配栈**

优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码malloc中进行了缓存操作，但未添加free方法释放内存。

* Category中亮色代表开发者调用栈，其中绿色代表ArkTS栈帧，橙色代表Native栈帧；灰色代表系统调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Whh1oVIqRcWkHmVe13cxwQ/zh-cn_image_0000002675020725.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C1FAA57CBB6DE07F7949F360A13FFCDBB47769342E2CB06BE6D9E4E3303F9C5 "点击放大")

### 优化修复

1. 修改代码增加free方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复多次操作泄漏场景。
4. 验证结果：
   * 内存曲线无明显上涨。
   * 泄漏问题已修复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/iM3x6SeBS5mlZkdhNgybYw/zh-cn_image_0000002645100774.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E6AA456E89B3B95CBCB92276482B9D6AB9590D3F1FD186A05ED746D59040C8B "点击放大")
