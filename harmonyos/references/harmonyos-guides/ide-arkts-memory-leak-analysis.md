---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkts-memory-leak-analysis
title: 案例：ArkTS内存泄漏分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 内存泄漏：Snapshot分析 > 案例：ArkTS内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:06+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9807092ab77c9a437b39000e28001c78f8f6ceaf714878ffcb9f9a9f670b8aeb
---

本案例介绍如何判断应用存在ArkTS内存泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/zVPTsK66TbuMIYIz2x4psQ/zh-cn_image_0000002808887045.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=F23E84F926FCA90E711935CC7A6AEF9AA2EB4672EE73EDA2F095471B80857BDA "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/perOdov4Tby1S-xfIVOF6g/zh-cn_image_0000002808887041.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0068B9DC604FEFE671ECBAD0566B0E76D903FE91D8EB6839B9CA7CF260C1EEC)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/omV327P5QriD77yAmSlwqg/zh-cn_image_0000002779407392.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=8278EC58A7209571AB4CA57BBF2251368B4C76BD54AFFB59CB791B3F11CB3A50 "点击放大")即开始录制。
5. 录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/dWbL73gJS5qtzVa3wPyysw/zh-cn_image_0000002779567374.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=E3CC5A6DA87474F396DF222F28F7EAC0EDE1E779488DE106F005BC5101B8B79F "点击放大")
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/jE-_ST86T1mobXXJjmMI0w/zh-cn_image_0000002779407380.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6C76748F8A0B893BEAA6FF23D09CD6D38483C8AEE3032870BB19A6FD207B683A "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/WMYDu2P6Tdq-mb8hW1fgQA/zh-cn_image_0000002808766969.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=393A1C933D30A96EB8D6987DAEC6A04C65D296C1351665A8C4A9F20CECEED9F5)
3. 待右侧泳道全部显示recording后则表明正在录制中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/oDeTrQz_Rr2EvOBwaMMNvA/zh-cn_image_0000002808766957.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=196435CD72EE8CF354A62C7FC6163FADEAEA2C795933153C412282E64377FEFA "点击放大")
4. 拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。

   **说明** 

   方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/EH0W9kXVQL-j9DUtfZq7uA/zh-cn_image_0000002779407382.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=93B6436566C23BF4ED1AF406E59BFDBE3FD8D2FBBFD6623DC346BEAFAC898A27 "点击放大")
5. 多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6. 拍摄第二次堆快照。
7. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/lf33F-nFQLyjxoWmTpbTYw/zh-cn_image_0000002808766965.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1F2D41F6C154FD78C7E645AFB3907EFB324C3C3A343C4EC44F7830C1597663EF "点击放大")

### 分析ArkTS Heap

1. 在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的**Comparison**区域，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/HzUo1z3KRsWBh0VEaezbYQ/zh-cn_image_0000002779407384.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A828CE32B8833D0FCC8BA170B6436AB1688BFF5E004D5C0A125ED5F729D8A0D "点击放大")
2. 优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。

   **说明** 

   选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

## 分析Snapshot数据

### 常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/a21D-2erQpikmiQEmxkJ9Q/zh-cn_image_0000002808766959.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C7EE2643C1EB51DE1A3E61D9462B2D127D15AAAB7F343D531DEB487D22F2853)

其中\_\_proto\_\_：原型对象，所有数组的\_\_proto\_\_应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于（array）标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于（array）标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于（array）标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/lKHSHBqzQXSJnXRzf0cvZw/zh-cn_image_0000002808887031.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=2820FA485280094A3F8484DE3DF9251029FB75A2E1418CB9DD13C1FDE7931009)

以下通过具体代码来介绍下实例化对象、声明对象、构造函数间的关系：

