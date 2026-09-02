---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-151
title: 点击PC端应用右上角的X按钮（关闭按钮），确认关闭前的回调处理事件
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 点击PC端应用右上角的X按钮（关闭按钮），确认关闭前的回调处理事件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4670366c1c9c47f138c2c1079e4aa966a49ee08ed043c420c923efdf041bd2c3
---

## 问题现象

HarmonyOS PC端应用右上角的X按钮（关闭按钮）点击关闭之前增加一个二次确认弹窗，这个X按钮的点击事件在哪里添加呢？

## 背景知识

[onPrepareToTerminate](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminate10)当UIAbility即将关闭前，系统触发该回调，用于在UIAbility正式关闭前执行其他操作。开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)接口关闭。例如，询问用户是否确认关闭UIAbility，再主动销毁UIAbility。

* 回调前提：该接口仅在2in1设备上生效，且需要应用申请[ohos.permission.PREPARE\_APP\_TERMINATE](../harmonyos-guides/permissions-for-all.md#ohospermissionprepare_app_terminate)权限。
* 回调时机：当用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时，可以使用该回调。
* 从API version 15开始，当[UIAbility.onPrepareToTerminateAsync](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminateasync15)实现时，本回调函数将不执行。当[AbilityStage.onPrepareTerminationAsync](../harmonyos-references/js-apis-app-ability-abilitystage.md#onprepareterminationasync15)或[AbilityStage.onPrepareTermination](../harmonyos-references/js-apis-app-ability-abilitystage.md#onpreparetermination15)实现时，在Dock栏或系统托盘处右键点击关闭，本回调函数将不执行。
* 如果应用本身或者所使用的三方框架注册了[window.WindowStage.on('windowStageClose')](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageclose14)监听，本回调函数将不执行。

## 解决方案

[onPrepareToTerminate](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminate10)当UIAbility即将关闭前，系统触发该回调，用于在UIAbility正式关闭前执行其他操作。开发者可以在该回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)接口关闭。该接口仅在2in1设备上生效，且需要应用申请ohos.permission.PREPARE\_APP\_TERMINATE权限。

具体实现请参考如下代码：

* 在module.json5配置文件中声明[ohos.permission.PREPARE\_APP\_TERMINATE](../harmonyos-guides/permissions-for-all.md#ohospermissionprepare_app_terminate)权限。
* EntryAbility.ets文件中添加onPrepareToTerminate回调事件，代码如下所示：

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    //当前window对象
    private currentWindowStage: window.WindowStage | null = null;

    onCreate(): void {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);

      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      if (this.currentWindowStage === null) {
        this.currentWindowStage = windowStage;
      }
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      });

    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    }

    onForeground(): void {
      // Ability has brought to foreground
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
    }

    onBackground(): void {
      // Ability has back to background
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
    }

    onPrepareToTerminate(): boolean {
      // 开发者定义预关闭动作
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onPrepareToTerminate');
      // 例如关闭应用之前弹窗提示是否关闭app
      if (this.currentWindowStage !== null) {
        this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showDialog({
          title: '提示',
          message: '确认是否关闭应用程序？',
          buttons: [
            {
              text: '取消',
              color: '#0091FF'
            },
            {
              text: '确定',
              color: '#ff0000'
            }
          ]
        }).then(data => {
          if (data.index === 0) {
            this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showToast({
              message: '已取消',
              duration: 2000
            });
          } else {
            // 确认关闭
            this.context.terminateSelf();
          }
        });
      }
      return true; // 已定义预关闭操作后，返回true表示UIAbility取消关闭
    }
  };
  ```
