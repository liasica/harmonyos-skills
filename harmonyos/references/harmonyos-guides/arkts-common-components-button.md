---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-button
title: 按钮 (Button)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 按钮与选择 > 按钮 (Button)
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:41+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:c1a492cf36778dd6b476db7bdfcdcccf7f2155247a01f50bab5bfb255c92b83d
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/CYoe-RtfRI-uMjIgEYvQlw/zh-cn_image_0000002791565086.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=D7DF5E048F3C7F4C20E2B5061BD7C19F7C6875E086723A0BF59DEE7826B4F75F)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/vkoH5oL5SICtYshI_U2n8A/zh-cn_image_0000002820525039.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F52850B80107BDC76C102CB8ABF604EF651160AB453C3D584187EE9CCA42E89)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/8As3ufaqQTu9_2-EZ_8Ldw/zh-cn_image_0000002820405039.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CD0E9A98B37630A38C5025ACFA10D6BC6875AD6497B43FF2385E8B1D389E197)
* 圆形按钮。

  此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Circle', { type: ButtonType.Circle, stateEffect: false })
    .backgroundColor(0x317aff)
    .width(90)
    .height(90)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/cojRKUWWR56kUKVIUw_-Iw/zh-cn_image_0000002791725060.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=6AB93A3F485521AD61A0800871A67E4723CBA9F4557D02D14F4D2D74C469DA4B)
* 普通按钮。

  此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Ok', { type: ButtonType.Normal, stateEffect: true })
    .borderRadius(8)
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/VEX05j-vRUank3KTk4ObRg/zh-cn_image_0000002791565088.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=A3454E84CF9E612F94410D66625B72E2D7ABD7CF07055FD8D9556FF3BA0785BB)
* 圆角矩形按钮。

  当[controlSize](../harmonyos-references/ts-basic-components-button.md#controlsize11)为NORMAL时，默认圆角大小为20vp，[controlSize](../harmonyos-references/ts-basic-components-button.md#controlsize11)为SMALL时，圆角大小为14vp，支持通过borderRadius属性重新设置圆角。

  ```typescript
  Button('Disable', { type: ButtonType.ROUNDED_RECTANGLE, stateEffect: true })
    .backgroundColor(0x317aff)
    .width(90)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/ldS1X_lGQ6aLd4MapncgrA/zh-cn_image_0000002820405039.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=1AFAB4FC040D01E622F566E105210DE8355E8A3641D4DF1187918853C04BD13E)

## 自定义样式

* 设置边框弧度。

  使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。

  ```typescript
  Button('circle border', { type: ButtonType.Normal })
    .borderRadius(20)
    .height(40)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/ZVEoCvZxShC3edem29C_KA/zh-cn_image_0000002820525041.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=05841EB87B47EF6F6F4C0FB8217D0A26693196BA416217E50CBF3B3E1A191112)
* 设置文本样式。

  通过添加文本样式设置按钮文本的展示样式。

  ```typescript
  Button('font style', { type: ButtonType.Normal })
    .fontSize(20)
    .fontColor(Color.Pink)
    .fontWeight(800)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/nXnb7mMgRyCjcLJ7orPegg/zh-cn_image_0000002820405041.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=51941EE32184AC14CDDDEB15897CD9BA33233946F75F48B56AEEE740F056A0E3)
* 设置背景颜色。

  添加backgroundColor属性设置按钮的背景颜色。

  ```typescript
  Button('background color').backgroundColor(0xF55A42)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/yZD0poXTTVm5FvbL6iwOAg/zh-cn_image_0000002791725062.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8A5701C9E6F7872CC98851FAA83727EFD623F6964721A5A8B5E63EF4D630826)
* 创建功能型按钮。

  创建删除操作的按钮。

  ```typescript
  Button({ type: ButtonType.Circle, stateEffect: true }) {
    // 请将$r('app.media.ic_public_delete_filled')替换为实际资源文件
    Image($r('app.media.ic_public_delete_filled')).width(30).height(30)
  }.width(55).height(55).margin({ 'left': 20 }).backgroundColor(0xF55A42)
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/a3yNHeV0TyKXR_ssELUITg/zh-cn_image_0000002791565090.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=3D94DF2844DA6F78F4189CA67A3DB417AE4359EA464BAB9B703A1942889D6EBE)

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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/xiknM_GhS-GplYE08GtQqw/zh-cn_image_0000002820525043.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F8145A0B04796CB187B0C5B3B02D073252EEE9B75F8B521755F3F196DECC356)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/gKhGNVv2TI-bdxhAPDDN6A/zh-cn_image_0000002820405043.png?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B04A24D631082970E9EADE9A71D5B5ED86839042A113E3206E9399C98B85035)
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/b9i8xSujTzGc4xrNEuAlpA/zh-cn_image_0000002791725064.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014650Z&HW-CC-Expire=31536000000&HW-CC-Sign=862E01DEF1DE8A5680F9A6E9EFF31D08A2F412E9A1EA37C7B341C176DAC075BF)
