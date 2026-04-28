---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout
title: SplitLayout
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SplitLayout
category: harmonyos-references
scraped_at: 2026-04-28T08:02:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2c87a8f7ae0df9eab41dfa7374a625f82ac582f0e32c952aad2efa8d69cfe143
---

上下结构布局介绍了常用的页面布局样式。主要分为上下文本和上下图文两种类型。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果SplitLayout设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SplitLayout本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SplitLayout设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { SplitLayout } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## SplitLayout

PhonePC/2in1TabletTVWearable

SplitLayout({mainImage: Resource, primaryText: string, secondaryText?: string, tertiaryText?: string, container: () => void })

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| mainImage | [ResourceStr](ts-types.md#resourcestr) | 是 | @State | 传入图片。 |
| primaryText | [ResourceStr](ts-types.md#resourcestr) | 是 | @Prop | 标题内容。 |
| secondaryText | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 副标题内容。当需要在标题下方显示副标题时传入，不传入时取默认值，不显示副标题。 |
| tertiaryText | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 辅助文本。当需要显示辅助文本时传入，不传入时取默认值，不显示辅助文本。 |
| container | () => void | 是 | @BuilderParam | 容器内组件。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

该示例通过SplitLayout实现了页面布局，并具备自适应能力。

```
1. import { SplitLayout } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State demoImage: Resource = $r("app.media.background");

8. build() {
9. Column() {
10. SplitLayout({
11. mainImage: this.demoImage,
12. primaryText: '新歌推荐',
13. secondaryText: '私人订制新歌精选站，为你推荐专属优质新歌;',
14. tertiaryText: '每日更新',
15. }) {
16. Text('示例：空白区域容器内可添加组件')
17. .margin({ top: 36 })
18. }
19. }
20. .justifyContent(FlexAlign.SpaceBetween)
21. .height('100%')
22. .width('100%')
23. }
24. }
```

小于等于600vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/DgmSnDq0SUSkNt5Me5nLJQ/zh-cn_image_0000002552800480.png?HW-CC-KV=V1&HW-CC-Date=20260428T000239Z&HW-CC-Expire=86400&HW-CC-Sign=BBF0ED9BC570E0C72863955CBE81145E141A4906E0B1BC83B4DE41D195B29BB6)

大于600vp且小于等于840vp的布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/Wf31ArsGRIGdcepSXHqFIg/zh-cn_image_0000002583440175.png?HW-CC-KV=V1&HW-CC-Date=20260428T000239Z&HW-CC-Expire=86400&HW-CC-Sign=FA10DC91370942EDEEDD23DD54B3C4E7005966375362FA27A5F3791D407B64FC)

大于840vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/3ukMoMmvTKGbZLYLSpeXkA/zh-cn_image_0000002552960130.png?HW-CC-KV=V1&HW-CC-Date=20260428T000239Z&HW-CC-Expire=86400&HW-CC-Sign=49B9BF7EB9CE3211F19BB359663CAE927E59BE0C297C9FA5D7EC77712BACF8E3)
