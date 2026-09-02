---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-833
title: 如何实现带有滚动动画效果的数字显示组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现带有滚动动画效果的数字显示组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1c325d43dd20cceb5b8d14c93184e143487a3350d4cc626575b5504141fa183c
---

## 问题现象

如何实现一个带有滚动动画效果的数字显示组件，可以通过单击按钮来增加数字，数字将以动画效果过渡至新值。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/YRFTDPToSJaNvDMhbTdMMw/zh-cn_image_0000002658797723.png "点击放大")

## 背景知识

* 显式动画接口[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)能够指定由于闭包代码导致的状态变化插入过渡动效。
* 通用属性[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)能够设置组件平移，可使组件在以组件左上角为坐标原点的坐标系中进行移动。[margin](../harmonyos-references/ts-universal-attributes-size.md#margin)属性能够设置组件的外边距属性，保持组件的相对位置。

## 解决方案

1. 定义状态变量：状态变量scrollNumber通过@Prop和@Watch装饰器绑定到父组件的num状态，当num变化时，调用changeNumber方法。其余状态变量如下：

   ```ts
   @Prop @Watch('changeNumber') scrollNumber: number = 0;
   @State bottomNum: number = 0;
   @State showNumber: string = '0';
   @State cacheNumber: string = '';
   changeNumberFinal: string = '';
   isScrolling: boolean = false;
   isInit: boolean = false;

   changeNumber() {
     if (this.isInit) {
       this.animateToScroll(this.scrollNumber);
     }
   }
   ```
2. 定义方法initAnimateToScroll，用来初始化动画，设置在50毫秒后开始动画的定时器。在方法animateToScroll中执行滚动动画，根据传入的newNum更新bottomNum和isScrolling，并在动画完成后更新showNumber和cacheNumber。

   ```ts
   initAnimateToScroll() {
     setTimeout(() => {
       this.getUIContext().animateTo({
         duration: 600,
         onFinish: () => {
           this.isInit = true;
         }
       }, () => {
         this.bottomNum = -50;
       });
     }, 50);
   }

   animateToScroll(newNum: number) {
     this.changeNumberFinal = String(newNum);
     if (this.isScrolling) {
       return;
     }
     this.cacheNumber = this.changeNumberFinal;
     this.getUIContext().animateTo({
       duration: 600,
       onFinish: () => {
         this.bottomNum = -50;
         this.showNumber = this.cacheNumber;
         this.cacheNumber = '';
         this.isScrolling = false;
         if (this.changeNumberFinal !== this.showNumber) {
           this.animateToScroll(Number(this.changeNumberFinal));
         }
       }
     }, () => {
       this.bottomNum = 0;
       this.isScrolling = true;
     });
   }
   ```
3. 通过translate和margin属性控制数字的垂直位置，配合动画实现滚动效果。

   ```ts
   Row() {
     Text(this.showNumber)
       .fontSize(35)
       .fontColor('#0A59F7');
   }
   .margin({ bottom: this.bottomNum })
   .height(50)
   .translate({ y: this.bottomNum });
   ```

完整示例参考如下：

```ts
@Entry
@Component
struct ScrollNum {
  @State num: number = 0;
  @State isEnabled: boolean = true;

  build() {
    Column({ space: 50 }) {
      ScrollNumComponent({ scrollNumber: this.num });

      Button('点击添加')
        .enabled(this.isEnabled)
        .onClick(() => {
          this.isEnabled = !this.isEnabled;
          setTimeout(() => {
            this.num += 50;
            this.isEnabled = !this.isEnabled;
          }, 600);
        });
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}

@Component
export struct ScrollNumComponent {
  @Prop @Watch('changeNumber') scrollNumber: number = 0;
  @State bottomNum: number = 0;
  @State showNumber: string = '0';
  @State cacheNumber: string = '';
  changeNumberFinal: string = '';
  isScrolling: boolean = false;
  isInit: boolean = false;

  changeNumber() {
    if (this.isInit) {
      this.animateToScroll(this.scrollNumber);
    }
  }

  aboutToAppear(): void {
    this.initAnimateToScroll();
  }

  initAnimateToScroll() {
    setTimeout(() => {
      this.getUIContext().animateTo({
        duration: 600,
        onFinish: () => {
          this.isInit = true;
        }
      }, () => {
        this.bottomNum = -50;
      });
    }, 50);
  }

  animateToScroll(newNum: number) {
    this.changeNumberFinal = String(newNum);
    if (this.isScrolling) {
      return;
    }
    this.cacheNumber = this.changeNumberFinal;
    this.getUIContext().animateTo({
      duration: 600,
      onFinish: () => {
        this.bottomNum = -50;
        this.showNumber = this.cacheNumber;
        this.cacheNumber = '';
        this.isScrolling = false;
        if (this.changeNumberFinal !== this.showNumber) {
          this.animateToScroll(Number(this.changeNumberFinal));
        }
      }
    }, () => {
      this.bottomNum = 0;
      this.isScrolling = true;
    });
  }

  build() {
    Column() {
      Row() {
        Text(this.cacheNumber)
          .fontSize(35)
          .fontColor('#0A59F7');
      }
      .height(50)
      .translate({ y: this.bottomNum });

      Row() {
        Text(this.showNumber)
          .fontSize(35)
          .fontColor('#0A59F7');
      }
      .margin({ bottom: this.bottomNum })
      .height(50)
      .translate({ y: this.bottomNum });
    }
    .clip(true)
    .height(50);
  }
}
```
