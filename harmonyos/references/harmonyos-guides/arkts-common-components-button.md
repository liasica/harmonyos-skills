---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-button
title: 按钮 (Button)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 按钮 (Button)
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:07+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3ea281bd819669bc4515fcfda1e16ce2971196193de4ff89f7e59db7cb6f4f7b
---

Button是按钮组件，通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮、圆角矩形按钮。Button作为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。具体用法请参考[Button](../harmonyos-references/ts-basic-components-button.md)。

## 创建按钮

Button通过调用接口来创建，接口调用有以下两种形式：

* 通过label和[ButtonOptions](../harmonyos-references/ts-basic-components-button.md#buttonoptions对象说明)创建不包含子组件的按钮。以ButtonOptions中的type和stateEffect为例。

  ```ts
  Button(label?: ResourceStr, options?: { type?: ButtonType, stateEffect?: boolean })
  ```

  其中，label用来设置按钮文字，type用于设置Button类型，stateEffect属性设置Button是否开启点击效果。

  ```typescript
  Button('Ok', { type: ButtonType.Normal, stateEffect: true })
    .borderRadius(8)
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/WFqVnguESeyQ2JHcGSQamA/zh-cn_image_0000002821756643.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=87E0AD61C9EAE4B9097C2C7184F5E1597430BDA9E7A4D4C7E12B63649012D150)
* 通过[ButtonOptions](../harmonyos-references/ts-basic-components-button.md#buttonoptions对象说明)创建包含子组件的按钮。以ButtonOptions中的type和stateEffect为例。

  ```ts
  Button(options?: {type?: ButtonType, stateEffect?: boolean})
  ```

  只支持包含一个子组件，子组件可以是基础组件或者容器组件。

  ```typescript
  Button({ type: ButtonType.Normal, stateEffect: true }) {
    Row() {
      // 请将$r('app.media.loading')替换为实际资源文件
      Image($r('app.media.loading')).width(20).height(40).margin({ left: 12 })
      Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
    }.alignItems(VerticalAlign.Center)
  }.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/EJU3dp-bRi61-wLaZQRWtw/zh-cn_image_0000002793036706.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=1CDFFFE691F3AF90FF55324549B9432CE55A77DCF564AD6C847DDE0754805278)

## 设置按钮类型

Button有四种可选类型，分别为胶囊类型（Capsule）、圆形按钮（Circle）、普通按钮（Normal）和圆角矩形按钮（ROUNDED\_RECTANGLE），通过type进行设置。

* 胶囊按钮（默认类型）。

  此类型按钮的圆角自动设置为高度的一半，不支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Disable', { type: ButtonType.Capsule, stateEffect: false })
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/tR4kQyeiRPu_srU_v20JpQ/zh-cn_image_0000002792876738.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=57CF90EC666756205A1B95D225A3BAF2DF59DC387A2CD773DA6A68163B9E41A9)
* 圆形按钮。

  此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Circle', { type: ButtonType.Circle, stateEffect: false })
    .backgroundColor(0x317aff)
    .width(90)
    .height(90)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/QGYs4kH3Qu29TDnZxMOdyA/zh-cn_image_0000002821836643.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=C8C383101D9DE6836F35F71A85E96601286DB1C67C232B6B860855EBC8259CCF)
* 普通按钮。

  此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Ok', { type: ButtonType.Normal, stateEffect: true })
    .borderRadius(8)
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/mQdYXch3QvWOQzeV6vPYbg/zh-cn_image_0000002821756645.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F838E68A649AB587CC5B5C6B7B34C1494B8E00BBE4CCD41C79BBAB0E839FF19)
* 圆角矩形按钮。

  当[controlSize](../harmonyos-references/ts-basic-components-button.md#controlsize11)为NORMAL时，默认圆角大小为20vp，[controlSize](../harmonyos-references/ts-basic-components-button.md#controlsize11)为SMALL时，圆角大小为14vp，支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Disable', { type: ButtonType.ROUNDED_RECTANGLE, stateEffect: true })
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Pclu6tijQKmmjnOOn9x6UQ/zh-cn_image_0000002792876738.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=5248544C2C94659E450A03BD9AAA1B8341688DAEF6F77D509ED0FCE08CEA3E6B)

## 自定义样式

* 设置边框弧度。

  使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。

  ```typescript
  Button('circle border', { type: ButtonType.Normal })
    .borderRadius(20)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/WITlIldlQPuuEMWwZEds2w/zh-cn_image_0000002793036708.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB0065491D47C213EBB22572B1BCBE6434A8D20D8A74F0F8D40B3C1A09BD56BC)
* 设置文本样式。

  通过添加文本样式设置按钮文本的展示样式。

  ```typescript
  Button('font style', { type: ButtonType.Normal })
    .fontSize(20)
    .fontColor(Color.Pink)
    .fontWeight(800)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/GzOcvatQRhSKmNyEfYrxcw/zh-cn_image_0000002792876740.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=C08451121A8883162FD86096B1AF58AEC585B17691A2144BBBE1B37FDC9B3059)
* 设置背景颜色。

  添加backgroundColor属性设置按钮的背景颜色。

  ```typescript
  Button('background color').backgroundColor(0xF55A42)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/ZmFw15bjQc-gJa2UX1s2EA/zh-cn_image_0000002821836645.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF1F5B93AEA431D5A6F3F148BAFD51B30423621CBC6D73796D2041F3B80AC84F)
* 创建功能型按钮。

  创建删除操作的按钮。

  ```typescript
  Button({ type: ButtonType.Circle, stateEffect: true }) {
    // 请将$r('app.media.ic_public_delete_filled')替换为实际资源文件
    Image($r('app.media.ic_public_delete_filled')).width(30).height(30)
  }.width(55).height(55).margin({ 'left': 20 }).backgroundColor(0xF55A42)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/CEKJSUCYR-auD6cL6kiVqg/zh-cn_image_0000002821756647.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=F95E3DE0630C3607CCA7FC6310D119E2BC176B81FD9AD922398E924DAF0C4CF0)

