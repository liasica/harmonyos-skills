---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-arkts-vmroot-mode
title: VMRoot类型内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkTS内存泄漏故障模式说明 > VMRoot类型内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-04T06:33:24+08:00
doc_updated_at: 2026-09-03
content_hash: sha256:76b933020144b37379ec02e2c4c95c09929df455e4d0d5cb79f0a508f4558913
---

## 概述

本文旨在指导HarmonyOS应用开发者定位VMRoot类型的ArkTS内存泄漏问题。若泄漏对象的根节点为VMRoot类型，即可确认为此类问题。

## 根因描述

系统侧创建的VMRoot类型根节点会持有应用在进程中创建的ArkTS对象。ArkTS引擎管理该类根节点，垃圾回收机制（GC）无法回收对应内存，从而引发内存泄漏。具体场景如下：

* SourceTextModule持有：当模块级变量（如export导出的对象）持有ArkTS对象导致其无法释放时，即为SourceTextModule持有导致的内存泄漏。
* GlobalObject持有：当全局变量（如globalThis挂载的对象）持有ArkTS对象导致其无法释放时，即为GlobalObject持有导致的内存泄漏。

## 问题分析思路

### 分析步骤

根据内存泄漏分析方法查看内存快照文件：

1. 确认泄漏对象：定位内存占用大的泄漏对象，查看其引用链，找到距离（Distance）为1的根节点。
2. 判断故障模式：若根节点是SourceTextModule对象，确认为模块级变量持有导致的泄漏；若根节点是GlobalEnv或GlobalObject对象，确认为全局变量持有导致的泄漏。
3. 梳理引用链：当根节点为VMRoot类型时，持有的对象无法释放。检查引用链中各对象的NodeId（快照中对象@符号后的数字）是否发生变化，若NodeId发生变化，说明该对象在重复创建。
4. 追溯业务代码：结合代码分析，尝试断开重复创建对象与复用对象间的引用关系，释放重复创建的对象。

### 模块级对象持有泄漏

在应用运行时，当开发者使用export将对象暴露，系统侧名为NameDictionary的ArkInternalArray对象会直接持有该对象。由于NameDictionary是系统侧SourceTextModule的属性，因此export导出的对象将一直无法释放。

系统侧创建SourceTextModule，用于管理模块级对象，其生命周期为全局，每个SourceTextModule对应一个ts文件，其关键属性如下：

* EcmaModuleRecordName：记录export导出的对象所在文件的名称。
* EcmaModuleFileName：记录所在abc文件名。
* NameDictionary：记录运行时export导出变量值的集合。
* LocalExportEntries：记录编译abc文件时的export声明。

SourceTextModule在内存快照中的属性如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/Nr1Xl3KATpW3XkkvP9QBAw/zh-cn_image_0000002699865074.png)

export导致泄漏的常见场景如下：

1. 直接导出集合对象：array、map、list等集合对象直接export导出后无法释放，若业务在该集合中添加对象后未删除，将导致泄漏内存不断上涨。
2. 间接引用集合对象：模块级对象间接引用array、map、list等集合对象（中间可能存在多层引用），若业务在该集合中添加对象后未删除，将导致泄漏内存不断上涨。
3. 无限累积对象：在应用设计时尝试保留大量对象在模块级对象中，但未做数量和大小限制处理，也未做超时释放逻辑。

### 全局对象持有泄漏

全局对象泄漏根因为GlobalEnv或GlobalObject直接或间接持有大量ArkTS对象，垃圾回收（GC）机制无法释放该对象。

在堆快照中，GlobalEnv是独立的堆对象且作为根节点存在，GlobalObject则是GlobalEnv的成员。globalThis和GlobalObject在内存快照中通常指向同一个对象，因此使用globalThis挂载对象时，在内存快照中GlobalObject持有该对象。

GlobalEnv或GlobalObject导致泄漏的常见场景：

1. 直接持有集合对象：GlobalEnv/GlobalObject直接持有array、map、list等集合对象无法释放，业务在该集合中添加对象后未删除，导致泄漏内存不断上涨。
2. 间接持有集合对象：GlobalEnv/GlobalObject间接持有array、map、list等集合对象（中间可能存在多层引用），业务在该集合中添加对象后未删除，导致泄漏内存不断上涨。
3. 不必要的全局化：开发者设定对象为全局后，其他模块未使用该对象，导致不必要的对象变为全局对象，致使全局对象内存超出必要值。
4. 缺乏限制逻辑：在应用设计时尝试保留大量对象在全局对象中，既未做数量和大小限制，也未做超时释放逻辑。

### 关键字

在Heap Snapshot快照文件中找到以下关键字：

* SourceTextModule：系统侧创建SourceTextModule，用于管理模块级对象。在生成Heap Snapshot时，模块级对象由SourceTextModule持有，开发者可据此确认泄漏对象问题类型。
* GlobalObject：系统侧创建GlobalObject，用于管理全局对象。在生成Heap Snapshot时，全局对象由GlobalObject持有，开发者可据此确认泄漏对象问题类型。

## 运维态故障案例分析思路

### 模块级对象持有泄漏案例

**问题现象**

