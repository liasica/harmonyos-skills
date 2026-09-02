---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot
title: ContentSlot
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义占位组件 > ContentSlot
category: harmonyos-references
scraped_at: 2026-09-02T15:01:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eda444bd4656a455f2dc3e87620665df5b2b06e365a6899a02ce15229af00562
---

用于渲染Native侧使用C-API创建的组件，并通过Content管理器管理这些组件。

支持混合模式开发，当容器是ArkTS组件，子组件在Native侧创建时，推荐使用ContentSlot占位组件。

**说明** 

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 接口

ContentSlot(content: Content)

创建ContentSlot占位组件，用于渲染Content管理器中Native侧创建的组件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [Content](ts-components-contentslot.md#content) | 是 | Content作为ContentSlot的管理器，通过Native侧提供的接口，可以注册并触发ContentSlot的上下树（即组件节点加入或移出组件渲染树）事件回调以及管理ContentSlot的子组件。 |

## Content

type Content = import('../api/@ohos.arkui.node').Content

定义ComponentContent和NodeContent的基类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.node').[Content](js-apis-arkui-content.md) | 定义ComponentContent和NodeContent的基类。 |

## 示例

下面的示例展示了ContentSlot的基本用法。

```ts
import { nativeNode } from 'libNativeNode.so'; // 开发者自己实现的so
import { NodeContent, Content } from '@kit.ArkUI';

@Entry
@Component
struct Parent {
  private nodeContent: Content = new NodeContent();

  aboutToAppear() {
    // 通过C-API创建节点，并添加到管理器nodeContent上
    nativeNode.createNativeNode(this.nodeContent);
  }

  build() {
    Column() {
      // 显示nodeContent管理器里存放的Native侧的组件
      ContentSlot(this.nodeContent)
    }
  }
}
```

上述代码中so的实现可参考[Native XComponent](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/ArkUISample/NativeXComponent)。
