---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-memory-manage-and-optimization
title: 应用内存优化
breadcrumb: 指南 > 应用体验建议 > 应用系统资源管理体验建议 > 系统内存使用与优化 > 应用内存优化
category: harmonyos-guides
scraped_at: 2026-11-28T10:35:01+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:97999e814bbb7faa7bf6e86b1cf795917066839f1e29f1cb21006b958f37f090
---

## 内存泄漏分析

在鸿蒙应用开发中，内存泄漏是影响性能和稳定性的关键问题。为帮助开发者系统化治理内存泄漏，最佳实践文档从开发态与运维态两个阶段，分别针对ArkTS（JS/TS）、Native（C/C++）等典型泄漏场景，提供了一整套定位、监控与闭环修复方案。开发态侧重于利用DevEco Studio Profiler等工具主动探查根因，运维态可使用应用质量管理（Application Performance Management Service，简称APMS）平台实现线上泄漏的告警、聚类和证据链追溯。

参考文档：

[开发态稳定性分析-资源泄漏类问题分析](../doccenter-app-quality/bpta-analysis-of-resource-leak-in-develop.md)

[运维态稳定性分析-资源泄漏类问题分析](../doccenter-app-quality/bpta-analysis-of-resource-leak-in-operation.md)

## 内存优化方法

鸿蒙应用优化方案按技术方向分为以下几类：

* 编译态优化
* ArkWeb优化
* ArkUI优化
* ImageKnifePro三方库优化

### 编译态优化

应用在C++代码编译时，选用对内存/存储较有优势的编译选项。

优化案例：某应用liblauncher.so，采用如下表格中方案1、3、5选项，so大小从220M优化到132M，进程内存收益30M。

|  |  |  |  |
| --- | --- | --- | --- |
| 方案编号 | 编译选项/手段 | 作用 | 备注 |
| 1 | -ffunction-sections -fdata-sections  -Wl,-gc-sections | 让每个函数/每个全局数据符号作为独立的section，链接器对未被使用的非导出的符号进行删除。 | 无。 |
| 2 | -Oz/-Os | 相比-O3/-O2，让编译器进行更进一步的code size优化。 | 可能造成性能劣化。 |
| 3 | -fvisibility=hidden  -fvisibility-inlines-hidden | 所有未显式声明为公开的符号（如函数、变量等）以及内联类成员函数都会被标记为隐藏的，减少产物中符号段大小。 | 无。 |
| 4 | -fno-rtti | 禁用C++的RTTI机制。 | 用户不能使用C++的RTTI机制，如dynamic\_cast。 |
| 5 | -fno-exceptions | 禁用C++的异常机制。 | 用户不能使用C++的异常机制，如try-catch、throw。 |
| 6 | -Wl,-z,pack-relative-relocs / -Wl,--pack-dyn-relocs=relr | 使用relr编码格式压缩动态重定位段。 | 无。 |
| 7 | -Wl,--hash-style=gnu | 为动态符号表仅生成gnu扩展的哈希表。 | 无。 |
| 8 | -Wl,-icf=all | 在链接阶段对相似代码片段进行合并处理。 | 可能造成性能劣化。 |
| 9 | -moutline | 在编译阶段对相似代码片段进行合并处理。 | 仅aarch64/arm支持，可能造成性能劣化。 |
| 10 | -mllvm -inline-threshold={数值} | 设置编译器inline优化时，最大可inline的函数成本阈值。 | 可能造成性能劣化。 |
| 11 | 在libc++.so中显式实例化STL模板 | 避免在每个动态库中都存在STL模板的实例化副本。 | 可能造成性能劣化。 |

### ArkWeb优化

**Web离线组件及时设置非活跃**

问题场景：应用使用Web离线组件进行预加载预渲染，每个组件在Active状态下占用2至5块DMA Buffer，用于渲染管线Buffer轮转。

优化方案：离线组件设置active状态后会进行绘制，在渲染完成后设置为Inactive状态，此时Web内核内存优化方案会清理至1块buffer。应用监听页面渲染完成回调后调用onInactive接口。

* 调用onInactive示例代码：

