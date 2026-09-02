---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-949
title: 如何保证组件与变化组件的高度一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何保证组件与变化组件的高度一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0513c38425c334f86f0853ed37d5da3490399b1a4e387811044a7e296736ebeb
---

## 问题现象

业务流程界面场景中，一个业务场景对应一个进度条和多个任务，任务文本长度和任务数量不确定，导致组件高度不确定，如何保证进度条和多个任务对齐？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/nbHbO8dITPSKZAeNJDsWVQ/zh-cn_image_0000002628561154.png "点击放大")

## 背景知识

* [onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)组件区域变化时触发该回调。仅会响应由布局变化所导致的组件尺寸发生变化时的回调。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)设置组件的布局权重，使组件在父容器（Row/Column/Flex）的主轴方向按照权重分配尺寸。

## 解决方案

使用onSizeChange获取变化组件高度，修改目标容器的高度变量，实现组件与变化组件相同高度的效果。

1. 业务流程子组件：通过onSizeChange获取容器高度，并将高度绑定到对应容器。
2. 流程数据实现：构造数据，模拟不同业务描述信息长度和业务数量的场景。

```ts
@Component
export struct TimeLineView {
  // 动态控制组件高度
  @State heightNumber: Length = '100%';
  // 编号
  code: string = '';
  // 内容存储
  @State service: Array<string> = [];

  build() {
    Column() {
      Row() {
        Column() {
          Image($r('app.media.startIcon'))
            .width(30)
            .height(30)
            .margin({ top: 10 })
            .objectFit(ImageFit.Contain);

          Progress({ value: 50, type: ProgressType.Linear })
            .width(10)
            .layoutWeight(1)
            .color('#0A59F7');
        }
        .height(this.heightNumber)
        .justifyContent(FlexAlign.Start)
        .alignItems(HorizontalAlign.Center);

        Column() {
          Text('步骤' + this.code)
            .fontColor(Color.Black)
            .fontSize(24)
            .height(50);
          ForEach(this.service, (item: string) => {
            Text(item)
              .margin({ top: 6, left: 10, right: 10 })
              .fontSize(18);
          });
          Blank().height(6);
        }
        .margin({ left: 10 })
        .width('80%')
        .alignItems(HorizontalAlign.Start)
        .justifyContent(FlexAlign.Start)
        .onSizeChange((oldValue, newValue) => {
          console.info(`oldValue: ${oldValue}, newValue: ${newValue}`);
          // 根据内容区高度控制进度条高度
          this.heightNumber = newValue.height ?? this.heightNumber;
        });
      };
    }
    .width('100%')
    .backgroundColor(Color.White);
  }
}

@Entry
struct Index {
  // 模拟数据
  one: Array<string> = ['流程-1', '流程-2'];
  two: Array<string> = ['流程-3', '流程-4，模拟长段文字效果---------------'];
  three: Array<string> = ['流程-5', '流程-6', '流程-7', '流程-8'];

  build() {
    Column() {
      TimeLineView({ code: '一', service: this.one });
      TimeLineView({ code: '二', service: this.two });
      TimeLineView({ code: '三', service: this.three });
    }
    .padding({
      top: 10,
      left: 5,
      right: 5,
      bottom: 10
    })
    .width('90%')
    .backgroundColor(Color.White)
    .borderRadius(15);
  }
}
```

## 常见FAQ

Q：是否还有其他可以获取组件高度的接口？

A：有，除上述组件尺寸变化事件onSizeChange外，还有[组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)和[组件可见区域变化事件](../harmonyos-references/ts-universal-component-visible-area-change-event.md)，但响应的场景不同，获取的信息也不同。建议使用组件尺寸变化事件，仅响应尺寸变化事件。