开发者单击应用“SourceTextModule memory leak”按钮，触发应用进程OOM闪退，系统生成jscrash日志和rawheap二进制快照文件。

**代码示例**

代码中ModuleHoldMain()函数申请300MB对象存放进数组baseArray，其中baseArray为export对象。前端按钮在单击后调用问题ModuleHoldMain()函数申请内存，然后申请300MB超大内存确保触发OOM崩溃。代码如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/t6Um1Fi5TeSPwYXPysHJ5A/zh-cn_image_0000002729584405.png "点击放大")

**问题分析思路**

1. 参考[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)，在应用崩溃后获取崩溃日志，查看崩溃日志中的Reason字段为OutOfMemory，明确应用进程崩溃原因是OOM故障。

2. 参考[运维态内存快照获取方法](bpta-overview-of-arkts-memory-leaks-overview.md#section16548548153614)，获取OOM生成的rawheap快照文件，将快照导入到DevEco Studio查看。从快照文件发现NodeId为154217的JSArray对象存放在NodeId为49439的JSArray中，而该JSArray对象的根节点是SourceTextModule，SourceTextModule无法释放。内存快照如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/4Bp_fsrGTGaHlXQlH_5JiA/zh-cn_image_0000002699705186.png "点击放大")

3. 分析引用链，发现模块级对象NodeId为49439的JSArray没有重复创建，但是JSArray中存放的其他JSArray对象在重复创建，需要主动断开两者间的引用关系。

**问题结论与总结**

SourceTextModule持有export的baseArray数组无法自动释放，而该数组中保存了大量其他数组，占用了大量内存。需要主动清空baseArray数组中保存的其他对象来清理泄漏内存。

**案例修复建议**

当应用侧使用export后，export对象无法主动释放，而export对象间接持有的对象也无法通过GC回收，可能导致内存泄漏。当前的解决方法为手动断开export对象与其他对象间的引用关系。

断开引用关系的首要判断依据是断开重复创建对象与复用对象间的引用关系。复用对象不会重复创建可以保留，重复创建对象要尽可能释放。参考上述案例，可以保留baseArray数组，将baseArray数组中存储的大量array对象释放。

**其他模块级对象泄漏修复建议**

1. 若遇到export导出的对象直接或间接持有集合对象，及时释放集合对象中存放的对象。

2. 若应用在设计上就希望保留大量的对象在模块级对象中，建议在数量或大小上做出限制，设计定时清理的逻辑。

### 全局对象持有泄漏案例

**问题现象**

开发者单击应用“globalEnv memory leak”按钮，触发应用进程OOM闪退，系统生成jscrash日志和rawheap二进制快照文件。

**代码示例**

代码中GlobalHoldMain()函数申请300MB对象存放进数组globalArray，其中globalArray挂载在globalThis上。前端按钮在单击后调用问题GlobalHoldMain()函数申请内存，然后申请300MB超大内存确保触发OOM崩溃。代码如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/PRJk-RFeQrmtaZEpv71ZHw/zh-cn_image_0000002729464447.png "点击放大")

**问题分析思路**

1. 参考[OOM故障事件订阅方式](bpta-overview-of-arkts-memory-leaks-overview.md#section844818101813)，在应用崩溃后获取崩溃日志，查看崩溃日志中的Reason字段为OutOfMemory，明确应用进程崩溃原因是OOM故障。

2. 参考[运维态内存快照获取方法](bpta-overview-of-arkts-memory-leaks-overview.md#section16548548153614)，获取OOM生成的rawheap快照文件，将快照导入到DevEco Studio查看。在快照文件中发现有内存占用大的JSArray对象。该JSArray对象的根节点是GlobalObject，GlobalObject无法释放。从持有关系为globalArray可以看出该JSArray对象名称为globalArray。内存快照如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ZuC3JnStRaCijy1vZ8y12w/zh-cn_image_0000002699865076.png)

3. 查看引用链，发现全局对象NodeId为1969的JSArray没有重复创建，但是JSArray中存放的其他JSArray对象在重复创建，需要主动断开两者间的引用关系。

**问题结论与总结**

GlobalObject最终持有globalArray，新创建的对象都存放在这个全局数组globalArray中，无法自动释放。持有的大量对象无法释放，需要主动清空globalArray数组中保存的其他对象来清理泄漏内存。

**案例修复建议**

当应用侧将对象设置为全局后，全局对象无法主动释放，而全局对象间接持有的对象也无法通过GC回收，可能导致内存泄漏。当前的解决方法为手动断开全局对象与其他对象间的引用关系。

断开引用关系的首要判断依据是断开重复创建对象与复用对象间的引用关系。复用对象不会重复创建，可以保留，重复创建对象要尽可能释放。参考上述案例，可以保留globalArray，将globalArray中存储的大量array对象释放。

**其他全局对象泄漏修复建议**

1. 若遇到GlobalEnv/GlobalObject直接或间接持有集合对象，及时释放集合对象中存放的对象。

2. 若遇到GlobalEnv/GlobalObject持有的全局对象，只在本模块使用，建议不再将其保存在全局，避免不必要的长期持有。

3. 若应用在设计上就希望保留大量的对象在全局对象中，建议在数量或大小上做出限制，设计定时清理的逻辑。
