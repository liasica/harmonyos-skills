---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1606
title: 如何实现Text短文本居中，长文本居左
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Text短文本居中，长文本居左
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a2981405a45b7c4e46d4d736fdad55813265fbde54177d8dadefb91f2b3332cd
---

## 问题现象

如何实现Text组件短文本时居中，长文本时居左的效果？

## 背景知识

* [margin](../harmonyos-references/ts-universal-attributes-size.md#margin)能够设置组件的外边距属性，可以与[Text](../harmonyos-references/ts-basic-components-text.md)文本组件配合使用。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)是在组件区域变化时触发的回调，仅会在布局变化所导致的组件大小、位置发生变化时响应，适合动态调整变量。

## 解决方案

可以使用[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)属性实现，通过计算Text组件的长度，判断其是否超出展示区域，如果超出，就通过设置margin属性实现居左效果，如果不超出，则不设置margin，保持居中。

* Index：在build方法中，创建一个可滚动的Scroll组件，在Scroll组件内部，创建一个Column组件，包含一个AppBar组件。

  ```screen
  import { AppBar } from '../components/AppBar';

  @Entry
  @ComponentV2
  struct Index {
    private title: string = '个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息个人信息';

    @Builder
    testBuilder() {
      Row({ space: 16 }) {
        Column() {
        }
        .width(24)
        .height(24)
        .backgroundColor(Color.Blue);

        Column() {
        }
        .width(24)
        .height(24)
        .backgroundColor(Color.Green);
      };
    }

    build() {
      Scroll() {
        Column() {
          AppBar({
            title: this.title, actions: () => {
              this.testBuilder();
            }
          });
        };
      }
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: false })
      .align(Alignment.Top)
      .width('100%');
    }
  }
  ```
* AppBar：使用Stack和RelativeContainer组件构建布局。Text文本组件使用自定义的AppBarTitleModifier类进行属性修饰，并且使用onAreaChange事件监听器，根据标题的宽度和容器的宽度比较，动态调整isneed状态变量，以决定是否需要通过调整margin来调整Text布局。

  ```screen
  import { MeasureUtils } from '@kit.ArkUI';
  import { AppBarTitleModifier } from './AppBarTitleModifier';

  @ComponentV2
  export struct AppBar {
    @Param title: ResourceStr = '';
    @BuilderParam actions: CustomBuilder;
    @Param barForegroundColor: ResourceColor | null = null;
    @Local leadingWidth: number = 0;
    @Local actionsWidth: number = 0;
    @Local isneed: boolean = false;
    private readonly titleId: string = 'AppBar_Title_Component';
    @Local uiContext: UIContext = this.getUIContext();
    @Local uiContextMeasure: MeasureUtils = this.uiContext.getMeasureUtils();

    build() {
      Stack() {
        RelativeContainer() {
          Row() {
            Text(this.title)
              .attributeModifier(new AppBarTitleModifier(this.barForegroundColor));
          }
          .id(this.titleId)
          .margin({ left: this.isneed ? this.leadingWidth : 0, right: this.isneed ? this.actionsWidth : 0 })
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            center: { anchor: '__container__', align: VerticalAlign.Center }
          })
          .onAreaChange((oldValue: Area, newValue: Area) => {
            let w = newValue.width;
            let s = this.getUIContext().px2vp(this.uiContextMeasure.measureText({
              textContent: this.title,
              fontSize: 16,
              maxLines: 1
            }));
            if (s > w) {
              this.isneed = true;
            }
            console.info(`oldValue：${oldValue}`);
          });
        }
        .size({ width: '100%', height: '100%' })
        .padding({ left: 12, right: 12 })
        .zIndex(2);
      }
      .width('100%')
      .zIndex(0);
    }
  }
  ```
* 定义AppBarTitleModifier类实现AttributeModifier接口，用于修饰Text组件的属性。

  ```screen
  export class AppBarTitleModifier implements AttributeModifier<TextAttribute> {
    // 字体颜色
    private fontColor?: ResourceColor;

    constructor(fontColor?: ResourceColor) {
      this.fontColor = fontColor;
    }

    applyNormalAttribute(instance: TextAttribute): void {
      instance
        .textOverflow({ overflow: TextOverflow.Ellipsis })
        .maxLines(1)
        .fontColor(this.fontColor ?? Color.Black)
        .fontSize(16)
        .fontWeight(FontWeight.Bold);
    }
  }
  ```

短文本效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/JyXUXofFRFWD6CnsK0FMqg/zh-cn_image_0000002628773272.png "点击放大")

长文本效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/CK3Q-VCmQhiCWGh2U8liNQ/zh-cn_image_0000002628613374.png "点击放大")
