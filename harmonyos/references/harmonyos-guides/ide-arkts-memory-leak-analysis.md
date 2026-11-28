---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkts-memory-leak-analysis
title: 案例：ArkTS内存泄漏分析
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 内存泄漏：Snapshot分析 > 案例：ArkTS内存泄漏分析
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:45+08:00
doc_updated_at: 2026-11-27
content_hash: sha256:bcea8169b10100187b5a4c40fdd15acabb51363b6e3b4fcce5dbbcd02b316c04
---

本案例介绍如何判断应用存在ArkTS内存泄漏，以及如何通过快照对比找出ArkTS内存泄漏的原因。

## 初步识别内存问题

1. 使用[实时监控功能](realtime-monitor.md)对应用的内存资源进行监控。正常操作应用，观察运行过程中Memory泳道的变化。

   当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，则可初步判断应用可能存在内存问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/azUMWHCRSGuRIXdKOLFWvQ/zh-cn_image_0000002808887045.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=8158F1A6E498DB7EF1B6774136E05230904176B9F66E1B1E1C72EC64DAB5E98E "点击放大")
2. 当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](deep-recording.md)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3. 以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。

   **说明** 

   其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/TWYDojc3Rkas3U_eioKezw/zh-cn_image_0000002808887041.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=096AADA8C8500120D4B6EE5F84A0A7135C07207D4E112ECE31C22ED058F77E3A)
4. 点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/QRDs6IvURW-NlI4iAoAP4w/zh-cn_image_0000002779407392.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=91E57BEEA9B46A90DDEC73A49EC08E9A7CCA87599558778003290CC19F60C6B1 "点击放大")即开始录制。
5. 录制过程中，不断操作应用在问题场景的功能，将问题放大，便于快速定界问题点。
6. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/__3ewg0fShG-0p4w07ro7g/zh-cn_image_0000002779567374.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=860D713A12C5A3923D8F794D3ADED4FAC725D6A1E9D72A93571EAF0143655032 "点击放大")
7. 录制完成后，展开Memory泳道，其中ArkTS Heap表示方舟虚拟机内存，这部分内存受到方舟虚拟机的管控。当ArkTS Heap有明显的上涨，说明在方舟虚拟机内的堆内存上可能存在内存泄漏，可以使用Snapshot模板进行下一步分析。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/B2HGxvnnTXm6FbOpgS5iuw/zh-cn_image_0000002779407380.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=5FD9A4C351B4466F569FCAA5CE8C0AC706F222BCB846F49F6F25DE7865680846 "点击放大")

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/0TCtks0rS4urqqv3KNiopg/zh-cn_image_0000002808766969.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=44D0C2EE351981C53F8B71A12057DD23B57FE6CD6EF3D536F8D7A5AFACB027F6)
3. 待右侧泳道全部显示recording后则表明正在录制中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Ki4u0nLeRSW8kSSFtDGNJQ/zh-cn_image_0000002808766957.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2B926636555ECD769518E3C5FCEF8756DAD0CFFF4E472798691C31AA85D530A "点击放大")
4. 拍摄第一次堆快照作为基准（点击图中①处拍摄按钮，待②处显示出紫色条块表示快照拍摄完成）。

   **说明** 

   方舟虚拟机提供了在获取快照前自动GC（Garbage Collection，对堆内存进行垃圾回收）的能力，因此拍摄快照之前不用主动触发GC。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/1UAQtPyIRh2WZmWtK_tLpQ/zh-cn_image_0000002779407382.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=21BE85D8755B4AF5C982B157B5E91C985015B1A7C0CA2DC5AD4909B03A49BC4A "点击放大")
5. 多次触发内存泄漏操作。可以操作5，7，11等这种特殊的次数。比如操作了5次对比两个快照发现有很多创建了5次没释放的场景，则可能存在内存泄漏，再操作7次，如果创建了7次那就可以确认发生了泄漏。
6. 拍摄第二次堆快照。
7. 点击下图中方块按钮或者左侧停止按钮结束录制。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/p0SvXEqaTi2ZrDy4eyCo7w/zh-cn_image_0000002808766965.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4CDE6983C1106FE8513E7900FB81ADAF7FEF724E7F8E7E69CFD768C8EB9BF7C "点击放大")

