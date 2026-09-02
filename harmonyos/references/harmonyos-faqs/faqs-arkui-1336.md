---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1336
title: AppStorageV2怎么更新已保存的数据
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > AppStorageV2怎么更新已保存的数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2fe35f367f4fe145f64208c9cd36a098d6697b61c2810bb7d3aa15eb7da02da5
---

## 问题现象

AppStorageV2只有connect、remove、keys方法，没有update更新方法，如何更新已保存的数据？每次更新是否需要remove后再保存新的数据？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/L_jr2R-LTAKGBJEQw6flKA/zh-cn_image_0000002628600020.png "点击放大")

## 背景知识

[AppStorageV2](../harmonyos-references/js-apis-statemanagement.md#appstoragev2)是在应用UI启动时会被创建的单例。它的目的是为了提供应用状态数据的中心存储，这些状态数据在应用级别都是可访问的。AppStorageV2将在应用运行过程保留其数据。数据通过唯一的键字符串值访问。

## 解决方案

AppStorageV2当前并未提供更新接口，开发者可以先connect获取已保存的对象，然后直接给对象的属性赋值就可以实现数据更新，示例代码如下：

```ts
import { AppStorageV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Page {
  promptAction = this.getUIContext().getPromptAction();

  aboutToAppear(): void {
    AppStorageV2.connect(Sample, () => new Sample())!;
  }

  build() {
    Column({ space: 10 }) {
      Button('AppStorageV2 update')
        .onClick(() => {
          let sample = AppStorageV2.connect(Sample, () => new Sample())!;
          sample.p1 = 100;
        });
      Button('AppStorageV2 get value')
        .onClick(() => {
          let sample = AppStorageV2.connect(Sample, () => new Sample())!;
          this.promptAction.showToast({ message: 'p1 =' + sample.p1 });
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}

@ObservedV2
export class Sample {
  p1: number = 0;
}
```

## 常见FAQ

Q：AppStorageV2如何保存简单的string、number、boolean等变量？

A：AppStorageV2局限性详见[使用限制](../harmonyos-guides/arkts-new-appstoragev2.md#使用限制)。字符串等简单数据保存可参考以下方式：

1. 参考“解决方案”，将数字（number）等基本类型封装为类。
2. 可以使用String、Number等构造类型：@Local prop: String = AppStorageV2.connect(String, () => new String('test'))!;

Q：若AppStorageV2与AppStorage使用相同的Key获取与储存数据是否会导致冲突？

A：AppStorageV2与AppStorage使用相同的Key并不会导致冲突。

Q：@Monitor如何监听AppStorageV2保存的数据的修改？

A：AppStorageV2的connect方法绑定状态变量后，状态变量的修改会同步到AppStorageV2内，可以通过监听该状态变量的修改实现AppStorageV2的修改监听。
