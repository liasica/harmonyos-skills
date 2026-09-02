---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-leak-in-develop
title: 开发态快速定位Native泄漏
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 开发态稳定性分析 > 资源泄漏类问题分析 > 开发态快速定位Native泄漏
category: best-practices
scraped_at: 2026-09-02T15:03:24+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:bcab7d7850a130c2aefdc45cc59ad06135174103d79fbe3cb7f61ba951b8f8dd
---

## 概述

Native内存泄漏是指在C/C++层（通过NDK或系统底层）分配的内存，由于未正确释放而导致的泄漏。本文将通过高频泄漏场景和Native内存泄漏分析案例，帮助开发者快速定位应用中的Native内存泄漏问题。

## 常见泄漏场景

**Native自身异常导致泄漏**

* 基础对象泄漏**：**使用malloc/new等手动分配堆内存后，因未调用free/delete、提前返回或指针丢失，导致内存无法回收。
* 循环引用**：**多个shared\_ptr或sptr之间相互持有形成环，导致引用计数无法归零，无法自动析构。
* 生命周期管理不当**：**通过系统接口申请的原生资源（如文件句柄、NativeWindow、相机会话、编解码器等）在使用完毕后未调用资源对应的释放接口，造成内核或系统服务资源泄漏。
* 过量缓存**：**为提升性能引入缓存，但未设上限或淘汰策略有缺陷，造成缓存内容持续增长，内存被长期无效占用。
* 业务过载（消费不及时）**：**生产者持续产生数据，而消费者因逻辑错误、阻塞或处理能力不足停止消费，导致缓冲队列无限积压，内存急剧膨胀。
* 业务过载（资源消耗极大）**：**业务一次性申请超大块内存，或同时持有多个高消耗资源（如高分辨率解码、模型纹理），超出设备可用内存上限。

**ArkTS引用导致Native泄漏**

* 跨语言导致泄漏：ArkTS对象通过NAPI持有Native对象，因Finalizer缺失、未实现或GC不可达导致Native对象永远无法释放。

## 标准化排查流程

主要排查Native泄漏的方式：使用Native Heap分析。Native Heap适合检测复杂泄漏模式（如生命周期管理不当，过量缓存等)，需结合调用栈和业务场景分析。

1. 复现与日志获取：使用DevEco Profiler的Allocation模板开启统计模式录制泄漏场景，重复多次操作疑似泄漏场景复现问题。
2. 识别泄漏点：点击Native Heap泳道，在下方详情Call Tree标签页中选择Created & Existing，查看内存占比较高的调用栈。
3. 分析调用栈：优先在调用栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。
4. 代码审查：结合调用栈，梳理相关代码中的内存持有逻辑，定位泄漏根因。
   * 业务逻辑无异常：则为ArkTS引用导致Native泄漏**，**参考[ArkTS内存泄漏分析案例](bpta-arkts-leak-in-develop.md#section1596252143114)。
   * 业务逻辑存在异常：修改相关代码。
5. 修复与验证：修改代码后，重复步骤1～2，确认内存曲线回归平稳。

使用Native Heap分析整体流程图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/N9OLLP_IT0mSn-S61KkosQ/zh-cn_image_0000002675100569.png "点击放大")

## Native内存泄漏分析案例

### 使用Native Heap分析

**案例背景**

**现象**：本案例中，通过反复操作复现问题场景，观察到应用Native Heap内存占用呈现“阶梯式持续增长”趋势。

**初步判断**：使用Allocation统计模式录制内存上涨过程，观察Memory泳道中的Native Heap曲线，呈现出典型的“阶梯式增长”，确认存在Native内存泄漏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/sKmWsID9Ri2eql_UNqD9Dw/zh-cn_image_0000002645100770.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Fe3y6WgATgqGy9tEMMVSqg/zh-cn_image_0000002644940868.png "点击放大")

**分析流程**

**步骤1：通过Allocation录制泄漏场景**

1. 基于DevEco Studio Profiler插件的Allocation模板分析堆内存分配、释放的信息，memory mapping信息，调用栈信息。这些信息中包括已释放内存和未释放内存。操作步骤如下：启动应用进程，选择Profiler工具 → 选择设备与应用进程 → 选择Allocation模板 → 创建Session → 配置录制选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/z3o1zn72TTSEuMlneGxfAw/zh-cn_image_0000002675100575.png "点击放大")

2. 开启统计模式，同时开启录制异步栈（方便追溯到业务代码）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/J1pTqzlpRAuZrxI9y0kEGg/zh-cn_image_0000002675020723.png "点击放大")

3. 点击按钮启动录制并复现问题场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/lNghfdpDQH2W8ipDfWQDqw/zh-cn_image_0000002645100772.png "点击放大")

**步骤2：查看内存分配栈**

1. 框选All Heap中的Native Heap子泳道。
2. 在下方详情区的“Statistics”页签中选择Created & Existing。
   * All Allocations：框选的时间段的所有分配内存信息。
   * Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
   * Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/7-o3o5YQTDCbaguQDVN3Yw/zh-cn_image_0000002644940870.png "点击放大")

3. 切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/CvPL9Cw8R_qHX1IJuLLrBg/zh-cn_image_0000002675100577.png "点击放大")

**步骤3：分析内存分配栈**

优先在内存分配栈信息中寻找占比较高且与业务代码强相关的Symbol Name，即Category中为亮色。根据调用栈分析相关代码（双击跳转源码），排查内存未释放原因。可以看到业务代码malloc中进行了缓存操作，但未添加free方法释放内存。

* Category中亮色代表开发者调用栈，其中绿色代表ArkTS栈帧，橙色代表Native栈帧；灰色代表系统调用栈。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/xHV-o1XgRLqUB1Uj3g-IVw/zh-cn_image_0000002675020725.png "点击放大")

### 优化修复

1. 修改代码增加free方法释放内存。
2. 重新运行应用，再次使用Allocation录制内存分配栈。
3. 重复多次操作泄漏场景。
4. 验证结果：
   * 内存曲线无明显上涨。
   * 泄漏问题已修复。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Iiq0ebZ0T_-QR9jwMuSXaQ/zh-cn_image_0000002645100774.png "点击放大")
