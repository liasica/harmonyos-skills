---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-load-custom-font
title: ArkTS卡片使用自定义字体
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片使用自定义字体
category: harmonyos-guides
scraped_at: 2026-09-10T06:22:19+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:2ea6d9da1324f3e34da6d65d53206309c596b33f2903db2677aa80cc74d2e101
---

API version 22开始新增了[ohos.graphics.text.FontCollection.getLocalInstance](../harmonyos-references/js-apis-graphics-text.md#getlocalinstance22)接口获取本地字体集实例，应用可以通过这个本地实例为卡片加载自定义字体。

## 开发步骤

1. 创建动态卡片：按照[创建ArkTS卡片](arkts-ui-widget-creation.md)里的描述创建动态卡片。
2. 在项目entry\src\main\resources\rawfile目录下添加自定义字体文件xxx.ttf。
3. 页面布局代码实现entry/src/main/ets/widget/pages/WidgetCard.ets。

   在卡片页面中布局两个按钮，点击按钮load font或按钮unload font，调用本地字体集实例的loadFontSync、unloadFontSync进行字体的加载、卸载。

```typescript
// entry/src/main/ets/widget/pages/WidgetCard.ets
import { text } from '@kit.ArkGraphics2D';

@Entry
@Component
struct loadFontSyncCard {
  // 在这里使用getLocalInstance访问本地字体集实例
  private fc: text.FontCollection = text.FontCollection.getLocalInstance();
  @State content: string = '默认字体';

  build() {
    Column({ space: 10 }) {
      Text(this.content)
        .fontFamily('custom') // 在此处声明组件使用自定义字体
      Button('load font')
        .onClick(() => {
          // 在此处加载自定义字体文件
          this.fc.loadFontSync('custom', $rawfile('xxx.ttf'));
          this.content = '自定义字体';
        })
      Button('unload font')
        .onClick(() => {
          this.fc.unloadFontSync('custom');
          this.content = '默认字体';
        })
    }.width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

**说明** 

* 本地字体集可加载多个自定义字体，所有字体合计最大内存限制加载20MB。
* 同一应用的所有卡片共用一个本地字体集实例。加载或卸载自定义字体后，所有卡片的字体显示会同步更新。

### 运行结果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/MYvwLRNeRxq1g5WBTIMiSg/zh-cn_image_0000002747290963.gif)
