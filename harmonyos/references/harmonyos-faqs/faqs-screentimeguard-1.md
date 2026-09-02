---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-screentimeguard-1
title: 屏幕时间守护服务的策略设置与使用时长查询
breadcrumb: FAQ > 应用服务开发 > 屏幕时长守护服务（Screen Time Guard Kit） > 屏幕时间守护服务的策略设置与使用时长查询
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:26+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:d7b9165e0fbf859824bc4e7db867aba837563671e7e090b50559bc44669f6c5b
---

## 问题现象

场景一：如何通过[Screen Time Guard Kit](../harmonyos-guides/screen-time-guard-kit-guide.md)实现限制每天只能使用1个小时的手机？

场景二：屏幕时间守护服务如何监听可用时长已用完？

场景三：应用内能否展示被限制应用的图标和应用名等信息？

## 背景知识

* [守护策略管理](../harmonyos-guides/screentimeguard-guard-strategy-manage.md)：当用户希望创建新的屏幕时间守护规则时，可以调用添加管控策略的接口。根据参数中传入的策略，用户可以添加各种策略，如设置各个应用的停用起止时间。一旦策略被创建并启用，系统将根据规则对用户的屏幕使用行为进行监管。
* ACL权限申请：使用Screen Time Guard Kit（屏幕时间守护服务）需要申请"ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD"ACL权限，具体参考官网[受限ACL权限申请](../harmonyos-guides/screentimeguard-permission-application.md)。
* [queryGuardStrategyData](../harmonyos-references/screentimeguard-guardservice.md#queryguardstrategydata)：查询守护策略的使用时长，即从启动该策略开始到调用该接口时所经过的时间。该接口只支持查询INCLUSIVE\_DURATION\_TYPE类型的策略使用时长。
* [TimeGuardExtensionAbility](../harmonyos-references/screentimeguard-timeguardextensionability.md)：为管控应用提供在守护策略生效和结束、获取授权和撤销授权场景下的生命周期回调，开发者通过定义该回调函数，可以在上述场景中执行特定逻辑。

## 解决方案

### 场景一

准备工作：完成[配置签名](../harmonyos-guides/screentimeguard-app-signature.md)和[受限ACL权限申请](../harmonyos-guides/screentimeguard-permission-application.md)。可使用自动签名完成ACL权限调试配置，具体参考[自动签名支持的ACL权限](../harmonyos-guides/ide-signing.md#section5301916183411)。

* **步骤一：**

  Screen Time Guard Kit支持对用户设备的时间管理和应用限制，因此在功能启用前，必须获得用户的明确授权。具体流程参考[请求用户授权](../harmonyos-guides/screentimeguard-request-user-auth.md)。

  ```ts
  try {
        const status = await guardService.getUserAuthStatus();
        hilog.info(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `user auth status: ${status}`);
        if (status != guardService.AuthStatus.AUTH_GRANTED) {
          await guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext);
        }
      } catch (err) {
        const message = (err as BusinessError).message;
        const code = (err as BusinessError).code;
        hilog.error(0x0000, `ScreenTimeGuard:requestUserAuth`,
          `requestUserAuth failed with error code: ${code}, message: ${message}`);
      }
  ```
* **步骤二：**

  [TimeStrategyType](../harmonyos-references/screentimeguard-guardservice.md#timestrategytype)时长策略类型有以下3种类型，按照不同的场景配置策略类型，具体配置如下：

  + START\_END\_TIME\_TYPE：管控策略可以设置为起止时间策略，表示策略在一天内配置的起始时间和结束时间内生效。常用于周期性管控，使用场景举例：每天22点到第二天7点，禁止使用XX应用。

    **说明** 

    如果为此类型，则TimeStrategy接口中的startTime、endTime必填，totalDuration非必填。

    ```ts
    // 添加起始时间策略
              try {
                // 先调用startAppPicker获取相应应用的token
                const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
                const startEndTime: guardService.TimeStrategy = {
                  type: guardService.TimeStrategyType.START_END_TIME_TYPE,
                  startTime: '08:00',
                  endTime: '19:00',
                };
                const info: guardService.AppInfo = {
                  appTokens: tokens
                };
                const strategy: guardService.GuardStrategy = {
                  name: 'startEndTimeStrategy',
                  timeStrategy: startEndTime,
                  appInfo: info,
                  appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
                };
                await guardService.addGuardStrategy(strategy);
                this.currentStrategy = 'startEndTimeStrategy';
              } catch (err) {
                const message = (err as BusinessError).message;
                const code = (err as BusinessError).code;
                hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
                  `addGuardStrategy failed with error code: ${code}, message: ${message}`);
              }
    ```
  + TOTAL\_DURATION\_TYPE：总时长策略类型，表示一天内策略生效的总时长，从调用startGuardStrategy接口成功后开始计时。使用场景举例：启动策略后1小时内，禁止使用XX应用。

    **说明** 

    如果为此类型，则TimeStrategy接口中的startTime、endTime非必填，totalDuration必填。

    ```ts
    // 添加总时长策略
              try {
                // 先调用startAppPicker获取相应应用的token
                const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
                const totalDurationTime: guardService.TimeStrategy = {
                  type: guardService.TimeStrategyType.TOTAL_DURATION_TYPE,
                  totalDuration: 3,
                };
                const info: guardService.AppInfo = {
                  appTokens: tokens
                };
                const strategy: guardService.GuardStrategy = {
                  name: 'totalDurationTimeStrategy',
                  timeStrategy: totalDurationTime,
                  appInfo: info,
                  appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
                };
                await guardService.addGuardStrategy(strategy);
                this.currentStrategy = 'totalDurationTimeStrategy';
              } catch (err) {
                const message = (err as BusinessError).message;
                const code = (err as BusinessError).code;
                hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
                  `addGuardStrategy failed with error code: ${code}, message: ${message}`);
              }
    ```
  + INCLUSIVE\_DURATION\_TYPE：共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额，超额后所有应用均受时长限制，从调用startGuardStrategy接口成功后开始计时。使用场景举例：每天限制使用指定视频类应用（A应用、B应用）时长2小时。

    **说明** 

    如果为此类型，则TimeStrategy接口中的startTime、endTime非必填，totalDuration必填，RestrictionType只支持TRUSTLIST\_TYPE。

    ```ts
    // 添加共享时长策略
              try {
                // 先调用startAppPicker获取相应应用的token
                const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
                const inclusiveDurationTime: guardService.TimeStrategy = {
                  type: guardService.TimeStrategyType.INCLUSIVE_DURATION_TYPE,
                  totalDuration: 3,
                };
                const info: guardService.AppInfo = {
                  appTokens: tokens
                };
                const strategy: guardService.GuardStrategy = {
                  name: 'inclusiveDurationTimeStrategy',
                  timeStrategy: inclusiveDurationTime,
                  appInfo: info,
                  appRestrictionType: guardService.RestrictionType.TRUSTLIST_TYPE
                };
                await guardService.addGuardStrategy(strategy);
                this.currentStrategy = 'inclusiveDurationTimeStrategy';
              } catch (err) {
                const message = (err as BusinessError).message;
                const code = (err as BusinessError).code;
                hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
                  `addGuardStrategy failed with error code: ${code}, message: ${message}`);
              }
    ```
* **步骤三：**

  确认并生成管控策略后，根据参数中传入的策略名，应用可以启动对应管控策略。具体流程参考[启动策略](../harmonyos-guides/screentimeguard-start-guard-strategy.md)。

  ```ts
  async startGuardStrategy(strategyName: string) {
      try {
        await guardService.startGuardStrategy(strategyName);
        hilog.info(0x0000, `ScreenTimeGuard:startGuardStrategy`, 'success');
        this.getUIContext().getPromptAction().showToast({
          message: 'startGuardStrategy success',
          duration: 2000,
        });
      } catch (err) {
        const message = (err as BusinessError).message;
        const code = (err as BusinessError).code;
        hilog.error(0x0000, `ScreenTimeGuard:startGuardStrategy`,
          `startGuardStrategy failed with error code: ${code}, message: ${message}`);
      }
    }
  ```

**完整代码：**

```ts
import { appPicker, guardService } from '@kit.ScreenTimeGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State currentStrategy?: string = '';

  async aboutToAppear(): Promise<void> {
    try {
      const status = await guardService.getUserAuthStatus();
      hilog.info(0x0000, `ScreenTimeGuard:getUserAuthStatus`, `user auth status: ${status}`);
      if (status != guardService.AuthStatus.AUTH_GRANTED) {
        await guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext);
      }
    } catch (err) {
      const message = (err as BusinessError).message;
      const code = (err as BusinessError).code;
      hilog.error(0x0000, `ScreenTimeGuard:requestUserAuth`,
        `requestUserAuth failed with error code: ${code}, message: ${message}`);
    }
  }

  async startGuardStrategy(strategyName: string) {
    try {
      await guardService.startGuardStrategy(strategyName);
      hilog.info(0x0000, `ScreenTimeGuard:startGuardStrategy`, 'success');
      this.getUIContext().getPromptAction().showToast({
        message: 'startGuardStrategy success',
        duration: 2000,
      });
    } catch (err) {
      const message = (err as BusinessError).message;
      const code = (err as BusinessError).code;
      hilog.error(0x0000, `ScreenTimeGuard:startGuardStrategy`,
        `startGuardStrategy failed with error code: ${code}, message: ${message}`);
    }
  }

  async stopGuardStrategy(strategyName: string) {
    try {
      await guardService.stopGuardStrategy(strategyName);
      hilog.info(0x0000, `ScreenTimeGuard:stopGuardStrategy`, 'success');
      this.getUIContext().getPromptAction().showToast({
        message: 'stopGuardStrategy success',
        duration: 2000,
      });
    } catch (err) {
      const message = (err as BusinessError).message;
      const code = (err as BusinessError).code;
      hilog.error(0x0000, `ScreenTimeGuard:stopGuardStrategy`,
        `stopGuardStrategy failed with error code: ${code}, message: ${message}`);
    }
  }

  build() {
    Column({ space: 10 }) {
      Text('当前策略：' + this.currentStrategy);

      Button('添加起始时间策略')
        .onClick(async () => {
          try {
            await guardService.removeGuardStrategy('startEndTimeStrategy');
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:removeGuardStrategy`,
              `removeGuardStrategy failed with error code: ${code}, message: ${message}`);
          }
          // 添加起始时间策略
          try {
            // 先调用startAppPicker获取相应应用的token
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
            const startEndTime: guardService.TimeStrategy = {
              type: guardService.TimeStrategyType.START_END_TIME_TYPE,
              startTime: '08:00',
              endTime: '19:00',
            };
            const info: guardService.AppInfo = {
              appTokens: tokens
            };
            const strategy: guardService.GuardStrategy = {
              name: 'startEndTimeStrategy',
              timeStrategy: startEndTime,
              appInfo: info,
              appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
            };
            await guardService.addGuardStrategy(strategy);
            this.currentStrategy = 'startEndTimeStrategy';
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
              `addGuardStrategy failed with error code: ${code}, message: ${message}`);
          }
        })

      Button('添加总时长策略')
        .onClick(async () => {
          try {
            await guardService.removeGuardStrategy('totalDurationTimeStrategy');
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:removeGuardStrategy`,
              `removeGuardStrategy failed with error code: ${code}, message: ${message}`);
          }

          // 添加总时长策略
          try {
            // 先调用startAppPicker获取相应应用的token
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
            const totalDurationTime: guardService.TimeStrategy = {
              type: guardService.TimeStrategyType.TOTAL_DURATION_TYPE,
              totalDuration: 3,
            };
            const info: guardService.AppInfo = {
              appTokens: tokens
            };
            const strategy: guardService.GuardStrategy = {
              name: 'totalDurationTimeStrategy',
              timeStrategy: totalDurationTime,
              appInfo: info,
              appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
            };
            await guardService.addGuardStrategy(strategy);
            this.currentStrategy = 'totalDurationTimeStrategy';
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
              `addGuardStrategy failed with error code: ${code}, message: ${message}`);
          }
        })

      Button('添加共享时长策略')
        .onClick(async () => {
          try {
            await guardService.removeGuardStrategy('inclusiveDurationTimeStrategy');
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:removeGuardStrategy`,
              `removeGuardStrategy failed with error code: ${code}, message: ${message}`);
          }

          // 添加共享时长策略
          try {
            // 先调用startAppPicker获取相应应用的token
            const tokens = await appPicker.startAppPicker(this.getUIContext().getHostContext(), { appTokens: [] });
            const inclusiveDurationTime: guardService.TimeStrategy = {
              type: guardService.TimeStrategyType.INCLUSIVE_DURATION_TYPE,
              totalDuration: 3,
            };
            const info: guardService.AppInfo = {
              appTokens: tokens
            };
            const strategy: guardService.GuardStrategy = {
              name: 'inclusiveDurationTimeStrategy',
              timeStrategy: inclusiveDurationTime,
              appInfo: info,
              appRestrictionType: guardService.RestrictionType.TRUSTLIST_TYPE
            };
            await guardService.addGuardStrategy(strategy);
            this.currentStrategy = 'inclusiveDurationTimeStrategy';
          } catch (err) {
            const message = (err as BusinessError).message;
            const code = (err as BusinessError).code;
            hilog.error(0x0000, `ScreenTimeGuard:addGuardStrategy`,
              `addGuardStrategy failed with error code: ${code}, message: ${message}`);
          }
        })

      Button('启动当前策略')
        .onClick(() => {
          if (this.currentStrategy) {
            this.startGuardStrategy(this.currentStrategy);
          } else {
            this.getUIContext().getPromptAction().showToast({
              message: '请先设置当前策略',
              duration: 2000,
            });
          }
        })

      Button('停止当前策略')
        .onClick(() => {
          if (this.currentStrategy) {
            this.stopGuardStrategy(this.currentStrategy);
          } else {
            this.getUIContext().getPromptAction().showToast({
              message: '请先设置当前策略',
              duration: 2000,
            });
          }
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

### 场景二

调用[queryGuardStrategyData](../harmonyos-references/screentimeguard-guardservice.md#queryguardstrategydata)接口查询INCLUSIVE\_DURATION\_TYPE类型的策略使用时长，获取从启动策略到当前时刻的已用时长。通过[TimeGuardExtensionAbility](../harmonyos-references/screentimeguard-timeguardextensionability.md)的[onStop](../harmonyos-references/screentimeguard-timeguardextensionability.md#onstop)回调监听守护策略停止事件，当管控应用停止守护策略时，系统将自动触发此回调函数，可在回调函数中执行业务逻辑。

### 场景三

暂不支持在应用内展示被限制应用的图标和应用名等信息。建议使用已有功能，根据tokens拉起许可应用跳转页。
