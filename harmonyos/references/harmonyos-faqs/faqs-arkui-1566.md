---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1566
title: 如何解决平板中多次点击按钮弹出多个弹窗导致弹窗区域背景色加深的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何解决平板中多次点击按钮弹出多个弹窗导致弹窗区域背景色加深的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fac7ae8ca54b8a2f1eef817dc1387898be1f342999d0c454f94e5422de741c87
---

## 问题现象

平板应用在横屏状态下，可以多次点击按钮弹出多个弹窗，弹窗区域的背景色跟随点击次数增加而加深。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/IdqGNdPSTWuo7mUDzg_MnQ/zh-cn_image_0000002658969075.png "点击放大")

## 背景知识

* [createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9-1)：可以根据WindowStage实例创建子窗口。
* [loadContentByName](../harmonyos-references/arkts-apis-window-window.md#loadcontentbyname11)：根据指定路由页面名称为当前窗口加载命名路由页面。
* [openCustomDialog](../harmonyos-guides/arkts-uicontext-custom-dialog.md)：可以使用UIContext中获取到的PromptAction对象提供的openCustomDialog接口，在相对应用复杂的场景来实现自定义弹出框。可以通过配置isModal来实现模态和非模态弹窗。

## 问题定位

排查弹窗创建的相关的代码。创建子窗时传递的参数是随时间动态变化的，每次点击操作都会随时间的变化创建新的子窗。moveWindowToAsync方法中传入的参数是固定值，所创建的子窗口的位置因此是固定的。多次点击，会在同一位置创建不同名字的窗口。

```ts
// 创建子窗，每次创建时使用不同的子窗名字
this.windowStage?.createSubWindow(`subWindowDialog${Date.now()}`).then((windowClass: window.Window) => {
  // 子窗加载页面
  // 此处仅为示例，需要更换为实际页面，并通过LocalStorage传入状态属性
  windowClass.loadContent('pages/DialogTest', new LocalStorage(), () => {
    // 设置子窗口的宽高，高度是屏幕高度的一半再减去导航条区域的高度
    windowClass.resize(screen.width / 2, screen.height / 2 - this.getUIContext().vp2px(40));
    // 设置子窗口的背景色
    windowClass.setWindowBackgroundColor('#33000000');
    // 移动子窗口的位置
    windowClass.moveWindowToAsync(screen.width / 4, screen.height / 2);
    // 显示子窗口
    windowClass.showWindow();
  });
});
```

## 分析结论

在相同位置重复创建不同的有半透明背景色的子窗口，子窗口重叠，导致弹窗区域颜色加深。

## 修改建议

* 调整createSubWindow的参数为固定值，保证窗口只创建一次，多次点击不会创建多个窗口，部分代码实现如下。

  ```ts
  // 创建弹窗的方法，subWindow方案
  // 此处仅为示例，实际现象是仅平板横屏时弹窗未遮挡按钮
  createWindow() {
    // 获取屏幕数据
    const screen = display.getDefaultDisplaySync();
    // 创建子窗，传入固定的子窗名字
    this.windowStage?.createSubWindow(`subWindowDialog`).then((windowClass: window.Window) => {
      // 子窗加载页面
      // 此处仅为示例，需要更换为实际页面，并通过LocalStorage传入状态属性
      windowClass.loadContent('pages/DialogTest', new LocalStorage(), () => {
        // 设置子窗口的宽高，高度是屏幕高度的一半再减去导航条区域的高度
        windowClass.resize(screen.width / 2, screen.height / 2 - this.getUIContext().vp2px(40));
        // 设置子窗口的背景色
        windowClass.setWindowBackgroundColor('#ffffffff');
        // 移动子窗口的位置
        windowClass.moveWindowToAsync(screen.width / 4, screen.height / 2);
        // 显示子窗口
        windowClass.showWindow();
      });
    });
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/4BujIfnHSZykFSw7_M4nDw/zh-cn_image_0000002658849125.png "点击放大")
* 推荐使用openCustomDialog弹出框替代。并使用模态窗覆盖旧页面，遮挡住创建弹窗的组件，防止多次点击，部分代码实现如下。

  ```ts
  // CustomDialog弹窗的builder函数
  @Builder
  customDialogComponent() {
    Scroll() {
      Column() {
        Row({ space: 50 }) {
          Text('这是一个弹窗')
        }.height(200).padding(5)
      }
    }
  }

  // 打开弹窗
  openDialog() {
    this.getUIContext().getPromptAction().openCustomDialog({
      // 弹出框的内容
      builder: () => {
        // @builder装饰器所装饰的函数
        this.customDialogComponent();
      },
      // 使用模态窗
      isModal: true,
      // 蒙层颜色
      maskColor: '#33000000',
    });
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/671kwHT_SwiRkcmeeZ5Qjw/zh-cn_image_0000002628609862.png "点击放大")

完整代码如下：

```ts
import { display, window } from '@kit.ArkUI';

@Entry
@Component
struct DialogTest {
  // 需要提前在EntryAbility的onWindowStageCreate声明周期中使用AppStorage保存windowStage实例
  // 在这里取出存储的windowStage实例
  @StorageLink('windowStage') windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');

  // 创建弹窗的方法，subWindow方案
  // 此处仅为示例，实际现象是仅平板横屏时弹窗未遮挡按钮
  createWindow() {
    // 获取屏幕数据
    const screen = display.getDefaultDisplaySync();
    // 创建子窗，传入固定的子窗名字
    this.windowStage?.createSubWindow(`subWindowDialog`).then((windowClass: window.Window) => {
      // 子窗加载页面
      // 此处仅为示例，需要更换为实际页面，并通过LocalStorage传入状态属性
      windowClass.loadContent('pages/DialogTest', new LocalStorage(), () => {
        // 设置子窗口的宽高，高度是屏幕高度的一半再减去导航条区域的高度
        windowClass.resize(screen.width / 2, screen.height / 2 - this.getUIContext().vp2px(40));
        // 设置子窗口的背景色
        windowClass.setWindowBackgroundColor('#ffffffff');
        // 移动子窗口的位置
        windowClass.moveWindowToAsync(screen.width / 4, screen.height / 2);
        // 显示子窗口
        windowClass.showWindow();
      });
    });
  }

  // CustomDialog弹窗的builder函数
  @Builder
  customDialogComponent() {
    Scroll() {
      Column() {
        Row({ space: 50 }) {
          Text('这是一个弹窗')
        }.height(200).padding(5)
      }
    }
  }

  // 打开弹窗
  openDialog() {
    this.getUIContext().getPromptAction().openCustomDialog({
      // 弹出框的内容
      builder: () => {
        // @builder装饰器所装饰的函数
        this.customDialogComponent();
      },
      // 使用模态窗
      isModal: true,
      // 蒙层颜色
      maskColor: '#33000000',
    });
  }

  build() {
    Column({ space: 20 }) {
      Button('弹出弹框-CustomDialog')
        .margin({ top: 40 })
        .onClick(() => {
          this.openDialog();
        });
      Button('弹出弹框-SubWindow')
        .onClick(() => {
          this.createWindow();
        })
      Button('关闭弹窗-SubWindow')
        .onClick(() => {
          window.getLastWindow(this.getUIContext().getHostContext()).then((windowClass) => {
            windowClass.destroyWindow();
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
