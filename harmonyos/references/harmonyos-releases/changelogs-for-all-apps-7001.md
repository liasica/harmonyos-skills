---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-7001
title: 针对所有应用的变更
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > OS平台行为变更说明 > 26.0.0 Beta1引入的行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:27+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:5ed8495dfeefaa0d40fc945838a9cdc6ac772e69734c18d2357ae3981ecf5dee
---

## Ability Kit

### 部分公共事件行为变更，增加管控

**变更原因**

Ability Kit部分公共事件中包含应用信息，存在信息泄露的安全风险，需要增加管控。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

对于公共事件[COMMON\_EVENT\_PACKAGE\_ADDED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_added)、[COMMON\_EVENT\_PACKAGE\_REMOVED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_removed)、[COMMON\_EVENT\_PACKAGE\_CHANGED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_changed)、[COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_cache_cleared)的订阅方增加了管控。

* 变更前：系统应用和三方应用都可以监听到In-House应用相关事件。
* 变更后：系统应用可以监听In-House应用的相关事件，API版本26.0.0以下三方应用仍然可以监听In-House应用的相关事件，API版本26.0.0及以上三方应用如需监听In-House应用的相关事件则需要对应的In-House应用在app.json5的[allowListenBundleChangedEvent](../harmonyos-guides/app-configuration-file.md#配置文件标签)中配置本应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。

**起始 API Level**

9

**变更的接口/组件**

变更的公共事件列表：

| 事件名称 | 描述 |
| --- | --- |
| [COMMON\_EVENT\_PACKAGE\_ADDED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_added) | 应用安装完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_REMOVED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_removed) | 应用卸载完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_CHANGED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_changed) | 应用更新完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_cache_cleared) | 应用缓存数据清理完成的事件。 |

**适配指导**

API版本26.0.0及以上的三方应用如需监听In-House应用的相关事件，需要对应的In-House应用在app.json5的[allowListenBundleChangedEvent](../harmonyos-guides/app-configuration-file.md)中配置本应用的[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)。

## ArkTS

### JSVM基于上游社区的Chromium/v8内核从132升级为144版本

**变更原因**

为了提升使用JSVM应用的安全性，为开发者提供最新的W3C HTML5特性，Chromium上游社区从133到144版本共发布300+项特性，带来了更多W3C特性、安全、性能、稳定性的提升，故本次进行内核升级 (132 -> 144)。

**变更影响**