## 添加事件

Button组件通常用于触发某些操作，可以绑定onClick事件来响应点击操作后的自定义行为。

```typescript
Button('Ok', { type: ButtonType.Normal, stateEffect: true })
  .onClick(()=>{
    hilog.info(DOMAIN, 'testTag', 'Button onClick');
  }).margin(10)
```

## 场景示例

* 用于启动操作。

  可以用按钮启动任何用户界面元素，按钮会根据用户的操作触发相应的事件。例如，在List容器里通过点击按钮进行页面跳转。

  ```typescript
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;
  // xxx.ets
  @Entry
  @Component
  export struct ButtonCaseTouch {
    pathStack: NavPathStack = new NavPathStack();

    @Builder
    PageMap(name: string) {
      if (name === 'first_page') {
        pageOneTmp()
      } else if (name === 'second_page') {
        pageTwoTmp()
      } else if (name === 'third_page') {
        pageThreeTmp()
      }
    }

    build() {
      NavDestination() {
        Navigation(this.pathStack) {
          List({ space: 4 }) {
            ListItem() {
              Button('First').onClick(() => {
                this.pathStack.pushPath({ name: 'first_page' });
              })
                .width('100%')
            }

            ListItem() {
              Button('Second').onClick(() => {
                this.pathStack.pushPath({ name: 'second_page' });
              })
                .width('100%')
            }

            ListItem() {
              Button('Third').onClick(() => {
                this.pathStack.pushPath({ name: 'third_page' });
              })
                .width('100%')
            }
          }
          .listDirection(Axis.Vertical)
          .backgroundColor(0xDCDCDC).padding(20)
        }
        .mode(NavigationMode.Stack)
        .navDestination(this.PageMap)
      }
    }
  }

  // pageOne
  @Component
  export struct pageOneTmp {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Text('first_page')
        }.width('100%').height('100%')
      }.title('pageOne')
      .onBackPressed(() => {
        const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
        // 请将$r('app.string.return_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
        hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return_value') + JSON.stringify(popDestinationInfo));
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
    }
  }

  // pageTwo
  @Component
  export struct pageTwoTmp {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Text('second_page')
        }.width('100%').height('100%')
      }.title('pageTwo')
      .onBackPressed(() => {
        const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
        // 请将$r('app.string.return_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
        hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return_value') + JSON.stringify(popDestinationInfo));
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
    }
  }

  // pageThree
  @Component
  export struct pageThreeTmp {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Text('third_page')
        }.width('100%').height('100%')
      }.title('pageThree')
      .onBackPressed(() => {
        const popDestinationInfo = this.pathStack.pop(); // 弹出路由栈栈顶元素
        // 请将$r('app.string.return_value')替换为实际资源文件，在本示例中该资源文件的value值为"返回值"
        hilog.info(DOMAIN, 'testTag', 'pop' + $r('app.string.return_value') + JSON.stringify(popDestinationInfo));
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/hc5RqzJnSF-4HJZiA0rZ8Q/zh-cn_image_0000002793036710.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=BFE212654CC55F11E51028967820E7F6D5514D515EDB150417A6FA233AC2ED5A)
* 用于提交表单。

  在用户登录/注册页面，使用按钮进行登录或注册操作。

  ```typescript
  // xxx.ets
  const DOMAIN = 0x0000;
  @Entry
  @Component
  export struct ButtonCaseLogin {
    build() {
      NavDestination() {
        Column() {
          TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
          TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
          Button('Register').width(300).margin({ top: 20 })
            .onClick(() => {
              // 需要执行的操作
            })
          // ···
        }.padding(20)
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/ofOrey2mRNml-gctzWdjag/zh-cn_image_0000002792876742.png?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=25992C492F6D88B594B12403DA6F2D45AE2AAB6E69641E8B0D484903ADC40137)
* 悬浮按钮。

  在可以滑动的界面，滑动时按钮始终保持悬浮状态。

  ```typescript
  // xxx.ets
  @Entry
  @Component
  export struct HoverButtonExample {
    private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    build() {
      NavDestination() {
        Stack() {
          List({ space: 20, initialIndex: 0 }) {
            ForEach(this.arr, (item: number) => {
              ListItem() {
                Text('' + item)
                  .width('100%')
                  .height(100)
                  .fontSize(16)
                  .textAlign(TextAlign.Center)
                  .borderRadius(10)
                  .backgroundColor(0xFFFFFF)
              }
            }, (item: number) => item.toString())
          }.width('90%')

          Button() {
            // 请将$r('app.media.ic_public_add')替换为实际资源文件
            Image($r('app.media.ic_public_add'))
              .width(50)
              .height(50)
          }
          .width(60)
          .height(60)
          .position({ x: '80%', y: 600 })
          .shadow({ radius: 10 })
          .onClick(() => {
            // 需要执行的操作
          })
        }
        .width('100%')
        .height('100%')
        .backgroundColor(0xDCDCDC)
        .padding({ top: 5 })
      }
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/lEKtNTAKSWyWVEUFbIo4FQ/zh-cn_image_0000002821836647.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=195B500E431950AE89350C9E24285B7D9A4DD1A427F3287F36CEE17D21DC731E)
