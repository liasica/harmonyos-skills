---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-screenmana-faq-0003
title: 如何监听屏幕旋转事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 常见问题 > 如何监听屏幕旋转事件
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:27+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9c12986613d71009c75be3fdcab273babaa9fc12af7d4ecbf75fe11de3cfd44e
---

**Q：在应用程序开发中，应当如何设置以检测并响应设备屏幕旋转的事件？**

**A**：可以通过以下方案实现：

* 方案一：监听屏幕旋转的能力可以通过[display.on('change')](../harmonyos-references/js-apis-display.md#displayonaddremovechange)监听屏幕状态改变实现，并通过[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)获取屏幕实例对象，其中rotation属性用于显示设备的屏幕顺时针旋转角度。实现示例如下：

  ```ts
  import window from '@ohos.window';
  import display from '@ohos.display';
  import { common } from '@kit.AbilityKit';

  const ORIENTATION: Array<string> = ['垂直', '水平', '反向垂直', '反向水平'];

  @Entry
  @Component
  struct Scene1 {
    @State rotation: number = 0;
    @State message: string = ORIENTATION[this.rotation];
    // 是否横屏状态
    @State @Watch('setWindowLayOut') isLandscape: boolean = false;

    aboutToAppear() {
      // 监听屏幕状态改变
      display.on('change', async () => {
        // 获取当前旋转角度
        this.rotation = display.getDefaultDisplaySync().rotation;
        this.message = ORIENTATION[this.rotation];
      });
    }

    setWindowLayOut() {
      // 调用该接口手动改变设备横竖屏状态（设置全屏模式，先强制横屏，再加上传感器模式）
      let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
      window.getLastWindow(context).then((windowClass) => {
        if (this.isLandscape) {
          // 设置屏幕横屏
          windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
        } else {
          // 设置屏幕竖屏
          windowClass.setPreferredOrientation(window.Orientation.AUTO_ROTATION_PORTRAIT);
        }
      });
    }

    build() {
      Row() {
        Column() {
          Text(`${this.rotation}`)
            .fontSize(25);
          Text(`${this.message}`)
            .fontSize(25);
          Button(this.isLandscape ? '竖屏' : '横屏')
            .width(140)
            .onClick(() => {
              // 设置横屏
              this.isLandscape = !this.isLandscape;
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* 方案二：可在EntryAbility的onWindowStageCreate中注册[windowSizeChange](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)事件，并通过[AppStorage](../harmonyos-references/ts-state-management.md#appstorage)存储，在页面中通过StorageProp监听数据的变化实现屏幕旋转的监听，可参考以下示例：
  + 在EntryAbility中注册监听窗口的windowSizeChange事件，并使用StorageProp存储屏幕的显示方向：

    ```ts
    import { UIAbility } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { display, window } from '@kit.ArkUI';

    export default class EntryAbility extends UIAbility {
      onCreate(): void {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
      }

      onDestroy(): void {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
      }

      onWindowStageCreate(windowStage: window.WindowStage): void {

        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

        let mainWindow: window.Window;
        try {
          mainWindow = windowStage.getMainWindowSync();
          let displayClass: display.Display = display.getDefaultDisplaySync();
          AppStorage.setOrCreate('orientation', displayClass.orientation);
          // 监听窗口的windowSizeChange事件，旋转屏时会触发该事件
          mainWindow.on('windowSizeChange', () => {
            let displayClass: display.Display | null = null;
            try {
              displayClass = display.getDefaultDisplaySync();
              // 获取屏幕的显示方向
              AppStorage.set('orientation', displayClass.orientation);
            } catch {
              return;
            }
          });
        } catch {
          hilog.info(0x0000, 'testTag', '%{public}s', 'error');
          return;
        }
        // 此处需要替换为需要展示的页面
        windowStage.loadContent('pages/Scene2', (err) => {
          if (err.code) {
            return;
          }
          hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
        });
      }

      onWindowStageDestroy(): void {
        // Main window is destroyed,release UI related resources
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
      }

      onForeground(): void {
        // Ability has brought to foreground
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
      }

      onBackground(): void {
        // Ability has back to background
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
      }
    };
    ```
  + 页面中通过StorageProp监听数据的变化实现屏幕旋转的监听：

    ```ts
    import { display } from '@kit.ArkUI';

    @Entry
    @Component
    struct Scene2 {
      // 获取通过监听窗口的windowSizeChange事件得到的屏幕显示方向
      @StorageProp('orientation') myOrientation: display.Orientation = 0;

      build() {
        Stack() {
          // 当屏幕显示方向变化时，切换组件的视图效果
          if (this.myOrientation === 0 ||
            this.myOrientation === 2) {
            Image($r('app.media.startIcon'))
              .size({ width: 100, height: 100 })
              .id('image1');
          } else {
            Image($r('app.media.background'))
              .position({ x: 0, y: 0 })
              .size({ width: 200, height: 200 })
              .id('image2');
          }
        }
        .backgroundColor(Color.White)
        .size({ width: '100%', height: '100%' });
      }
    }
    ```
  + 需要在项目的module.json5文件中的abilities列表里添加"orientation"，指定为"auto\_rotation"：

    ```json
    "orientation": "auto_rotation",
    ```
* 方案三：通过设备中的重力传感器，可以检测该设备在三个坐标轴（即X轴、Y轴及Z轴）上的线性加速度。基于这些数据，能够计算出屏幕当前的旋转状态。有关具体实现方式，可参考以下样例：

  ```ts
  import sensor from '@ohos.sensor';
  import base from '@ohos.base';

  @Entry
  @Component
  struct Scene3 {
    @State rotation: string = 'INVALID';

    onDegree(callback: base.Callback<string>): void {
      sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
        let degree: number = -1;
        degree = this.CalDegree(data.x, data.y, data.z);
        if (degree >= 0 && (degree <= 30 || degree >= 330)) {
          this.rotation = 'ROTATION_0';
        } else if (degree >= 60 && degree <= 120) {
          this.rotation = 'ROTATION_90';
        } else if (degree >= 150 && degree <= 210) {
          this.rotation = 'ROTATION_180';
        } else if (degree >= 240 && degree <= 300) {
          this.rotation = 'ROTATION_270';
        }
        callback(this.rotation);
      });
    }

    CalDegree(x: number, y: number, z: number): number {
      let degree: number = -1;
      // 3为有效_增量_角度_阈值_系数
      if ((x * x + y * y) * 3 < z * z) {
        return degree;
      }
      degree = 90 - (Number)(Math.round(Math.atan2(y, -x) / Math.PI * 180));
      return degree >= 0 ? degree % 360 : degree % 360 + 360;
    }

    aboutToAppear() {
      let callback = async (rotation: string) => {
        console.info(`rotation = ${rotation}`);
      };
      try {
        this.onDegree(callback);
      } catch (exception) {
      }
    }

    build() {
      Row() {
        Column() {
          Text(`${this.rotation}`)
            .fontSize(25);
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* 方案四：使用媒体查询接口监听屏幕旋转，设置媒体查询的查询条件为屏幕的方向，可选值为orientation:portrait（设备竖屏）和orientation: landscape（设备横屏）。有关具体实现方式，请参考：[媒体查询 (@ohos.mediaquery)场景示例](../harmonyos-guides/arkts-layout-development-media-query.md#场景示例)。

**Q：通过window.setPreferredOrientation(window.Orientation.LANDSCAPE)设置方向后，调用display.getDefaultDisplaySync().orientation获取到的是LANDSCAPE\_INVERTED，与预期相反。**

**A**：window侧的orientation代表的是旋转策略，LANDSCAPE代表横屏，此横屏表示横屏时电源键在上的方向（竖屏时电源键在左侧和在右侧LANDSCAPE旋转的方向是相反的）。对于直板机来说，设置window.setPreferredOrientation(window.Orientation.LANDSCAPE)，当电源键在左侧时，display.on('change')监听的也为LANDSCAPE，当电源键在右侧时，display.on('change')监听的结果为LANDSCAPE\_INVERTED。

**Q：屏幕旋转锁定和不锁定情况下，display.orientation的值有什么区别？**

**A**：屏幕锁定后，display.orientation的值不会随设备物理旋转而变化，保持锁定时的方向不变。屏幕不锁定时，display.orientation会根据设备当前的物理朝向实时上报。无论屏幕是否锁定，重力传感器监听到的数据不会有所不同。

**Q：手机录屏后的文件存放路径是哪里？**

**A**：录屏文件保存在 /storage/media/100/local/files/Photo/1（或其他数字）和 /storage/cloud/100/files/Photo/1 中。

**Q：如何获取设备横竖屏的状态变化通知？**

**A**：可以通过以下方式实现订阅系统环境变量的变化：

* 使用ApplicationContext订阅回调。
* 在AbilityStage组件容器中订阅回调。
* 在UIAbility组件中订阅回调。
* 在ExtensionAbility组件中订阅回调。

在onConfigurationUpdate回调方法中订阅或监听系统环境变量的变化，包括语言、颜色模式和屏幕方向。

详细请参见[获取/设置环境变量](../harmonyos-guides/subscribe-system-environment-variable-changes.md)。
