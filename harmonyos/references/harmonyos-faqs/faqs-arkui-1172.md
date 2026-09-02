---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1172
title: 如何根据API版本动态增加Image组件的属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何根据API版本动态增加Image组件的属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:922b3bab3f28d2ed95cbbfca9d3df459209bf73bdbc307f0d72c533786a0d6b5
---

## 问题现象

如何根据不同的API版本动态设置Image组件的属性？如：orientation属性在API 14及以上版本上生效，如何动态添加此属性？

## 背景知识

* [deviceInfo (设备信息)](../harmonyos-references/js-apis-device-info.md)：获取终端设备信息，其中sdkApiVersion表示系统软件API版本。
* [attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)：动态属性设置，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。

## 解决方案

可以通过获取[deviceInfo.sdkApiVersion](../harmonyos-references/js-apis-device-info.md#常量)判断当前系统的API版本再使用[动态属性](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)设置需要的属性，如：

为Image组件设置attributeModifier动态属性：

```ts
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State modifierImg: ImageModifier = new ImageModifier();

  aboutToAppear(): void {
    // 设置动态属性判断的API版本
    this.modifierImg.sdkApiVersionInfo = deviceInfo.sdkApiVersion;
  }

  build() {
    Flex({justifyContent: FlexAlign.Center}) {
      // 加载的图片请替换为实际项目所需图片资源
      Image($r('app.media.img'))
        .width(100)
        .height(100)
        .draggable(true)
        .attributeModifier(this.modifierImg)
    }
  }
}
```

通过判断API版本动态设置orientation属性：

```ts
export class ImageModifier implements AttributeModifier<ImageAttribute> {
  // 可以实现一个Modifier，定义私有的成员变量，外部可动态修改
  sdkApiVersionInfo: number = 12;
  applyNormalAttribute(instance: ImageAttribute): void {
    if (deviceInfo.sdkApiVersion >= 14) { // 支持业务逻辑实现
      // 属性变化触发apply函数时，变化前已设置并且变化后未设置的属性会恢复为默认值
      instance.orientation(ImageRotateOrientation.RIGHT);
    }
  }
}
```

示例代码运行效果如下：

系统API版本小于API 14：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/E3_a5plyS_CmlVYoInbEIg/zh-cn_image_0000002628569782.png "点击放大")

系统API版本大于API 14：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9UnMBnl2SYyIVU1wgt_lqA/zh-cn_image_0000002628409878.png "点击放大")
