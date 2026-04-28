---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkts-memory-leak-analysis
title: 案例：ArkTS内存泄漏分析
breadcrumb: 指南 > 优化应用性能 > 内存泄露：Snapshot分析 > 案例：ArkTS内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3584b6aad27ee6f169bf83540141adbcd137aee3b7dbdef4dfa97fb821063b43
---

本案例介绍如何判断应用存在ArkTS泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。

   监控Memory用到变化。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/NcGqCAvUTZWgmX1zhtGmRg/zh-cn_image_0000002561833153.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=413F608823F341951EE6C3302E6E5A48C8CB35E8D4E193A39C18CE43E25EEA81 "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   说明

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/kXV9RqN5QY2-uhPeSaGa4Q/zh-cn_image_0000002530913220.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=A2141808D4EFA5616B2F64C0747C679C71589F1148E97A2167C0A75CEE691ABD)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/06Ex7YDRSMC7taUiCLC4WQ/zh-cn_image_0000002561833127.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=3C70890326222B68ABFE575E1384C1D33E8BB0270FAAC24047C5253112D5E1C5)即开始录制。
5. 录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/vVhYGMxNQgWSnZMNuY2iFg/zh-cn_image_0000002561753143.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=4923D3EAAC7A9E3D7FB676C14042631DAE36699E48E2F38EF833689910B93343 "点击放大")
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/BNLJjck_SJCTyqcxJcAGrg/zh-cn_image_0000002561753137.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=F2E5C2EA1A4DDF4A62A4BC7EA6A986DCC3C1B8E177BCCD89B3DB3F64C3226F0F "点击放大")

## 使用Snapshot模板分析ArkTS内存问题

分析内存泄漏问题步骤如下：

1. 使用Snapshot模板录制数据；
2. 在问题场景前拍摄快照；
3. 触发问题场景后，再次拍摄快照；
4. 对比两次快照的数据，可快速找到泄漏对象并做进一步分析；
5. 当有多个对象在比较视图都存在时，可以重复多次触发问题场景后拍摄快照，分别和问题场景前拍摄的快照进行对比，观察是否有对象出现明显的线性变化趋势，进一步缩小泄漏对象的范围。

### 录制模板数据

1. 连接设备后启动应用，点击应用选择框选择需要录制的应用，选择**Snapshot**模板，点击Create Session或双击Snapshot图标即可创建一个Snapshot的录制模板。
2. 创建模板后，点击三角按钮即开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/z8057CLLT1a5HRKkwrhsXQ/zh-cn_image_0000002561833155.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=1207985AE41E3A1EAF6FD138CC42E71948DC5B2E7071002D0FDC8F0B93AF7CA6 "点击放大")
3. 待右侧泳道全部显示recording后则表明正在录制中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/STaMU9_NTEmrO2_PcHQP9g/zh-cn_image_0000002530913210.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=115E7254E7529947BE0D7378760534E4D7B739BA105EACB72CFBE18D79D7C20B "点击放大")
4. 拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。

   说明

   方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/vWkKpy9tQRiUxCsAxSKODg/zh-cn_image_0000002561833121.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=AA94386A1BE8546B21521DAC17FF6C9B8E7B0BB6A239B85A426467AF9AD7ED19 "点击放大")
5. 多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6. 拍摄第二次堆快照。
7. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/RF6mY8tjTVWdZg1FQWb-WA/zh-cn_image_0000002530753210.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=6C7CC5217FEF56AAA35516526DFA87779B07E1DB9E38EDA61D29D909110F0203 "点击放大")

### 分析ArkTS Heap

1. 在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的“Comparison”页签，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/rywR7gkGTEWlEM2hsNFPlw/zh-cn_image_0000002530753208.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=394532BFBDF624A4109C3D2F6116205DFE215D9C6832D918EAC2B1BF0AD87D5E "点击放大")
2. 优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。

   说明

   选择一个实例结点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮，系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的结点），并在右侧区域展示。

## 分析Snapshot数据

### 常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/EWF7uBMDRU6oXXFQHFaqfQ/zh-cn_image_0000002530753220.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=F20B905FAF40E177E7E12D4BAD828E9D9EB2F8E295D8C8031FBA0F7432D5F79A)

