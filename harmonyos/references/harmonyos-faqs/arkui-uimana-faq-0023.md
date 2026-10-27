---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0023
title: 软键盘避让与布局弹起常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 软键盘避让与布局弹起常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7b2f080d9d49af3d13ee67d17e35e0473a2d5f7a830566b02edd4cac21cc0938
---

**Q：用户与软键盘进行交互时，可能会出现重要信息被软键盘遮挡、软键盘弹出导致布局错位、软键盘弹出导致弹窗过度上抬问题，如何实现软键盘避让，提高用户体验？**

**A**：实现软键盘避让的方式及其适用场景内容如下：

| 实现场景 | 实现方式 | 适用场景 |
| --- | --- | --- |
| 场景一 | 设置避让模式为RESIZE（压缩模式） | 重要信息被软键盘遮挡(如底部操作栏被遮挡) |
| 场景二 | 设置避让模式为OFFSET\_WITH\_CARET或RESIZE\_WITH\_CARET | 多个输入框中切换时触发键盘避让（输入框光标位置发生变化时候也会触发） |
| 场景三 | 组件设置.expandSafeArea([SafeAreaType.KEYBOARD])属性 | 软键盘弹出导致布局错位（如顶部标题被软键盘向上抬） |
| 场景四 | 设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，将软键盘避让模式设置为压缩 | 软键盘弹出导致弹窗过度上抬（如自定义弹窗被键盘顶起） |
| 场景五 | 设置KeyboardOptions属性的supportAvoidance字段为true | 自定义软键盘 |
| 场景六 | 使用window.on('keyboardHeightChange', callback)监听键盘高度变化 | 重要信息被软键盘遮挡(如底部操作栏被遮挡) |

