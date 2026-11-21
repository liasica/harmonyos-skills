---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-controlbar-adapt
title: 顶部窗口控制条避让适配智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口模式 > 智慧多窗应用开发指导 > 顶部窗口控制条避让适配智慧多窗
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:16+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:3b10dcc08970ba245e262cf2d7c3d8286ebe72586b64a8c2e5b89fa1bdbc99aa
---

顶部窗口控制条是应用窗口处于智慧多窗模式下，应用顶部的操作横条 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/MokgWbWvSma0rCGOZqqWpg/zh-cn_image_0000002821757025.png?HW-CC-KV=V1&HW-CC-Date=20261121T010952Z&HW-CC-Expire=31536000000&HW-CC-Sign=871FEF55644B76D1BF06CF1169CE9A08F80EFC7751558A64FF92E074A84949AC) 。

顶部窗口控制条示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/SGCE9DmLR9az2NGwTe0aSw/zh-cn_image_0000002793037088.png?HW-CC-KV=V1&HW-CC-Date=20261121T010952Z&HW-CC-Expire=31536000000&HW-CC-Sign=425F57482D2FF05C741A458F3F93745396E5BCDF62AD4C3848A3DF117DF7FE44)

顶部横条的避让可通过以下两种方式适配：

* 使用窗口的避让能力：通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置窗口布局是否为沉浸式布局。

  沉浸式布局是指应用布局不避让状态栏、导航栏以及智慧多窗顶部横条，这可能发生组件与顶部横条的重叠，导致文字遮挡、点击事件冲突等情况。非沉浸式布局是指布局避让状态栏、导航栏以及智慧多窗顶部横条，组件不会与其重叠。因此可设置isLayoutFullScreen值为false使窗口的布局为非沉浸式布局。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/a4qxvzpwRZmoULP7t1eTdQ/zh-cn_image_0000002792877118.png?HW-CC-KV=V1&HW-CC-Date=20261121T010952Z&HW-CC-Expire=31536000000&HW-CC-Sign=9107EEBAB36CECBD6AF4784DEE01643453BCB19F2974F6EFBF45257523FCEE38)

  示例：

  ```ts
  // Index.ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { window } from '@kit.ArkUI';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    @State message: string = '非沉浸式布局';
    private windowClass: window.Window | undefined = undefined;

    aboutToAppear(): void {
      try {
        window.getLastWindow(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
          (err: BusinessError, data) => {
            const errCode: number = err.code;
            if (errCode) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
              return;
            }
            this.windowClass = data;
            console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
          });
      } catch (exception) {
        console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
      }
    }

    private setWindowLayoutFullScreen(isLayoutFullScreen: boolean) {
      if (!this.windowClass) {
        return;
      }
      this.windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
        console.info('Succeeded in setting the window layout to full-screen mode.');
      }).catch((err: BusinessError) => {
        const errCode: number = err.code;
        if (errCode) {
          console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
          return;
        }
      });
    }

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        Column() {
          Text(this.message)
            .fontSize(25)
            .fontWeight(FontWeight.Bold)
            .margin({
              top: '2%',
              bottom: '40%'
            })

          Button() {
            Text('设置窗口为沉浸式布局')
              .fontSize(18)
              .fontWeight(FontWeight.Normal)
          }
          .type(ButtonType.Normal)
          .borderRadius(15)
          .margin({ top: 20 })
          .stateStyles({
            normal: {
              .backgroundColor('#ff6b89d4')
            },
            pressed: {
              .backgroundColor('#ffc81f2a')
            }
          })
          .width('60%')
          .height('6%')
          .onClick(() => {
            this.setWindowLayoutFullScreen(true);
            this.message = '沉浸式布局';
          })

          Button() {
            Text('设置窗口为非沉浸式布局')
              .fontSize(18)
              .fontWeight(FontWeight.Normal)
          }
          .type(ButtonType.Normal)
          .borderRadius(15)
          .margin({ top: 20 })
          .stateStyles({
            normal: {
              .backgroundColor('#ff6b89d4')
            },
            pressed: {
              .backgroundColor('#ffc81f2a')
            }
          })
          .width('60%')
          .height('6%')
          .onClick(() => {
            this.setWindowLayoutFullScreen(false);
            this.message = '非沉浸式布局';
          })
        }
        .width('100%')
      }
      .backgroundColor('#fceaeaea')
      .height('100%')
    }
  }
  ```

  图1 设置窗口是否为沉浸式布局

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/QVYyMFIiTpGPzzgpg2K4Mg/zh-cn_image_0000002821837025.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010952Z&HW-CC-Expire=31536000000&HW-CC-Sign=A9820803D9BBF91BD005204BAF9913C7DE5D2E63DE051F41AC9A00315BCA0086)
* 应用主动避让：应用不使用窗口避让能力（即设置窗口为沉浸式布局）。首次通过[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口可获取屏幕顶部需要规避的矩阵区域topRect，获取到该值后应用可对应做布局避让，并且注册[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听系统避让区域变化以进行布局的动态调整。

  ```ts
  // Index.ets
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  @Entry
  @Component
  struct Index {
    @State topSafeHeight: number = 0;

    aboutToAppear(): void {
      try {
        let windowClass: window.Window | undefined = undefined;
        window.getLastWindow(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
          (err: BusinessError, data) => {
            const errCode: number = err.code;
            if (errCode) {
              console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
              return;
            }
            windowClass = data;
            windowClass.setWindowLayoutFullScreen(true);
            this.topSafeHeight = this.getUIContext()?.px2vp(
              windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
            windowClass.on('avoidAreaChange', (data) => {
              if (data.type == window.AvoidAreaType.TYPE_SYSTEM) {
                this.topSafeHeight = this.getUIContext()?.px2vp(data.area.topRect.height)
              }
            })
            console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
          });
      } catch (exception) {
        console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
      }
    }

    build() {
      Stack({ alignContent: Alignment.TopStart }) {
        // 顶部避让区域
        Row() {
        }
        .height(this.topSafeHeight)
        .width("100%")
        .backgroundColor('#ccbbf375')
        // 根据topSafeHeight动态调整应用布局
        // ...
      }
      .height('100%')
    }
  }
  ```

  图2 应用主动做布局避让

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/OEI5smJvTQetkbye3OD-bg/zh-cn_image_0000002821757027.gif?HW-CC-KV=V1&HW-CC-Date=20261121T010952Z&HW-CC-Expire=31536000000&HW-CC-Sign=F4D211D5EEA28A3809513D9526BDCE96DB2539C17C3CFCF9540BE51ACCE0EEF0)