从上游社区300+ issue说明、社区5000+ ReleaseNotes以及JSVM xts/tdd用例测试，当前共发现38项需要开发者注意的变更点，请参考[JSVM 132 内核升级 144 内核版本差异总结](https://gitcode.com/openharmony/arkcompiler_jsvm/blob/master/ReleaseNote/JSVM_132_144.md)。

**起始 API Level**

不涉及

**变更的接口/组件**

ArkTS/JSVM

**适配指导**

如果在应用中使用Web组件展示网页内容，则需要遵循[JSVM 132 内核升级 144 内核版本差异总结](https://gitcode.com/openharmony/arkcompiler_jsvm/blob/master/ReleaseNote/JSVM_132_144.md)中所涉及的最新W3C规格变更。

### async函数类型判定修复

**变更原因**

在类中getter/setter之后定义的async函数，实际被初始化的类型为普通函数，导致无法在运行时正确地判定函数类型。

**变更影响**

1. 由于async的行为并不依赖函数类型，而是通过特定的字节码实现的，此变更前后async的语义均无问题。
2. 该变更会修复在运行时对async函数进行的类型判定，具体行为变化如下：

   变更前：

   在类中getter/setter（@State变量经过编译也会在TS中生成对应的getter/setter）之后定义的async函数：

   1. new util.types().isAsyncFunction 判断为false。
   2. (async () => {}).constructor.name 的结果为："Function"。
   3. worker通过callGlobalCallObjectMethod调用返回的错误码及错误信息为："10200006 An exception occurred during serialization"。

   变更后：

   在类中getter/setter（@State变量经过编译也会在TS中生成对应的getter/setter）之后定义的async函数：

   1. new util.types().isAsyncFunction 判断为true。
   2. (async () => {}).constructor.name 的结果为："AsyncFunction"。
   3. worker通过callGlobalCallObjectMethod调用返回的错误码及错误信息为："10200020 The method to be called is not callable or is an async method or a generator"。

具体的代码示例如下：

```screen
import { util } from '@kit.ArkTS';

class Model {
  // 在类中getter setter之前定义的async function，类型正确。
  async testFunction1() {}
  get id() { return 1 }
  set id(id) {}
  // 在类中getter setter之后定义的async function，类型不正确，应当为AsyncFunction，实际为普通Function。
  async testFunction2() {}
}

@Entry
@Component
struct Index {
  // 在类中getter setter之前定义的async function，类型正确。
  async testFunction1() {}
  // 经过编译也会生成getter setter
  @State message: string = 'Hello World';
  // 在类中getter setter之后定义的async function，类型不正确，应当为AsyncFunction，实际为普通Function。
  async testFunction2() {}
  build() {
    RelativeContainer() {
      Text(this.message)
        .onClick(() => {
          let model: Model = new Model();
          let type = new util.types();

          // 输出true，行为是正确的，该变更无影响。
          console.info(`${type.isAsyncFunction(this.testFunction1)}`);
          console.info(`${type.isAsyncFunction(model.testFunction1)}`);
          // 输出AsyncFunction，行为是正确的，该变更无影响。
          console.info(this.testFunction1.constructor.name);
          console.info(model.testFunction1.constructor.name);

          // 输出false，变更后输出true。
          console.info(`${type.isAsyncFunction(this.testFunction2)}`);
          console.info(`${type.isAsyncFunction(model.testFunction2)}`);
          // 输出Function，变更后输出AsyncFunction。
          console.info(this.testFunction2.constructor.name);
          console.info(model.testFunction2.constructor.name);
        })
    }
  }
}
```

**起始 API Level**

API 8

**变更的接口/组件**

1. new util.types().isAsyncFunction
2. Function.constructor.name

**适配指导**

默认行为变更，开发者需排查new util.types().isAsyncFunction和Function.constructor.name的调用点，审视接口输出结果的变化是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行相应的适配。

### JSVM支持Wasm解释器，jitless默认行为发生变更

**变更原因**

需要支持jitless条件下执行Wasm能力，支撑坚盾守护模式下特效/直播等业务场景。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

JSVM Wasm相关接口补充了jitless下默认行为，不再返回错误码[JSVM\_JIT\_MODE\_EXPECTED](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h#jsvm_status)，Wasm解释器正常运行。

变更前：

[OH\_JSVM\_CompileWasmModule](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilewasmmodule)，返回错误码 [JSVM\_JIT\_MODE\_EXPECTED](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h#jsvm_status)，并设置JSVM异常。

[OH\_JSVM\_CompileWasmFunction](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilewasmfunction)，返回错误码 [JSVM\_JIT\_MODE\_EXPECTED](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h#jsvm_status)，并设置JSVM异常。

[OH\_JSVM\_CreateWasmCache](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_createwasmcache)，返回错误码 [JSVM\_JIT\_MODE\_EXPECTED](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h#jsvm_status)，并设置JSVM异常。

变更后：

[OH\_JSVM\_CompileWasmModule](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilewasmmodule)，WasmCache不生效，其他行为与JIT模式一致。

[OH\_JSVM\_CompileWasmFunction](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_compilewasmfunction)，直接返回JSVM\_OK（解释执行不依赖当前接口）。

[OH\_JSVM\_CreateWasmCache](http://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-h#oh_jsvm_createwasmcache)，直接返回JSVM\_OK，并将WasmCache置为空。

**起始 API Level**

12

**变更的接口/组件**

ArkTS/JSVM

**适配指导**

开发者需要检视调用OH\_JSVM\_CompileWasmModule，OH\_JSVM\_CompileWasmFunction，OH\_JSVM\_CreateWasmCache三个接口的代码上下文，判断接口返回值从“返回错误码”变更为“返回JSVM\_OK”对代码逻辑造成的影响，按照代码预期修改代码。

### 修复ConvertXML的fastConvertToJSObject接口解析时丢失同级text节点的问题

**变更原因**

ConvertXML的[fastConvertToJSObject](../harmonyos-references/js-apis-convertxml.md#fastconverttojsobject14)接口在解析XML时，若XML内容包含子元素、与子元素同级的文本节点，会丢失与子元素同级的文本节点。此变更修复了该问题。

**变更影响**

此变更涉及应用适配。

变更前：fastConvertToJSObject接口在解析XML时，若XML内容包含子元素、与子元素同级的文本节点，会丢失与子元素同级的文本节点。例如解析 <root>text1<child>子元素</child>text2</root> 时，与子元素同级的文本节点"text1"和"text2"会丢失。

变更后：fastConvertToJSObject接口在解析XML时，若XML内容包含子元素、与子元素同级的文本节点，会正确保留与子元素同级的文本节点。

**起始 API Level**

14

**变更的接口/组件**

fastConvertToJSObject(xml: string, options?: ConvertOptions) : Object;

**适配指导**

排查应用中是否使用了fastConvertToJSObject接口解析XML内容有包含子元素、与子元素同级的文本节点数据，并检查解析结果是否依赖原有的丢失同级文本节点的行为。

例如：

```typescript
import { convertxml } from '@kit.ArkTS';

let xml = '<wrapper>前缀文本<child>子内容</child>后缀文本</wrapper>';
let conv = new convertxml.ConvertXML();
let result = JSON.stringify(conv.fastConvertToJSObject(xml));
console.info(result);
```

变更前该用例输出为：

```json
{"_elements":[{"_type":"element","_name":"wrapper","_elements":[{"_type":"element","_name":"child","_parent":"wrapper","_elements":[{"_type":"text","_text":"子内容"}]}]}]}
```

变更后该用例输出为：

```json
{"_elements":[{"_type":"element","_name":"wrapper","_elements":[{"_type":"text","_text":"前缀文本"},{"_type":"element","_name":"child","_parent":"wrapper","_elements":[{"_type":"text","_text":"子内容"}]},{"_type":"text","_text":"后缀文本"}]}]}
```

本变更修复该问题，fastConvertToJSObject接口现在能够正确解析并保留与子元素同级的文本节点。

## ArkUI

### NodeAdapter的onAttachToNode回调触发时机变更

**变更原因**

NodeAdapter绑定的宿主节点在主树挂载时，ArkTS API会触发onAttachToNode回调，C API会触发OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver绑定的、事件类型为NODE\_APPEAR\_EVENT\_WILL\_ATTACH\_TO\_NODE的回调，与文档描述的在绑定时触发回调的时机不符。

**变更影响**

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：NodeAdapter所绑定的宿主节点上主树时，ArkTS API会触发NodeAdapter的onAttachToNode回调，C API会触发OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver绑定的、事件类型为NODE\_APPEAR\_EVENT\_WILL\_ATTACH\_TO\_NODE的回调。

变更后：NodeAdapter被绑定到宿主节点时，ArkTS API触发onAttachToNode的回调，C API触发OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver绑定的、事件类型为NODE\_APPEAR\_EVENT\_WILL\_ATTACH\_TO\_NODE的回调。

**起始 API Level**

12

**变更的接口/组件**

[onAttachToNode](../harmonyos-references/js-apis-arkui-framenode.md#onattachtonode12)

[OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeadapter_registereventreceiver)

**适配指导**

* onAttachToNode触发时节点未上树

  在使用[attachNodeAdapter](../harmonyos-references/js-apis-arkui-framenode.md#attachnodeadapter12)接口为FrameNode绑定NodeAdapter时，节点可能尚未完全挂载。因此，建议在FrameNode绑定NodeAdapter时的onAttachToNode回调中，注册[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)，并将访问布局信息或执行动画等强依赖主树的操作放入其中，避免因节点未上树引发的执行异常。

  ```ts
  import { NodeAdapter, NodeController, FrameNode, typeNode, UIContext } from '@kit.ArkUI';
  import hilog from '@ohos.hilog';

  class MyNodeAdapter extends NodeAdapter {
    private rootNode: FrameNode | undefined;

    setRootNode(node: FrameNode) {
      this.rootNode = node;
    }

    // 从API版本26.0.0开始，当NodeAdapter绑定到宿主节点时，会调用如下回调
    onAttachToNode(): void {
      // 适配前：直接在此处执行依赖主树的逻辑，可能因节点未上树引发执行异常
      // this.doWhenNodeAttached();

      // 适配后：通过onAppear确保节点已挂载
      this.rootNode?.commonEvent.setOnAppear(() => {
        this.doWhenNodeAttached();
      });
    }

    private doWhenNodeAttached() {
      hilog.info(0x0000, 'testTag', 'Node is now attached to main tree');
    }
  }

  class MyNodeController extends NodeController {
    private adapter: MyNodeAdapter | undefined;

    makeNode(uiContext: UIContext): FrameNode | null {
      this.adapter = new MyNodeAdapter();
      const rootNode = typeNode.createNode(uiContext, 'List');
      rootNode.commonAttribute.width(200).height(200);

      // 将宿主节点传递给adapter，以便在onAttachToNode中注册onAppear
      this.adapter.setRootNode(rootNode);

      // 绑定adapter，此时会触发onAttachToNode回调
      NodeAdapter.attachNodeAdapter(this.adapter, rootNode);

      return rootNode;
    }
  }
  ```
* onAttachToNode回调在attachNodeAdapter前设置

  变更前，onAttachToNode生命周期回调，是在通过attachNodeAdapter接口将节点成功挂载到主树之后触发，因此attachNodeAdapter的调用与onAttachToNode回调函数的设置之间并无严格的时序要求。变更后，调用attachNodeAdapter后会立即触发onAttachToNode回调。因此变更后必须在调用attachNodeAdapter之前，设置onAttachToNode回调，否则将导致回调无法被触发，适配指导如下。

  ```ts
   import { FrameNode, NodeAdapter, NodeController, typeNode, UIContext } from '@kit.ArkUI';

   class NodeAdapterTest extends NodeAdapter {
    uiContext:UIContext;
    frameNodeList:Array<FrameNode> = new Array();
    totalNodeCount_:number;
    public onAttachToNodeFunc:undefined|Function = undefined;
    constructor(uiContext:UIContext) {
      super();
      this.uiContext = uiContext;
      this.totalNodeCount_ = 10;
      this.totalNodeCount = this.totalNodeCount_;
      this.initItem();
    }
    initItem(){
      for(let i=0;i<this.totalNodeCount;i++) {
        let textNode = typeNode.createNode(this.uiContext,'Text');
        textNode.initialize('this is '+i+' node');
        this.frameNodeList.push(textNode);
      }
    }
    onAttachToNode():void {
      if(this.onAttachToNodeFunc) {
        this.onAttachToNodeFunc()
      }
    }
    onGetChildId(index: number):number {
      return index;
    }
    onCreateChild(index: number): FrameNode {
      return this.frameNodeList[index];
    }

  }
  class TestController extends NodeController {
    nodeAdapterTest: NodeAdapterTest | undefined;
    rootNode:FrameNode|undefined ;
    makeNode(uiContext: UIContext): FrameNode | null {
      this.nodeAdapterTest =new NodeAdapterTest(uiContext)
      let rootNode = typeNode.createNode(uiContext, 'Column');
      rootNode.commonAttribute.width(200);
      rootNode.commonAttribute.height(200);

      // 适配后，onAttachToNode中使用的变量必须在attachNodeAdapter前赋值
      this.nodeAdapterTest.onAttachToNodeFunc = ()=>{
        hilog.info(0x0000, 'testTag', 'on attach to NodeAdapter');
      }
      NodeAdapter.attachNodeAdapter(this.nodeAdapterTest, rootNode);
     
      // 适配前，onAttachToNode中使用的变量可以在attachNodeAdapter后赋值
      this.nodeAdapterTest.onAttachToNodeFunc = ()=>{
         hilog.info(0x0000, 'testTag', 'on attach to NodeAdapter');
      }
     
      return rootNode;
    }
  }

  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';

    build() {
      Row() {
        Column() {
          NodeContainer(new TestController())
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```
* OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver绑定方法触发时节点未上树

  在NDK开发中，如果通过[OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeadapter_registereventreceiver)注册了事件相关回调，并且回调事件枚举为NODE\_APPEAR\_EVENT\_WILL\_ATTACH\_TO\_NODE，该事件会在NodeAdapter绑定宿主节点后立即触发。由于此时节点可能尚未完全挂载，如果事件回调逻辑依赖宿主节点已挂载的状态（如访问布局信息或执行动画），需要将该部分逻辑迁移至宿主节点的onAppear回调中执行，具体示例如下。

  ```c
  #include <arkui/native_node.h>
  #include <arkui/native_interface.h>
  #include <stdio.h>
  #include <hilog/log.h>

  // 组件挂载时的回调函数
  static void OnAppear(ArkUI_NodeEvent* event) {
      OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, LOG_PRINT_TEXT, "Node is now attached to main tree");
  }

  // NodeAdapter事件监听器
  static void OnNodeAdapterEvent(ArkUI_NodeAdapterEvent* event, void* userData) {
      ArkUI_NodeAdapterEventType eventType = OH_ArkUI_NodeAdapterEvent_GetType(event);
      
      if (eventType == NODE_ADAPTER_EVENT_ON_ADD_NODE_TO_ADAPTER) {
          // 获取需要创建组件的索引位置
          uint32_t index = OH_ArkUI_NodeAdapterEvent_GetItemIndex(event);
          
          // 创建子组件
          ArkUINodeHandle childNode = OH_ArkUI_Node_Create("Text");
          
          // 获取NativeNodeAPI实例
          ArkUI_NativeNodeAPI_1* nativeNodeAPI = OH_ArkUI_GetNativeNodeAPI();
          
          // 设置子组件属性
          ArkUI_NumberValue widthValue[] = {{.f32 = 100.0f}};
          ArkUI_AttributeItem widthItem = {widthValue, 1, nullptr, nullptr};
          nativeNodeAPI->setAttribute(childNode, NODE_WIDTH, &widthItem);
          
          ArkUI_NumberValue heightValue[] = {{.f32 = 50.0f}};
          ArkUI_AttributeItem heightItem = {heightValue, 1, nullptr, nullptr};
          nativeNodeAPI->setAttribute(childNode, NODE_HEIGHT, &heightItem);
          
          // 将创建的组件返回给Adapter
          OH_ArkUI_NodeAdapterEvent_SetItem(event, childNode);
          
          // 为子组件注册onAppear事件
          nativeNodeAPI->registerNodeEvent(childNode, NODE_EVENT_ON_APPEAR, 0, NULL);
          nativeNodeAPI->addNodeEventReceiver(childNode, OnAppear);
      }
  }

  ArkUINodeHandle CreateRootNode(ArkUINodeAdapterHandle adapter) {
      // 1. 创建List容器节点
      ArkUINodeHandle listNode = OH_ArkUI_Node_Create("List");
      
      // 获取NativeNodeAPI实例
      ArkUI_NativeNodeAPI_1* nativeNodeAPI = OH_ArkUI_GetNativeNodeAPI();
      
      // 2. 设置List的基本属性
      ArkUI_NumberValue widthValue[] = {{.f32 = 200.0f}};
      ArkUI_AttributeItem widthItem = {widthValue, 1, nullptr, nullptr};
      nativeNodeAPI->setAttribute(listNode, NODE_WIDTH, &widthItem);
      
      ArkUI_NumberValue heightValue[] = {{.f32 = 200.0f}};
      ArkUI_AttributeItem heightItem = {heightValue, 1, nullptr, nullptr};
      nativeNodeAPI->setAttribute(listNode, NODE_HEIGHT, &heightItem);
      
      // 3. 设置NodeAdapter的总节点数量
      OH_ArkUI_NodeAdapter_SetTotalNodeCount(adapter, 100);
      
      // 4. 注册NodeAdapter事件监听器
      OH_ArkUI_NodeAdapter_RegisterEventReceiver(adapter, NULL, OnNodeAdapterEvent);
      
      // 5. 将NodeAdapter作为属性绑定到List节点
      // 不再使用OH_ArkUI_NodeAdapter_Attach，而是通过setAttribute设置
      ArkUI_AttributeItem adapterItem = {nullptr, 0, nullptr, adapter};
      nativeNodeAPI->setAttribute(listNode, NODE_LIST_NODE_ADAPTER, &adapterItem);
      
      return listNode;
  }
  ```
* OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver绑定方法在NodeAdapter绑定节点前设置

  开发者在NodeAdapter绑定宿主节点时，必须提前为NodeAdapter注册相关回调事件。如果OH\_ArkUI\_NodeAdapter\_RegisterEventReceiver回调中包含NODE\_APPEAR\_EVENT\_WILL\_ATTACH\_TO\_NODE事件的处理逻辑，必须将这部分逻辑前移至绑定宿主节点前，以确保事件正常执行。

  ```c
  static void OnNodeAdapterEvent(ArkUINodeAdapterEvent* event, void* userData) {
      if (event->type == NODE_APPEAR_EVENT_WILL_ATTACH_TO_NODE) {
          // 处理添加节点事件
      }
  }

  void SetupAdapter(ArkUINodeAdapterHandle adapter, ArkUINodeHandle rootNode) {
       
      // 适配前，先绑定宿主节点再注册事件监听
      ArkUI_AttributeItem adapterItem = {nullptr, 0, nullptr, adapter};
      // 绑定宿主节点
      nativeNodeAPI->setAttribute(listNode, NODE_LIST_NODE_ADAPTER, &adapterItem);
      // 设置事件监听
      OH_ArkUI_NodeAdapter_RegisterEventReceiver(adapter, OnNodeAdapterEvent, NULL);
     
      // 适配后，先注册事件监听再绑定宿主节点
      // 设置事件监听
      OH_ArkUI_NodeAdapter_RegisterEventReceiver(adapter, OnNodeAdapterEvent, NULL);
      ArkUI_AttributeItem adapterItem = {nullptr, 0, nullptr, adapter};
      // 绑定宿主节点
      nativeNodeAPI->setAttribute(listNode, NODE_LIST_NODE_ADAPTER, &adapterItem);
  }
  ```

### 鼠标事件rawDeltaX和rawDeltaY的返回值变更

**变更原因**

鼠标事件rawDeltaX和rawDeltaY的返回值的含义为鼠标设备在二维平面的物理移动偏移量，其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示，上报由鼠标硬件本身决定。当前实现返回值并非是原始移动数据，而是原始移动数据缩小了X倍，X为系统的显示大小比例。因此需要变更返回值使其符合本身的含义。

**变更影响**

此变更涉及应用适配。

* 变更前：rawDeltaX和rawDeltaY的返回值并非鼠标硬件的原始移动数据，而是原始数据缩小了X倍，X为系统的显示大小比例。
* 变更后：rawDeltaX和rawDeltaY的返回值为鼠标硬件的原始移动数据。

**起始API Level**

15

**变更的接口/组件**

[rawDeltaX](../harmonyos-references/ts-universal-mouse-key.md#mouseevent对象说明)、[rawDeltaY](../harmonyos-references/ts-universal-mouse-key.md#mouseevent对象说明)、[OH\_ArkUI\_MouseEvent\_GetRawDeltaX](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_mouseevent_getrawdeltax)和[OH\_ArkUI\_MouseEvent\_GetRawDeltaY](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_mouseevent_getrawdeltay)。

**适配指导**

如需恢复为变更前的效果，可以使用[px2vp](../harmonyos-references/arkts-apis-uicontext-uicontext.md#px2vp12)接口获取变更之前的值。

```ts
// xxx.ets
@Entry
@Component
struct MouseEventExample {
  @State mouseText: string = '';

  build() {
    Column({ space: 20 }) {
      Button('onMouse')
        .width(180).height(80)
        .fontSize(24)
        .onMouse((event: MouseEvent): void => {
          if (event) {
            this.mouseText = 'rawDeltaX = ' + this.getUIContext().px2vp(event.rawDeltaX) +
              '\nrawDeltaY = ' + this.getUIContext().px2vp(event.rawDeltaY);
          }
        })
      Text(this.mouseText)
    }.padding({ top: 30 }).width('100%')
  }
}
```

### 属性字符串段落首个占位为CustomSpan或ImageAttachment时，支持设置段落样式

**变更原因**

历史版本中，[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)或[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)在创建时未拷贝段落样式。因此，当属性字符串段落的首个占位为[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)或[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)时，段落样式不生效。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：如果属性字符串段落内首个占位为[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)或[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)，设置在该段落上的段落样式不生效。

变更后：如果属性字符串段落内首个占位为[CustomSpan](../harmonyos-references/ts-universal-styled-string.md#customspan)或[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)，设置在该段落上的段落样式生效。

**起始 API Level**

12

**变更的接口/组件**

[ParagraphStyle](../harmonyos-references/ts-universal-styled-string.md#paragraphstyle)

**适配指导**

接口默认效果变更，开发者需审视此变更是否对自身相关业务展示效果产生影响，若有影响需根据自身业务代码进行对应适配。

以下示例代码将属性字符串段落中类型为[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)的首个占位，设置段落样式为[TextAlign](../harmonyos-references/ts-appendix-enums.md#textalign).End。

```ts
// xxx.ets
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct styled_string_paraStyle_demo {
  mutableStr: MutableStyledString = new MutableStyledString('TextAlign:End', [{
    start: 0,
    length: 5,
    styledKey: StyledStringKey.PARAGRAPH_STYLE,
    styledValue: new ParagraphStyle({
      textAlign: TextAlign.End
    })
  }]);
  mutableStr2: MutableStyledString = new MutableStyledString('TextAlign:End');
  controller: TextController = new TextController();
  controller2: TextController = new TextController();

  build() {
    Row() {
      Column({ space: 5 }) {
        Text(undefined, { controller: this.controller })
          .copyOption(CopyOptions.InApp)
          .draggable(true)
          .fontSize(30)
          .borderWidth(1)
          .width(300)
          .onAppear(() => {
            this.controller.setStyledString(this.mutableStr);
          })
        Text(undefined, { controller: this.controller2 })
          .copyOption(CopyOptions.InApp)
          .draggable(true)
          .fontSize(30)
          .borderWidth(1)
          .width(300)
          .onAppear(() => {
            this.mutableStr2.insertStyledString(0, new MutableStyledString(new ImageAttachment({
              resourceValue: $r('app.media.startIcon'),
              size: { width: 50, height: 50 },
              layoutStyle: { borderRadius: LengthMetrics.vp(10) },
              verticalAlign: ImageSpanAlignment.BASELINE,
              objectFit: ImageFit.Contain,
              syncLoad: true
            })))
            this.mutableStr2.setStyle({
              start: 0,
              length: 5,
              styledKey: StyledStringKey.PARAGRAPH_STYLE,
              styledValue: new ParagraphStyle({
                textAlign: TextAlign.End
              })
            }) // API版本26.0.0前，设置的TextAlign.End不会生效
            this.controller2.setStyledString(this.mutableStr2);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### LayoutPolicy.matchParent父组件为Row、Column、Flex组件时，单方向设置matchParent的子组件布局行为变更

**变更原因**

当前Row、Column、Flex组件布局过程中，单方向设置matchParent的子组件不会参与父组件的尺寸计算。变更后，Row、Column、Flex组件会自适应单方向matchParent子组件尺寸，布局效果更符合API语义。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：当Row、Column、Flex组件主轴尺寸自适应子组件，且子组件A仅交叉轴设置matchParent时，子组件A不参与Row、Column、Flex组件的主轴尺寸测量过程，此时Row、Column、Flex组件主轴方向不自适应子组件A的尺寸。交叉轴方向同理。

变更后：当Row、Column、Flex组件主轴尺寸自适应子组件，且子组件A仅交叉轴设置matchParent时，子组件A会参与Row、Column、Flex组件的主轴尺寸测量过程，此时Row、Column、Flex组件主轴方向会自适应子组件A的尺寸。交叉轴方向同理。

例如：运行以下示例，进入页面后观察父组件Column的大小。变更前Column组件只会被第一个子组件撑大，变更后，Column组件高度自适应第一个和第二个子组件，宽度自适应第一个和第三个子组件。

```ts
@Entry
@Component
struct Demo {
  build() {
    Column() {
      Column({space: "30px"}) {
        Column()
          .width("200px")
          .height("200px")
          .backgroundColor('rgb(0, 74, 175)')

        Column()
          .width(LayoutPolicy.matchParent)
          .height("200px")
          .backgroundColor('rgb(0, 74, 175)')

        Column()
          .width("400px")
          .height(LayoutPolicy.matchParent)
          .backgroundColor('rgb(0, 74, 175)')
      }
      .width(LayoutPolicy.wrapContent)
      .height(LayoutPolicy.wrapContent)
      .backgroundColor('rgb(39, 135, 217)')
      .padding("30px")
    }.width("100%")
  }
}
```

变更前后效果如下：

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始 API Level**

15

**变更的接口/组件**

涉及组件：[Row](../harmonyos-references/ts-container-row.md)、[Column](../harmonyos-references/ts-container-column.md)、[Flex](../harmonyos-references/ts-container-flex.md)。

涉及接口：[LayoutPolicy.matchParent](../harmonyos-references/ts-universal-attributes-size.md#layoutpolicy15)。

**适配指导**

默认行为变更，但开发者需审视此变更是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行适配。如果开发者要用原先的布局效果，可以根据未设置matchParent的子组件手动设置父组件尺寸。

### EmbeddedComponent获焦能力变更

**变更原因**

[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)获焦后，其拉起的EmbeddedUIExtensionAbility窗口内焦点不会停留在容器组件，而是下发到容器内第一个可获焦子节点。当获焦节点为[TextInput](../harmonyos-references/ts-basic-components-textinput.md)时，会出现软键盘被意外拉起的情况。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：EmbeddedComponent获焦时，如果外部走焦到EmbeddedUIExtensionAbility，焦点正常下发到第一个可获焦子节点；如果由于层级页面切换导致焦点转移到EmbeddedUIExtensionAbility，在EmbeddedUIExtensionAbility页面内未设置[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)、未[主动请求焦点](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)时，焦点仍然下发到第一个可获焦子节点。

变更后：EmbeddedComponent获焦时，如果外部走焦到EmbeddedUIExtensionAbility，焦点正常下发到第一个可获焦子节点；如果由于层级页面切换导致焦点转移到EmbeddedUIExtensionAbility，则与UIAbility保持统一规则，两者在拉起一个层级页面且该页面未设置[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)、未[主动请求焦点](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)时，焦点均停留在根容器，不下发到子节点。

**起始 API Level**

18

**变更的接口/组件**

[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)

**适配指导**

在由于层级页面切换导致焦点转移到EmbeddedUIExtensionAbility的场景下，焦点默认停留在根容器。如果期望第一个可获焦子组件自动获焦，可以通过如下两种方式显式设置焦点。

* 方式一：在EmbeddedUIExtensionAbility的页面中，通过将[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)设置为true，使得第一个可获焦子组件成为层级页面的默认焦点。

  ```ts
  @Entry
  @Component
  struct UIExtensionPage {
    build() {
      Column({ space: 20 }) {
        TextInput({ placeholder: 'Input something...' })
          .width(300)
          .height(50)
          .defaultFocus(true)

        Button('Submit')
          .width(200)
          .height(50)
      }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    }
  }
  ```

* 方式二：在EmbeddedUIExtensionAbility的页面中，通过[requestFocus](../harmonyos-guides/arkts-common-events-focus-event.md#主动获焦失焦)主动为第一个可获焦子组件请求焦点。

  ```ts
  @Entry
  @Component
  struct UIExtensionPage {
    build() {
      Column({ space: 20 }) {
        TextInput({ placeholder: 'Input something...' })
          .width(300)
          .height(50)
          .id('targetInput')

        Button('Submit')
          .width(200)
          .height(50)
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .onAppear(() => {
        this.getUIContext().getFocusController().requestFocus('targetInput');
      })
    }
  }
  ```

### WithTheme相关组件行为变更

**变更原因**

为提升主题功能的一致性与完整性，对下述场景下的组件行为进行优化适配。

1. 当前已支持[WithTheme](../harmonyos-references/ts-container-with-theme.md)的组件，在特定场景下部分组件未能正确应用[WithTheme](../harmonyos-references/ts-container-with-theme.md)所设置的主题样式，与预期设计效果不符。

   * 弹窗类组件不跟随宿主节点的局部主题或深浅色样式。
   * 部分组件（组件范围见**场景二**）动态添加至[WithTheme](../harmonyos-references/ts-container-with-theme.md)中后，不会跟随局部主题或深浅色变化而变化（例如通过ForEach+ListItem，将组件添加到WithTheme组件下）。
2. 对于暂不支持[WithTheme](../harmonyos-references/ts-container-with-theme.md)的组件，其样式不会响应WithTheme或默认主题[setDefaultTheme](../harmonyos-references/js-apis-arkui-theme.md#setdefaulttheme)设置的主题样式。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

**场景一：弹窗类组件跟随宿主节点的WithTheme样式**

变更前：宿主节点的[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)、[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)、[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)、[CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md)弹窗类组件弹出时，不跟随宿主节点的局部主题或深浅色样式。

变更后：宿主节点的[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)、[bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup)、[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)、[CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md)弹窗类组件弹出时，会跟随宿主节点的局部主题或深浅色样式。

**场景二：动态添加到WithTheme的组件响应主题变化**

变更前：当WithTheme的主题样式或深浅色发生动态变化时，后续动态添加到WithTheme中的组件不会同步响应这些变化。

变更后：当WithTheme的主题样式或深浅色发生动态变化时，后续动态添加到WithTheme中的组件会同步响应这些变化。

| 涉及场景 | 涉及组件 |
| --- | --- |
| 动态添加场景 | [Button](../harmonyos-references/ts-basic-components-button.md)、[Menu](../harmonyos-references/ts-basic-components-menu.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、[TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)、[Counter](../harmonyos-references/ts-container-counter.md)、[Progress](../harmonyos-references/ts-basic-components-progress.md)、[TextClock](../harmonyos-references/ts-basic-components-textclock.md)、[LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)、[Tabs](../harmonyos-references/ts-container-tabs.md)、[TabContent](../harmonyos-references/ts-container-tabcontent.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)、[Indicator](../harmonyos-references/ts-swiper-components-indicator.md)。 |

**场景三：组件新增WithTheme支持能力**

变更前：组件不受WithTheme或setDefaultTheme设置的样式影响，显示为系统默认样式。

变更后：组件会响应WithTheme或setDefaultTheme设置的样式，并优先显示对应的主题效果。

| 涉及场景 | 涉及组件 |
| --- | --- |
| 组件新增WithTheme支持能力 | [TextArea](../harmonyos-references/ts-basic-components-textarea.md)、[Search](../harmonyos-references/ts-basic-components-search.md)、[RichEditor](../harmonyos-references/ts-basic-components-richeditor.md)、[Image](../harmonyos-references/ts-basic-components-image.md)、[ImageAnimator](../harmonyos-references/ts-basic-components-imageanimator.md)、[PatternLock](../harmonyos-references/ts-basic-components-patternlock.md)、[QRCode](../harmonyos-references/ts-basic-components-qrcode.md)、[DataPanel](../harmonyos-references/ts-basic-components-datapanel.md)、[文本选择菜单](../harmonyos-references/ts-basic-components-text.md)、[Badge](../harmonyos-references/ts-container-badge.md)、[styleString](../harmonyos-references/ts-universal-styled-string.md)、[LocalBuilder](../harmonyos-guides/arkts-localbuilder.md)、[Tabs](../harmonyos-references/ts-container-tabs.md)、[TabContent](../harmonyos-references/ts-container-tabcontent.md)、[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)、[ListItem](../harmonyos-references/ts-container-listitem.md)、[ArcListItem](../harmonyos-references/ts-container-arclistitem.md)、[GridItem](../harmonyos-references/ts-container-griditem.md)、[Refresh](../harmonyos-references/ts-container-refresh.md)、[TextPicker](../harmonyos-references/ts-basic-components-textpicker.md)、[TimePicker](../harmonyos-references/ts-basic-components-timepicker.md)、[DatePicker](../harmonyos-references/ts-basic-components-datepicker.md)、[CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md)、[UIPickerComponent](../harmonyos-references/ts-container-ui-picker-component.md)、[MenuItem](../harmonyos-references/ts-basic-components-menuitem.md)和[menuItemGroup](../harmonyos-references/ts-basic-components-menuitemgroup.md)。 |

**起始API Level**

12

**变更的接口/组件**

WithThemeInterface、setDefaultTheme。

**适配指导**

1. 若希望上述组件在WithTheme下保持变更前的行为，即继续跟随系统样式或系统深浅色模式，可将该组件放入WithTheme({ colorMode: ThemeColorMode.SYSTEM })组件下。

   ```ts
   @Entry
   @Component
   struct WithThemeExample {
     @State message: string = 'Hello World';
     @State arr: number[] = [];
     private index: number = 0;
     build() {
       Row() {
         Column() {
           Button("Add Element")
             .onClick(() => {
               this.arr.push(this.index++);
             })
           WithTheme({ colorMode: ThemeColorMode.DARK }) {
             List() {
               ForEach(this.arr, (item: number, index) => {
                 ListItem() {
                   Column() {
                     WithTheme({ colorMode: ThemeColorMode.SYSTEM }) {
                       Column() {
                         Button("Button In ForEach with COLOR_MODE_SYSTEM")
                       }
                     }
                   }
                 }
               })
             }
             .width('100%')
             .height('100%')
           }
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. 如果WithTheme容器内的部分组件使用了固定颜色值，组件放入WithTheme中，生效WithTheme设置的样式时，可能影响显示效果。可通过将该组件放入新的WithTheme容器中，并将该容器的colorMode设置为ThemeColorMode.SYSTEM，恢复为变更前的行为。

   ```ts
   @Entry
   @Component
   struct WithThemeExample {
     @State arr: number[] = [];
     private index: number = 0

     build() {
       Row() {
         Column() {
           Button("Add Element")
             .onClick(() => {
               this.arr.push(this.index++);
             })
           WithTheme({ colorMode: ThemeColorMode.DARK }) {
             List() {
               ForEach(this.arr, (item: number, index) => {
                 ListItem() {
                   WithTheme({ colorMode: ThemeColorMode.SYSTEM }) {
                     Column() {
                       Text("Set ColorMode SYSTEM")
                         .fontColor("#FF383838")
                     }
                     .backgroundColor($r('sys.color.background_primary'))

                   }
                 }
               })
             }
             .width('100%')
             .height('100%')
           }
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

### ArkUI接口新增仅支持Stage模型的约束

**变更原因**

ArkUI存在API接口未明确标注所支持的模型标签，导致DevEco Studio和开发者无法准确感知FA模型和Stage模型的支持情况。

**变更影响**

此变更涉及应用适配。

变更前：ArkUI提供的API version 10及以上版本的接口，如果未明确标注模型标签，可在FA模型工程中使用。

变更后：ArkUI提供的API version 10及以上版本的接口，均补充仅支持Stage模型的标签，此时接口无法在FA模型中使用，会产生编译报错。

**起始 API Level**

10

**变更的接口/组件**

ArkUI API version 10及以上的全量接口。

**适配指导**

推荐使用Stage模型。Stage模型是当前系统主推的应用模型，请参考[应用模型开发概述](../harmonyos-guides/stage-model-development-overview.md)了解模型差异。

### 主页NavDestination中使用queryNavDestinationInfo接口和onResult接口的行为变更

**变更原因**

1. 通过queryNavDestinationInfo(isInner: Optional<boolean>)接口无法获取到主页NavDestination的信息，不符合接口设计规格。
2. 主页NavDestination的onResult接口在如下场景中表现不符合预期，具体场景为：开发者使用了主页NavDestination，且操作前栈为PageA（未设置onResult）、PageB。从PageB返回到PageA时，会触发主页NavDestination的onResult，不符合接口设计规格。

**变更影响**

变更前：

1. 通过入参包含HomePathInfo的Navigation接口，指定一个NavDestination作为Navigation主页后，通过[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo18)接口无法获取主页NavDestination的信息。
2. 通过入参包含HomePathInfo的Navigation接口，指定一个NavDestination作为Navigation主页后，栈操作的目标页面非主页面，且没有设置[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)，返回该页面时会触发主页NavDestination的onResult。

变更后：

1. 通过[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo18)接口能够获取主页NavDestination的信息。
2. 栈操作的目标页面非主页面，且没有设置[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)，返回该页面时不会触发主页NavDestination的onResult。

**起始 API Level**

20

**变更的接口/组件**

1. [queryNavDestinationInfo(isInner: Optional<boolean>)](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo18)接口。
2. NavDestination的[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)接口。

**适配指导**

开发者需要根据变更内容审视自身业务代码是否需要进行适配，下面的两段示例代码分别展示了：

1. 主页NavDestination中使用queryNavDestinationInfo接口在变更前后的差异。
2. 主页NavDestination的onResult接口在如下场景中的变化：使用了主页NavDestination，栈中当前有PageA（未设置onResult）和PageB两个页面，然后从PageB返回到PageA，变更前会触发主页的NavDestination的onResult，变更后不会触发主页NavDestination的onResult。

示例代码1：

```ts
import hilog from '@ohos.hilog';

@Component
struct MyPage {
  build() {
    NavDestination() {
    }
    .width('100%')
    .height('100%')
    .title('DetailPage')
  }
}

@Component
struct InnerCustomComponent {
  GetDestInfo() {
    // 向上查找当前自定义组件的所在的NavDestination
    let info = this.queryNavDestinationInfo(false);
    if (info) {
      // 变更后能够获取到主页NavDestination的信息，会走这个分支
      hilog.info(0x0000, 'testTag', `success to get HomeNavDestination's name: ${info.name}`)
    } else {
      // 变更前无法获取到主页NavDestination的信息，会走这个分支
      hilog.info(0x0000, 'testTag', `failed to get NavDestinationInfo for HomeNavDestination`)
    }
  }

  build() {
    Column() {
      Button('queryOuterNavDestination').onClick(() => {
        this.GetDestInfo();
      })
    }
  }
}

@Component
struct MyHomeDestination {
  GetDestInfo() {
    // 向下查找当前自定义组件内部的NavDestination
    let info = this.queryNavDestinationInfo(true);
    if (info) {
      // 变更后能够获取到主页NavDestination的信息，会走这个分支
      hilog.info(0x0000, 'testTag', `success to get HomeNavDestination's name: ${info.name}`)
    } else {
      // 变更前无法获取到主页NavDestination的信息，会走这个分支
      hilog.info(0x0000, 'testTag', `failed to get NavDestinationInfo for HomeNavDestination`)
    }
  }

  build() {
    NavDestination() {
      Column() {
        Button('queryInnerNavDestination').onClick(() => {
          this.GetDestInfo();
        })
        InnerCustomComponent()
      }
    }
    .width('100%')
    .height('100%')
    .title('HomePage')
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  MyPageName(name: string) {
    if (name === 'Home') {
      MyHomeDestination()
    } else {
      MyPage()
    }
  }

  build() {
    // 使用主页NavDestination功能
    Navigation(this.stack, {name: 'Home'}) {
    }
    .width('100%')
    .height('100%')
    .navDestination(this.MyPageName)
  }
}
```

示例代码2：

```ts
import hilog from '@ohos.hilog';

@Component
struct MyPage {
  @State name: string = '';
  build() {
    // PageA不设置onResult事件
    NavDestination() {
    }
    .width('100%')
    .height('100%')
    .title(`${this.name}`)
    .onReady((ctx: NavDestinationContext) => {
      this.name = ctx.pathInfo.name;
    })
  }
}

@Component
struct MyHomeDestination {
  build() {
    NavDestination() {
    }
    .width('100%')
    .height('100%')
    .title('HomePage')
    .onResult((param: ESObject) => {
      // PageA未设置onResult事件，从PageB返回到PageA时，
      // 在变更前会触发主页NavDestination的onResult函数，在变更后不会触发主页NavDestination的onResult函数
      hilog.info(0x0000, 'testTag', `HomeDestination onResult`)
    })
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();

  @Builder
  MyPageName(name: string) {
    if (name === 'Home') {
      MyHomeDestination()
    } else {
      MyPage()
    }
  }

  aboutToAppear(): void {
    this.stack.pushPath({name: 'PageA'})
    this.stack.pushPath({name: 'PageB'})
  }

  build() {
    // 使用主页NavDestination功能
    Navigation(this.stack, {name: 'Home'}) {
    }
    .width('100%')
    .height('100%')
    .navDestination(this.MyPageName)
  }
}
```

### NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL事件回调的返回值行为变更

**变更原因**

[NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)事件回调返回值中的主轴方向上页面的长度ArkUI\_NodeComponentEvent.data[3].f32，和实际长度不符。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

* 变更前：NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL的返回值中的ArkUI\_NodeComponentEvent.data[3].f32不符合页面的实际主轴长度。例如实际长度为100vp，开发者接收vp单位时，返回的值是100/屏幕像素密度，开发者接收px单位时，返回的值是100。
* 变更后：NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL的返回值中的ArkUI\_NodeComponentEvent.data[3].f32符合页面的实际主轴长度。例如实际长度为100vp，开发者接收vp单位时，返回的值是100，开发者接收px单位时，返回的值是100\*屏幕像素密度。

**起始API Level**

12

**变更的接口/组件**

[NODE\_SWIPER\_EVENT\_ON\_CONTENT\_DID\_SCROLL](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)的返回参数值ArkUI\_NodeComponentEvent.data[3].f32。

**适配指导**

原先的返回值不符合实际页面主轴长度，开发者在使用时需要给获取的返回值\*屏幕像素密度。变更后可以直接使用正确的长度值进行业务开发。

```cpp
static ArkUI_NativeNodeAPI_1 *nodeAPI_ = reinterpret_cast<ArkUI_NativeNodeAPI_1 *>(
    OH_ArkUI_QueryModuleInterfaceByName(ARKUI_NATIVE_NODE, "ArkUI_NativeNodeAPI_1"));
const unsigned int LOG_PRINT_DOMAIN = 0xFF00;

static napi_value CreateSwiperNode(napi_env env, napi_callback_info info) {
    const int size = 11;
    const char *arr[size] = {"0", "1", "2", "3"};
    static ArkUI_NodeHandle swiper = nodeAPI_->createNode(ARKUI_NODE_SWIPER);

    for (int j = ConstIde::NUMBER_0; j < size; j++) {
        ArkUI_NodeHandle textNode = nodeAPI_->createNode(ARKUI_NODE_TEXT);
        ArkUI_AttributeItem content = {.string = arr[j]};
        nodeAPI_->setAttribute(textNode, NODE_TEXT_CONTENT, &content);

        ArkUI_NumberValue value[] = {0};
        ArkUI_AttributeItem item = {.value = value, .size = 1};
        value[ConstIde::NUMBER_0].f32 = ConstIde::TEXT_HEIGHT_VP;
        nodeAPI_->setAttribute(textNode, NODE_HEIGHT, &item);
        value[ConstIde::NUMBER_0].u32 = ConstIde::TEXT_BG_COLOR;
        nodeAPI_->setAttribute(textNode, NODE_BACKGROUND_COLOR, &item);
        value[ConstIde::NUMBER_0].i32 = ConstIde::TEXT_ALIGN_CENTER;
        nodeAPI_->setAttribute(textNode, NODE_TEXT_ALIGN, &item);
        value[ConstIde::NUMBER_0].f32 = ConstIde::TEXT_FONT_SIZE_VP;
        nodeAPI_->setAttribute(textNode, NODE_FONT_SIZE, &item);

        ArkUI_AttributeItem textId = {.string = "SwiperAutoPlayText"};
        nodeAPI_->setAttribute(textNode, NODE_ID, &textId);
        nodeAPI_->addChild(swiper, textNode);
    }
    ArkUI_NumberValue value[] = {};
    ArkUI_AttributeItem item = {.value = value, .size = 1};
    
    value[0].f32 = 300;
    nodeAPI_->setAttribute(swiper, NODE_WIDTH, &item);

    nodeAPI_->setLengthMetricUnit(swiper, ArkUI_LengthMetricUnit::ARKUI_LENGTH_METRIC_UNIT_PX);
    nodeAPI_->registerNodeEvent(swiper, NODE_SWIPER_EVENT_ON_CONTENT_DID_SCROLL, 0, nullptr);
    nodeAPI_->addNodeEventReceiver(swiper, [](ArkUI_NodeEvent *event) {
        ArkUI_NodeComponentEvent* compEvent = OH_ArkUI_NodeEvent_GetNodeComponentEvent(event) ;
        int selectedIndex = compEvent->data[0].i32;
        int index = compEvent->data[1].i32;
        float position = compEvent->data[2].f32;
        float maxAxisLength = compEvent->data[3].f32;
        // 变更前页面真实的长度为maxAxisLength * 屏幕像素密度，变更后为maxAxisLength
        OH_LOG_Print(LOG_APP, LOG_INFO, LOG_PRINT_DOMAIN, "Manager", "maxAxisLength: %{public}f", maxAxisLength);
    });
}
```

### @ReusableV2组件复用的reuse属性支持动态复用标识

**变更原因**

当前[@ReusableV2](../harmonyos-guides/arkts-new-reusablev2.md)装饰器装饰的自定义组件的reuse属性不支持使用动态的reuseId，变更后可增强V2组件复用能力，支持动态复用标识。

**变更影响**

此变更涉及应用适配。

* 变更前：如果开发者使用了如下所示等非显式返回字符串字面量形式的reuseId，实际的复用标识ID为该可复用自定义组件的名称。
* 变更后：如果开发者使用了下述形式的reuseId，实际的复用标识ID为该回调的返回值。

```ts
const globalReuseId: string = 'globalReuseId';
@Entry
@ComponentV2
struct Index {
  getReuseIdInMethod(idNumber: number): string {
    return `reuseIdInMethod${idNumber}`;
  }
  build() {
    Column() {
      ReusableV2Component()
        // 变更前实际复用标识为自定义组件名称"ReusableV2Component"
        // 变更后实际复用标识为"globalReuseId"
        .reuse({reuseId: () => globalReuseId})
      ReusableV2Component()
        // 变更前实际复用标识为自定义组件名称"ReusableV2Component"
        // 变更后实际复用标识为"reuseIdInMethod1"
        .reuse({reuseId: () => this.getReuseIdInMethod(1)})
    }
  }
}
@ReusableV2
@ComponentV2
struct ReusableV2Component {
  build() {
    Column() {
      Text('ReusableV2Component')
    }
  }
}
```

**起始 API Level**

18

**变更的接口/组件**

涉及接口：[ReuseOptions](../harmonyos-references/ts-universal-attributes-reuse.md#reuseoptions)里的reuseId参数。

变更前后会受到影响的组件为@ReusableV2装饰器装饰的自定义组件。该变更可能导致：

* 原本可以相互复用的自定义组件无法再相互复用：

  ```ts
  @Entry
  @ComponentV2
  struct Index {
    getReuseIdInMethod(idNumber: number): string {
      return `reuseIdInMethod${idNumber}`;
    }

    build() {
      Column() {
        // 变更后，在API版本26.0.0及以上，下述两个ReusableComponentOne组件的实际复用标识不一致，无法相互复用。
        ReusableComponentOne()
          // 变更前实际复用标识为自定义组件名称"ReusableComponentOne"
          // 变更后实际复用标识为"reuseIdInMethod1"
          .reuse({reuseId: () => this.getReuseIdInMethod(1)})
        ReusableComponentOne()
          // 变更前实际复用标识为自定义组件名称"ReusableComponentOne"
          // 变更后实际复用标识为"reuseIdInMethod2"
          .reuse({reuseId: () => this.getReuseIdInMethod(2)})
      }
    }
  }
  @ReusableV2
  @ComponentV2
  struct ReusableComponentOne {
    build() {
      Column() {
        Text('ReusableComponentOne')
      }
    }
  }
  ```
* 原本不可以相互复用的自定义组件可以相互复用：

  ```ts
  @Entry
  @ComponentV2
  struct Index {
    getReuseIdInMethod(idNumber: number): string {
      return `reuseIdInMethod${idNumber}`;
    }

    build() {
      Column() {
        // 变更后，在API版本26.0.0及以上ReusableComponentOne和ReusableComponentTwo组件实际复用标识一致，可以相互复用
        ReusableComponentOne()
          // 变更前实际复用标识为自定义组件名称"ReusableComponentOne"
          // 变更后实际复用标识为"reuseIdInMethod1"
          .reuse({reuseId: () => this.getReuseIdInMethod(1)})
        ReusableComponentTwo()
          // 变更前实际复用标识为自定义组件名称"ReusableComponentTwo"
          // 变更后实际复用标识为"reuseIdInMethod1"
          .reuse({reuseId: () => this.getReuseIdInMethod(1)})
      }
    }
  }
  @ReusableV2
  @ComponentV2
  struct ReusableComponentOne {
    build() {
      Column() {
        Text('ReusableComponentOne')
      }
    }
  }
  @ReusableV2
  @ComponentV2
  struct ReusableComponentTwo {
    build() {
      Column() {
        Text('ReusableComponentTwo')
      }
    }
  }
  ```

**适配指导**

对于不希望相互复用的V2复用组件，使用不同的复用标识reuseId；对于希望相互复用的组件，使用相同的复用标识reuseId。例如，当希望如下两个组件ComponentA和ComponentB组件可以相互复用时，设置同样的复用标识。点击按钮让两个组件消失，二者进入同一复用池中，可以相互复用。再次点击任一按钮，后进入复用池的组件先显示到页面上：

```ts
const globalReuseId = 'globalReuseId';
@Entry
@ComponentV2
struct Index {
  @Local condition1: boolean = true;
  @Local condition2: boolean = true;
  build() {
    Column({ space: 10 }) {
      // 变更后，在API版本26.0.0及以上ComponentA和ComponentB组件实际复用标识一致，均为'globalReuseId'，可以相互复用。
      Button('change condition1')
        .onClick(() => { this.condition1 = !this.condition1; })
      Button('change condition2')
        .onClick(() => { this.condition2 = !this.condition2; })
      if (this.condition1) {
        ComponentA().reuse({ reuseId: () => globalReuseId })
      }
      if (this.condition2) {
        ComponentB().reuse({ reuseId: () => globalReuseId })
      }
    }
  }
}
@ReusableV2
@ComponentV2
struct ComponentA {
  build() {
    Column() {
      Text('ComponentA')
    }
  }
}
@ReusableV2
@ComponentV2
struct ComponentB {
  build() {
    Column() {
      Text('ComponentB')
    }
  }
}
```

### 组件的阴影模糊半径规格变更

**变更原因**

修改阴影模糊半径生效范围，使shadow属性中的所有阴影类型新增支持模糊半径为0时的阴影能力。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：通过shadow属性添加阴影效果，将参数ShadowOptions中的阴影模糊半径radius设置为0时，无阴影；设置为负数时按0处理，无阴影。

变更后：通过shadow属性添加阴影效果，将参数ShadowOptions中的阴影模糊半径radius设置为0时，存在阴影但不存在模糊效果；设置为负数时，无阴影。

例如使用以下代码片段，通过shadow设置Column组件的边框阴影效果，变更前radius设置0和-1效果一致，变更后radius设置0且带有偏移量[OffsetX](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)或[OffsetY](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)时会有无模糊阴影显示。

```ts
// xxx.ets
@Entry
@Component
struct Index {
  private shadowValue: Array<ShadowOptions> = [
    { radius: -1 },
    { radius: -1, offsetX: 20, offsetY: 20 },
    { radius: 0 },
    { radius: 0, offsetX: 20, offsetY: 20 },
    { radius: 50 },
    { radius: 50, offsetX: 20, offsetY: 20 },
  ];

  build() {
    Column() {
      Row({ space: 10 }) {
        Column({ space: 20 }) {
          Text('ShadowType.Color')

          ForEach(this.shadowValue, (shadow: ShadowOptions) => {
            Column()
              .width(100)
              .height(50)
              .borderRadius(10)
              .backgroundColor(Color.Pink)
              .shadow({
                radius: shadow.radius,
                color: Color.Green,
                offsetX: shadow.offsetX,
                offsetY: shadow.offsetY
              })
          })
        }
        
        Column({ space: 20 }) {
          Text('ShadowType.Blur')

          ForEach(this.shadowValue, (shadow: ShadowOptions) => {
            Column()
              .width(100)
              .height(50)
              .borderRadius(10)
              .backgroundColor(Color.Pink)
              .shadow({
                radius: shadow.radius,
                type: ShadowType.BLUR,
                offsetX: shadow.offsetX,
                offsetY: shadow.offsetY
              })
          })
        }
      }
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始 API Level**

7

**变更的接口/组件**

通用属性[shadow](../harmonyos-references/ts-universal-attributes-image-effect.md#shadow)的[ShadowOptions.radius](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)参数。

列表选择弹窗组件的[actionsheetoptions.shadow](../harmonyos-references/ts-methods-action-sheet.md#actionsheetoptions对象说明)。

警告弹窗组件的[alertdialogparam.shadow](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparam对象说明)。

日历选择器弹窗组件的[calendardialogoptions.shadow](../harmonyos-references/ts-methods-calendarpicker-dialog.md#calendardialogoptions对象说明)。

自定义弹窗组件的[customdialogcontrolleroptions.shadow](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)。

日期滑动选择器弹窗组件的[datepickerdialogoptions.shadow](../harmonyos-references/ts-methods-datepicker-dialog.md#datepickerdialogoptions对象说明)。

文本滑动选择器弹窗组件的[textpickerdialogoptions.shadow](../harmonyos-references/ts-methods-textpicker-dialog.md#textpickerdialogoptions对象说明)和[TextPickerDialogOptionsExt.shadow](../harmonyos-references/ts-methods-textpicker-dialog.md#textpickerdialogoptionsext20对象说明)。

时间滑动选择器弹窗组件的[timepickerdialogoptions.shadow](../harmonyos-references/ts-methods-timepicker-dialog.md#timepickerdialogoptions对象说明)。

半模态转场的[sheetoptions.shadow](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)。

Popup控制的[popupoptions.shadow](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)、[custompopupoptions.shadow](../harmonyos-references/ts-universal-attributes-popup.md#custompopupoptions8类型说明)和[popupcommonoptions.shadow](../harmonyos-references/ts-universal-attributes-popup.md#popupcommonoptions18类型说明)。

弹窗的[showtoastoptions.shadow](../harmonyos-references/js-apis-promptaction.md#showtoastoptions)、[showdialogoptions.shadow](../harmonyos-references/js-apis-promptaction.md#showdialogoptions)和[customdialogoptions.shadow](../harmonyos-references/js-apis-promptaction.md#customdialogoptions11)。

SegmentButtonV2组件的[TabSegmentButtonV2.itemShadow](../harmonyos-references/ohos-arkui-advanced-segmentbuttonv2.md#tabsegmentbuttonv2)和[CapsuleSegmentButtonV2.itemShadow](../harmonyos-references/ohos-arkui-advanced-segmentbuttonv2.md#capsulesegmentbuttonv2)。

symbolglyph组件的[symbolShadow](../harmonyos-references/ts-basic-components-symbolglyph.md#symbolshadow20)。

**适配指导**

如果应用在API版本26.0.0及之后期望阴影消失，需要将radius的取值从0调整为-1。如果期望保留阴影但不产生模糊效果，应将radius设置为0。

Text组件的[textShadow](../harmonyos-references/ts-basic-components-text.md#textshadow10)不发生规格变更，仍然维持原有规格。

## ArkWeb

### ArkWeb基于上游社区的Chromium内核从132升级为144版本

**变更原因**

为了提升使用ArkWeb内核应用的安全性，开发者使用最新的W3C HTML5特性，以及获得Chromium上游社区最新的性能体验优化成果，故本次进行内核升级(132 -> 144)。

**变更影响**

从上游社区323项功能变更说明，以及社区1000+问题单分析，WPT测试集结果分析，当前共发现100+项需要开发者注意的变更点，请参考[ArkWeb 版本的差异总结](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/ArkWeb_132_144.md)。

**起始 API Level**

不涉及

**变更的接口/组件**

ArkWeb

**适配指导**

如果在应用中使用Web组件展示网页内容，则需要遵循[ArkWeb 版本的差异总结](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/ArkWeb_132_144.md)中所涉及的最新W3C规格变更。

## Media Library Kit

### 通过ohos.permission.READ\_IMAGEVIDEO权限可读取的媒体库文件的范围变更

**变更原因**

限制网盘等应用访问云图库的图片或视频，避免因为访问云图库资产导致隐私安全与设备功耗高、发热等问题。

**变更影响**

此变更涉及应用适配。

变更前：应用申请ohos.permission.READ\_IMAGEVIDEO权限，调用Media Library Kit接口可以获取云图库和本地图片或视频。

变更后：应用申请ohos.permission.READ\_IMAGEVIDEO权限，调用Media Library Kit接口仅可以获取本地图片或视频。

**起始 API Level**

API 9

**变更的接口/组件**

* PhotoAccessHelper.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;
* PhotoAccessHelper.getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
* PhotoAccessHelper.getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
* AbsAlbum.getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void;
* AbsAlbum.getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>;
* fileIo.open(path: string, mode?: number): Promise<File>;
* fileIo.open(path: string, callback: AsyncCallback<File>): void;
* fileIo.open(path: string, mode: number, callback: AsyncCallback<File>): void;
* fileIo.openSync(path: string, mode?: number): File;

**适配指导**

涉及默认行为变更：变更前应用能访问云图库和本地图片或视频，变更后应用仅能访问本地图片或视频。

如果应用需要访问云图库的图片或视频，请通过PhotoViewPicker进行访问。

## Network Kit

### getUidRxBytes、getUidTxBytes接口权限变更

**变更原因**

getUidRxBytes、getUidTxBytes接口需要添加权限管控。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更前：应用可通过本接口传入指定Uid查询其上下行流量数据。

变更后：若接口传入的Uid为自身应用Uid，则无需申请权限，接口行为与变更前一致；若接口传入的Uid非自身应用Uid时，需要申请ohos.permission.GET\_NETWORK\_STATS权限，其授权方式为system\_grant，当前只允许MDM应用申请。

**起始 API Level**

API 10

**变更的接口/组件**

statistics.getUidRxBytes(uid: number, callback: AsyncCallback<number>): void

statistics.getUidRxBytes(uid: number): Promise<number>

statistics.getUidTxBytes(uid: number, callback: AsyncCallback<number>): void

statistics.getUidTxBytes(uid: number): Promise<number>

**适配指导**

1. 若应用仅使用上述接口查询自身流量，则无需适配；
2. 若非MDM应用使用上述接口查询其他应用流量，则需审视调用场景，若有影响需根据自身业务代码进行对应适配；
3. 若MDM应用使用上述接口查询其他应用流量，则需要申请ohos.permission.GET\_NETWORK\_STATS权限，接口其他行为与变更前一致。

## 权限管控

### 权限策略变更说明

**变更原因**

Binary（可执行二进制，以下简称bin）是操作系统中可通过execve系统调用创建为独立进程的文件，bin独立进程具备完整的程序入口点和运行时上下文，内核为其分配独立的地址空间、PID、文件描述符表等进程资源，同样它也具有独立的”进程身份”。

在历史版本中，系统已向应用开放了一些在内核进行权限管控的资源的权限，如ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY（允许应用申请可执行的匿名内存）。这类权限在权限名中带有“.kernel”字段，这类权限被称为kernelpermission。

从ROM版本7.0开始，bin进程若想要使用kernelpermission的权限，需要应用主动为bin声明权限并签名。

**变更影响**

此变更涉及应用适配。

**说明** 

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于26.0.0时生效。

变更后：

* 开发者使用的API版本小于26.0.0：应用不受影响，建议开发者尽早适配。
* 开发者使用的API版本大于等于26.0.0：应用进程执行bin，bin不再自动继承应用的kernelpermission，需要bin主动声明权限。

**起始 API Level**

14

**变更的接口/组件**

不涉及

**适配指导**

1. 确认应用是否申请了权限名中带有”.kernel”的权限（kernelpermission），如果没有则不涉及本次适配。
2. 该适配不涉及手机应用，手机应用不存在拉起bin独立进程的场景，但建议涉及kernelpermission的应用二次确认。
3. 确认应用是否涉及拉起bin独立进程，没有则不涉及本次适配。
4. 确认拉起的bin独立进程是否需要应用申请的kernelpermission，不需要则不涉及本次适配。

下图流程供应用参考进行排查，如果需要适配，则根据下文中的具体步骤进行适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/aBfRgNJwTj641cT_sxCChw/zh-cn_image_0000002623074963.png)

适配步骤：

1. 设置bin需要的权限策略段。

   新建一个json文件，下文称为example.json，开发者可根据需要自定义文件名。

   该json文件格式如下：

   ```screen
   {
       // binary涉及的权限都需要填写，除权限名带kernel字段的kernelpermission外，需要的其他permission也要填写。
       "requestPermissions":[
           {
               "name": "ohos.permission.kernel.xxx"
           },
           {
               "name": "ohos.permission.xxx"
           }
       ]
   }
   ```

2. HNP中的bin授权。

   1）HNP配置中配置"independentSign": true （API 23生效），配置该字段后HNP包中的bin为独立授权，需要主动配置需要的权限。

   配置的权限除kernelpermission外，其余需要的权限也需要放入，如不确定权限策略文件中需要配置的权限，也可以直接配置ohos.permission.INHERIT\_PARENT\_PERMISSION，系统会自动帮bin进程继承可以继承的父进程权限，示例配置如下：

   ```screen
   {
       "requestPermissions":[
           {
               "name": "ohos.permission.INHERIT_PARENT_PERMISSION"
           }
       ]
   }
   ```

   2）使用命令给bin文件（如下以myprogram举例）添加上权限段，然后重新打包。llvm-objcopy可通过[Command line tools](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)获取。

   使用步骤1中新建的example.json，执行如下命令：

   ```screen
   llvm-objcopy --add-section .permission=path/to/example.json myprogram myprogram_modified
   ```

3. 非HNP的二进制授权方法。

   1）获取二进制签名工具。签名工具获取地址：[binary-sign-tool](../harmonyos-guides/binary-sign-tool.md)

   2）准备好证书、p12等文件后，使用二进制签名工具设置权限策略段，对应签名工具命令-moduleFile参数，json文件为[步骤1 - 设置bin需要的权限策略段](changelogs-for-all-apps-7001.md#li10472721191517)中新建的json文件。

   ```screen
   ./binary-sign-tool sign -keyAlias "基于csr生成时的填写结果补充" -signAlg "SHA256withECDSA" -appCertFile "基于csr生成时的pem文件补充" -inFile "hello" -keystoreFile "基于csr生成时的p12文件名补充" -outFile "signed_hello_release" -keyPwd "基于csr文件密钥补充" -keystorePwd "基于csr文件密钥补充" -moduleFile "权限策略段json文件名" -selfSign 0
   ```

   样例：

   ```screen
   ./binary-sign-tool sign -keyAlias "openharmony application release" -signAlg "SHA256withECDSA" -appCertFile "OpenHarmonyApplication-old-test-ou1031.pem" -inFile "hello" -keystoreFile "OpenHarmony.p12" -outFile "signed_hello_release" -keyPwd "123456" -keystorePwd "123456" -moduleFile "example.json" -selfSign 0
   ```