### 分析ArkTS Heap

1. 在每次拍摄堆快照之前，虚拟机都会触发GC，所以理论上堆快照内存在的对象都是当前虚拟机已经无法GC掉的对象。我们可以将两个堆快照进行比较，来查看哪些对象是在触发问题场景时新增了且不能释放的。切换到窗口下方详情区域的**Comparison**区域，将两次快照进行对比。图中数据的含义是以Snapshot2作为基准，Snapshot2对比Snapshot1的数据变化量。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/fxUEDrYUT9S1QinEDpxsUA/zh-cn_image_0000002779407384.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=839C47576B27910E00E746D23C1C797A000091B345731560B2B5EBD262F1FF4D "点击放大")
2. 优先寻找与触发内存泄漏操作次数强相关、与业务代码强相关的Constructor，首先来分析这些对象是否正常。主要是按照Distance逐渐减小的方式找引用链，可以从references里面一层层去寻找，排查引用链上的可疑对象（一般指与业务代码关联的对象）。

   **说明** 

   选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

## 分析Snapshot数据

### 常见对象介绍

**JSArray**

目前所有JSArray展开后为数组里的各个元素：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/IrGCViu-S3KPuvZZ0D_Fzg/zh-cn_image_0000002808766959.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=E893022775AF7B615A35EB6B1F939292E50B30B44E48B74A47CAA10E637AFD0D)

其中\_\_proto\_\_：原型对象，所有数组的\_\_proto\_\_应该是一致的；length：内置属性访问器，可以访问数组长度。

**TaggedDict**

位于（array）标签中，一般为虚拟机内部创建的字典，ArkTS代码层面不可见。

**TaggedArray**

位于（array）标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**COWArray**

位于（array）标签中，一般为虚拟机内部创建的数组，ArkTS代码层面不可见。

**JSObject**

JSObject展开后为内部的各个属性如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/a_gNp63GTQWLrhHeVPQBCQ/zh-cn_image_0000002808887031.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=CA6887A9EAF0D6C41804C74F0E1E2E2332AEC9AA4D11B35C4304B66E6C20B1DF)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/cAXRHzPVQk28w5C8d2X_PQ/zh-cn_image_0000002808887047.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D76F6D9CD7767286B6F53504EB4956FE612580ED5D0329C35C6090DA886EDB5)

202169对象对应的是People，其主要声明了对象的属性和方法。

实例化对象的\_\_proto\_\_属性指向声明时的对象，声明对象里则会有constructor()构造函数。当实例化多个对象时，实例化对象会有多个，但是声明对象和构造函数只有一个。

**JSFunction**

目前所有JSFunction都在（closure）标签中，展开即可看到所有JSFunction：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/CM7KREjfRemRTM7rInJu5Q/zh-cn_image_0000002779407394.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=52154722A40D5301CF1C00B559E8718028DA9012AD1BBEB42B01DF239FDC65FF "点击放大")

每个函数展开后为函数内的各个属性：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/iLx6H13dRIGLFXhzravNDA/zh-cn_image_0000002808887049.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5E57B3A122180A435F88F17FA769B706495F9684C4D84C2CCC520CD7D545A3D)

其中HomeObject表示父类对象，即该方法属于哪个对象；\_proto\_表示原型对象；LexicalEnv表示该函数的闭包上下文；name是内置属性访问器，可获取函数名；FunctionExtraInfo表示额外信息，比如一些napi接口会在这里记录函数地址；ProtoOrHClass表示原型或者隐藏类。