* 场景一：若重要信息被软键盘遮挡(如底部操作栏被遮挡)，可以设置软键盘的避让模式为KeyboardAvoidMode.RESIZE（压缩模式），压缩内容区域的高度。
* 场景二：若想在多个输入框中切换时触发键盘避让（输入框光标位置发生变化时候也会触发），可以将键盘避让模式设置为[KeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-e.md#keyboardavoidmode11)类型的枚举值OFFSET\_WITH\_CARET或RESIZE\_WITH\_CARET，可以根据需要选择使用OFFSET或RESIZE模式。
* 场景三：若软键盘弹出导致布局错位（如顶部标题被软键盘向上抬），需要给对应的组件设置.expandSafeArea([SafeAreaType.KEYBOARD])属性，使标题组件不避让键盘。以下示例展示了在聊天页面中为顶部标题设置.expandSafeArea([SafeAreaType.KEYBOARD])属性，使标题在键盘弹出时保持固定位置：

  ```ts
  import { KeyboardAvoidMode } from '@kit.ArkUI';

  @Entry
  @Component
  struct KeyboardDemo {
    textList: string[] = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];

    aboutToAppear(): void {
      this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE)
    }

    build() {
        Column() {
          Row() {
            Text('标题')
          }
          .expandSafeArea([SafeAreaType.KEYBOARD])
          Column(){
            List() {
              ForEach(this.textList, (item: string) => {
                ListItem() {
                  Text('消息列表' + item)
                }
                .margin(30)
              }, (item: string) => item)
            }
          }.layoutWeight(1)
          TextInput({ placeholder: '输入消息' })
        }
      .width('100%')
      .height('100%')
    }
  }
  ```

* 场景四：若软键盘弹出导致弹窗过度上抬（如自定义弹窗被键盘顶起），可以参考[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)中的弹窗类型，通过设置NavDestination的mode为NavDestinationMode.DIALOG弹窗类型，并且将软键盘避让模式设置为压缩模式，具体实现可参考[自定义弹窗被键盘顶起](../best-practices/bpta-keyboard-layout-adapt.md#section381324419328)。
* 场景五：若使用自定义软键盘，则设置KeyboardOptions属性的supportAvoidance字段为true，设置自定义键盘支持避让功能。
* 场景六：若唤起软键盘时，系统会自动向上移动页面让输入组件位于键盘避让区的上方，但输入组件下方的组件会被遮挡，可以通过监听键盘高度变化，自行控制页面向上偏移的距离。
  + 关闭页面对键盘的自动避让，避免键盘避让区对计算页面偏移距离的影响。
  + 设置状态变量offsetNum，用来控制组件向上偏移的距离。
  + 使用window.on('keyboardHeightChange', callback)监听键盘高度变化，在键盘弹出和收起时高度变化均会触发回调，在回调函数中改变状态变量offsetNum的数值。
  + 使用offset()设置页面向上指定offsetNum。

    ```ts
    import window from '@ohos.window';
    import { KeyboardAvoidMode } from '@kit.ArkUI';

    @Entry
    @Component
    struct KeyboardAvoidDemo {
      @State text: string = '';
      controller: TextInputController = new TextInputController();
      @State offsetNum: number = 0;

      onPageShow(): void {
        // 获取当前窗口实例
        window.getLastWindow(this.getUIContext().getHostContext()).then((curWindow) => {
          try {
            curWindow.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE); // 关闭当前页面对键盘的自动避让
            // 监听键盘高度变化，返回键盘高度，单位为像素px
            curWindow.on('keyboardHeightChange', (height) => {
              // 在键盘高度变化时改变状态变量offsetNum
              if (height > 0) {
                this.getUIContext().animateTo({
                  duration: 200,
                  curve: Curve.Smooth
                }, () => {
                  this.offsetNum = this.getUIContext().px2vp(height); // 页面向上偏移的距离为键盘的高度
                });
              } else {
                this.getUIContext().animateTo({
                  duration: 200,
                  curve: Curve.Smooth
                }, () => {
                  this.offsetNum = 0; // height为0说明键盘收起
                });
              }
              console.info(`Succeeded in enabling the listener for keyboard height changes. Data: ${height}`);
            });
          } catch (exception) {
            console.error(`Failed to listen keyboard height. Cause: ${exception.code}, message: ${exception.message}`);
          }
        }).catch((err: string) => {
          console.error(`setWindowOrientation： Failed to obtain the top window. Cause: ${err}`);
        });
      }

      build() {
        Column() {
          Row() {
          }
          .width('100%')
          .height(550);

          Column() {
            Text('这是一个文本组件text1，和输入框同层级');
            TextInput({ text: this.text, controller: this.controller, placeholder: '请输入内容' })
              .placeholderFont({ size: 16, weight: 400 })
              .width('90%')
              .onChange((value: string) => {
                this.text = value;
              });
            Text('这是一个文本组件text2，和输入框同层级');
          }
          .justifyContent(FlexAlign.SpaceAround)
          .height('600px');

          Text('这是一个文本组件text3')
            .width('100%')
            .textAlign(TextAlign.Center);
        }
        .width('100%')
        .height('100%')
        .offset({
          bottom: this.offsetNum // 相对于页面底部偏移
        });
      }
    }
    ```

    效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/nz2yRD6mRTqdi0EU4ABuGw/zh-cn_image_0000002801460809.png "点击放大")
  + 更多场景案例请参考官网：[软键盘布局适配](../best-practices/bpta-keyboard-layout-adapt.md)。

**Q：设置软键盘避让模式时报错，报错信息如下所示：**

```ts
Property 'RESIZE' does not exist on type 'typeof KeyboardAvoidMode'. <ArkTSCheck>
```

**A**：需要导入模块KeyboardAvoidMode。

```ts
import { KeyboardAvoidMode } from '@kit.ArkUI';
```

**Q：KeyboardAvoidMode的生效范围是什么？**

**A**：生效范围是整个窗口，如果需要在单页面指定特定的KeyboardAvoidMode，可以在aboutToAppear和aboutToDisappear中更改和回退KeyboardAvoidMode的值。

**Q：默认上抬模式下键盘弹出后页面上抬高度不符合预期，改为KeyboardAvoidMode.RESIZE后高度才正确，是什么原因？**

**A**：默认OFFSET模式是根据光标位置进行避让，并非输入框底部，因此上抬高度可能与预期不一致，此为预期行为。若需要在输入框底部进行避让，可以参考[on('keyboardHeightChange')](../harmonyos-references/arkts-apis-window-window.md#onkeyboardheightchange7)接口，在业务中自行处理避让逻辑。

**Q：使用window.on('keyboardHeightChange')监听键盘高度变化并自行控制偏移时，键盘收起时输入框动画不够流畅，如何优化？**

**A**：在animateTo中使用[curves.interpolatingSpring](../harmonyos-references/js-apis-curve.md#curvesinterpolatingspring10)曲线，使输入框与窗口的键盘动画同步移动。键盘弹出和收起时使用不同参数的interpolatingSpring曲线，可以实现更流畅的动画效果，示例代码如下：

```ts
import { curves } from '@kit.ArkUI';
import window from '@ohos.window';

// 监听键盘高度变化，windowClass为获取到的窗口实例
windowClass.on('keyboardHeightChange', (height: number) => {
  this.getUIContext().animateTo({
    curve: height > 0 ? curves.interpolatingSpring(0, 1, 342, 37) : curves.interpolatingSpring(4, 1, 342, 37)
  }, () => {
    this.keyboardHeight = this.getUIContext().px2vp(height);
  });
});
```

**Q：setKeyboardAvoidMode的默认值是什么？默认是否会遮挡？**

**A**：[setKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)的默认值为KeyboardAvoidMode.OFFSET，即键盘抬起时默认采用上抬模式，页面会向上抬起以避让键盘，不会被键盘遮挡。

**Q：输入框拉起键盘时，如何将底部布局弹起到键盘顶部？**

**A**：原因分析：软键盘弹出时，默认顶起输入框，下方的显示组件将被遮挡。

解决措施：获取窗口内容规避的区域，规避区域类型为软键盘区域（TYPE\_KEYBOARD）。当软键盘弹出时，获取规避区域的高度，并通过设置margin-bottom顶起组件。参考代码如下：

```ts
import { window } from '@kit.ArkUI';

@Entry
struct BottomPopsUpAsTheTopOfKeyboard {
  context = this.getUIContext();
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5];
  @State scrollHeight: number = 0;
  @State isRebuild: boolean = false;
  @State keyHeight: number = 0;
  @State text: string = '';
  aboutToAppear() {
    window.getLastWindow(this.context.getHostContext()).then(currentWindow => {
      // Set the layout of the window to immersive layout
      currentWindow.setWindowLayoutFullScreen(true);
      let property = currentWindow.getWindowProperties();
      // Initialize window height
      let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
      this.scrollHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.bottomRect.height);
      // Monitor the hiding and showing of the soft keyboard
      currentWindow.on('avoidAreaChange', data => {
        if (data.type == window.AvoidAreaType.TYPE_KEYBOARD) {
          this.keyHeight = this.getUIContext().px2vp(data.area.bottomRect.height);
          this.scrollHeight =
            this.getUIContext().px2vp(currentWindow.getWindowProperties().windowRect.height - data.area.bottomRect.height);
          return;
        }
      })
    })
  }
  build() {
    Stack({ alignContent: Alignment.TopStart }) {
      Column() {
        Scroll(this.scroller) {
          Column() {
            TextInput({ text: this.text, placeholder: 'input your word...' })
              .placeholderFont({
                size: 14,
                weight: 400
              })
              .width(320)
              .height(40)
              .margin(200)
              .fontSize(14)
              .fontColor(Color.Black)
              .backgroundColor(Color.White)
            ForEach(this.arr, (item: number) => {
              Text(item.toString())
                .width('90%')
                .height(150)
                .backgroundColor(0xFFFFFF)
                .borderRadius(15)
                .fontSize(16)
                .textAlign(TextAlign.Center)
                .margin({ top: 10 })
            })
          }
          .width('100%')
        }
        .width('100%')
        .height(this.scrollHeight)
        .layoutWeight(1)
        Text('This is a test text')
          .width('100%')
          .height(50)
          .backgroundColor(Color.Red)
          .margin({ bottom: this.keyHeight })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Start)
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
  }
}
```

参考链接：[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)。