```screen
build() {
         Column() {
                   Web({ src: 'www.example.com', controller: this.controller })
                            .onPageBegin(() => {
                                     this.controller.onActive();
                            })
                            .onFirstMeaningfulPaint(() => {
                                     this.controller.onInactive();
                            })
         }
}
```

参考文档：

[@performance/web-on-active-check](ide-web-on-active-check.md)

**减少Web离线组件使用数量**

问题场景：离线Web组件的作用是预加载预渲染，可以提升进入特定页面的性能，但过度使用离线Web组件会带来巨大的内存开销。创建Web组件将占用内存（每个Web组件大约200MB）和计算资源，建议避免一次性创建大量离线Web组件，以减少资源消耗。

优化方案：减少Web离线组件的使用数量。

* 释放Web离线组件示例代码

```screen
export const recycleWeb = (url: ResourceStr, force: boolean = false): boolean => {
         console.info('recycleWeb, url: ' + url);
         let baseNode = nodeMap.get(url);
         if (!baseNode) {
                   console.info('no such node, url= ' + url);
                   return false;
         }
         if (force && baseNode.isBound()) {
                   console.info('the node is in bound and not force, can not delete');
                   return false;
         }
         baseNode.rootNode?.dispose();
         baseNode.rebuild();
         nodeMap.delete(url);
         recycledWebs.add(url);
         return true;
}
```

参考文档：

[使用离线Web组件](web-offline-mode.md)

**应用退后台释放离线Web组件**

问题场景：应用在前台时通过离线Web组件实现特定页面的预加载预渲染，但在应用后台时未对离线Web组件进行释放，仍占用大量内存。

优化方案：应用在退到后台前释放并销毁所有的离线Web组件并记录，在应用回到前台时基于后台记录重建恢复离线Web组件。

* 应用后台释放离线组件前台重建示例代码：

```screen
onForeground(): void {
         // Ability has brought to foreground
         hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
         restoreNWebS();
}
 
onBackground(): void {
         // Ability has back to background
         hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
         recycleNWebS();
}
```

* 退后台销毁并记录离线Web组件：

```screen
export const recycleNWebS = (url: ResourceStr, force: boolean = false): boolean => {
         console.info('recycleNWeb, url = ' + url);
         let baseNode = nodeMap.get(url);
         if (!baseNode) {
                   console.info('no such node, url = ' + url);
                   return false;
         }
         if (force && baseNode.isBound()) {
                   console.info('the node is in bound and not force, can not delete');
                   return false;
         }
         baseNode.rootNode?.dispose();
         baseNode.rebuild();
         nodeMap.delete(url);
         recycledNWebs.add(url);
         return true;
}
```

* 回前台重新创建恢复离线Web组件：

```screen
export const restoreNWebS = (uicontext: UIContext | undefined) => {
         if (!uicontext) {
                   uicontext = globalUIContext;
         }
         for (let url of recycledNWebs) {
                   if (uicontext) {
                            createNWeb(url, uicontext);
                   }
         }
         recycledNWebs.clear();
}
```

参考文档：

[使用离线Web组件](web-offline-mode.md)

### ArkUI之Navigation优化

**Navigation栈深度限制配置**

问题场景：应用使用Navigation组件进行页面导航时，系统对页面栈深度不做限制，应用如果不做控制，可能造成用户使用时栈内存无限增长导致溢出，尤其在低内存设备上更容易出现内存不足的问题。

优化方案：通过Navigation的configuration接口配置stackSizeLimit属性，限制页面栈的最大深度。当栈深度超过限制时，最早的页面节点将按FIFO（先进先出）顺序自动销毁，同时保留NavPathInfo，以支持页面重建。

* 配置stackSizeLimit示例代码：

```screen
build() {
  Navigation(this.navStack) {
    // 首页内容
  }
  .configuration({
    stackSizeLimit: 10  
  })
}
```

说明：

- stackSizeLimit <= 0：不限制栈深度（默认值）。

- stackSizeLimit > 0：限制栈深度为指定值，超出时自动销毁最早入栈的页面。

参考文档：

