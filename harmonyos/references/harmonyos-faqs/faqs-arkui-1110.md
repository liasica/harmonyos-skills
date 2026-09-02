---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1110
title: NavDestination生命周期使用常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > NavDestination生命周期使用常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f42b37edd346a71fcedff88129ba090f9ca52ce2a226a6b3232ce31c1966c24
---

## 问题现象

设置NavDestination生命周期时，可能会遇到以下问题：

场景一：NavDestination生命周期不执行。

场景二：为什么NavDestinationMode.DIALOG模式不触发onHidden和onShown回调。

场景三：申请权限的弹窗为什么能触发NavDestination的onHidden和onShown？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：子页面的根容器，用于显示Navigation的内容区。
* [onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)：当该NavDestination页面显示时触发此回调。
* [onHidden](../harmonyos-references/ts-basic-components-navdestination.md#onhidden10)：当该NavDestination页面隐藏时触发此回调。
* [NavDestinationMode](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)：其中DIALOG模式常用于实现弹窗效果。
* [onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)：NavDestination处于激活态（处于栈顶可操作，且上层无特殊组件遮挡）时，触发该回调。
* [onInactive](../harmonyos-references/ts-basic-components-navdestination.md#oninactive17)：NavDestination处于非激活态（处于非栈顶不可操作，或处于栈顶时上层有特殊组件遮挡）时，触发该回调。
* [uiObserver.on('navDestinationUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)：监听NavDestination组件的状态变化。
* [声明权限](../harmonyos-guides/declare-permissions.md)：应用在申请权限时，需在项目的配置文件中逐个声明所需权限，否则无法获取授权，并可能导致应用上架申请被驳回。

## 解决方案

* **场景一**：NavDestination生命周期不执行。
  + **情景一**：NavDestination的onPageHide和onPageShow不执行。

    NavDestination是Navigation容器的子组件，不是独立页面，整个Navigation对应1个@Entry页面，内部跳转仅切换NavDestination组件，页面栈未发生改变，故不触发onPageHide和onPageShow。若需要监听其显示和隐藏，可以使用其自有事件[onShown](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)和[onHidden](../harmonyos-references/ts-basic-components-navdestination.md#onhidden10)。
  + **情景二**：Navigation内部嵌套NavDestination，生命周期不执行。

    [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件必须配合Navigation使用，作为Navigation目的页面的根节点，单独使用只能作为普通容器组件，不具备路由相关属性能力。Navigation和NavDestination的配合使用可参考[Navigation页面路由的示例](../harmonyos-guides/arkts-navigation-jump.md#示例)。
* **场景二**：NavDestinationMode.DIALOG模式不触发onHidden和onShown。

  DIALOG模式进出路由栈不影响下层NavDestination的可见性（onShown、onHidden等生命周期）。

  + **方案一**：使用onActive和onInactive感知下层NavDestination状态。

    从API17开始，NavDestination新增了onActive和onInactive回调，用于感知NavDestination的激活态和非激活态。

    ```ts
    .onActive(() => {
      promptAction.openToast({ message: 'onActive触发了' });
    })
    .onInactive(() => {
      promptAction.openToast({ message: 'onInactive触发了' });
    });
    ```
  + **方案二**：使用无感监听感知下层NavDestination状态。

    当页面切换时，会触发监听NavDestination组件的状态变化，并返回组件信息[NavDestinationInfo](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)。通过NavDestinationInfo的name和state可以监听指定NavDestination组件的状态。

    ```ts
    aboutToAppear(): void {
      uiObserver.on('navDestinationUpdate', (info: NavDestinationInfo) => {
        if (info.name === 'NavPage') {
          console.info(`Succeeded in getting state.state:${info.state}.`);
        }
      });
    }

    aboutToDisappear(): void {
      uiObserver.off('navDestinationUpdate');
    }
    ```

  完整示例参考如下：

  ```ts
  import { promptAction, uiObserver } from '@kit.ArkUI';

  @Entry
  @Component
  struct DialogPage {
    @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();

    @Builder
    pageMap(name: string) {
      if (name === 'NavPage') {
        NavPage();
      } else if (name === 'DialogNav') {
        DialogNav();
      }
    }

    aboutToAppear(): void {
      uiObserver.on('navDestinationUpdate', (info: NavDestinationInfo) => {
        if (info.name === 'NavPage') {
          console.info(`Succeeded in getting state.state:${info.state}.`);
        }
      });
    }

    aboutToDisappear(): void {
      uiObserver.off('navDestinationUpdate');
    }

    build() {
      Navigation(this.pageInfo) {
        Button('跳转到Dialog')
          .onClick(() => {
            this.pageInfo.pushPathByName('DialogNav', null, false);
          });
      }
      .height('100%')
      .width('100%')
      .navDestination(this.pageMap)
      .hideNavBar(true)
      .hideTitleBar(true)
      .onAppear(() => {
        this.pageInfo.pushPathByName('NavPage', null, false);
      });

    }
  }

  @Component
  struct NavPage {
    @Consume('pageInfo') pageInfo: NavPathStack;

    build() {
      NavDestination() {
        Button('跳转到Dialog')
          .onClick(() => {
            this.pageInfo.pushPathByName('DialogNav', null, false);
          });
      }
      .height('100%')
      .width('100%')
      .onActive(() => {
        promptAction.openToast({ message: 'onActive触发了' });
      })
      .onInactive(() => {
        promptAction.openToast({ message: 'onInactive触发了' });
      });
    }
  }

  @Component
  struct DialogNav {
    @Consume('pageInfo') pageInfo: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Text('DIALOG');
        }
        .width('80%')
        .height(100)
        .backgroundColor('#f1f3f5')
        .borderRadius(15);
      }
      .mode(NavDestinationMode.DIALOG);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/NBtX6De-QWCrTo1MpmYo4Q/zh-cn_image_0000002658806747.png "点击放大")
* **场景三**：申请权限弹窗触发onHidden和onShown。

  权限弹窗属于全局模态组件，会强制覆盖当前页面。当弹窗显示时，当前NavDestination页面会触发onHidden（页面被遮挡）和onInactive（失去焦点）。弹窗关闭后，页面重新可见并激活，触发onShown和onActive回调。

  onWillShow仅在页面即将通过路由操作进入前台时触发。权限弹窗的显示/隐藏不涉及路由栈的变化（页面未离开导航栈），因此不会触发路由相关的生命周期onWillShow回调。

  ```ts
  import { abilityAccessCtrl, common, Context, bundleManager } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { PermissionRequestResult, Permissions } from '@ohos.abilityAccessCtrl';
  import { promptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct PermissionPage {
    @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();

    @Builder
    pageMap(name: string) {
      if (name === 'Page') {
        Page();
      }
    }

    build() {
      Navigation(this.pageInfo) {
        Button('跳转到NavDestination')
          .onClick(() => {
            this.pageInfo.pushPathByName('Page', null, false);
          });
      }
      .width('100%')
      .height('100%')
      .navDestination(this.pageMap);
    }
  }

  @Component
  struct Page {
    @Consume('pageInfo') pageInfo: NavPathStack;

    // 检查权限
    async checkPermissionGrant(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      let grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;
      // 获取应用程序的accessTokenID。
      let tokenId: number = 0;
      try {
        let bundleInfo: bundleManager.BundleInfo =
          await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
        let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
        tokenId = appInfo.accessTokenId;
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to get bundle info for self, code: ${err.code}, message: ${err.message}`);
      }
      // 校验应用是否被授予权限。
      try {
        grantStatus = await atManager.checkAccessToken(tokenId, permission);
      } catch (error) {
        const err: BusinessError = error as BusinessError;
        console.error(`Failed to check access token, code: ${err.code}, message: ${err.message}`);
      }
      return grantStatus;
    }

    // 检查位置定位权限，若未授权则开启二次授权
    async checkPermissions(): Promise<void> {
      // 获取精确定位权限状态。
      let grantStatus1: boolean =
        await this.checkPermissionGrant('ohos.permission.LOCATION') === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      // 获取模糊定位权限状态。
      let grantStatus2: boolean = await this.checkPermissionGrant('ohos.permission.APPROXIMATELY_LOCATION') ===
        abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
      // 精确定位、模糊定位均授权
      if (grantStatus1 && grantStatus2) {
        promptAction.openToast({ message: '用户已授权' });
      } else {
        // 进行二次授权
        await this.requestPermissionSecond();
      }
    }

    // 申请权限
    async requestPermission(): Promise<void> {
      let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      atManager.requestPermissionsFromUser(context,
        ['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'],
        (err: BusinessError, result: PermissionRequestResult) => {
          if (err) {
            promptAction.openToast({ message: '请求失败' });
          } else {
            let isGrant = result.authResults.every((status) => {
              return status === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
            });
            if (isGrant) {
              promptAction.openToast({ message: '用户已授权' });
            } else {
              promptAction.openToast({ message: '用户拒绝授权' });
            }
          }
        });
    }

    // 二次授权
    async requestPermissionSecond(): Promise<void> {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      atManager.requestPermissionOnSetting(context,
        ['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'])
        .then((data: abilityAccessCtrl.GrantStatus[]) => {
          console.info(`Succeeded in requestPermissionOnSetting, result: ${data}`);
        })
        .catch((err: BusinessError) => {
          console.error(`Failed to requestPermissionOnSetting, code: ${err.code}, message: ${err.message}`);
        });
    }

    build() {
      NavDestination() {
        Column({ space: 16 }) {
          Button('申请权限')
            .onClick(async () => {
              await this.requestPermission();
            });
          Button('二次申请')
            .onClick(async () => {
              await this.checkPermissions();
            });
        };
      }
      .onShown(() => {
        console.info(`Succeeded in triggering onShown.`);
      })
      .onHidden(() => {
        console.info(`Succeeded in triggering onHidden.`);
      })
      .onActive(() => {
        console.info(`Succeeded in triggering onActive.`);
      })
      .onInactive(() => {
        console.info(`Succeeded in triggering onInactive.`);
      })
      .onWillShow(() => {
        console.info(`Succeeded in triggering onWillShow. `);
      })
      .onWillHide(() => {
        console.info(`Succeeded in triggering onWillHide. `);
      });
    }
  }
  ```

  在module.json5中声明所需权限：

  ```json
  "requestPermissions": [
    {
      "name": "ohos.permission.INTERNET"
    },
    {
      "name": "ohos.permission.APPROXIMATELY_LOCATION",
      "reason": "$string:approximately_location",
      "usedScene": {
        "abilities": [
          "EntryAbility"
        ],
        "when": "inuse"
      }
    },
    {
      "name": "ohos.permission.LOCATION",
      "reason": "$string:location",
      "usedScene": {
        "abilities": [
          "EntryAbility"
        ],
        "when": "inuse"
      }
    }
  ],
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/F5EeRKi-SBmG4EokPZZE-w/zh-cn_image_0000002628407494.png "点击放大")

  日志如下所示：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/2Xg3cYd1Q7q25XU-e9yzxA/zh-cn_image_0000002628567390.png "点击放大")

## 常见FAQ

Q：如何感知自定义组件的销毁？

A：可使用[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)，函数在自定义组件析构销毁时执行。
