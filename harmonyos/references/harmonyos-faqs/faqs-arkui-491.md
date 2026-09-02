---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-491
title: 如何实现三键导航的监听与避让
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现三键导航的监听与避让
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fa8092151b0af971a9d805db366bae30c8b8fcd49dad4744f1b56dabac9c62e0
---

**解决措施**

1、通过[settings.registerKeyObserver](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)监听三键导航的开启。

```screen
settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
  settings.domainName.USER_PROPERTY, () => {
    this.adaptLayout();
  });
```

2、通过[setting.getValue](../harmonyos-references/js-apis-settings.md#settingsgetvalue11)获取导航的信息。

```screen
settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
  settings.domainName.USER_PROPERTY).then((data: string) => {
  if (data) {
    let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
    this.adaptValue = navigationInfo.getAdaptValue();
  }
})
```

3、定义三键导航信息。

```ts
class NavigationButtonInfo {
  // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
  private showType: number = -1;
  // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
  private region: number[] = [0, 0, 0, 0];

  // Obtain the adaptation area and implement this function as required
  public getAdaptValue(): number {
    // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
    // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
    if (this.showType === 0 && this.region[2] < this.region[3]) {
      return this.region[2];
    } else {
      return 0;
    }
  }
}
```

4、根据region中的布局信息进行适配。

```screen
.padding({ right: this.getUIContext().px2vp(this.adaptValue) })
```

示例代码参考如下：

```ts
import settings from '@ohos.settings';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import window from '@ohos.window';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  @State adaptValue: number = 0;

  aboutToAppear(): void {
    this.watchNavigationButtonChange();
    window.getLastWindow(this.getUIContext().getHostContext(), ((err: BusinessError, data) => {
      data.setWindowLayoutFullScreen(true);
    }));
  }

  // Monitor the changes of three-key navigation information
  private watchNavigationButtonChange(): void {
    this.adaptLayout();

    settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
      settings.domainName.USER_PROPERTY, () => {
        this.adaptLayout();
      });
  }

  // Adapt the app layout based on the Three Key Navigation information
  private adaptLayout(): void {
    try {
      settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
        settings.domainName.USER_PROPERTY).then((data: string) => {
        if (data) {
          let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
          this.adaptValue = navigationInfo.getAdaptValue();
        }
      })
    } catch (e) {
      this.adaptValue = 0;
      hilog.warn(0, 'tag', 'adaptMargin err:' + e);
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Row() {
          Text(this.message)
            .id('HelloWorld')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .onClick(() => {
              this.message = 'Welcome';
            })
        }
        .backgroundColor(Color.Red)
        .height('100%')
        .width('100%')
      }
      .backgroundColor(Color.Yellow)
      .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
    }
    .height('100%')
    .width('100%')
  }
}

class NavigationButtonInfo {
  // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
  private showType: number = -1;
  // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
  private region: number[] = [0, 0, 0, 0];

  // Obtain the adaptation area and implement this function as required
  public getAdaptValue(): number {
    // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
    // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
    if (this.showType === 0 && this.region[2] < this.region[3]) {
      return this.region[2];
    } else {
      return 0;
    }
  }
}
```

导航条、状态栏、挖孔区沉浸式方案参考链接：[实现沉浸式效果](../best-practices/bpta-multi-device-window-immersive.md#section180431120426)。
