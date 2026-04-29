---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay
title: 浮层
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 浮层
category: harmonyos-references
scraped_at: 2026-04-29T13:51:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c974539521ba26af917cf6f05ee0ece7d955a31ac192f29d7d22450233a04367
---

设置组件的浮层。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## overlay

PhonePC/2in1TabletTVWearable

overlay(value: string | CustomBuilder | ComponentContent, options?: OverlayOptions ): T

在当前组件上，增加遮罩文本或者叠加自定义组件以及[ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)作为该组件的浮层。浮层的定位同样基于当前组件进行计算。浮层不通过组件树进行渲染，部分接口（例如[getRectangleById](js-apis-arkui-componentutils.md#componentutilsgetrectanglebyiddeprecated)）不支持获取浮层中的组件。

说明

* overlay会将浮层组件覆盖在所绑定的组件上方，阻塞用户对浮层下方组件的所有交互操作。若需用户可操作下方组件，应参照[示例2（通过builder设置浮层）](ts-universal-attributes-overlay.md#示例2通过builder设置浮层)中的实现，在浮层builder的最外层组件上配置.hitTestBehavior(HitTestMode.Transparent)。此配置在通过浮层实现水印时尤其重要，因为水印显示不应妨碍用户对下层组件的操作。
* 多次调用overlay接口时，如果同时传入string类型和[CustomBuilder](ts-types.md#custombuilder8)类型，或者同时传入string类型和[ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)类型，浮层内容会叠加显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [CustomBuilder](ts-types.md#custombuilder8)10+ | [ComponentContent](ts-universal-attributes-overlay.md#componentcontent12)12+ | 是 | 遮罩文本内容或自定义组件构造函数。  **说明：**  自定义组件作为浮层时，不支持键盘走焦到自定义组件中。通过CustomBuilder设置浮层时，浮层中的内容会在页面刷新时销毁并重新创建，存在一定的性能损耗，页面频繁刷新的场景推荐使用ComponentContent方式设置浮层。 |
| options | [OverlayOptions](ts-universal-attributes-overlay.md#overlayoptions12) | 否 | 浮层的定位。  **说明：**  API version 12之前，options:  {  align?: [Alignment](ts-appendix-enums.md#alignment),  offset?: {x?: number, y?: number}  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

overlay节点不支持[onAppear](ts-universal-events-show-hide.md#onappear)和[onDisAppear](ts-universal-events-show-hide.md#ondisappear)等和节点挂载/卸载相关的事件。

## OverlayOptions12+

PhonePC/2in1TabletTVWearable

说明

为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| align7+ | [Alignment](ts-appendix-enums.md#alignment) | 否 | 是 | 设置浮层相对于组件的方位。  默认值：TopStart  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset7+ | [OverlayOffset](ts-universal-attributes-overlay.md#overlayoffset12) | 否 | 是 | 设置浮层基于自身左上角的偏移量。浮层默认处于组件左上角。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

说明

align和offset都设置时，效果重叠，浮层相对于组件方位定位后，再基于当前位置的左上角进行偏移。

## OverlayOffset12+

PhonePC/2in1TabletTVWearable

说明

为规范匿名对象的定义，API 12版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x7+ | number | 否 | 是 | 横向偏移量。  默认值：0  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y7+ | number | 否 | 是 | 纵向偏移量。  默认值：0  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ComponentContent12+

PhonePC/2in1TabletTVWearable

type ComponentContent<T = Object> = ComponentContent<T>

组件内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ComponentContent](js-apis-arkui-componentcontent.md)<T> | 组件内容的实体封装。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（通过string设置浮层）

该示例通过传入string设置浮层。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OverlayExample {
5. build() {
6. Column() {
7. Column() {
8. Text('floating layer')
9. .fontSize(12).fontColor(0xCCCCCC).maxLines(1)
10. Column() {
11. // $r('app.media.img')需要替换为开发者所需的图像资源文件
12. Image($r('app.media.img'))
13. .width(240).height(240)
14. .overlay("Winter is a beautiful season, especially when it snows.", {
15. align: Alignment.Bottom,
16. offset: { x: 0, y: -15 }
17. })
18. }.border({ color: Color.Black, width: 2 })
19. }.width('100%')
20. }.padding({ top: 20 })
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/FarTrtX1RzauQ10bBpcAcg/zh-cn_image_0000002558766004.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=DAA82EB20131A7636D9381E5B0B729CF2F6C13B6F2F5A8F4173548EFFEDECC05)

### 示例2（通过builder设置浮层）

该示例通过传入builder设置浮层。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OverlayExample {
5. @Builder
6. OverlayNode() {
7. Column() {
8. // $r('app.media.img1')需要替换为开发者所需的图像资源文件
9. Image($r('app.media.img1'))
10. Text("This is overlayNode").fontSize(20).fontColor(Color.White)
11. }
12. .width(180)
13. .height(180)
14. .alignItems(HorizontalAlign.Center)
15. .hitTestBehavior(HitTestMode.Transparent) // 配置浮层不阻塞交互
16. }

18. build() {
19. Column() {
20. // $r('app.media.img2')需要替换为开发者所需的图像资源文件
21. Image($r('app.media.img2'))
22. .overlay(this.OverlayNode(), { align: Alignment.Center })
23. .objectFit(ImageFit.Contain)
24. }.width('100%')
25. .border({ color: Color.Black, width: 2 }).padding(20)
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/OHKhK21KQiKG_SDZgbPvbA/zh-cn_image_0000002558606346.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=E440929A200BFE94E813B8893BFDFC39A6002FD1E15F5FBB300A87B039BE05B3)

### 示例3（通过ComponentContent设置浮层）

该示例通过overlay传入了ComponentContent使backgroundColor不断发生变化。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. backgroundColor: string | Resource = ""

7. constructor(backgroundColor: string | Resource) {
8. this.backgroundColor = backgroundColor;
9. }
10. }

12. @Builder
13. function overlayBuilder(params: Params) {
14. Row() {
15. }.width('100%').height('100%').backgroundColor(params.backgroundColor)
16. }

18. @Entry
19. @Component
20. struct Page_4040 {
21. @State overlayColor: string = 'rgba(0, 0, 0, 0.6)';
22. private uiContext: UIContext = this.getUIContext();
23. private overlayNode: ComponentContent<Params> =
24. new ComponentContent(this.uiContext, wrapBuilder(overlayBuilder), new Params(this.overlayColor))

26. aboutToAppear(): void {
27. setInterval(() => {
28. if (this.overlayColor.includes('0.6')) {
29. this.overlayColor = 'rgba(0, 0, 0, 0.1)'
30. this.overlayNode.update(new Params(this.overlayColor));
31. } else {
32. this.overlayColor = 'rgba(0, 0, 0, 0.6)'
33. this.overlayNode.update(new Params(this.overlayColor));
34. }
35. }, 1000)
36. }

38. build() {
39. Row() {
40. Column() {
41. Text(this.overlayColor)
42. .fontSize(40)
43. .fontWeight(FontWeight.Bold)
44. }
45. .width('100%')
46. }
47. .height('100%')
48. .overlay(this.overlayNode)
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/KnKYMg39Tu2hAioU68n9Nw/zh-cn_image_0000002589325873.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=5840785C778453CD4DE7E3984C8F17B196ED8F7752E8C0C7AD8B24A397A140E0)
