---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1343
title: 应用启动页图片截断
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用启动页图片截断
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b1221148ed089991c63ceabb5ad8751f84d31d72cce20081221d06c6b98ff471
---

## 问题现象

应用系统默认启动页图片截断，无法显示完整大小，只展示部分内容。

## 背景知识

[getDefaultDisplaySync](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取当前默认的display对象。

## 问题定位

1. 使用图片查看工具（如系统自带的图片属性）获取精确尺寸。
2. 比较图片尺寸与屏幕的尺寸比例是否存在差异。

## 分析结论

module.json5中设置的startWindowIcon无法完全展示不符合屏幕比例的图片，如果超过屏幕显示极限，则截断显示。

## 修改建议

目前启动页展示整页图片只能使用与屏幕大小相同的图片，可以依照屏幕尺寸设置一个相同尺寸的图片，尺寸可以使用代码获取参数。具体代码见下：

```ts
import { display} from '@kit.ArkUI';

@Entry
@Component
struct Splash {
  @State screenWidth: number = 0;
  @State screenHeight: number = 0;
  @State screenWidth2: number = 0;
  @State imageResource: Resource = $r('app.media.startIcon');

  aboutToAppear(): void {
    let displayClass: display.Display | null = null;

    displayClass = display.getDefaultDisplaySync();
    this.screenWidth = displayClass.width;
    this.screenHeight = displayClass.height;
    console.log('width = ' + this.screenWidth + 'height = ' + this.screenHeight);
  }

  build() {
    Column() {
      Image(this.imageResource) // 启动图路径需替换成自定义的资源路径
        .width('100%')
        .height('100%')
        .syncLoad(true); // 设置图片为同步加载
    }
    .width('100%')
    .height('100%')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
    .backgroundColor(Color.White)
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
