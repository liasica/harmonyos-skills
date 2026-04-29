---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-memleak-detection
title: JS内存泄漏问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 资源泄漏类问题检测 > 内存泄漏类问题检测方法 > JS内存泄漏问题检测方法
category: best-practices
scraped_at: 2026-04-29T14:14:02+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:b03ce651e90a06637cd4d91fe2053f6340916b0b53a6c62b9004a53fb2457187
---

## 使用Snapshot检测虚拟机内存泄漏

### 查看快照详情

1. 创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](../harmonyos-guides/deep-recording.md)。

   说明

   * 在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
   * 将鼠标悬停在泳道任意位置，可以通过M键添加单点时间标签。
   * 鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段标签。
   * 在任务分析窗口，可以通过“ctrl+,”向前选中单点时间标签，通过“ctrl+.”向后选中单点时间标签。
   * 在任务分析窗口，可以通过“ctrl+[”向前选中时间段标签，通过“ctrl+]”向后选中时间段标签。
2. 设置Snapshot泳道。

   单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/r7c-bTpITAmRZNStGNPXVQ/zh-cn_image_0000002370405552.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=4D17DBB8F04458130A49CCC7AB5592E742A0E50E917AFCD18D0F94EA278A6230)进行泳道的新增和删除，再次单击此按钮可关闭设置并生效。
3. 开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/q5GTgCwmQhSWwfhK3rrlAQ/zh-cn_image_0000002404045265.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=1CD78DCCDA7B7218021A53DBD40CBA65A7ABAA673F4AA466DF785475443E4D19)启动一次快照。

   “ArkTS Snapshot”泳道的紫色区块表示一次快照完成。

   说明

   * 在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/LRv0P9cpTIaVzEXKW304PA/zh-cn_image_0000002370565436.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=DB64F71B7B71E6889B6E30F04FC284D32E1DDA8E6C9C7CCBBCB08C205A9C521D)可启动内存回收机制。
   * 当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/cRBf1RI-QQuwhxOJUX6ROw/zh-cn_image_0000002404125105.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=FCB26790822B88B4CF413EFE1289CDF7EA2F9CB8F3F34AF62D9DFC358EA02528)

在“Statistics”页签中显示当前快照的详细信息：

* Constructor：构造器。
* Distance：从GC Root到这个对象的距离。
* Shallow Size：该对象的实际大小。
* Retained Size：当前对象释放时，总共可以释放的内存大小。
* Native Size：该对象所引用的Native内存大小。
* Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
* 构造函数名称后的“x数字”，表示该类型对象的数量，可单击折叠按钮展开。
* 单击列表中任一对象，右侧区域会显示从GC roots到这个对象的路径，通过这些路径可以看到该对象的句柄被谁持有，从而方便定位问题产生的原因。
* 带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/sNO4dCIMRHOcicde7idnlw/zh-cn_image_0000002370405556.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=79B41A65E55F36F89A227E6581E603E4F6E734758E0A951FACBB8565AB00C6A7)标识的对象，表示其为全局对象，可以通过全局window对象直接访问。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/XZZ7TtNzRlGMVntJTq3jEw/zh-cn_image_0000002404045269.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=18668595720644CC703A063159AEA5E38BAB051AA45E9B86CEB7AE1605AF1045)

### 节点属性与引用链

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示“<fields>”以及“<references>”，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/1Brp6EtUTECuLwSyw-hNuw/zh-cn_image_0000002370565440.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=990916AD91E51F9FE4F546C5AAC0EE2D7D20A67BB717048119493B5695D85870)

### 节点跳转

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/WyfzrREQQUW9tNyY0CSwxg/zh-cn_image_0000002404125109.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=6B52B8750AD119773856B66C4B067284B26DAC62653A389624AFDAA6CF61F0F8)

### 历史节点前进/后退

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/dN9yXp_5T4uC4Jikb5uSEA/zh-cn_image_0000002370405560.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=E0E9199ADCA3AFCC4C08C97D4D4FBFC0B07A5A152D357F982119C8A284B3EF1B)

### 比较快照差异

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/VhL14fCSQMSJfZXoOqkZBA/zh-cn_image_0000002404045273.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=D897BF7F8FFDC74B033E263A9165C905F3EA0BBD2B387598E61DC0C75FA61042)在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/exfmZfMkSRGEk-uO70txuw/zh-cn_image_0000002370565444.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=111C6464442D35A1C1ECB659B6350004A2FE8679B2651999F98521173380A885)

### Heap Snapshot离线导入

DevEco Profiler提供Heap Snapshot离线导入能力，可导入一个或多个.heapsnapshot文件。

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot文件。

说明

* .heapsnapshot文件为方舟虚拟机堆内存dump生成的原始文件。
* 导入的单个文件大小不超过150M。
* 批量导入的文件数量不超过10个。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/NA6bbJ-BSaOV1j7i3zedJw/zh-cn_image_0000002404125113.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=37BD039CEA4324E804C1744BA2E48DFB9842E0C7214506823DD804F11105F2CC)可以导入与heapsnapshot文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

说明

* .jsleaklist文件由JSLeakWatcher内存泄漏检测框架生成。
* 导入的单个jsleaklist文件大小不超过30M。
* 导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
* 可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/DtNJ-TiqRqayxVLeRlM9Pw/zh-cn_image_0000002370405564.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=9EA3658C4BC81748D56F93C8D07A82FF818046B73657612429176396BF481B1D)

