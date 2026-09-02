---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-754
title: PC应用内组件如何实现悬浮样式Hover效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > PC应用内组件如何实现悬浮样式Hover效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:deae29d1ec550864beed121db5aa4972bd1db9c5eb77c5cc384afdb57d857d49
---

## 问题现象

PC应用如何实现鼠标悬停在组件上时，组件UI效果变更？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/hC5wTvM6T6CXMLIWueaSSA/zh-cn_image_0000002628395472.gif "点击放大")

## 背景知识

* [@Styles](../harmonyos-guides/arkts-style.md)：@Styles装饰器可以将多条样式设置提炼成一个方法，直接在组件声明的位置调用。通过@Styles装饰器可以快速定义并复用自定义样式，仅仅应用于静态页面的样式复用。
* [stateStyles](../harmonyos-guides/arkts-statestyles.md)：stateStyles可以依据组件的内部状态的不同，快速设置不同样式。stateStyles是属性方法，可以根据UI内部状态来设置样式，类似于css伪类，但语法不同。ArkUI提供以下五种状态：focused、normal、pressed、disabled、selected。

## 解决方案

例如按钮的默认状态、按下状态、禁用状态可以将@Styles与stateStyles组合使用来实现对应效果，悬浮状态还需要结合[onHover](../harmonyos-references/ts-universal-events-hover.md)事件来实现。

```ts
// 定义在全局的Button样式
@Styles
function globalButtonStyle() {
  .width(160)
  .height(80)
  .borderRadius(16);
}

@Entry
@Component
struct CustomerButton {
  @State isHover: boolean = false;

  // 定义在组件内的@Styles封装的样式
  // Disable
  @Styles
  disabledStyle(){
    .backgroundColor('#A8B8F7');
  }

  // normal
  @Styles
  normalStyle() {
    .backgroundColor('#0A59F7');
  }

  // pressed
  @Styles
  pressedStyle() {
    .backgroundColor('#0950DE');
  }

  // hover
  @Styles
  hoverStyle() {
    .backgroundColor(this.isHover ? '#0954EA' : '#0A59F7');
  }

  build() {
    Column() {
      Row() {
        Text('Default')
          .width(120)
          .fontSize(30);
        Button('默认状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .stateStyles({
            normal: this.normalStyle
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Pressed')
          .width(120)
          .fontSize(30);
        Button('按下状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .stateStyles({
            normal: this.normalStyle,
            pressed: this.pressedStyle,
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Hover')
          .width(120)
          .fontSize(30);
        Button('悬浮状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .onHover((isHover: boolean) => {
            console.info(`${isHover}`);
            this.isHover = !this.isHover;
          })
          .stateStyles({
            normal: this.hoverStyle
          });
      }
      .margin({
        bottom: 20
      });

      Row() {
        Text('Disable')
          .width(120)
          .fontSize(30);
        Button('禁用状态', { type: ButtonType.Normal, stateEffect: false })
          .globalButtonStyle()
          .fontSize(30)
          .enabled(false)
          .stateStyles({
            disabled: this.disabledStyle
          });
      }
      .margin({
        bottom: 20
      });
    }
    .padding({ top: 20 })
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
