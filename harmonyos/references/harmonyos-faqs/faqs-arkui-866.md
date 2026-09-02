---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-866
title: 登录界面焦点在非密码输入框时可被截屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 登录界面焦点在非密码输入框时可被截屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f525b919ebb7142a7244f86d0e811a47cc14ef6b8f9cc1971b5ba87e16f68d91
---

## 问题现象

用户打开应用在账号登陆界面进行登录时，当点击密码输入框时进行屏幕截屏，系统提示“当前界面涉及隐私内容，不允许截屏”。但是当点击非密码输入框时，如账号输入框，进行截屏可以成功完成。

## 背景知识

* [setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)：设置窗口是否为隐私模式，使用callback异步回调。设置为隐私模式的窗口，窗口内容将无法被截屏或录屏。此接口可用于禁止截屏/录屏的场景。
* [onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)：导航栏显示状态切换时触发该回调。

## 问题定位

1. 检查是否设置了窗口隐私模式，可以在代码中检索关键字“setWindowPrivacyMode”，该API用于设置当前窗口为隐私模式。或者，可以通过在Hilog日志中检索关键字“isPrivacyMode”。如下日志信息：

   ```shell
   07-18 08:20:05.537   26598-26902   C04213/com.example...InputKeyFlow  com.hm.example   I     [] ConsumePointerEventInner(818): InputId:17513,wid:137,pointId:0,srcType:2,rect:[0,0,2240,2440],notify:1
   07-18 08:20:05.537   26598-26598   C03951/com.example...InputKeyFlow  com.hm.example   I     [(100000:100000:scope)] InputTracking id:17513, fingerId:0, type=0, inject=0, isPrivacyMode=0
   07-18 08:20:05.537   26598-26902   C02805/com.example...InputKeyFlow  com.hm.example   I     [][OnPointerEvent:216] ac: move: 17514
   ```

   日志中isPrivacyMode=0，说明当前为非隐私状态，可以被截屏。
2. 当焦点位于密码输入框时，在Hilog日志中检索关键字“setPrivacyMode”，如下日志信息：

   ```shell
   07-18 08:24:00.853   3146-55280    C01C10/com.oho...board/ImsaKit  com.ohos.sceneboard   I     line: 72, function: OnRemoteRequest,SystemCmdChannelStub, code: 0, callingPid: 3837, callingUid: 20020026.
   07-18 08:24:00.853   3837-3837     A000FF/i.hmos....rd_InputPanel  com.huawe...utMethod  I     setPrivacyMode: true
   07-18 08:24:00.853   3146-3146     A04200/com.oho...eboard/WINDOW  com.ohos.sceneboard   I     SCBKeyboardSession --> No need open transaction, keyboard is not rebuild
   ```

   日志中setPrivacyMode: true，说明当前为隐私状态，不可以被截屏。

## 分析结论

应用使用了华为安全键盘，当焦点处于密码输入框时，设置当前为隐私状态，不可以被截屏。当焦点不处于密码输入框时，窗体处于非隐私状态，可以被截屏。

## 修改建议

使用setWindowPrivacyMode接口设置窗口隐私模式，禁止截屏或录屏。此接口适用于禁止截屏/录屏的场景。

* 首先，在module.json5文件中声明需要使用ohos.permission.PRIVACY\_WINDOW权限。
* 通过导航栏显示状态切换触发onNavBarStateChange回调。进入页面时，isVisible为true，调用setWindowPrivacyMode设置窗口为隐私模式。离开页面时，isVisible为false，设置窗口为非隐私模式。参考示例代码如下：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';

  class windowUtils {
    static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
      window.getLastWindow(context).then((lastWindow) => {
        lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
          const errCode: number = err.code;
          if (errCode) {
            return;
          }
          console.info('Succeeded in setting the window to privacy mode.');
        });
      });
    }
  }

  @Entry
  @Component
  struct Index {
    message: string = 'hello world';
    @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();
    context = this.getUIContext();

    @Builder
    PagesMap(name: string) {
      if (name === 'Index') {
        Index();
      } else if (name === 'PageOne') {
        PageOne();
      }
    }

    build() {
      Navigation(this.pageStack) {
        Column() {
          Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageStack.pushPath({ name: 'PageOne' }); // 进行页面跳转
            })
        }
      }
      .navDestination(this.PagesMap)
      .onNavBarStateChange((isVisible: boolean) => {
        // 页面跳转回调时触发设置窗口为隐私模式
        windowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext, isVisible);
      })
    }
  }

  @Component
  struct PageOne {
    @Consume('NavPathStack') pageStack: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Text('PageOne')
        }
      }
      .title('pageOne')
      .onBackPressed(() => {
        return true;
      })
    }
  }
  ```

  更多信息请参考[如何实现防截屏功能](faqs-arkui-3.md)。
