---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-xcomponentnode
title: XComponentNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > XComponentNode
category: harmonyos-references
scraped_at: 2026-09-02T15:00:54+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ee943913f2fe830ee6430a8e1f1bff110888eab7dca9586f6caab6a5c5f5d39d
---

提供XComponent节点XComponentNode，表示组件树中的[XComponent](ts-basic-components-xcomponent.md)组件，用于[EGL](egl.md)/[OpenGL ES](opengles.md)渲染和媒体数据写入，并支持动态修改节点渲染类型，适用于需要在ArkUI组件树中嵌入Native自渲染内容的场景。

**说明** 

* 从API version 11开始支持，从API version 12开始废弃，建议使用[XComponent](js-apis-arkui-framenode.md#xcomponent12)类型的typeNode替代。
* 本模块接口仅可在Stage模型下使用。
* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 当前不支持在预览器中使用XComponentNode。

## 导入模块

```ts
import { XComponentNode } from '@kit.ArkUI';
```

## XComponentNode(deprecated)

### constructor(deprecated)

constructor(uiContext: UIContext, options: RenderOptions, id: string, type: XComponentType, libraryName?: string)

XComponentNode的构造函数。

**说明** 

从API version 11开始支持，从API version 12开始废弃，建议使用[createNode](js-apis-arkui-framenode.md#createnodexcomponent12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UI上下文，获取方式可参考[UIContext获取方法](js-apis-arkui-node.md#uicontext获取方法)。 |
| options | [RenderOptions](js-apis-arkui-buildernode.md#renderoptions) | 是 | XComponentNode的渲染配置选项，用于设置节点渲染相关参数，如理想尺寸（selfIdealSize）等。 |
| id | string | 是 | XComponent的唯一标识，最大支持字符串长度128，超出长度时接口创建失败。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |
| type | [XComponentType](ts-appendix-enums.md#xcomponenttype10) | 是 | 用于指定XComponent组件类型，取值为[XComponentType](ts-appendix-enums.md#xcomponenttype10)枚举定义的值。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |
| libraryName | string | 否 | Native层编译输出动态库名称。不传该参数时，默认不加载Native动态库。详见[XComponent](ts-basic-components-xcomponent.md)组件。 |

**说明** 

需要显式指定[RenderOptions](js-apis-arkui-buildernode.md#renderoptions)中的selfIdealSize，否则XComponentNode内容大小为空，不显示任何内容。

### onCreate(deprecated)

onCreate(event?: Object): void

XComponentNode加载完成时触发该回调。

**说明** 

从API version 11开始支持，从API version 12开始废弃，建议使用[onLoad](ts-basic-components-xcomponent.md#onload)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Object | 否 | XComponent实例对象的事件参数，用于获取XComponent实例的context。context上挂载的方法由开发者在C++层定义，开发者可通过该context调用Native层注册的方法。 |

### onDestroy(deprecated)

onDestroy(): void

XComponentNode销毁时触发该回调。

**说明** 

从API version 11开始支持，从API version 12开始废弃，建议使用[onDestroy](ts-basic-components-xcomponent.md#ondestroy)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### changeRenderType(deprecated)

changeRenderType(type: NodeRenderType): boolean

动态修改XComponentNode的渲染类型。可在运行时动态切换渲染策略，适用于根据内容渲染需求选择不同渲染类型的场景。例如，当需要在组件上进行EGL/OpenGL ES直接绘制时可使用DISPLAY类型；当需要将渲染内容作为纹理参与合成（如实现半透明叠加效果或离屏渲染）时可切换为TEXTURE类型。

**说明** 

从API version 11开始支持，从API version 12开始废弃，建议使用[appendChild](js-apis-arkui-framenode.md#appendchild12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [NodeRenderType](js-apis-arkui-buildernode.md#noderendertype) | 是 | 需要修改的目标渲染类型，取值为[NodeRenderType](js-apis-arkui-buildernode.md#noderendertype)枚举定义的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 修改渲染类型是否成功。  true：修改渲染类型成功；false：修改渲染类型失败。 |

## 示例

```ts
import { NodeController, FrameNode, XComponentNode, NodeRenderType, XComponentType, UIContext } from '@kit.ArkUI';

class XComponentNodeController extends NodeController {
  private xComponentNode: MyXComponentNode | null = null;
  private soName: string = 'tetrahedron_napi'; // 该 so 由开发者通过 NAPI 编写并生成

  constructor() {
    super();
  }

  makeNode(context: UIContext): FrameNode | null {
    this.xComponentNode = new MyXComponentNode(context, {
      selfIdealSize: { width: 200, height: 200 }
    }, 'xComponentId', XComponentType.SURFACE, this.soName);
    return this.xComponentNode;
  }

  changeRenderType(renderType: NodeRenderType): void {
    if (this.xComponentNode) {
      this.xComponentNode.changeRenderType(renderType);
    }
  }
}

class MyXComponentNode extends XComponentNode {
  onCreate(event: Object) {
    // do something when XComponentNode has created
  }

  onDestroy() {
    // do something when XComponentNode is destroying
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        NodeContainer(new XComponentNodeController())
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/LtynQfsAQjqCjOxFavy_FQ/zh-cn_image_0000002706835592.jpg)