[导航与切换-Navigation](../doccenter-references/api/ts-basic-components-navigation.md#configuration)

### 使用ImageKnifePro及优化

**升级到ImageKnifePro**

ImageKnifePro是ImageKnife的升级版本，95%的接口保持兼容，个别差异点进行了单独说明。建议将ImageKnife升级到ImageKnifePro。

参考文档：

[@ohos/imageknifepro(V1.0.13-beta.0)](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fimageknifepro/v/1.0.13-beta.0)

**退后台内存主动回收**

应用退后台时，清理掉所有隐藏页面的图片内存。对当前页面UI树进行遍历，保留屏幕范围内的组件，清除在屏幕外组件的图片内存。应用返回前台时，重新加载被清理的图片，优先加载当前页面的图片。

应用退后台后，在EntryAbility::onBackground()触发调用ImageKnife.getInstance().clearOnBackground()；应用从后台返回前台，在EntryAbility::onForeground()触发调用ImageKnife.getInstance().reloadOnForeground()。

参考文档：

<https://gitcode.com/CPF-ApplicationTPC/imageknifepro/pull/199>

<https://gitcode.com/CPF-ApplicationTPC/imageknifepro/pull/212>

**GIF逐帧解码方案**

ImageKnifePro提供了三种动图解码模式，针对GIF等多帧图片的加载进行了优化。通过合理选择解码模式，建议使用逐帧解码，可大幅节省内存。

参考文档：

<https://gitcode.com/CPF-ApplicationTPC/imageknifepro>

**图片降采样方案**

ImageKnifePro提供了11种图片降采样策略，建议应用根据场景使用FIT\_CENTER\_MEMORY/FIT\_CENTER\_QUALITY：

* FIT\_CENTER\_MEMORY：适用图片列表、缩略图场景。
* FIT\_CENTER\_QUALITY：详情页大图场景。

参考文档：

<https://gitcode.com/CPF-ApplicationTPC/imageknifepro>

**修改setCacheLimit内存缓存的大小**

ImageKnife默认缓存大小128M，可根据自身使用图片场景修改为指定大小。调用方式为ImageKnife.getInstance().setCacheLimit(CacheStrategy.Memory, 128, 64 \* 1024 \* 1024)，其中第一个参数设置内存缓存，第二个参数设置缓存的最大图片张数，第三个参数设置内存缓存的使用量上限（建议50M以内）。

ImageKnife ArkTS版本通过initMemoryCache接口修改内存缓存大小。

|  |  |  |  |
| --- | --- | --- | --- |
| 分档 | 场景 | 优化设置 | 预估收益（M） |
| 档位1 | 缓存大小设置>128M | 设置成128M | 设置的缓存大小-128M |
| 档位2 | 缓存大小设置=128M | 设置成100M | 28M |
| 档位3 | 缓存大小设置<128M | 不变 | 无 |

## 内存防劣化检测方法

内存劣化检测包含两类问题：1、内存泄漏故障检测，及时检测与发现内存泄漏故障，并修复，降低内存占用；2、场景内存峰值检测，对比基线及时识别内存使用的合理性，抑制应用场景内存不必要的过快增长。

根据内存防劣化的检测阶段不同，可分为开发态检测和应用集成检测。开发态内存自测（范围明确，场景聚焦，效果好，成本低），开发人员及时针对新增修改场景覆盖，提前发现并修复泄漏故障，观测场景内存峰值是否正常。通过DevEco Studio上提供的DevEco Profiler，进行内存峰值监控，allocations等模板进行内存泳道监控，提前识别内存峰值异常和泄漏故障。开发态下的内存泄漏检测工具包括：leaks、globalhandle、localhandle、jsleakwatcher等。应用集成内存检测（集成验证，范围不明确，问题发现、修复成本高），测试或者质量管控人员，对应用整体集成测试，覆盖应用核心业务场景、辅助遍历场景用例，补充发现内存泄漏及使用不合理的问题。

DevEco Testing内存泄漏检测工具：

* ArkTS泄漏，集成开发态ArkTS泄漏检测工具（localhandle，jsleakwatcher）
* Kernel、Native、KMP泄漏，内存申请调用栈趋势检测，识别泄漏故障
* 无脚本自动识别风险路径并通过压测激发发现泄漏
