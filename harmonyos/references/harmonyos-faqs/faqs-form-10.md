---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-10
title: 服务卡片拉起编辑页，出现闪屏
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 服务卡片拉起编辑页，出现闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ce6d98fe975b1671f0494da04b2187ba34dae6ca7b7a7ab7823e6209edbe8102
---

## 问题现象

在应用内添加服务卡片（应用此时进入后台），在桌面长按卡片，点击编辑按钮后，跳转编辑卡片的页面，跳转动画中间部分有桌面一闪而过的效果。观察视频慢放，是先拉起应用，添加卡片成功的页面，然后消失，再重新打开组件编辑页。

## 背景知识

* [loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)：根据当前工程中指定的页面路径为窗口加载具体页面内容，通过LocalStorage传递状态属性给加载的页面，使用callback异步回调。建议在UIAbility启动过程中使用该接口，重复调用将先销毁旧的页面内容（即UIContent）再加载新的页面内容，请谨慎使用。
* [目标UIAbility热启动](../harmonyos-guides/uiability-intra-device-interaction.md#目标uiability热启动)：在应用开发中，会遇到目标UIAbility实例之前已经启动过的场景，这时再次启动目标UIAbility时，不会重新走初始化逻辑，只会直接触发onNewWant生命周期方法。为了实现跳转到指定页面，需要在onNewWant中解析参数进行处理。
* [createSubWindow](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9)：可以创建该WindowStage实例下的子窗口。
* [setUIContent](../harmonyos-references/arkts-apis-window-window.md#setuicontent9)：根据当前工程中指定的某个页面路径，为窗口加载具体页面内容。

## 问题定位

1. 使用DevEco Studio查看hilog日志，查找关键字onNewWant，显示调用了loadContent方法。

   ```screen
   OnNewWant:Window [xxx,id:1625]
   LoadContent:[NAPI]
   [js_ui_ability.cpp:1398]end,name:onNewWant,time:4
   ```
2. 排查onNewWant中是否调用onWindowStageCreate方法，该方法会调用loadContent方法。

   ```screen
   onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
     // 不建议，调用onWindowStageCreate，使用loadContent方法，拉起应用的过程中可能有闪屏现象
     if (this.currentWindowStage !== null) {
       this.onWindowStageCreate(this.currentWindowStage);
     }
   }
   ```

## 分析结论

卡片拉起应用时触发了应用EntryAbility的onNewWant生命周期，且在onNewWant里调用了loadContent方法，销毁了旧的页面内容再加载新的页面，导致了卡片拉起编辑页时的闪屏问题。

## 修改建议

* 方案一：通过UIContext中获取Router对象，再进行指定页面的跳转。页面跳转默认会有跳转动画，可以返回其他页面。示例代码如下：

  ```screen
  // 通过Router路由对象，跳转对应页面，want参数是onNewWant回调函数的want参数
  toPageByRouter(want: Want) {
    if (want?.parameters?.params) {
      // want.parameters.params对应postCardAction方法和FormLink组件中的params参数
      let params = JSON.parse(want.parameters.params as string) as Record<string, Object>;
      // 如果传入targetPage参数，则拉起对应页面，如果没有就拉起Index页面
      // targetPage参数是自定义的，可以根据实际需要调整参数名称
      this.selectPage = (params.targetPage as string) || 'pages/Index';
      // 需要提前在onWindowStageCreate中给uiContext赋值
      if (this.uiContext) {
        this.uiContext.getRouter().pushUrl({
          url: this.selectPage
        }, router.RouterMode.Single); // 单实例模式，如果页面栈中存在该页面直接移动该url页面至栈顶
      }
    }
  }
  ```
* 方案二：调用setUIContent方法加载新页面。可以直接显示页面，如果需要可以在方法的else分支上恢复应用原本的路由页面。示例代码如下：

  ```screen
  // 通过Window的setUIContent方法加载页面，want参数是onNewWant回调函数的want参数
  toPageByWindow(want: Want) {
    // 获取want中的页面路径，使用子窗口加载对应页面
    if (want?.parameters?.params) {
      // want.parameters.params对应postCardAction方法和FormLink组件中的params参数
      let params = JSON.parse(want.parameters.params as string) as Record<string, Object>;
      // 如果传入targetPage参数，则拉起对应页面，如果没有就拉起Index页面
      // targetPage参数是自定义的，可以根据实际需要调整参数名称
      this.selectPage = (params.targetPage as string) || 'pages/Index';
      if (this.windowClass) {
        // 加载页面
        this.windowClass.setUIContent(this.selectPage, (err: BusinessError) => {
          // 异常处理
          console.info('[setUIContent]', `error: ${JSON.stringify(err)}`);
        });
      }
    }
  }
  ```

  EntryAbility.ets文件完整代码如下：

  ```screen
  import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { router, window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { JSON } from '@kit.ArkTS';

  export default class EntryAbility extends UIAbility {
    // 需要跳转的页面路由
    private selectPage: string = '';
    // UIContext，在onWindowStageCreate中获取
    uiContext: UIContext | undefined = undefined;
    // 窗口实例，在onWindowStageCreate中获取
    windowClass: window.Window | undefined = undefined;

    onWindowStageCreate(windowStage: window.WindowStage): void {
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          // 如果需要，请自行添加异常处理
          return;
        }
        windowStage.getMainWindow((err, data) => {
          // 获取UIContext并保存
          this.uiContext = data.getUIContext();
          // 获取窗口实例并保存
          this.windowClass = data;
        });
      });
    }

    onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      // launchParam是启动参数，主要包括Ability启动原因以及上次退出原因
      console.info('[onNewWant]', `launchParam: ${JSON.stringify(launchParam)}`);
      // 根据需要选择合适的方案，toPageByRouter、toPageByWindow两个方法，传入want参数
      // 通过Router跳转页面，默认会有页面跳转的动画
      // 更推荐setUIContent方案，直接拉起页面
      this.toPageByWindow(want);
    }

    // 通过Router路由对象，跳转对应页面，want参数是onNewWant回调函数的want参数
    toPageByRouter(want: Want) {
      if (want?.parameters?.params) {
        // want.parameters.params对应postCardAction方法和FormLink组件中的params参数
        let params = JSON.parse(want.parameters.params as string) as Record<string, Object>;
        // 如果传入targetPage参数，则拉起对应页面，如果没有就拉起Index页面
        // targetPage参数是自定义的，可以根据实际需要调整参数名称
        this.selectPage = (params.targetPage as string) || 'pages/Index';
        // 需要提前在onWindowStageCreate中给uiContext赋值
        if (this.uiContext) {
          this.uiContext.getRouter().pushUrl({
            url: this.selectPage
          }, router.RouterMode.Single); // 单实例模式，如果页面栈中存在该页面直接移动该url页面至栈顶
        }
      }
    }

    // 通过Window的setUIContent方法加载页面，want参数是onNewWant回调函数的want参数
    toPageByWindow(want: Want) {
      // 获取want中的页面路径，使用子窗口加载对应页面
      if (want?.parameters?.params) {
        // want.parameters.params对应postCardAction方法和FormLink组件中的params参数
        let params = JSON.parse(want.parameters.params as string) as Record<string, Object>;
        // 如果传入targetPage参数，则拉起对应页面，如果没有就拉起Index页面
        // targetPage参数是自定义的，可以根据实际需要调整参数名称
        this.selectPage = (params.targetPage as string) || 'pages/Index';
        if (this.windowClass) {
          // 加载页面
          this.windowClass.setUIContent(this.selectPage, (err: BusinessError) => {
            // 异常处理
            console.info('[setUIContent]', `error: ${JSON.stringify(err)}`);
          });
        }
      }
    }
  }
  ```