其中\_\_proto\_\_：原型对象，所有数组的\_\_proto\_\_应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于(array)标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于(array)标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/X8J-56LpQRe_g19qVmTMjQ/zh-cn_image_0000002530913202.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=9E0A7D58355031DB15C5A5D47C35F2EC147A6B967F25C063646483FBC2DAA639)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

```
1. // HelloWorldPage.ets
2. class People {
3. old: number
4. name: string
5. constructor(old: number, name: string) {
6. this.old = old;
7. this.name = name;
8. }
9. printOld() {
10. console.log("old = ", this.old);
11. }
12. printName() {
13. console.log("name = ", this.name);
14. }
15. }

17. @Entry
18. @Component
19. struct HelloWorldPage {
20. @State message: string = 'Hello World';
21. private people: People = new People(20, "Tom");

23. build() {
24. Row() {
25. Column() {
26. Text(this.message)
27. .fontSize(50)
28. .fontWeight(FontWeight.Bold)
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }
34. }
```

采集到的snapshot数据如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Gkk3YZ61Q_y3GS9rMSBb7A/zh-cn_image_0000002530753228.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=D52E111F2BE2F0C5D5EE729BC462E408438B1F7D6109A1C9238BC5706720BDF8)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_\_proto\_\_属性指向声明时的对象，声明对象里则会有constructor构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在(closure)标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/rPgVSZBZRP6nP2JbrddBtg/zh-cn_image_0000002561833131.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=0DBF4FBB9D705A7D25D036EBA686165A7FA6488D6BC0B32BD1D54A50A6EC9AC6 "点击放大")

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/brd44dS_Sr6XxBQwySje7g/zh-cn_image_0000002530753234.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=358FAE0A1BE78486BA6C7BF4BCEE97CA38E1A3C59892BDF2164C06E8AE8337EE)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/Z5PapSeES9GB67W25ypvmw/zh-cn_image_0000002530753230.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=7FE8583866B0B27ECD3AE712E5AA7F351C9703FAE8069816F163F223AADC8AC4)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在(array)标签中展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/lZnvLlV9Simj8XhO1ZG0fA/zh-cn_image_0000002530913204.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=42ADC4FCEB2F9299B661C59D3A9EBB9555A3327C6EB4B482031D2C48CBE6973C "点击放大")

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/SKNh0D1qQ5uI2X5ErIuPNw/zh-cn_image_0000002561833139.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=8180C5DA773AB6DA14753ED65A39AC224B30E2218CE4E38B7940E35AC564CDE5)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**LocalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，用于管理JS对象生命周期的引用句柄（napi\_value）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/dBTqYUkRSveRRPa3qK6ZyA/zh-cn_image_0000002531842516.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=85F86446C70E48E2D2A269A1A1A4F429811F8885E5C88CF04B31638FD5CEEF55)

**GlobalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于(handle)标签中，允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref）。

### 常见属性介绍

| 属性 | 含义 |
| --- | --- |
| \_\_proto\_\_ | 原型对象 |
| (object elements) | 对象元素 |
| (object properties) | 对象属性 |
| hclass | 隐藏类 |
| ArkInternalHash | ArkTS运行时内部的哈希值 |
| ProtoOrHClass | 原型或隐藏类指针 |
| RawProfileTypeInfo | 运行时类型剖析信息 |
| HomeObject | 父类对象 |
| FunctionKind | 函数类型标识 |
| FunctionExtraInfo | 函数附加信息 |
| prototype | 构造函数或类对象关联的原型对象 |
| Inlineproperty | 内联属性 |

### 分析方法

**查看对象名称**

对于声明对象，可以通过constructor属性来确定对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/ouNZ67LlQKqXXuHLnXV49w/zh-cn_image_0000002530913208.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=47361647F611C92D050719142005D479655995DFE8820DEEBECD3A721D9DF371)

对于实例化对象，一般没有constructor，则需要展开\_\_proto\_\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/w2hw0mtvQIqlfpwxruqzUQ/zh-cn_image_0000002530913216.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=8FC62A0ADB403126D1A83E045145EE14E34BE9BEFBC86A66A20E790705D51F88)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_\_proto\_\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/zMfLcjOJRza8iJPr5ORtDA/zh-cn_image_0000002561833143.png?HW-CC-KV=V1&HW-CC-Date=20260427T235732Z&HW-CC-Expire=86400&HW-CC-Sign=7B7A8824B37323A7270B420B79FB195EEAF596283C2C7FB6D4250090846F0A9B)

如上图则表明Man对象继承自People对象。
