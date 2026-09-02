---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-oom-js-object-held-by-js-object
title: JS对象长期被JS持有导致内存泄漏故障模式说明
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 稳定性故障模式说明 > 内存泄漏故障模式说明 > ArkWeb OOM故障模式说明 > JS对象长期被JS持有导致内存泄漏故障模式说明
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:d2d25d37bcea1f0a5622dc4cd4818e3c3ef0447d5a2dd629f135384287e3e258
---

ArkWeb V8引擎通过GC机制保证JS代码执行结束后释放JS对象占用的内存，如需在JS代码执行过程中及时释放内存，则依靠开发者对JS对象生命周期的管理。本文通过两种场景分析JS对象内存占用过高导致引擎OOM的问题，并通过堆快照文件展示相关堆内存特征。

## 根因描述

* 在函数内创建的对象其生命周期与函数一致，当使用Array、Map、Set、Object、Class等内存占用过大的对象时，结合循环、递归等语法，会导致引擎OOM。
* 闭包函数可以引用闭包外部的临时对象，对象的生命周期会延长至与闭包函数相同。当闭包被加入微任务队列，对象的生命周期会进一步延长至微任务执行完毕。对象数量多、单个对象内存占用过大以及微任务队列积压都会导致引擎OOM。

## 内存泄漏分析方法

1. 获取问题场景的Heap Snapshot，使用Chrome浏览器的DevTools工具展示各类JS对象在内存中的占比。
2. 将内存占比从高到低排序，关注Stack roots、Micro tasks的内存占用。
3. 开发者可结合源码，逐对象分析内存占用的合理性，找到引发OOM的对象。

## 关键字

在Heap Snapshot引用链中找到：Stack roots或Micro tasks。

* Stack roots：函数内部创建的临时变量，在生成Heap Snapshot时归入Stack roots。
* Micro tasks：Promise或queueMicrotask语法向微任务队列中放入的微任务，在生成Heap Snapshot时归入Micro tasks。

## 案例一：创建过大的临时对象导致堆内存泄漏

以下为负向用例，旨在说明创建过大的临时对象导致的内存泄漏。用例在func()函数内创建了两个内存占用较大的临时对象，在func()函数执行结束之前，这两个对象所占据的内存都不会释放，导致堆内存使用量保持较高水平。

```javascript
function func()
{
    // Create a sufficiently large local object inside the function.
    let bigObject = new Array(1024 * 1024 * 20).fill(0);
    debugger;
    for (let index = 0; index < bigObject.length; index++) {
        bigObject[index] = index;
    }
}
func();
const msgEl = document.getElementById('message');
msgEl.innerHTML = 'JS execute finish.';
```

在Chrome浏览器DevTools调试中，JS执行到第一次创建临时对象后，会停留在debugger语句，开发者可通过hidumper获取并分析快照，了解临时对象在堆内存快照上的特征，以辅助分析类似问题场景。

### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](bpta-overview-of-arkweb-oom-fault-modes.md#section1276158153214)章节中介绍，本节介绍使用Chrome浏览器DevTools工具分析Heap Snapshot文件的流程。

1. 打开Chrome浏览器，按下F12打开DevTools开发者工具。

2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/MqycamkeRZmhmzPzq2pSzQ/zh-cn_image_0000002677818392.png)

3. 打开后默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见98%的内存分布在Array对象中，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/77qa1TYwS5G2bvTXNKehMg/zh-cn_image_0000002707578253.png)

4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，大致估算每个节点的Retained size累计值，找到累计值最大的节点，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/WCv3ahSvTiGhmIyoxG2aYQ/zh-cn_image_0000002677658544.png)

可见大量内存被Stack roots引用，表明当前内存分布主要集中在栈上局部变量。

**说明** 

Containment视图以Retained Size大小降序排序结果中，Stack roots的Retained Size为0，按照**依次展开保留大小最大的节点**的思路无法得到**内存分布主要集中在栈上局部变量**的结论。从Summary视图中能看到Array对象拥有Stack roots与DevTools console两个引用，Array对象的Retained Size不能累计给Stack roots。来自DevTools console的引用与用例本身无关，DevTools停留在JS代码断点处时，会引用断点附近的所有局部变量。

**依次展开保留大小最大的节点**的分析方法，是统计节点下所有引用对象内存占用方法的简化版，多数情况下该方法是有效可行的。

5. 结合内存快照中给出的对象类型以及其他信息，梳理内存泄漏对象的生命周期是否合理，是否可以被优化。

### 预防建议

由函数内分配的临时对象引发的OOM，需要检查JS代码，判断是否在栈上进行了大量的内存分配（如超大数组分配、扩容等），或者是函数递归调用，导致栈上内存始终无法被回收并持续进行累积，最终导致OOM发生。开发者需要梳理业务逻辑，为临时对象给出合理的作用范围与生命周期，降低临时对象的内存占用峰值。

## 案例二：微任务长时间引用临时对象导致内存泄漏

以下为负向用例，旨在说明微任务长时间引用临时对象会造成内存泄漏。用例在closure内引用了func()创建的临时对象bigObject，并将closure加入微任务队列，当func()执行结束，closure成为bigObject的唯一引用，在closure执行完成之前，bigObject占用的内存不会释放，堆内存使用量会维持较高水平。

```javascript
function func()
{
    // Create a sufficiently large local object inside the function.
    let bigObject = new Array(1024 * 1024 * 20).fill(0);
    let closure = () => {
        for (let index = 0; index < bigObject.length; index++) {
            bigObject[index] = index;
        }
    };
    // Enqueue the closure into the microtask queue.
    Promise.resolve().then(closure);
}
// After the fun function finishes execution, its reference to the large object ends,
// and the closure in the microtask queue becomes the only reference to the large object.
func();
debugger;
const msgEl = document.getElementById('message');
msgEl.innerHTML = 'JS execute finish.';
```

在Chrome DevTools调试中，func()执行完成后，会停留在debugger语句，开发者可通过hidumper获取并分析快照，了解微任务队列中临时对象在堆内存快照上的特征，以辅助分析类似问题场景。

### 分析思路

获取问题场景中Heap Snapshot的方法已在[堆内存快照](bpta-overview-of-arkweb-oom-fault-modes.md#section1276158153214)章节中介绍，本节介绍使用Chrome浏览器DevTools分析Heap Snapshot文件的流程。

1. 打开Chrome浏览器，按F12打开DevTools。

2. 在Memory页中，单击Load profile，上传内存快照文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/_F_Ra0CGRwmgbYgf7iy-TQ/zh-cn_image_0000002707458405.png)

3. 打开后，默认显示Summary视图（按对象构造函数分组），按Retained size从大到小排序，可见97%的内存被bigObject占用，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/3s2Y_SdATV-mDAM-vxwUlg/zh-cn_image_0000002677818394.png)

4. 切换至Containment视图（按引用关系追溯），按Retained size从大到小排序，依次展开Retained size最大的节点，直至无法进一步细分，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/Q_HJ3_wMTR2KVzXNKPmwQQ/zh-cn_image_0000002707578255.png)

可见大量内存被Micro tasks引用，表明当前内存分布集中于微任务所引用的变量。

5. 结合内存快照中的对象类型及其他信息，梳理Promise或queueMicrotask语法的使用情况，识别业务逻辑是否存在微任务队列积压或微任务长时间引用外部变量的情况。

### 预防建议

由微任务队列引发的OOM，需梳理JS代码上下文，检查微任务队列是否长期处于任务积压状态，或微任务是否大量持有闭包外的对象引用且未执行完毕。开发者需对业务场景中Promise或queueMicrotask的使用进行优化。
