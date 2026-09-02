---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1516
title: 开发自定义键盘，HarmonyOS中有没有长按按键子项生成气泡效果的API
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 开发自定义键盘，HarmonyOS中有没有长按按键子项生成气泡效果的API
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a05396333cfa5d9f24660ecc4bbbdce77e4a8c582d3230671210e11496a4fcf2
---

## 问题现象

按键子项生成气泡效果用什么组件实现好？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/2wD3PJLYQLG7k18xTnSvyA/zh-cn_image_0000002658845807.png "点击放大")

## 背景知识

使用[自定义键盘实现](../best-practices/bpta-custom-keyboard.md)官网示例代码进行自定义键盘调试，然后用[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)增加长按手势事件，最后使用[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)为组件绑定Popup气泡，使用Popup气泡，如果按键处于边缘位置，组件会自动偏移，完整的显示在屏幕中间。

## 解决方案

自定义键盘没有直接长按生成气泡的接口，需要自定义长按逻辑，手指在长按小键盘组件时，使用Popup生成一个气泡，在气泡生成之后，使用onTouch获取手指位置并且根据气泡组件的位置和横向大小，计算当前手指划过的距离从而标记手指当前选择的内容。

代码实现思路如下：

1. 创建变量控制气泡显隐样式以及气泡在边缘的位置：

   ```ts
   @State customPopup: boolean = false;
   @State indexNum: number = 0;
   // 手指位置1、2、3、4（长按气泡中显示的内容数量）四个参数，分别代指长按后出现的四个位置，参数值与实际业务有关。
   @State fingerRect: string = '1';
   // 组件宽度
   @State widthRect: number = 0;
   // 键盘宽度
   @State inputWidthRect: number = 0;
   // 判断是否在偏右侧位置
   @State isRight: boolean = false;
   ```
2. 增加LongPressGesture长按控制手势，在onAction事件中增加逻辑，让气泡仅显示在指定按键上方；长按手势默认最短长按时间为500毫秒，可配置duration参数控制最短长按时长：

   ```ts
   .gesture(
     // 绑定可以重复触发的LongPressGesture
     LongPressGesture({ repeat: true })
       .onAction(() => {
         for (let i = 0; i < EnglishKeyboardData[0].length; i++) {
           if (item.text === EnglishKeyboardData[0][i].text) {
             this.indexNum = i;
             break;
           }
         }
         this.customPopup = true;
       })
       .onActionEnd(() => {
         this.customPopup = !this.customPopup;
       })
   )
   ```
3. 增加bindPopup气泡控制，设置placement: Placement.TopRight,让气泡显示在按钮上方，通过this.popupBuilder(item)给自定义气泡组件传参然后自定义气泡内容：

   ```ts
   .bindPopup(this.customPopup && EnglishKeyboardData[0].indexOf(item) === this.indexNum, {
     // CustomPopupOptions类型气泡的内容
     builder: this.popupBuilder(item),
     placement: Placement.TopLeft,
     targetSpace: '15vp',
     enableArrow: false,
     onStateChange: (e) => {
       if (!e.isVisible) {
         this.customPopup = false;
       }
     }
   })
   ```

   ```ts
   @Builder
   popupBuilder(item: Menu) {
     Row() {
       ForEach([1, 2, 3, 4], (num: number, index: number) => {
         if (this.fingerRect === index + 1 + '') {
           Row() {
             Text(item.text + '' + num)
               .fontColor(Color.White);
           }
           .globalFancy()
           .backgroundColor(Color.Blue)
           .justifyContent(FlexAlign.Center);
         } else {
           Row() {
             Text(item.text + '' + num);
           }
           .globalFancy()
           .justifyContent(FlexAlign.Center);
         }
       }, (num: number) => JSON.stringify(num));
     }
     .height(50)
     .width(150)
     .padding(5)
     .justifyContent(FlexAlign.SpaceAround)
     .onAreaChange((oldVal, newVal) => {
       // 如果此时键盘在偏右侧位置，需要重新计算位置
       this.isRight = this.inputWidthRect <= Math.ceil(Number(newVal.globalPosition.x) + Number(newVal.width));
     });
   }
   ```
