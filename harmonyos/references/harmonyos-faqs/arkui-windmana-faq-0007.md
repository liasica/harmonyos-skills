---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-windmana-faq-0007
title: 如何监听窗口大小的变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 常见问题 > 如何监听窗口大小的变化
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:28+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:53a37deaaa2693ddead582713aec92cdc75a44947078930d99c4436d1fb520c2
---

**Q：如何动态监听应用窗口大小的变化？**

**A**：

| 方案 | 优缺点 | 适用场景 |
| --- | --- | --- |
| 方案一：display.on('change')。 | 使用便捷，当设备为手机或者Pad且未开启分屏、悬浮窗、自由多窗模式时，应用窗口的大小数值上等于屏幕的大小，可用此方法获取窗口大小。当设备为PC或者Pad的自由多窗模式下，此方法不适用。 | 折叠屏折叠状态改变、屏幕旋转时获取实时窗口大小。 |
| 方案二：on('windowRectChange')。 | 该监听在以下操作下均会触发：切换分屏、悬浮窗、折叠状态变化、屏幕旋转、PC上点击标题栏最大化最小化按钮、PC上鼠标拖动改变应用窗口大小、Pad切换自由多窗模式，同时此方法可动态返回窗口的位置信息。 | 若需同时监听窗口位置和尺寸变化（如监听子窗口移动），则使用 windowRectChange。 |
| 方案三：on('windowSizeChange')。 | 该方法仅在主线程调用，该方法在以下操作下均会触发切换分屏、悬浮窗、折叠状态变化、屏幕旋转、PC上点击标题栏最大化最小化按钮、PC上鼠标拖动改变应用窗口大小、Pad切换自由多窗模式，但此方法无法获取窗口的位置信息。 | 若仅需监听窗口尺寸变化，如窗口尺寸变化时更新布局（调整 Grid 列数），优先使用 windowSizeChange。 |
| 方案四：display.on('foldDisplayModeChange')。 | 该接口在2in1设备、非折叠设备中不生效也不报错，在其他设备中可正常调用，此方法可以监听当前显示内容是显示在折叠设备的内屏还是外屏。 | 折叠屏折叠状态变化时，获取窗口当前的宽度和高度，以达到折叠屏适配的效果。 |
| 方案五：display.on('foldStatusChange') 。 | 该接口在2in1设备、非折叠设备中不生效也不报错，在其他设备中可正常调用，但无法监听当前显示内容是显示在折叠设备的内屏还是外屏。 | 折叠屏折叠状态变化时，获取窗口当前的宽度和高度，以达到折叠屏适配的效果。 |

方案一：通过display.on('change')方法监听显示设备的变化，再通过display.getDefaultDisplaySync方法返回的Display对象获取屏幕的宽度和高度。

