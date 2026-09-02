---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-component-arview
title: ARView（AR场景可视化）
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > ArkTS组件 > ARView（AR场景可视化）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ef5d7b55984e32ecbffda6d03e75799fc1353c091b4f3e341343af7c22cd00a
---

用于承载ARViewContext，实现AR场景可视化呈现。

需要与[arViewController](arengine-api-arviewcontroller.md)配合一起使用，完成AR场景的可视化呈现。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

## 导入模块

```typescript
import { ARView, arViewController } from '@kit.AREngine';
```

## ARView

该类为AR场景可视化呈现组件。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| context | [arViewController.ARViewContext](arengine-api-arviewcontroller.md#arviewcontext) | 是 | @Require  @State | ARView上下文、AR会话和场景的状态管理。 |

### build

build(): void

用于创建ARView对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**示例：**

```typescript
import { ARView, arViewController } from '@kit.AREngine';

let arContext: arViewController.ARViewContext = new arViewController.ARViewContext();

@Entry
@Component
struct ARWorld {
  // context配置及初始化
  build() {
    RelativeContainer() {
      if (arContext) {
        ARView({ context: arContext })
          .height('100%')
          .width('100%')
      }
    }
  }
}
```