```screen
// HelloWorldPage.ets
class People {
  old: number
  name: string
  constructor(old: number, name: string) {
    this.old = old;
    this.name = name;
  }
  printOld() {
    console.log("old = ", this.old);
  }
  printName() {
    console.log("name = ", this.name);
  }
}

@Entry
@Component
struct HelloWorldPage {
  @State message: string = 'Hello World';
  private people: People = new People(20, "Tom");

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

采集到的snapshot数据如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/KBv4UwPGTRqSy2gBtzqVXg/zh-cn_image_0000002808887047.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=C690D4593EA17D9EB6AA2D1E048609D474B4A29A96D51F6E469F7D3028507663)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_\_proto\_\_属性指向声明时的对象，声明对象里则会有constructor()构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在（closure）标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/ROFCzfTuRhqbn4jIi_7weQ/zh-cn_image_0000002779407394.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=C7A9425A81A3D0E969170E4C03A69C540195B63A615C5A4AE8A44DD81F338741 "点击放大")

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Bf5gfXZmRLaRlP8Chs6MtQ/zh-cn_image_0000002808887049.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC5BAFF1974CF194123CAF95E059D8817F68F5598D660FDD82778A7A240528E1)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/eMg5J_CiRBestcMw2fKKlw/zh-cn_image_0000002808766967.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=872B7D7FCD7645F1C6BD207A16DB9346DA599D2BD4D72C204826C0523BFBAA15)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在（array）标签中展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/4HmkY5bER5uyEGl1HB4CoQ/zh-cn_image_0000002779567372.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=7354D3536610E3214FD9417F8E54445CA08B271A509A6F04B88E7C39C1238EC8 "点击放大")

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/zFRFpab9ROiK7j61SzYRZg/zh-cn_image_0000002808766961.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=16989DFC96679B7BFB793D7F005F578E07F4C3800E8C97AEF39EDFCC60E08B40)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**LocalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于（handle）标签中，用于管理JS对象生命周期的引用句柄（napi\_value）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/1ULyhSeuQniVQ4VuPVEvTw/zh-cn_image_0000002808887039.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0AF4D46347E356AF7F523C16FEE7E4033610E325572A10D59BB29AB96C2234C)

**GlobalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于（handle）标签中，允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref），默认情况下不记录napi\_ref地址。

**GlobalHandleObject**

26.0.0版本新增，位于（handle）标签中，用于记录napi\_ref地址，并建立napi\_ref和ArkTS对象的引用关系。该功能需要先调用[@util.ArkTSVM.setTrackGlobalRef](../harmonyos-references/js-apis-util.md#settrackglobalref)接口使能 ，使能后会在快照导出过程中记录napi\_ref地址和引用关系。开发者可根据快照中napi\_ref相关信息，分析跨语言导致的内存泄漏。

如下图，ReferenceAddress:0x5b0b560160是napi\_ref地址，子节点是napi\_ref关联的ArkTS对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/meedO1sNSWOq8YcX39_tiA/zh-cn_image_0000002808887027.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6F756FDF2D84436892C49698C00451D06D64770537EE13FC30085F6824507956)

**说明** 

GlobalHandleObject中记录了存在napi\_ref的ArkTS对象，对象是GlobalHandleRoot对象子集。

**VMRoot**

26.0.0版本新增，位于（handle）标签中，表示虚拟机层面的根节点。

**FrameRoot**

26.0.0版本新增，位于（handle）标签中，表示函数调用栈帧在GC遍历过程中的根节点。

**SourceTextModule**

SourceTextModule为虚拟机创建的对象，当应用使用export暴露对象后会被SourceTextModule对象持有。

属性EcmaModuleRecordName表示export对象所在的文件名，属性EcmaModuleFileName表示export对象文件所在的abc文件名，这两个属性名在26.0.0版本新增。如果快照用TRIM\_LEVEL\_2级别裁剪生成的.rawheap文件转换成的.heapsnapshot文件则不显示这两个属性名。

**Proxy-<对象实例名称>**

26.0.0版本新增，被@Observed装饰的class实例，或被状态管理V1装饰器（如@State）装饰的对象实例，系统会自动在Proxy后带上对象实例名称。

**说明** 

若开启进程级堆快照转储以后，是由子线程触发的进程级堆快照转储将不会展示对象实例名称。

**HeapMetadata**

26.0.0版本新增，HeapMetadata用于记录触发OOM（Out of Memory，内存溢出）的ArkTS堆内存（Heap）信息，包括heapType（堆类型）、spaceType（堆空间类型）、vmType（虚拟机类型）。

其中heapType记录触发OOM的heap，包含Local Heap、Shared Heap、Process Heap；spaceType记录触发OOM具体的堆空间类型；vmType记录当前虚拟机的类型，dynamic表示动态虚拟机类型，static表示静态虚拟机类型。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/o3WnZzrgQqOTKrVGYaNXJQ/zh-cn_image_0000002779407396.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=26895AEE373B36B8CB0A68007C416982BD95A45068A1FDC9D0ED6100745B597D)

对于实例化对象，一般没有constructor，则需要展开\_\_proto\_\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/l00GtR8lSd-RpZUuBeJTgw/zh-cn_image_0000002808887043.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=11FC5DD9EF9A651DA51D6D9D52566B6BC6DC112CDBDC60E753C1BB84712E0C9E)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_\_proto\_\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/2euswLP8TpOekkFeizAR2Q/zh-cn_image_0000002808766963.png?HW-CC-KV=V1&HW-CC-Date=20261114T004718Z&HW-CC-Expire=31536000000&HW-CC-Sign=6D303C33F8F6B9CA121FD0928FF56AA236CCCD58B14796EDF9953298648CB3A5)

如上图则表明Man对象继承自People对象。