## 使用IDE工具检测虚拟机内存泄漏的详细步骤

### 检测步骤

检测内存泄漏问题步骤如下：

1. 在内存泄漏前拍摄快照；
2. 触发内存泄漏操作后，再次拍摄快照；
3. 对比两次快照的数据，可快速找到泄漏对象并做进一步分析；
4. 当有多个对象在比较视图都存在时，可以重复多次步骤2的操作，分别和未进行操作时对比，观察是否有对象出现明显的线性变化趋势，进一步缩小泄漏对象的范围。

### 录制Snapshot模板数据

1. 连接好设备后启动应用，点击应用选择框(下图中①处)选择需要录制的应用，选择Snapshot模板(下图中②处)，点击Create Session或双击Snapshot图标即可创建一个Snapshot的录制模板。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/P8z_eDPBQ0SDme10p9nzvg/zh-cn_image_0000002404045277.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=C97AEFAC4146E2ABE35DE0976B886CB4A29554239D74EAA0AC82004FD7BE73D8)
2. 创建好模板后，点击三角按钮即开始录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/CQZH6lB_QHKFdGwGmgSYJw/zh-cn_image_0000002370565448.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=D2E7F031723C48B9F2A3F52C9F24281B19B35324FBF984B24BEE145249BF85B5)
3. 待右侧泳道全部显示recording后则表明正在录制中，此时点击下图中方块按钮或者左侧暂停按钮都可结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/KyJ08qbmTniUx54e5yHUMQ/zh-cn_image_0000002404125117.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=CA8C68E5CA16FCA1F476B3B2E8209257FAED85767D8255230BF5F236E2210672 "点击放大")
4. 拍摄快照：开始录制后，待右侧泳道全部显示recording后点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/Wu1eScy7QAm0PVIjIwaUoA/zh-cn_image_0000002370405568.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=FFD31845D48FB009F4DC04459EC0B9A81BFAFF7AE72DFFDA7B75D040EE921454)
5. 录制完成后可点击下图①处按钮将录制文件导出，而点击下图②处的按钮即可导入之前录制好的导出件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/QPc4HTljS7OQVQ6jZLBcUg/zh-cn_image_0000002404045281.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=A843BDC77E6CD486F46B92EC760BD0317A0B2407673B731C25F9D504A12500A6)

### 常见虚拟机内存对象介绍

JSObject

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/CYXhT40kTMSsV0OIvbUvhw/zh-cn_image_0000002370565452.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=DDEEB81FBCA323ADBD2A74CDDA4F38A5D168C1A376ABA10CA974AAA84830445A)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

```
1. class People {
2. old: number;
3. name: string;
4. constructor(old: number, name: string) {
5. this.old = old;
6. this.name = name;
7. }
8. printOld() {
9. console.log("old = ", this.old);
10. }
11. printName() {
12. console.log("name = ", this.name);
13. }
14. };
15. let p = new People(20, "Tom");
```

[MemoryLeakDetection.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/bacbf85d70037d5aad5457a63ce3cb1e9bce283b/MemoryDetection/entry/src/main/ets/pages/MemoryLeakDetection.ets#L7-L21)

采集到的snapshot数据如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/iZY26NYoT-a-f8N4Xr1EOw/zh-cn_image_0000002404125125.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=64DB19F50E52650B3B75B43331D10054859F3893E775D4DD155B0D419516CC1C)

92729对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_proto\_属性指向声明时的对象，声明对象里则会有constructor()构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

JSFunction

目前所有JSFunction都在（closure）标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/GTsS9SjKQhee0TmVFcJgRQ/zh-cn_image_0000002370405572.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=8B41804810541625FF17B447A0469B069EA8F2D4ABD06824F5D1F5FF97F60FD5)

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/lLu8QUFtSOudDcxcZYipcA/zh-cn_image_0000002404045285.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=0D5BEF59C9A757398D524EC90241D9A591693B5D63F8D2596F107072C23B178F)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/z3SUulC7QDy3JURhHvUVKg/zh-cn_image_0000002370565456.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=FDB44030E04400ACEE532AF0171CA67151AAF169341A87DBB802B74401B02EB2)

LexicalEnv

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/sFYX-CLZSvKTTzAmQQfqlw/zh-cn_image_0000002404125129.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=321A7B31283A335BFDED5FD77DE4DE02302016AB1D459CBC4585E7F8BC135C43)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

InternalAccessor

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**分析方法**

查看对象名称

对于声明对象，可以通过constructor属性来确定对象名称。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/bYDtucQWT6qhdZQgD5LKqA/zh-cn_image_0000002370405576.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=F9ED16E0BE208DBD2C21DEEC995177EB76D8FD4CA660B7D4AAF4DB87DE092AC9)

对于实例化对象，一般没有constructor，则需要展开\_proto\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gN06XF28RfSS0DWHvHsF2w/zh-cn_image_0000002404045289.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=CAE60D71760AA0942BCDF9B88AFA8CAD0A79FE5B17F9A6D7769963CB0BC5C2D8)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_proto\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/nmgIfkA-Sj-Cio3Lys_KfQ/zh-cn_image_0000002370565460.png?HW-CC-KV=V1&HW-CC-Date=20260429T061401Z&HW-CC-Expire=86400&HW-CC-Sign=470E4551FB42627C974C8BEBA14A2857131ABE94F95704FBB35A3BAB4A3F0E49)

如上图则表明Man对象继承自People对象。
