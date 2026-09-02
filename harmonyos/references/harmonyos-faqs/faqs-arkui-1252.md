---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1252
title: 文本内容未居中，两侧留白不一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 文本内容未居中，两侧留白不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f75b34fd0bf9e517598febce608dbeb08fd16c7d7cf183e2e0a270279883a25
---

## 问题现象

调整字体到最大尺寸后，文本两侧留白不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/fLYJlrcTQJqUsbk3YycWbQ/zh-cn_image_0000002658834709.png "点击放大")

## 背景知识

* [Slider](../harmonyos-references/ts-basic-components-slider.md)为滑动条组件，通常用于快速调节设置值，如音量调节、亮度调节等应用场景。
* [Text](../harmonyos-references/ts-basic-components-text.md)为显示一段文本的组件。可通过[fontSize](../harmonyos-references/ts-basic-components-text.md#fontsize)属性设置字体大小。
* [textAlign](../harmonyos-references/ts-basic-components-text.md#textalign)可设置文本段落在水平方向的对齐方式。

## 问题定位

1. 使用DevEco Testing查看问题组件，调整字体大小的组件为Slider组件，文本组件为Text组件，且组件内部因字体过大，文字右侧剩余空间不足以容纳文字，导致一侧留白。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/7iIR0kNsTSKtyRo8Vk2GKg/zh-cn_image_0000002628595454.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/J2hTC-3pRoWsX0zXHsD7Pw/zh-cn_image_0000002628755350.png "点击放大")
2. 查看Slider组件和Text组件的相关设置，Slider组件的字体尺寸最大值设置不合理，且Text组件未设置textAlign属性，文本内容默认左侧对齐。

   ```screen
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State textFontSize: number = 24;
     myText: string =
       '永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修禊事也。群贤毕至，少长咸集。此地有崇山峻岭，茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。是日也，天朗气清，惠风和畅，仰观宇宙之大，俯察品类之盛，所以游目骋怀，足以极视听之娱，信可乐也。\n' +
         '\n' +
         '　　夫人之相与，俯仰一世，或取诸怀抱，悟言一室之内；或因寄所托，放浪形骸之外。虽趣舍万殊，静躁不同，当其欣于所遇，暂得于己，快然自足，不知老之将至。及其所之既倦，情随事迁，感慨系之矣。向之所欣，俯仰之间，已为陈迹，犹不能不以之兴怀。况修短随化，终期于尽。古人云：“死生亦大矣。”岂不痛哉！(不知老之将至 一作：曾不知老之将至)\n' +
         '\n' +
         '　　每览昔人兴感之由，若合一契，未尝不临文嗟悼，不能喻之于怀。固知一死生为虚诞，齐彭殇为妄作。后之视今，亦犹今之视昔。悲夫！故列叙时人，录其所述，虽世殊事异，所以兴怀，其致一也。后之览者，亦将有感于斯文。';

     aboutToAppear(): void {
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true);
       });
     }

     build() {
       Column() {
         Scroll() {
           Column() {
             Text(this.myText)
               .fontSize(this.textFontSize);
             // 未设置textAlign属性
           };
         }
         .height('80%')
         .width('100%')
         .scrollBar(BarState.Off)
         .padding({ left: 10, right: 10 });

         Column() {
           Text('字体大小：' + this.textFontSize)
             .fontSize(20)
             .margin({ top: 10 });
           Row() {
             Image($r('app.media.minus'))
               .height(20)
               .width(20)
               .objectFit(ImageFit.Contain)
               .onClick(() => {
                 this.textFontSize -= 1;
               });

             Slider({
               value: this.textFontSize,
               min: 24,
               max: 56, // 字体尺寸最大值设置过大
               style: SliderStyle.InSet
             })
               .id('Slider')
               .blockColor(Color.White)
               .trackColor('#D1D1D6')
               .selectedColor('#0A59F7')
               .trackThickness(20)
               .blockSize({ width: 15, height: 15 })
               .showTips(false)
               .width('70%')
               .onChange((value: number) => {
                 this.textFontSize = value;
               });

             Image($r('app.media.plus'))
               .height(20)
               .width(20)
               .objectFit(ImageFit.Contain)
               .onClick(() => {
                 this.textFontSize += 1;
               });
           }
           .width('90%')
           .justifyContent(FlexAlign.SpaceAround)
           .margin({ top: 10 });
         }
         .backgroundColor('#f1f3f5')
         .width('100%')
         .height('20%')
         .borderRadius({ topLeft: 20, topRight: 20 });
       }
       .padding({ top: '123px' })
       .height('100%')
       .width('100%');
     }
   }
   ```

## 分析结论

Slider组件的字体尺寸最大值设置不合理，且Text组件未设置textAlign属性，文本内容默认左侧对齐，导致文本内容与组件边框一侧留白，页面两侧留白不一致，影响用户体验。

## 修改建议

* 方案一：合理设置Slider组件的字体尺寸最大值，避免字体过大导致文本内容与组件边框一侧留白。

  ```screen
  Slider({
    value: this.textFontSize,
    min: 24,
    max: 36, // 字体尺寸最大值设置在合适范围
    style: SliderStyle.InSet
  })
  ```

  完整示例：

  ```screen
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  @Builder
  export function SolutionOneBuilder() {
    SolutionOne();
  }

  @Entry
  @Component
  struct SolutionOne {
    @State textFontSize: number = 24;
    pathStack: NavPathStack = new NavPathStack();
    myText: string =
      '永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修禊事也。群贤毕至，少长咸集。此地有崇山峻岭，茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。是日也，天朗气清，惠风和畅，仰观宇宙之大，俯察品类之盛，所以游目骋怀，足以极视听之娱，信可乐也。\n' +
        '\n' +
        '　　夫人之相与，俯仰一世，或取诸怀抱，悟言一室之内；或因寄所托，放浪形骸之外。虽趣舍万殊，静躁不同，当其欣于所遇，暂得于己，快然自足，不知老之将至。及其所之既倦，情随事迁，感慨系之矣。向之所欣，俯仰之间，已为陈迹，犹不能不以之兴怀。况修短随化，终期于尽。古人云：“死生亦大矣。”岂不痛哉！(不知老之将至 一作：曾不知老之将至)\n' +
        '\n' +
        '　　每览昔人兴感之由，若合一契，未尝不临文嗟悼，不能喻之于怀。固知一死生为虚诞，齐彭殇为妄作。后之视今，亦犹今之视昔。悲夫！故列叙时人，录其所述，虽世殊事异，所以兴怀，其致一也。后之览者，亦将有感于斯文。';

    aboutToAppear(): void {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowLayoutFullScreen(true);
      });
    }

    build() {
      NavDestination() {
        Column() {
          Scroll() {
            Column() {
              Text(this.myText)
                .fontSize(this.textFontSize);
              // 未设置textAlign属性
            };
          }
          .height('80%')
          .width('100%')
          .scrollBar(BarState.Off)
          .padding({ left: 10, right: 10 });

          Column() {
            Text('字体大小：' + this.textFontSize)
              .fontSize(20)
              .margin({ top: 10 });
            Row() {
              Image($r('app.media.minus')) // $r('app.media.minus')需要替换为开发者需要的图片资源文件
                .height(20)
                .width(20)
                .objectFit(ImageFit.Contain)
                .onClick(() => {
                  this.textFontSize -= 1;
                });

              Slider({
                value: this.textFontSize,
                min: 24,
                max: 36, // 字体尺寸最大值设置在合适范围
                style: SliderStyle.InSet
              })
                .id('Slider')
                .blockColor(Color.White)
                .trackColor('#D1D1D6')
                .selectedColor('#0A59F7')
                .trackThickness(20)
                .blockSize({ width: 15, height: 15 })
                .showTips(false)
                .width('70%')
                .onChange((value: number) => {
                  this.textFontSize = value;
                });

              Image($r('app.media.plus')) // $r('app.media.plus')需要替换为开发者需要的图片资源文件
                .height(20)
                .width(20)
                .objectFit(ImageFit.Contain)
                .onClick(() => {
                  this.textFontSize += 1;
                });
            }
            .width('90%')
            .justifyContent(FlexAlign.SpaceAround)
            .margin({ top: 10 });
          }
          .backgroundColor('#f1f3f5')
          .width('100%')
          .height('20%')
          .borderRadius({ topLeft: 20, topRight: 20 });
        }
        .height('100%')
        .width('100%');
      }
      .onBackPressed(() => {
        this.pathStack.pop();
        return true;
      })
      .hideTitleBar(true)
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
      .padding({ top: '123px' })
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/4MBNi78PQtyPEWKooeSZjA/zh-cn_image_0000002658954671.png "点击放大")
* 方案二：设置文本内容两端对齐。

  ```screen
  Text(this.myText)
    .fontSize(this.textFontSize)
    .textAlign(TextAlign.Center); // 设置文本居中显示
  ```

  完整示例：

  ```screen
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  @Builder
  export function SolutionTwoBuilder() {
    SolutionTwo();
  }

  @Entry
  @Component
  struct SolutionTwo {
    @State textFontSize: number = 24;
    pathStack: NavPathStack = new NavPathStack();
    myText: string =
      '永和九年，岁在癸丑，暮春之初，会于会稽山阴之兰亭，修禊事也。群贤毕至，少长咸集。此地有崇山峻岭，茂林修竹；又有清流激湍，映带左右，引以为流觞曲水，列坐其次。虽无丝竹管弦之盛，一觞一咏，亦足以畅叙幽情。是日也，天朗气清，惠风和畅，仰观宇宙之大，俯察品类之盛，所以游目骋怀，足以极视听之娱，信可乐也。\n' +
        '\n' +
        '　　夫人之相与，俯仰一世，或取诸怀抱，悟言一室之内；或因寄所托，放浪形骸之外。虽趣舍万殊，静躁不同，当其欣于所遇，暂得于己，快然自足，不知老之将至。及其所之既倦，情随事迁，感慨系之矣。向之所欣，俯仰之间，已为陈迹，犹不能不以之兴怀。况修短随化，终期于尽。古人云：“死生亦大矣。”岂不痛哉！(不知老之将至 一作：曾不知老之将至)\n' +
        '\n' +
        '　　每览昔人兴感之由，若合一契，未尝不临文嗟悼，不能喻之于怀。固知一死生为虚诞，齐彭殇为妄作。后之视今，亦犹今之视昔。悲夫！故列叙时人，录其所述，虽世殊事异，所以兴怀，其致一也。后之览者，亦将有感于斯文。';

    aboutToAppear(): void {
      let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowLayoutFullScreen(true);
      });
    }

    build() {
      NavDestination() {
        Column() {
          Scroll() {
            Column() {
              Text(this.myText)
                .fontSize(this.textFontSize)
                .textAlign(TextAlign.Center); // 设置文本居中显示
            };
          }
          .height('80%')
          .width('100%')
          .scrollBar(BarState.Off)
          .padding({ left: 10, right: 10 });

          Column() {
            Text('字体大小：' + this.textFontSize)
              .fontSize(20)
              .margin({ top: 10 });
            Row() {
              Image($r('app.media.minus')) // $r('app.media.minus')需要替换为开发者需要的图片资源文件
                .height(20)
                .width(20)
                .objectFit(ImageFit.Contain)
                .onClick(() => {
                  this.textFontSize -= 1;
                });

              Slider({
                value: this.textFontSize,
                min: 24,
                max: 56, // 字体尺寸最大值设置过大
                style: SliderStyle.InSet
              })
                .id('Slider')
                .blockColor(Color.White)
                .trackColor('#D1D1D6')
                .selectedColor('#0A59F7')
                .trackThickness(20)
                .blockSize({ width: 15, height: 15 })
                .showTips(false)
                .width('70%')
                .onChange((value: number) => {
                  this.textFontSize = value;
                });

              Image($r('app.media.plus')) // $r('app.media.plus')需要替换为开发者需要的图片资源文件
                .height(20)
                .width(20)
                .objectFit(ImageFit.Contain)
                .onClick(() => {
                  this.textFontSize += 1;
                });
            }
            .width('90%')
            .justifyContent(FlexAlign.SpaceAround)
            .margin({ top: 10 });
          }
          .backgroundColor('#f1f3f5')
          .width('100%')
          .height('20%')
          .borderRadius({ topLeft: 20, topRight: 20 });
        }
        .height('100%')
        .width('100%');
      }
      .onBackPressed(() => {
        this.pathStack.pop();
        return true;
      })
      .hideTitleBar(true)
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
      .padding({ top: '123px' })
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/d9K43DKVTWaRFJ7AtiAa7A/zh-cn_image_0000002658834713.png "点击放大")
