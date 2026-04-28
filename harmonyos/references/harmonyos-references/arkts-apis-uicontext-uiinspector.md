---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector
title: Class (UIInspector)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (UIInspector)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ce8e8aa31676ba17ab1db58eb3ac8ecee97398b029527ed4e6cef399934441b8
---

提供注册组件布局和组件绘制送显完成回调通知的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 10开始支持。
* 以下API需先使用UIContext中的[getUIInspector()](arkts-apis-uicontext-uicontext.md#getuiinspector)方法获取到UIInspector对象，再通过该对象调用对应方法。

## createComponentObserver

PhonePC/2in1TabletTVWearable

createComponentObserver(id: string): inspector.ComponentObserver

注册组件布局和组件绘制送显完成回调通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定组件id，该id通过通用属性[id](ts-universal-attributes-component-id.md#id)或者[key](ts-universal-attributes-component-id.md#key12)设置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [inspector.ComponentObserver](js-apis-arkui-inspector.md#componentobserver) | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```
1. import { inspector, UIInspector } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct UIInspectorExample {
6. build() {
7. Column() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
9. Row({ space: 5 }) {
10. Text("UIInspector")
11. .width(110)
12. .height(110)
13. .border({ width: 1 })
14. .id('TEXT_ID')
15. }.width(80).width(80)
16. }.width(80).width(80)
17. }.height(320).width(360).padding({ right: 10, top: 10 })
18. }

20. uiInspector: UIInspector = this.getUIContext().getUIInspector();
21. listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver("TEXT_ID")

23. aboutToAppear() {
24. let onLayoutComplete:()=>void=():void=>{
25. console.info("TEXT_ID layout complete")
26. }
27. let onDrawComplete:()=>void=():void=>{
28. console.info("TEXT_ID draw complete")
29. }

31. this.listener.on('layout', onLayoutComplete)
32. this.listener.on('draw', onDrawComplete)

34. // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
35. // this.listener.off('layout', onLayoutComplete)
36. // this.listener.off('draw', onDrawComplete)
37. }
38. }
```

## createComponentObserver23+

PhonePC/2in1TabletTVWearable

createComponentObserver(id: string | number): inspector.ComponentObserver

注册组件布局和组件绘制送显完成回调通知。送显指节点的绘制命令发送到图形服务并完成显示。

相比[createComponentObserver](arkts-apis-uicontext-uiinspector.md#createcomponentobserver)，新增支持传入UniqueID（系统给节点分配的唯一id）。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | number | 是 | 类型为string时，为指定的组件id，该id通过通用属性[id](ts-universal-attributes-component-id.md#id)或者[key](ts-universal-attributes-component-id.md#key12)设置。类型为number时，为系统分配的唯一标识的节点UniqueID，UniqueID通过[getUniqueId](js-apis-arkui-framenode.md#getuniqueid12)获取。使用UniqueID创建监听句柄时，请确保UniqueID对应的节点已经存在，否则后续监听无法生效。number的范围为1~2147483647的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [inspector.ComponentObserver](js-apis-arkui-inspector.md#componentobserver) | 组件回调事件监听句柄，用于注册和取消注册监听回调。 |

**示例：**

```
1. import { inspector, UIInspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct UIInspectorExample {
6. build() {
7. Column() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
9. Row({ space: 5 }) {
10. Text('UIInspector')
11. .width(110)
12. .height(110)
13. .border({ width: 1 })
14. .id('TEXT_ID')
15. }.width(80).width(80)
16. }.width(80).width(80)
17. }.height(320).width(360).padding({ right: 10, top: 10 })
18. }

20. uiInspector: UIInspector = this.getUIContext().getUIInspector();
21. listener:inspector.ComponentObserver = this.uiInspector.createComponentObserver('TEXT_ID')

23. aboutToAppear() {
24. let onLayoutComplete:()=>void=():void=>{
25. console.info('TEXT_ID layout complete')
26. }
27. let onDrawComplete:()=>void=():void=>{
28. console.info('TEXT_ID draw complete')
29. }
30. let onLayoutChildrenComplete :()=>void=():void=> {
31. console.info('UIInspectorExample children layout')
32. }

34. this.listener.on('layout', onLayoutComplete)
35. this.listener.on('draw', onDrawComplete)

37. let listenerForThis = this.getUIContext().getUIInspector().createComponentObserver(this.getUniqueId());
38. listenerForThis.onLayoutChildren(onLayoutChildrenComplete);

40. // 通过句柄向对应的查询条件取消注册回调，由开发者自行决定在何时调用。
41. // this.listener.off('layout', onLayoutComplete)
42. // this.listener.off('draw', onDrawComplete)
43. }
44. }
```
