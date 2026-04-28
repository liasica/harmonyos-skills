---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery
title: @ohos.mediaquery (媒体查询)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.mediaquery (媒体查询)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:33+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:785c5d4e7b214495e84b70d39e4f0bd31c00a41436e05f560e4b8cb5400912ec
---

提供根据不同媒体类型定义不同的样式。

说明

* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该模块不支持在[UIAbility](js-apis-app-ability-uiability.md)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { mediaquery } from '@kit.ArkUI';
```

## mediaquery.matchMediaSync(deprecated)

PhonePC/2in1TabletTVWearable

matchMediaSync(condition: string): MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

说明

* 从API version 7开始支持，从API version 18开始废弃，建议使用[matchMediaSync](arkts-apis-uicontext-mediaquery.md#matchmediasync)替代。matchMediaSync需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMediaQuery](arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取[MediaQuery](arkts-apis-uicontext-mediaquery.md)对象，然后通过该对象进行调用。
* 从API version 10开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMediaQuery](arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取当前UI上下文关联的[MediaQuery](arkts-apis-uicontext-mediaquery.md)对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| condition | string | 是 | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](../harmonyos-guides/arkts-layout-development-media-query.md#语法规则)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaQueryListener](js-apis-mediaquery.md#mediaquerylistener) | 媒体事件监听句柄，用于注册和去注册监听回调。 |

**示例：**

```
1. import { mediaquery } from '@kit.ArkUI';

3. let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // 监听横屏事件
```

## MediaQueryListener

PhonePC/2in1TabletTVWearable

媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width <= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。

继承自[MediaQueryResult](js-apis-mediaquery.md#mediaqueryresult)。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### on('change')

PhonePC/2in1TabletTVWearable

on(type: 'change', callback: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件注册回调，当媒体属性发生变更时会触发该回调。

说明

注册的回调中不允许进一步调用on或off。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'change'。 |
| callback | Callback<[MediaQueryResult](js-apis-mediaquery.md#mediaqueryresult)> | 是 | 向媒体查询注册的回调。 |

**示例：**

详见[off('change')](js-apis-mediaquery.md#offchange)示例。

### off('change')

PhonePC/2in1TabletTVWearable

off(type: 'change', callback?: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件取消注册回调，当媒体属性发生变更时不再触发指定的回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 必须填写字符串'change'。 |
| callback | Callback<[MediaQueryResult](js-apis-mediaquery.md#mediaqueryresult)> | 否 | 需要取消注册的回调，如果参数缺省则去注册该句柄下所有的回调。 |

**示例：**

```
1. import { mediaquery } from '@kit.ArkUI';

3. let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // 监听横屏事件
4. function onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
5. if (mediaQueryResult.matches) {
6. // do something here
7. } else {
8. // do something here
9. }
10. }
11. listener.on('change', onPortrait) // 注册回调
12. listener.off('change', onPortrait) // 取消注册回调
```

## MediaQueryResult

PhonePC/2in1TabletTVWearable

用于执行媒体查询操作。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| matches | boolean | 是 | 否 | 是否符合匹配条件。true表示满足查询条件，false表示不满足查询条件。 |
| media | string | 是 | 否 | 媒体事件的匹配条件。 |

### 示例

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getMediaQuery](arkts-apis-uicontext-uicontext.md#getmediaquery)方法获取当前UI上下文关联的[MediaQuery](arkts-apis-uicontext-mediaquery.md)对象。

```
1. import { mediaquery } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MediaQueryExample {
6. @State color: string = '#DB7093'
7. @State text: string = 'Portrait'
8. listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)'); // 监听横屏事件，mediaquery.matchMediaSync接口已废弃，建议使用this.getUIContext().getMediaQuery().matchMediaSync()来获取

10. onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
11. if (mediaQueryResult.matches) {
12. this.color = '#FFD700'
13. this.text = 'Landscape'
14. } else {
15. this.color = '#DB7093'
16. this.text = 'Portrait'
17. }
18. }

20. aboutToAppear() {
21. let portraitFunc = (mediaQueryResult: mediaquery.MediaQueryResult): void => this.onPortrait(mediaQueryResult)
22. // 绑定回调函数
23. this.listener.on('change', portraitFunc);
24. }

26. aboutToDisappear() {
27. // 解绑listener中注册的回调函数
28. this.listener.off('change');
29. }

31. build() {
32. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
33. Text(this.text).fontSize(24).fontColor(this.color)
34. }
35. .width('100%').height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/8IScUhAOQ6e3zplGb6iTgA/zh-cn_image_0000002583479423.png?HW-CC-KV=V1&HW-CC-Date=20260428T000031Z&HW-CC-Expire=86400&HW-CC-Sign=0D1F5ACA28B653B68E26B827900A81E96A22CA70BE0956C638ED9055F5AF5E05)
