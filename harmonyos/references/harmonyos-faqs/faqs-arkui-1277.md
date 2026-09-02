---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1277
title: 如何在滑块上添加文字
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在滑块上添加文字
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b852d7da2930157e5379821eef5da6973bd77a19ca149d710ae165106865788
---

## 问题现象

开发者想要在Slider的滑块上添加文字，如何实现？

## 背景知识

在ArkUI中，UI显示的内容均为组件，由框架直接提供的称为系统组件，由开发者定义的称为自定义组件。

* HarmonyOS提供的[Slider](../harmonyos-references/ts-basic-components-slider.md)组件没有暴露对滑块内容样式进行修改的相关接口。
* [自定义组件](../harmonyos-guides/arkts-create-custom-components.md)允许开发者组合使用系统组件、及其属性和方法。
* [attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)支持参数传递及业务逻辑编写，并且通过状态变量触发刷新。

## 解决方案

* 将Slider看作两个圆角横条的叠加，通过两种颜色显示进度，通过改变Row组件的width属性控制进度大小：

  ```ts
  Stack({ alignContent: Alignment.TopStart }) {
    Row() {
    }.width('100%').height('100%').backgroundColor(Color.Gray).borderRadius('25px');

    Row() {
      this.sliderText();
    }
    .alignItems(VerticalAlign.Center)
    .attributeModifier(this.modifier)
    .height('50px')
    .backgroundColor('#0A59F7')
    .borderRadius('25px')
    .justifyContent(FlexAlign.End);
  }.width(250).height('50px');
  ```
* 通过绑定拖动手势监听偏移量调整滑块进度：

  ```ts
  @Builder
  sliderText() {
    Text('测试')
      .width(50)
      .height('80px')
      .borderRadius('40px')
      .backgroundColor('#F1F3F5')
      .textAlign(TextAlign.Center)
      .gesture(
        PanGesture({ fingers: 1, direction: PanDirection.All, distance: 0 })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
              let diffOffsetX: number = 0; // 定义当前手指相对于屏幕滑动距离，为最新滑动距离与前一次滑动距离之差
              let currentOffsetX: number = event.offsetX;
              diffOffsetX = currentOffsetX - this.frontOffsetX;  // 大于0表示向右滑动，小于0表示向左滑动
              let offsetX: number = this.currentPosition + diffOffsetX; // 滑块滑至距离为滑动前位置+当前手指相对于屏幕滑动距离
              this.currentPosition =
                offsetX > this.maxPosition ? this.maxPosition : (offsetX < this.minPosition ? this.minPosition : offsetX);
              this.modifier.currentPosition = this.currentPosition; // 设置当前滑块位置后会回调applyNormalAttribute函数
              this.frontOffsetX = currentOffsetX; // 更新前一次滑动距离
            }
          })
          .onActionEnd((event: GestureEvent | undefined) => {
            if (event) {
              this.frontOffsetX = 0; // 当手指滑动停止时，需刷新前一次滑动距离为0
            }
          })
      );
  }
  ```

完整示例参考如下：

```ts
class innerWidthModifier implements AttributeModifier<RowAttribute> {
  modifierWidth: number = 0;
  currentPosition: number = 50; // 由于需要排除滑块自身长度影响，定义初始滑块位置为滑块自身width
  maxFontPosition: number = 250; // 滑块最大长度

  applyNormalAttribute(instance: RowAttribute): void {
    this.modifierWidth = this.currentPosition / this.maxFontPosition * 100;
    instance.width(`${this.modifierWidth}%`);
  }
}

@Entry
@Component
struct MySlider {
  currentPosition: number = 50; // 同步滑块初始位置
  minPosition: number = 50; // 避免滑块向左滑出父组件
  maxPosition: number = 250; // 避免滑块向右滑出父组件
  frontOffsetX: number = 0;
  @State modifier: innerWidthModifier = new innerWidthModifier();

  @Builder
  sliderText() {
    Text('测试')
      .width(50)
      .height('80px')
      .borderRadius('40px')
      .backgroundColor('#F1F3F5')
      .textAlign(TextAlign.Center)
      .gesture(
        PanGesture({ fingers: 1, direction: PanDirection.All, distance: 0 })
          .onActionUpdate((event: GestureEvent | undefined) => {
            if (event) {
              let diffOffsetX: number = 0; // 定义当前手指相对于屏幕滑动距离，为最新滑动距离与前一次滑动距离之差
              let currentOffsetX: number = event.offsetX;
              diffOffsetX = currentOffsetX - this.frontOffsetX;  // 大于0表示向右滑动，小于0表示向左滑动
              let offsetX: number = this.currentPosition + diffOffsetX; // 滑块滑至距离为滑动前位置+当前手指相对于屏幕滑动距离
              this.currentPosition =
                offsetX > this.maxPosition ? this.maxPosition : (offsetX < this.minPosition ? this.minPosition : offsetX);
              this.modifier.currentPosition = this.currentPosition; // 设置当前滑块位置后会回调applyNormalAttribute函数
              this.frontOffsetX = currentOffsetX; // 更新前一次滑动距离
            }
          })
          .onActionEnd((event: GestureEvent | undefined) => {
            if (event) {
              this.frontOffsetX = 0; // 当手指滑动停止时，需刷新前一次滑动距离为0
            }
          })
      );
  }

  build() {
    Column() {
      Flex() {
        Text('-')
          .width('80px')
          .height('80px')
          .backgroundColor(Color.Gray)
          .borderRadius('40px')
          .textAlign(TextAlign.Center)
          .onClick(() => {
            if (this.currentPosition > this.minPosition) {
              this.currentPosition--;
              this.modifier.currentPosition = this.currentPosition;
            }
          });
        Stack({ alignContent: Alignment.TopStart }) {
          Row() {
          }.width('100%').height('100%').backgroundColor(Color.Gray).borderRadius('25px');

          Row() {
            this.sliderText();
          }
          .alignItems(VerticalAlign.Center)
          .attributeModifier(this.modifier)
          .height('50px')
          .backgroundColor('#0A59F7')
          .borderRadius('25px')
          .justifyContent(FlexAlign.End);
        }.width(250).height('50px');

        Text('+')
          .width('80px')
          .height('80px')
          .backgroundColor(Color.Gray)
          .borderRadius('40px')
          .textAlign(TextAlign.Center)
          .onClick(() => {
            if (this.currentPosition < this.maxPosition) {
              this.currentPosition++;
              this.modifier.currentPosition = this.currentPosition;
            }
          });
      }
      .margin({ top: '50%', left: '10%' });
    }
    .height('100%')
    .width('100%');
  }
}
```