```ts
import { display } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State newDisplay: display.Display | undefined = undefined;

  aboutToAppear(): void {
    this.observerWindowByChange();
  }

  aboutToDisappear(): void {
    // 移除监听。
    try {
      display.off('change');
    } catch (error) {
      console.info('offchange-error');
    }
  }

  observerWindowByChange() {
    this.newDisplay = display.getDefaultDisplaySync();
    // 听显示设备的变化（如屏幕方向、分辨率、可用区域改变等）
    display.on('change', () => {
      // display.getDefaultDisplaySync返回应用所在屏幕的Display对象，该对象的width和height属性可获取当前屏幕的宽度和高度。
      this.newDisplay = display.getDefaultDisplaySync();
    });
  }

  build() {
    Column() {
      Column() {
        Text('display.on(\'change\')');
        Row() {
          Text('窗口宽度：');
          Text(this.newDisplay?.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：');
          Text(this.newDisplay?.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

| 竖屏 | 横屏 |
| --- | --- |
|  |  |

方案二：通过on('windowRectChange')方法开启窗口位置及窗口大小变化的监听。

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State windowRect: window.Rect = {
    left: 0,
    top: 0,
    width: 0,
    height: 0
  };
  private windowClass: window.Window | undefined = undefined;

  aboutToAppear(): void {
    try {
      window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          return;
        }
        this.windowClass = data;
        this.observerWindowByWindowRectChange();
      });
    } catch (exception) {
      console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  aboutToDisappear(): void {
    // 移除监听。
    try {
      this.windowClass?.off('windowRectChange');
    } catch (error) {
      console.info('offwindowRectChange-error');
    }
  }

  observerWindowByWindowRectChange() {
    let newDisplay: display.Display = display.getDefaultDisplaySync();
    this.windowRect.width = newDisplay.width;
    this.windowRect.height = newDisplay.height;
    // 在应用分屏和悬浮窗模式下可用此方法监听窗口大小的变化，对应用进行适配
    this.windowClass?.on('windowRectChange', (data: window.RectChangeOptions) => {
      this.windowRect = data.rect;
    });
  }

  build() {
    Column() {
      Column() {
        Text('windowClass.on(\'windowRectChange\')');
        Row() {
          Text('窗口宽度：');
          Text(this.windowRect?.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：');
          Text(this.windowRect?.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/PdLwrxUVTMapreCxiiVoUw/zh-cn_image_0000002772679744.png "点击放大")

方案三：通过on('windowSizeChange')方法开启窗口尺寸变化的监听。

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State windowSize: window.Size = {
    width: 0,
    height: 0
  };
  private windowClass: window.Window | undefined = undefined;

  aboutToAppear(): void {
    let newDisplay: display.Display = display.getDefaultDisplaySync();
    this.windowSize.width = newDisplay.width;
    this.windowSize.height = newDisplay.height;
    try {
      window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
        const errCode: number = err.code;
        if (errCode) {
          return;
        }
        this.windowClass = data;
        this.observerWindowByWindowSizeChange();
      });
    } catch (exception) {
      console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  aboutToDisappear(): void {
    // 移除监听。
    try {
      this.windowClass?.off('windowSizeChange');
    } catch (error) {
      console.info('offwindowSizeChange-error');
    }
  }

  observerWindowByWindowSizeChange() {
    const callback = (size: window.Size) => {
      this.windowSize = size;
    };
    try {
      // 通过on接口开启监听
      // 在应用分屏和悬浮窗模式下可用此方法监听窗口大小的变化，对应用进行适配
      this.windowClass?.on('windowSizeChange', callback);
      // 关闭指定callback的监听
    } catch (exception) {
      console.error(`Failed to disable the listener for window size changes. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  build() {
    Column() {
      Column() {
        Text('windowClass.on(\'windowSizeChange\')');
        Row() {
          Text('窗口宽度：');
          Text(this.windowSize?.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：');
          Text(this.windowSize?.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/jXphkU_1R_ii0Qt0i3y21g/zh-cn_image_0000002802119573.png "点击放大")

方案四：通过display.on('foldDisplayModeChange')监听折叠屏折叠状态的变化，再通过getLastWindow方法返回的窗口实例中的getGlobalRect方法获取窗口的宽度和高度。该方法适用于折叠屏折叠状态变化时，获取窗口当前的宽度和高度，以达到折叠屏适配的效果。

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State windowRect: window.Size = {
    width: 0,
    height: 0
  };

  aboutToAppear(): void {
    let newDisplay: display.Display = display.getDefaultDisplaySync();
    this.windowRect.width = newDisplay.width;
    this.windowRect.height = newDisplay.height;
    this.observerWindowByFoldDisplayModeChange();
  }

  aboutToDisappear(): void {
    // 移除监听。
    try {
      display.off('foldDisplayModeChange');
    } catch (error) {
      console.info('offfoldDisplayModeChange-error');
    }
  }

  observerWindowByFoldDisplayModeChange() {
    display.on('foldDisplayModeChange', () => {
      // getLastWindow为异步方法因此需要添加延时来获取最新的窗口实例
      setTimeout(() => {
        try {
          window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
            const errCode: number = err.code;
            if (errCode) {
              return;
            }
            this.windowRect.width = data.getGlobalRect().width;
            this.windowRect.height = data.getGlobalRect().height;
          });
        } catch (exception) {
          console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
        }
      }, 500);
    });
  }

  build() {
    Column() {
      Column() {
        Text('display.on(\'foldDisplayModeChange\')');
        Row() {
          Text('窗口宽度：');
          Text(this.windowRect?.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：');
          Text(this.windowRect?.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/K0swCK8sRViD5mOsoice8A/zh-cn_image_0000002802039477.png "点击放大")

方案五：通过display.on('foldStatusChange')监听折叠屏折叠状态的变化，再通过getLastWindow方法返回的窗口实例中的getGlobalRect方法获取窗口的宽度和高度。

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State windowRect1: window.Size = {
    width: 0,
    height: 0
  };

  aboutToAppear(): void {
    let newDisplay: display.Display = display.getDefaultDisplaySync();
    this.windowRect1.width = newDisplay.width;
    this.windowRect1.height = newDisplay.height;
    this.observerWindowByFoldStatusChange();
  }

  aboutToDisappear(): void {
    // 移除监听。
    try {
      display.off('foldStatusChange');
    } catch (error) {
      console.info('offfoldStatusChange-error');
    }
  }

  observerWindowByFoldStatusChange() {
    display.on('foldStatusChange', () => {
      // getLastWindow为异步方法因此需要添加延时来获取最新的窗口实例
      setTimeout(() => {
        try {
          window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data) => {
            const errCode: number = err.code;
            if (errCode) {
              return;
            }
            this.windowRect1.width = data.getGlobalRect().width;
            this.windowRect1.height = data.getGlobalRect().height;
          });
        } catch (exception) {
          console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
        }
      }, 500);

    });
  }

  build() {
    Column() {
      Column() {
        Text('display.on(\'foldStatusChange\')');
        Row() {
          Text('窗口宽度：');
          Text(this.windowRect1?.width.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };

        Row() {
          Text('窗口高度：');
          Text(this.windowRect1?.height.toString())
            .fontSize(15)
            .fontWeight(FontWeight.Bold);
        };
      };
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/b1CtR2GrSx-NMT4L7Y6ONg/zh-cn_image_0000002772839720.png "点击放大")
