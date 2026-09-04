---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout
title: SplitLayout
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > SplitLayout
category: harmonyos-references
scraped_at: 2026-09-05T06:17:30+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:5991e61912fe0e5450a52665c2e7c8905b1f2cd6fb598b4b9d5a62ba38eee880
---

SplitLayout组件提供了常用的页面布局样式，主要用于展示图片、标题和内容容器的组合布局，适用于需要自适应不同屏幕尺寸的分栏展示场景（如详情页、设置页等）。支持自适应不同屏幕宽度（小于等于600vp、大于600vp且小于等于840vp、大于840vp三种布局），解决了在不同尺寸设备上需要展示不同布局样式的需求，提升页面适配性和用户体验。

**说明** 

* 该组件从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 如果SplitLayout设置[通用属性](ts-component-general-attributes.md)或[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到SplitLayout本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议SplitLayout设置通用属性和通用事件。

## 导入模块

```ts
import { SplitLayout } from '@kit.ArkUI';
```

## 子组件

无

## SplitLayout

SplitLayout({mainImage: ResourceStr, primaryText: ResourceStr, secondaryText?: ResourceStr, tertiaryText?: ResourceStr, container: () => void })

SplitLayout是分栏布局组件，支持自适应布局能力，在不同宽度下显示不同的布局样式。

**装饰器类型：**@Component

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| mainImage | [ResourceStr](ts-types.md#resourcestr) | 是 | @State | 主图片资源，显示在布局上方区域，支持png、jpg、svg等常见图片格式。 |
| primaryText | [ResourceStr](ts-types.md#resourcestr) | 是 | @Prop | 主标题内容，无长度限制。显示在布局的标题区域。 |
| secondaryText | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 副标题内容，无长度限制。当需要在标题下方显示副标题时传入，不传入时不显示副标题。 |
| tertiaryText | [ResourceStr](ts-types.md#resourcestr) | 否 | @Prop | 辅助文本，无长度限制。显示在副标题下方区域，当需要显示辅助文本时传入，不传入时不显示辅助文本。 |
| container | () => void | 是 | @BuilderParam | 容器内组件，用于在布局下方区域承载自定义组件内容，无返回值。 |

## 示例

该示例通过SplitLayout实现了页面布局，并具备自适应能力。

```ts
import { SplitLayout } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State demoImage: Resource = $r('app.media.background');

  build() {
    Column() {
      SplitLayout({
        mainImage: this.demoImage,
        primaryText: '新歌推荐',
        secondaryText: '私人订制新歌精选站，为你推荐专属优质新歌;',
        tertiaryText: '每日更新',
      }) {
        Text('示例：空白区域容器内可添加组件')
          .margin({ top: 36 })
      }
    }
    .justifyContent(FlexAlign.SpaceBetween)
    .height('100%')
    .width('100%')
  }
}
```

小于等于600vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/PVjg0kggR1yxS8hENmlKkg/zh-cn_image_0000002742125503.png)

大于600vp且小于等于840vp的布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IbT95CXDQ12rGFoYpB9s4g/zh-cn_image_0000002712246596.png)

大于840vp布局：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/FtYdB7WhTs-Bst5SK97d5Q/zh-cn_image_0000002742005547.png)
