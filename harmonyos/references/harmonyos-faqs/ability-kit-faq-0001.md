---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0001
title: Context功能使用常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > Context功能使用常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:43+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:621b27ed4b4859c1cebdba294a884dad12a188799d67046a6b3e8a1e1a98173c
---

**Q：如何获取App版本号，版本名，屏幕分辨率等信息？**

**A**：获取方式如下：

1. 通过@kit.AbilityKit中的bundleManager模块查询bundleInfo，其中包含App版本号和版本名。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { bundleManager } from '@kit.AbilityKit';

   // ...
   bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION).then((bundleInfo) => {
     let versionName = bundleInfo.versionName; // App version name
     let versionNo = bundleInfo.versionCode; // App version code
   }).catch((error: BusinessError) => {
     console.error('get bundleInfo failed, error is ' + error);
   })
   ```
2. 在context.config中获取screenDensity，其中包含屏幕分辨率信息。

   ```ts
   import { common } from '@kit.AbilityKit';

   // ...
   // In the utility class: Save the context to AppStorage in the EntryAbility - onCreate lifecycle, then use AppStorage to retrieve it in the utility class
   let context = AppStorage.get('context') as common.UIAbilityContext;

   let screenDensity = context.config.screenDensity;
   ```

**Q：如何在TaskPool和Woker获取上下文Context？**

**A**：Worker线程和TaskPool线程中无法直接获取到组件级的Context 。可以通过主线程参数传递应用级Context，通过[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)接口获取Context上下文。

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';

// Support for ordinary functions and passing of reference parameters as input.
@Concurrent
function printArgs(args: string, uiContext: Context | undefined): string {
  hilog.info(0x0000, 'printArgs', `func: ${args}`);
  hilog.info(0x0000, 'printArgs',
    `Obtain the bundle name of the application: ${uiContext?.applicationInfo.name.toString()}`);
  return args;
}

async function taskpoolExecute(uiContext: Context | undefined): Promise<void> {
  try {
    let task: taskpool.Task = new taskpool.Task(printArgs, 'create task, then execute', uiContext!);
    hilog.info(0x0000, 'taskpoolExecute', 'taskpool.execute(task) result: ' + await taskpool.execute(task));
    hilog.info(0x0000, 'taskpoolExecute',
      'taskpool.execute(function) result: ' + await taskpool.execute(printArgs, 'execute task by func', uiContext!));
  } catch (error) {
    hilog.info(0x0000, 'taskpoolExecute', `taskpool: error code: ${error.code}, info: ${error.message}`);
  }
}

@Entry
@Component
struct TaskPoolGetContext {
  @State message: string = 'Hello World';
  // Obtain the context.
  uiContext = this.getUIContext().getHostContext();

  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          taskpoolExecute(this.uiContext);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

**Q：如何主动退出整个应用？**

**A**：可以通过ApplicationContext的killAllProcesses()方法退出当前应用。调用killAllProcesses()方法后，会逐个终止应用中的所有进程。

**Q：如何设置应用自动重启？**

**A**：可以通过ApplicationContext.restartApp实现，具体请参考示例代码：

```ts
import { Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })

      Button('RESTART').onClick(() => {
        let applicationContext = this.context.getApplicationContext();
        let want: Want = {
          bundleName: 'com.example.myapp',
          abilityName: 'EntryAbility'
        };
        try {
          applicationContext.restartApp(want);
          hilog.info(0x0000, 'testTag', '%{public}s', 'applicationContext.restartApp');
        } catch (error) {
          console.error(`restartApp fail, error: ${JSON.stringify(error)}`);
        }
      })
    }
    .height('100%')
    .width('100%')
  }
}
```

参考链接：[ApplicationContext.restartApp](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextrestartapp12)。

**Q：如何在Page中获取WindowStage实例？**

**A**：

* 方式一：在onWindowStageCreate方法中获取，此方式适用于Ability生命周期内需要持久化WindowStage实例的场景。

  ```ts
  import { UIAbility } from '@kit.AbilityKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  export default class EntryAbility extends UIAbility {
    // ...
    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
      });
      console.info('windowStage', JSON.stringify(windowStage))
      // Store windowStage instance globally for cross-page access
      AppStorage.setAndLink('windowStage', windowStage)
    }

    // ...
  }
  ```

* 方式二：UIAbilityContext提供了获取WindowStage实例的接口，此方式适用于需要动态获取WindowStage的页面级场景，无需持久化存储。

  ```ts
  // Index.ets
  import common from '@ohos.app.ability.common';

  @Entry
  @Component
  struct Index {
    @State showAbility: string = 'get windowStage'

    build() {
      Row() {
        Column() {
          Text(this.showAbility)
            .fontSize(30)
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              console.info('Obtained WindowStage instance:',JSON.stringify(context.windowStage))
            });
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

参考链接：[onWindowStageCreate](../harmonyos-references/js-apis-app-ability-uiability.md#onwindowstagecreate)、[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md)。

**Q：如何将Resource资源对象转成string类型？**

**A**：Resource 为字符串，支持使用 this.context.resourceManager.getStringSync(r(′app.string.test′).id)同步转换为字符串，也支持使用*r*(′*a**pp*.*s**t**r**in**g*.*t**es**t*′).*i**d*)同步转换为字符串，也支持使用r('app.string.test', 2) 进行格式化。

参考链接：[getStringSync](../harmonyos-references/js-apis-resource-manager.md#getstringsync10)。

**Q：如何获取应用级别的temp路径和files路径？**

**A**：通过上下文 context 获取。例如：

* temp路径：通过 this.context.getApplicationContext().tempDir 获取。
* 文件路径：可通过 this.context.getApplicationContext().filesDir 获取。

参考链接：[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。