如果函数显示为anonymous()，则表示为匿名函数；如果函数显示为JSFunction()，则表示该函数可能为框架层函数，创建函数的时候未设置函数名。对于这两种函数名不可见的情况，可以通过查看其引用来间接确认其名称：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/tfGAptibQuKvdSbtdziB9g/zh-cn_image_0000002808766967.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=032A099D2048E4E24EB8CA6795019AA734CC5E25B6C8E44AC188948721A55041)

**ArkInternalConstantPool**

虚拟机创建的常量池，ArkTS代码层面不可见，涉及到的字符串常量会在（array）标签中展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/fpXtYmScTLK2wjxxuNOakQ/zh-cn_image_0000002779567372.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=B53CF8DFACA0F2220D270A105AD612B635CEEF084ABD9D695F935B072DE313F8 "点击放大")

**LexicalEnv**

闭包变量上下文；闭包是一个链状结构，如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/9wZkqcGES4qKqtkyVE6boA/zh-cn_image_0000002808766961.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E45E8087EC9BEAB7349C70907D32F1E8B8A70F8192CEF69C3FA7841281DD612)

733这个节点本身是一个闭包数组，其中0号元素是调用者（或者再往上的调用者，以此类推）的闭包；1号元素存储的是调试信息；2号及以后的元素存储的就是闭包传递的变量，上例传递了一个变量。

**InternalAccessor**

内置属性访问器，会有getter和setter方法，通过getter、setter可以获取、设置该属性。

**LocalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于（handle）标签中，用于管理JS对象生命周期的引用句柄（napi\_value）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ntiozhYzR9G97dNirhDbjA/zh-cn_image_0000002808887039.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=D5E692D4D929532A5A3422E1F9472E875D2C1BAAC7BD18F015EF0DA763A1E54A)

**GlobalHandleRoot**

DevEco Studio 6.1.0 Release版本新增，位于（handle）标签中，允许用户管理ArkTS/JS值的生命周期的引用句柄（napi\_ref），默认情况下不记录napi\_ref地址。

**GlobalHandleObject**

26.0.0版本新增，位于（handle）标签中，用于记录napi\_ref地址，并建立napi\_ref和ArkTS对象的引用关系。该功能需要先调用[@util.ArkTSVM.setTrackGlobalRef](../harmonyos-references/js-apis-util.md#settrackglobalref)接口使能 ，使能后会在快照导出过程中记录napi\_ref地址和引用关系。开发者可根据快照中napi\_ref相关信息，分析跨语言导致的内存泄漏。

如下图，ReferenceAddress:0x5b0b560160是napi\_ref地址，子节点是napi\_ref关联的ArkTS对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/HLfnw28BQfqiuR_51bK6NQ/zh-cn_image_0000002808887027.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=F917ECF77899D4DBAAF5831B1EFD25692B26ECE2A023497EE64BAFAB9262D862)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/S4Qx7muFQFiVM0dz75LTSA/zh-cn_image_0000002779407396.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=17CDA7B0994659D2F555613EC6F0047B8585AF143990046325CCBAFB167BBDE5)

对于实例化对象，一般没有constructor，则需要展开\_\_proto\_\_属性后查找constructor；

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/a7m3HL6ZTGOh7UHVBUc5yw/zh-cn_image_0000002808887043.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=B41F96CCC71695CA64A81CF46EC5DFD627BB85B7376C9CAA3FEC7BD231446B10)

若对象里有一些标志性属性，可以通过在代码里搜索属性名称来找到具体是哪个对象。

如果对象间有继承关系，则可以继续展开\_\_proto\_\_：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/aRZgx0jDQOqacfsLguKJDQ/zh-cn_image_0000002808766963.png?HW-CC-KV=V1&HW-CC-Date=20261128T023445Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C54D7D1687A1BBF5D31FF73C5BB63736FE66FBF165D352DB28FC65412E8BA74)

如上图则表明Man对象继承自People对象。

更多高频泄漏场景和ArkTS内存泄漏分析案例请参考[开发态快速定位ArkTS泄漏](../doccenter-app-quality/bpta-arkts-leak-in-develop.md)。
