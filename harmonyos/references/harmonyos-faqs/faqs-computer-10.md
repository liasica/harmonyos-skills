---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-10
title: PC端点击Dock栏关闭窗口时，如何弹窗确认
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC端点击Dock栏关闭窗口时，如何弹窗确认
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95385d0c7a33603b325e1c2c936e6be45282b2b2cb20dfe3705dd55df165cfd1
---

## 问题现象

HarmonyOS PC端应用最小化Dock栏后，如何在应用右键点击关闭窗口时，增加一个二次确认弹窗给到用户操作。

## 背景知识

* [onPrepareToTerminate](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminate10)：在UIAbility即将关闭前（例如用户通过点击应用窗口右上角的关闭按钮、或者通过Dock栏/托盘右键退出应用时），系统会触发该回调，用于在UIAbility正式关闭前执行其他操作。
* 开发者可以在onPrepareToTerminate回调中返回true阻拦此次关闭，然后在合适时机主动调用[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)接口关闭。
* [showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog)：创建并显示对话框，对话框响应结果使用callback异步回调返回。

## 解决方案

HarmonyOS PC端应用最小化Dock栏后，可以通过监听onPrepareToTerminate回调，在触发右键点击关闭窗口时，恢复主窗口并弹窗通知用户二次确认后再关闭窗口。

* 在module.json5配置文件中声明[ohos.permission.PREPARE\_APP\_TERMINATE](../harmonyos-guides/permissions-for-all.md#ohospermissionprepare_app_terminate)权限。

  ```json
  "requestPermissions":[
    {
      "name" : "ohos.permission.PREPARE_APP_TERMINATE"
    }
  ],
  ```
* 在EntryAbility.ets文件中添加onPrepareToTerminate回调事件，在Dock栏关闭窗口时，进行弹窗提示。

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

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
      // 存储windowStage
      AppStorage.setOrCreate('windowStage', windowStage);
      windowStage.loadContent('pages/Index', (err) => {
        // 存储windowStatus
        AppStorage.setOrCreate('windowStatus', window.WindowStatusType.FULL_SCREEN);
        windowStage.getMainWindow((err: BusinessError, data) => {
          if (err) {
            // To do sth.
          }
          let windowClass = data;
          windowClass.on('windowStatusChange', (windowStatusType) => {
            AppStorage.setOrCreate('windowStatus', windowStatusType);
          });
        });
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
      let windowStatus = AppStorage.get('windowStatus') as window.WindowStatusType;
      if (windowStatus == window.WindowStatusType.MINIMIZE) {
        let mainWindowClass = this.currentWindowStage?.getMainWindowSync() as window.Window;
        let promise = mainWindowClass.restore();
        promise.then(() => {
          console.info('Succeeded in restoring the window.');
          if (this.currentWindowStage !== null) {
            this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showDialog({
              title: '提示',
              message: '确认是否关闭APP？',
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
        }).catch((err: BusinessError) => {
          console.error(`Failed to restore the window. Cause code: ${err.code},
                    message: ${err.message}`);
        });
        return true;
      } else {
        if (this.currentWindowStage !== null) {
          this.currentWindowStage?.getMainWindowSync().getUIContext().getPromptAction().showDialog({
            title: '提示',
            message: '确认是否关闭APP？',
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
      }
      return true;
    }
  };
  ```