4. 使用onAreaChange监听新生成的气泡组件的宽度，再使用onTouch事件获取当前手指的坐标，然后根据手指的坐标和气泡组件的宽度，获取当前手指在气泡组件中的位置：

   ```ts
   .onTouch((event) => {
     // 获取当前手指的坐标（相对于父容器，与组件rect的坐标系一致）
     const fingerX = event.touches[0].x;
     // 靠近右边屏幕时，需要特殊处理。
     this.fingerRect =
       this.isRight ? Math.ceil(((fingerX + event.touches[0].displayX) - 230) / this.widthRect) + '' :
         Math.ceil(fingerX / this.widthRect) + '';
     this.fingerRect =
       (Number(this.fingerRect) <= 1) ? '1' : Number(this.fingerRect) >= 4 ? '4' : this.fingerRect;
   })
   .onAreaChange((oldVal, newVal) => {
     this.widthRect = Number(newVal.width);
   });
   ```

参考官网[自定义键盘实现](../best-practices/bpta-custom-keyboard.md)，将demo中的NumberKeyboard文件替换为以下示例代码：

```ts
  // 该场景代码基于自定义键盘实现官网示例代码https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-keyboard#section1680905412256进行调试；
  // 修改demo中NumberKeyboard文件如下
@Component
export struct NumberKeyboard {
  @State customPopup: boolean = false;
  @State indexNum: number = 0;
  // 手指位置1、2、3、4（长按气泡中显示的内容数量）四个参数，分别代指长按后出现的四个位置，参数值与实际业务有关。
  @State fingerRect: string = '1';
  // 组件宽度
  @State widthRect: number = 0;
  // 键盘宽度
  @State inputWidthRect: number = 0;
  // 判断是否在偏右侧位置
  @State isRight: boolean = false;

  build() {
    Row() {
      Scroll() {
        Column() {
          Row({ space: Constants.ENGLISH_KEYBOARD_BUTTON_SPACE }) {
            ForEach(EnglishKeyboardData[0], (item: Menu) => {
              EnglishButton({ item: item })
                .gesture(
                  // 绑定可以重复触发的LongPressGesture
                  LongPressGesture({ repeat: true })
                    .onAction(() => {
                      for (let i = 0; i < EnglishKeyboardData[0].length; i++) {
                        if (item.text === EnglishKeyboardData[0][i].text) {
                          this.indexNum = i;
                          break;
                        }
                      }
                      this.customPopup = true;
                    })
                    .onActionEnd(() => {
                      this.customPopup = !this.customPopup;
                    })
                )
                .bindPopup(this.customPopup && EnglishKeyboardData[0].indexOf(item) === this.indexNum, {
                  // CustomPopupOptions类型气泡的内容
                  builder: this.popupBuilder(item),
                  placement: Placement.TopLeft,
                  targetSpace: '15vp',
                  enableArrow: false,
                  onStateChange: (e) => {
                    if (!e.isVisible) {
                      this.customPopup = false;
                    }
                  }
                })
                .onTouch((event) => {
                  // 获取当前手指的坐标（相对于父容器，与组件rect的坐标系一致）
                  const fingerX = event.touches[0].x;
                  // 靠近右边屏幕时，需要特殊处理。
                  this.fingerRect =
                    this.isRight ? Math.ceil(((fingerX + event.touches[0].displayX) - 230) / this.widthRect) + '' :
                      Math.ceil(fingerX / this.widthRect) + '';
                  this.fingerRect =
                    (Number(this.fingerRect) <= 1) ? '1' : Number(this.fingerRect) >= 4 ? '4' : this.fingerRect;
                })
                .onAreaChange((oldVal, newVal) => {
                  this.widthRect = Number(newVal.width);
                });
            }, (item: Menu) => JSON.stringify(item));
          };

          Row({ space: Constants.ENGLISH_KEYBOARD_BUTTON_SPACE }) {
            ForEach(EnglishKeyboardData[1], (item: Menu) => {
              EnglishButton({ item: item });
            }, (item: Menu) => JSON.stringify(item));
          }
          .padding({
            left: 18,
            right: 18,
            top: 11
          });

          Row({ space: Constants.ENGLISH_KEYBOARD_BUTTON_SPACE }) {
            ForEach(EnglishKeyboardData[2], (item: Menu) => {
              EnglishButton({ item: item });
            }, (item: Menu) => JSON.stringify(item));
          }
          .padding({ top: 11 });

          Row({ space: Constants.ENGLISH_KEYBOARD_BUTTON_SPACE }) {
            ForEach(EnglishKeyboardData[3], (item: Menu) => {
              EnglishButton({ item: item });
            }, (item: Menu) => JSON.stringify(item));
          }
          .padding({ top: 11 });
        }
        .onAreaChange((oldVal, newVal) => {
          // 键盘宽度
          this.inputWidthRect = Math.ceil(Number(newVal.globalPosition.x) + Number(newVal.width));
        });
      }
      .scrollable(ScrollDirection.Horizontal)
      .scrollBar(BarState.Off);
    };
  }

  @Builder
  popupBuilder(item: Menu) {
    Row() {
      ForEach([1, 2, 3, 4], (num: number, index: number) => {
        if (this.fingerRect === index + 1 + '') {
          Row() {
            Text(item.text + '' + num)
              .fontColor(Color.White);
          }
          .globalFancy()
          .backgroundColor(Color.Blue)
          .justifyContent(FlexAlign.Center);
        } else {
          Row() {
            Text(item.text + '' + num);
          }
          .globalFancy()
          .justifyContent(FlexAlign.Center);
        }
      }, (num: number) => JSON.stringify(num));
    }
    .height(50)
    .width(150)
    .padding(5)
    .justifyContent(FlexAlign.SpaceAround)
    .onAreaChange((oldVal, newVal) => {
      // 如果此时键盘在偏右侧位置，需要重新计算位置
      this.isRight = this.inputWidthRect <= Math.ceil(Number(newVal.globalPosition.x) + Number(newVal.width));
    });
  }

}

@Styles
function globalFancy() {
  .borderRadius(10)
  .width('25%')
  .height('100%');
}

// [Start EnglishButton_start]
@Component
struct EnglishButton {
  @Consume inputText: string;
  // [StartExclude EnglishButton_start]
  @Prop item: Menu;
  @Consume keyboardController: KeyboardController;

  getEnglishText(item: Menu): string | Resource {
    if (this.keyboardController.isUpperCase && item.upperText) {
      return item.upperText;
    } else {
      return item.text;
    }
  }

  // [EndExclude EnglishButton_start]

  build() {
    Button({ type: ButtonType.Normal }) {
      if (typeof this.getEnglishText(this.item) === 'string' ||
        (this.getEnglishText(this.item) as Resource).type !== Constants.RESOURCE_TYPE_MEDIA) {
        Text(this.getEnglishText(this.item));
      } else {
        Image(this.getEnglishText(this.item))
          .width(Constants.KEYBOARD_BUTTON_FONTSIZE_18)
          .height(Constants.KEYBOARD_BUTTON_FONTSIZE_18);
      }
    }
    .fontColor(Color.Black)
    .backgroundColor(this.item.backgroundColor)
    .borderRadius(Constants.KEYBOARD_BUTTON_RADIUS)
    .fontSize(Constants.KEYBOARD_BUTTON_FONTSIZE_18)
    .padding(0)
    .width(this.item.width)
    .height(this.item.height)
    .onClick(() => {
      this.inputText = this.keyboardController.onInput(this.getEnglishText(this.item));
    });
  }
}

// [End EnglishButton_start]
```
