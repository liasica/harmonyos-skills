---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-load-custom-font
title: ArkTS卡片使用自定义字体
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片使用自定义字体
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:26+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:b22ccf940b65d842d8d2a7f8f17829e14e106ce79b89ead8e8169ef2695da241
---

API version 22开始新增了[ohos.graphics.text.FontCollection.getLocalInstance](../harmonyos-references/js-apis-graphics-text.md#getlocalinstance22)接口获取本地字体集实例，应用可以通过这个本地实例为卡片加载自定义字体。

## 开发步骤

1. 创建动态卡片：按照[创建ArkTS卡片](arkts-ui-widget-creation.md)里的描述创建动态卡片。
2. 在项目entry\src\main\resources\rawfile目录下添加自定义字体文件xxx.ttf。
3. 页面布局代码实现entry/src/main/ets/widget/pages/WidgetCard.ets。

   在卡片页面中布局两个按钮，点击按钮load font或按钮unload font，调用本地字体集实例的loadFontSync、unloadFontSync进行字体的加载、卸载。

```
1. // entry/src/main/ets/widget/pages/WidgetCard.ets
2. import { text } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct loadFontSyncCard {
7. // 在这里使用getLocalInstance访问本地字体集实例
8. private fc: text.FontCollection = text.FontCollection.getLocalInstance();
9. @State content: string = '默认字体';

11. build() {
12. Column({ space: 10 }) {
13. Text(this.content)
14. .fontFamily('custom') // 在此处声明组件使用自定义字体
15. Button('load font')
16. .onClick(() => {
17. // 在此处加载自定义字体文件
18. this.fc.loadFontSync('custom', $rawfile('xxx.ttf'));
19. this.content = '自定义字体';
20. })
21. Button('unload font')
22. .onClick(() => {
23. this.fc.unloadFontSync('custom');
24. this.content = '默认字体';
25. })
26. }.width('100%')
27. .height('100%')
28. .justifyContent(FlexAlign.Center)
29. }
30. }
```

说明

* 本地字体集可加载多个自定义字体，所有字体合计最大内存限制加载20MB。
* 同一应用的所有卡片共用一个本地字体集实例。加载或卸载自定义字体后，所有卡片的字体显示会同步更新。

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kpsObgNZR7uGnBUbSXiD4A/zh-cn_image_0000002552798644.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234125Z&HW-CC-Expire=86400&HW-CC-Sign=6FF9E8C629403A79A1761BAA1F358F4ABF9C2CC1B78F039E6F37662B1578A5B2)
