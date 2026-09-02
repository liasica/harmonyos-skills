---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-941
title: 水印遮罩导致TextInput无法获取粘贴权限
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 水印遮罩导致TextInput无法获取粘贴权限
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b6f8ec483a79c502db3f3870d01f27d0da9e7de512190c411d96a31047e6c5e4
---

## 问题现象

用户长按复制文本后，先在TextInput组件上添加水印遮罩，随后通过长按输入框唤起菜单，但点击“粘贴”时不生效。

问题效果预览:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/2rznFASaQ16OBBDxjmyRMw/zh-cn_image_0000002658800465.png "点击放大")

## 效果预览

| 申请剪贴板权限 | 配置setMenuOptions |
| --- | --- |
|  |  |

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件，用于接收并展示输入内容。
* [Window](../harmonyos-references/arkts-apis-window-window.md)：窗口提供管理窗口的一些基础能力，包括对当前窗口的创建、销毁、各属性设置，以及对各窗口间的管理调度。用于生成子窗口形成水印遮罩。
* [约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)：安全控件因其自动授权的特性，为了保障用户的隐私不被恶意应用获取，针对安全控件做了很多的限制。其中安全控件被其他组件或窗口遮挡会导致授权失败。
* [ohos.permission.READ\_PASTEBOARD](../harmonyos-guides/restricted-permissions.md#ohospermissionread_pasteboard)：允许应用读取剪贴板。申请权限后，应用会有剪贴板权限，不需要获取临时权限。

## 问题定位

* 剪贴板是否存在粘贴内容。
* 是否拦截点击事件。
* 是否获取剪贴板权限。

## 分析结论

长按输入框进行粘贴动作需要校验剪贴板权限。因为输入框上存在遮罩的水印子窗口，导致TextInput组件无法获取到剪贴板内容的权限，因此粘贴内容为空。

## 修改建议

* **方案一**：若要实现有水印时可粘贴，建议申请剪贴板权限。在使用长按粘贴功能前获取权限。

  **说明** 

  ohos.permission.READ\_PASTEBOARD是受限开放权限。若使用自动签名，需要在权限配置后重新生成自动签名。若使用手动签名，需要申请对应权限。

  + 权限配置：

    ```json
    "requestPermissions": [
      {
        "name": "ohos.permission.READ_PASTEBOARD",
        "reason": "$string:app_name",
        "usedScene": {
          "abilities": ["EntryAbility"],
          "when": "inuse"
        }
      }
    ],
    ```
  + 主页面（Index）：

    ```ts
    // 剪贴板权限方式
    import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    import { BusinessError } from '@kit.BasicServicesKit';

    const permissions: Array<Permissions> = ['ohos.permission.READ_PASTEBOARD'];

    // 申请权限
    function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
      atManager.requestPermissionsFromUser(context, permissions).then((data) => {
        let grantStatus: Array<number> = data.authResults;
        let length: number = grantStatus.length;
        for (let i = 0; i < length; i++) {
          if (grantStatus[i] === 0) {
            // 用户授权，可以继续访问目标操作
          } else {
            // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
            return;
          }
        }
        // 授权成功
      }).catch((err: BusinessError) => {
        console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
      });
    }

    @Entry
    @Component
    struct Scene1 {
      private context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取Context

      build() {
        Row() {
          Column() {
            TextInput({ placeholder: '输入文本后可复制，也可以粘贴到此处' })
              .width('90%')
              .margin(5)

            Button('弹出水印子窗口')
              .width('90%')
              .margin(5)
              .onClick(() => {
                try {
                  this.context.windowStage.createSubWindow('subWindowTest')
                    .then((win: window.Window) => {
                      win.setUIContent('pages/Watermark');
                      win.setWindowFocusable(false);
                      win.setWindowTouchable(false);
                      win.showWindow().then(() => {
                        win.setWindowBackgroundColor('#00000000');
                      });
                    })
                    .catch((err: BusinessError) => {
                      console.info(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
                    });
                } catch (exception) {
                  console.info(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
                }
              })

            Button('获取剪贴板权限')
              .onClick(() => {
                reqPermissionsFromUser(permissions, this.context);
              })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    ```
  + 水印页面（Watermark）：

    ```ts
    // 水印页面
    @Entry
    @Component
    struct Watermark {
      opacityValue: number = 0.1;
      watermark: string = 'watermark';
      canvas: CanvasRenderingContext2D = new CanvasRenderingContext2D(new RenderingContextSettings(true));

      build() {
        Column() {
          Column() {
            Canvas(this.canvas)
              .width('100%')
              .height('100%')
              .hitTestBehavior(HitTestMode.Transparent)
              .onReady(() => {
                this.canvas.fillStyle = '#ff000000';
                this.canvas.font = '16vp';
                this.canvas.textAlign = 'center';
                this.canvas.textBaseline = 'middle';
                // 在这里绘制文字水印，也可以是图片水印
                for (let i = 0; i < this.canvas.width / 120; i++) {
                  this.canvas.translate(120, 0);
                  let j = 0;
                  for (; j < this.canvas.height / 120; j++) {
                    this.canvas.rotate(-Math.PI / 180 * 30);
                    // 此处水印数据是写死的，具体请替换为自己的水印
                    this.canvas.fillText('test', -60, -60);
                    this.canvas.rotate(Math.PI / 180 * 30);
                    this.canvas.translate(0, 120);
                  }
                  this.canvas.translate(0, -120 * j);
                }
              })
          }
          .backgroundColor(Color.White)
          .borderRadius(20)
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center)
        }
        .opacity(this.opacityValue)
        .justifyContent(FlexAlign.Center)
        .height('100%')
        .width('100%')
        .backgroundColor('#60000000')
        .transition(TransitionEffect.OPACITY.animation({ duration: 300 }))
      }
    }
    ```
* **方案二**：可以通过配置[setMenuOptions](../harmonyos-references/arkts-apis-uicontext-textmenucontroller.md#setmenuoptions16)来实现显示子窗水印后TextInput实现粘贴，当TextInput、TextArea可支持拉起[enableAutoFill](../harmonyos-references/ts-basic-components-textinput.md#enableautofill11)时，不支持将其对应的文本选择菜单显示在独立窗口中。因为TextInput配置了placeholder触发了自动填充，所以需要将自动填充关闭.enableAutoFill(false)。

  ```ts
  // 控制Text菜单显示方式
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Scene2 {
    private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

    aboutToAppear(): void {
      // 优先显示在独立窗口中
      this.getUIContext()
        .getTextMenuController()
        .setMenuOptions(
          {
            showMode: TextMenuShowMode.PREFER_WINDOW
          }
        );
    }

    build() {
      Row() {
        Column() {
          TextInput({ placeholder: '输入文本后可复制，也可以粘贴到此处' })
            .width('90%')
            .margin(5)
            .enableAutoFill(false)

          Button('弹出水印子窗口')
            .width('90%')
            .margin(5)
            .onClick(() => {
              try {
                this.context.windowStage.createSubWindow('subWindowTest')
                  .then((win: window.Window) => {
                    win.setUIContent('pages/Watermark');
                    win.setWindowFocusable(false);
                    win.setWindowTouchable(false);
                    win.showWindow().then(() => {
                      win.setWindowBackgroundColor('#00000000');
                    });
                  })
                  .catch((err: BusinessError) => {
                    console.info(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
                  });
              } catch (exception) {
                console.info(`Failed to create the subwindow. Cause code: ${exception.code}, message: ${exception.message}`);
              }
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

## 常见FAQ

Q：为何长按输入框粘贴后，再生成水印，此时长按输入框可以粘贴内容？

A：先长按输入框粘贴，因为没有遮挡，此时可以正常获取剪贴板临时权限，后续再进行粘贴的时候已经获得了剪贴板的权限，所以可以进行粘贴。

Q：如何改变水印子窗口位置大小？

A：可以通过[resize](../harmonyos-references/arkts-apis-window-window.md#resize9-1)来设置子窗口宽高，[moveWindowTo](../harmonyos-references/arkts-apis-window-window.md#movewindowto9-1)设置子窗口起始位置，以改变子窗口大小和位置。
