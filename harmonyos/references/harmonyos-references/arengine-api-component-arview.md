---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-api-component-arview
title: ARView（AR场景可视化）
breadcrumb: API参考 > 图形 > AR Engine（AR引擎服务） > ArkTS组件 > ARView（AR场景可视化）
category: harmonyos-references
scraped_at: 2026-04-28T08:14:30+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:adfcb377cbb240ef94070941d953a9a6a37e419e6f13c5b74fdaed2d497a7a63
---

用于承载ARViewContext，实现AR场景可视化呈现。

需要与[arViewController](arengine-api-arviewcontroller.md)配合一起使用，完成AR场景的可视化呈现。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.1.0(18)

## 导入模块

PhoneTabletTV

```
1. import { ARView, arViewController } from '@kit.AREngine';
```

## ARView

PhoneTabletTV

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

PhoneTabletTV

build(): void

用于创建ARView对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AREngine.Core

**设备行为差异：** 该接口在部分Phone、部分Tablet、TV中可正常调用，在不支持的设备中无法正常调用。可使用[arViewController.isARTypeSupported](arengine-api-arviewcontroller.md#arviewcontrollerisartypesupported)接口查询能力是否支持。

**起始版本：** 5.1.0(18)

**示例：**

```
1. import { ARView, arViewController } from '@kit.AREngine';

3. let arContext: arViewController.ARViewContext = new arViewController.ARViewContext();

5. @Entry
6. @Component
7. struct ARWorld {
8. // context配置及初始化
9. build() {
10. RelativeContainer() {
11. if (arContext) {
12. ARView({ context: arContext })
13. .height('100%')
14. .width('100%')
15. }
16. }
17. }
18. }
```
