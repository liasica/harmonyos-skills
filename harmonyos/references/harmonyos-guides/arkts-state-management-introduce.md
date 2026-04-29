---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-introduce
title: 状态管理原理介绍
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理原理介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fe7c62cec0b1cf371d69cdf1f6c3b7af5dbf675ba594eed0cf84f61708980346
---

本文将介绍状态管理的基本原理。状态管理的核心逻辑是处理状态变量、自定义组件和系统组件之间的绑定关系。其工作流程可以概括为两个核心阶段：收集依赖和触发更新。

## 收集依赖

收集依赖是指建立状态变量与组件之间的数据绑定关系。在UI渲染时，状态管理框架会“观察”哪些状态变量被读取了，并记录下这个“依赖关系”。一个UI界面上可能使用了多个状态变量，在修改状态变量时，仅与该状态变量相关的组件进行UI刷新，其他不相关的组件不会刷新。因此，UI刷新时需要明确哪些组件使用了被修改的状态变量，以能够实现这些组件的精准刷新。

```
1. @Entry
2. @Component
3. struct Index {
4. @State name: string = 'Jack';
5. @State age: number = 10;
6. @State grade: number = 5;

8. build() {
9. Column() {
10. Text(`${this.name}'s age is ${this.age}`) // Text1
11. Text(`${this.name}'s grade is ${this.grade}`) // Text2
12. Button('change age') // Button1
13. .onClick(() => {
14. this.age++;
15. })
16. Button('change grade') // Button2
17. .onClick(() => {
18. this.grade++;
19. })
20. }
21. }
22. }
```

上述示例代码中，自定义组件Index中定义了三个状态变量name，age和grade，在build函数中创建了两个Text系统组件和两个Button系统组件。收集依赖的具体步骤为：

1. 自定义组件Index被创建并首次调用build方法创建组件。
2. 当框架执行到Text(`${this.name}'s age is ${this.age}`)时，为了显示文本内容，需要读取this.name和this.age的值。
3. name和age都是被@State装饰器装饰的状态变量，状态变量在被读取时会收集当前正在渲染的系统组件的唯一标识elementId，并将其存储到一个Set集合中。因此，状态变量name和age均收集到Text1的唯一标识elementId1。
4. 同理，当框架执行到Text(`${this.name}'s grade is ${this.grade}`)时，状态变量name和grade收集到了Text2的唯一标识elementId2。

每个状态变量中维护了一个Set集合，保存所有与其绑定的系统组件的标识信息。在上述示例中，状态变量name的依赖集合中保存了Text1和Text2的信息，状态变量age的依赖集合中保存了Text1的信息，状态变量grade中保存了Text2的信息。由此，框架完成了收集依赖的过程。

## 触发更新

当状态变量发生改变时，状态管理框架会通知所有依赖于它的UI组件，重新计算并刷新，这个过程称为触发更新。触发更新大致可以分为三个步骤：

* 计算状态变量发生改变后的新值。
* 修改状态变量的值，并将与其绑定的组件标脏。
* 刷新所有的脏节点，更新UI的同时重新收集依赖。

说明

更新是以自定义组件为单位的。

同样对于上述示例代码，点击Button组件修改状态变量，对应的Text组件刷新，具体步骤为：

1. 点击Button1，触发 onClick 事件。
2. 在事件处理函数中执行this.age++。由于age是状态变量，在改值的过程中会执行状态管理内部的更新操作。
3. 由于在一个UI更新周期中，自定义组件中可能存在多个状态变量发生改变，而更新是以自定义组件为单位的，所以每个自定义组件中维护了一个标脏的系统组件集合（下称脏系统组件集合），用于保存在当前UI更新周期中标脏的系统组件的elementId。在状态变量age的更新操作中，将其依赖集合中系统组件的elementId加入到其所属的自定义组件Index的脏系统组件集合中。
4. 完成系统组件标脏后，将状态变量age所属的自定义组件Index标脏，加入到标脏的自定义组件节点列表（下称脏自定义组件列表）中，并请求一个刷新信号。
5. 在下一个UI更新周期中，框架遍历脏自定义组件列表，重新调用它们的rerender方法（rerender方法是由系统生成的），执行Index自定义组件的rerender方法时，遍历脏系统组件，刷新Text1组件并更新依赖。
6. 同理，点击Button2修改状态变量grade的值，对应刷新Text2组件并更新依赖。

触发更新就是根据状态变量收集到的依赖关系，当状态变量发生改变时，找到所有受影响的组件，标记为“脏”，在一个UI更新周期中，只刷新标脏的组件，实现最小化更新。

## 状态管理在渲染管线中的流程

UI渲染的流程主要有以下几个步骤：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Vf2tab52T-uPL06eYk-i7g/zh-cn_image_0000002558604424.png?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=0D7061B7E129D9844B074A1687F3FD1CB4421A994F700BC8D869F327F6B19320)

1. 事件触发状态变量发生改变，执行状态变量的set方法，将自定义组件和系统组件标脏，并请求一个刷新信号。
2. 刷新脏节点：刷新标脏的自定义组件和系统组件。
3. 布局：根据标脏局部刷新组件树，触发子树上节点的尺寸测量和位置确认。

同样以上述示例代码为例，使用DevEco Studio的[Profiler工具](ui-inspector-profiler.md#状态管理profiler调优能力)，点击Button1，抓取状态变量的变化打点，trace如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/1lmNRuxtSGaUmtNa1Ufh4w/zh-cn_image_0000002589323949.png?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=73D0F1E534782B5F29AA90ECCCA4B59396FDFB15D0A6158BF39365C53E92C33B)

对上图中的标记点进行逐一介绍：

1. 点击Button1按钮，产生手势事件的trace点。
2. 手势事件触发onClick回调。
3. 在onClick回调中改变状态变量age的值。
4. 下一帧信号到来，执行VSync回调。
5. 刷新脏自定义组件Index。
6. 遍历自定义组件中的脏系统组件，重新渲染Text1组件。
7. 执行后续布局流程。

其中，状态管理的基本流程如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/8oARJ4DFTkaoE3d_N_WZ7A/zh-cn_image_0000002589243889.png?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=52FFEE4C5CF7B53F0390985AA4AFED7BF518531FA76ECECF6353E10055489E5B)

状态管理循环执行两大步骤：收集依赖和触发更新。收集状态变量与组件之间的依赖关系。当状态变量发生变化时，执行标脏，刷新对应的UI，同时更新依赖关系。

相比状态管理V1，状态管理V2在状态变量变化时，会异步标脏组件，这两者的更新差异详细可参考[状态管理V1和V2更新机制差异](arkts-v1-v2-update-difference.md)文档。
