---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-900
title: PersistentStorage无法获取持久化的数据如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > PersistentStorage无法获取持久化的数据如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9bb3cf92909426a7f3af5ff94b2e32c0d5fe9319b99999a98a5e188bf6a85474
---

## 问题现象

使用PersistentStorage对UI状态变量操作时，该变量不能正确持久化，每次启动应用时数值都被重新初始化。

如下示例代码，示例应用中有3个UI状态变量，分别使用LocalStorage、AppStorage、PersistentStorage进行管理。其中totalClickCount由PersistentStorage进行管理，会持久化存储，应用每次启动时页面应当展示持久化的数据，但示例中无法正常获取，每次启动应用时都会被初始化为0。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/ol3EF8gWQWiS7S7FhhCn3Q/zh-cn_image_0000002628559668.png "点击放大")

问题代码示例参考如下：

* “src/main/ets/const/StorageKeyConst.ets”。

  ```ts
  export namespace StorageKeyConst {
    // 应用级UI状态存储
    export const APP_PROP_KEY: string = 'APP_PROP';

    // 页面级UI状态存储
    export const LOCAL_PROP_KEY: string = 'LOCAL_PROP';

    // 持久化UI状态存储
    export const PERSIST_PROP_KEY: string = 'PERSIST_PROP';
  }
  ```
* “src/main/ets/entryability/EntryAbility.ets”。

  ```ts
  export default class EntryAbility extends UIAbility {
    onWindowStageCreate(windowStage: window.WindowStage): void {
      // 初始化应用级存储
      AppStorage.setOrCreate(StorageKeyConst.APP_PROP_KEY, 0);
      // 初始化应用持久化存储
      PersistentStorage.persistProp(StorageKeyConst.PERSIST_PROP_KEY, 0);
      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          // 处理异常
          return;
        }
      });
    }
  }
  ```
* “src/main/ets/pages/Index.ets”。

  ```ts
  import { StorageKeyConst } from '../const/StorageKeyConst';
  import { Router } from '@kit.ArkUI';

  let storage: LocalStorage = new LocalStorage();

  @Entry(storage)
  @Component
  struct Index {
    // 页面序号
    @State pageNo: string = '';
    // 页面级UI状态存储（仅保存在当前页面）
    @LocalStorageLink(StorageKeyConst.LOCAL_PROP_KEY)
    pageClickCount: number = 0;
    // 应用级UI状态存储（保存在应用内存中，应用退出后释放）
    @StorageLink(StorageKeyConst.APP_PROP_KEY)
    startupClickCount: number = 0;
    // 持久化UI状态存储（持久化保存，应用退出后数据保留）
    @StorageLink(StorageKeyConst.PERSIST_PROP_KEY)
    totalClickCount: number = 0;
    router: Router = this.getUIContext().getRouter()

    aboutToAppear(): void {
      // 当前页面序号
      this.pageNo = this.router.getLength()
    }

    build() {
      RelativeContainer() {
        Column() {
          Text(`当前页面序号：${this.pageNo}`)
            .margin(20)
          Text(`当前页面点击次数：${this.pageClickCount}`)
            .margin(10)
          Text(`本次启动点击次数：${this.startupClickCount}`)
            .margin(10)
          Text(`总计点击次数：${this.totalClickCount}`)
            .margin(10)
          Button('Click!')
            .margin(10)
            .onClick(() => {
              // 点击计数
              this.pageClickCount++
              this.startupClickCount++
              this.totalClickCount++
            })
          Button('New Page')
            .margin(10)
            .onClick(() => {
              this.router.pushUrl({ url: 'pages/Index' })
            })
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center)
      }
    }
  }
  ```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/MTrcd-JURJeQKlggGAgJrw/zh-cn_image_0000002658918975.gif "点击放大")

## 背景知识

* [LocalStorage](../harmonyos-guides/arkts-localstorage.md)：LocalStorage是页面级的UI状态存储，通过@Entry装饰器接收的参数可以在页面内共享同一个LocalStorage实例。LocalStorage支持UIAbility实例内多个页面间状态共享。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：AppStorage是应用全局的UI状态存储，是和应用的进程绑定的，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储。
* [PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)：PersistentStorage是应用程序中的可选单例对象。此对象的作用是持久化存储选定的AppStorage属性，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同。

## 解决方案

PersistentStorage和UI实例相关联，持久化操作需要在UI实例初始化成功后（即[loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)传入的回调被调用时）才可以被调用，由于问题代码中PersistentStorage早于该时机调用，所以会导致持久化失败。参考[PersistentStorage：持久化存储UI状态 - 限制条件](../harmonyos-guides/arkts-persiststorage.md#限制条件)。

通过以上分析可以得出结论：此问题关键点在于PersistentStorage初始化时机不对。因此只需要修改EntryAbility.ets中的onWindowStageCreate函数，在windowStage加载页面完成回调函数中初始化应用持久化存储即可。关键代码修改示例如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      return;
    }
    // 初始化应用级存储
    AppStorage.setOrCreate(StorageKeyConst.APP_PROP_KEY, 0);
    // 初始化应用持久化存储
    PersistentStorage.persistProp(StorageKeyConst.PERSIST_PROP_KEY, 0);
    hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
  });
}
```

完整示例参考如下：

1. StorageKeyConst.ets：

   ```ts
   export namespace StorageKeyConst {
     // 应用级UI状态存储
     export const APP_PROP_KEY: string = 'APP_PROP';

     // 页面级UI状态存储
     export const LOCAL_PROP_KEY: string = 'LOCAL_PROP';

     // 持久化UI状态存储
     export const PERSIST_PROP_KEY: string = 'PERSIST_PROP';
   }
   ```
2. EntryAbility.ets：

   ```ts
   import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { window } from '@kit.ArkUI';
   import { StorageKeyConst } from '../const/StorageKeyConst';

   const DOMAIN = 0x0000;

   export default class EntryAbility extends UIAbility {
     onCreate(): void {
       try {
         this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
       } catch (err) {
         hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
       }
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
     }

     onDestroy(): void {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
     }

     onWindowStageCreate(windowStage: window.WindowStage): void {
       // Main window is created, set main page for this ability
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
       windowStage.loadContent('pages/Index', (err) => {
         if (err.code) {
           hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
           return;
         }
         // 初始化应用级存储
         AppStorage.setOrCreate(StorageKeyConst.APP_PROP_KEY, 0);
         // 初始化应用持久化存储
         PersistentStorage.persistProp(StorageKeyConst.PERSIST_PROP_KEY, 0);
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
   }
   ```
3. Index.ets：

   ```screen
   import { StorageKeyConst } from '../const/StorageKeyConst';
   import { Router } from '@kit.ArkUI';

   let storage: LocalStorage = new LocalStorage();

   @Entry(storage)
   @Component
   export struct Index {
     // 页面序号
     @State pageNo: string = '';
     // 页面级UI状态存储（仅保存在当前页面）
     @LocalStorageLink(StorageKeyConst.LOCAL_PROP_KEY) pageClickCount: number = 0;
     // 应用级UI状态存储（保存在应用内存中，应用退出后释放）
     @StorageLink(StorageKeyConst.APP_PROP_KEY) startupClickCount: number = 0;
     // 持久化UI状态存储（持久化保存，应用退出后数据保留）
     @StorageLink(StorageKeyConst.PERSIST_PROP_KEY) totalClickCount: number = 0;
     router: Router = this.getUIContext().getRouter();

     aboutToAppear(): void {
       // 当前页面序号
       this.pageNo = this.router.getLength();
     }

     build() {
       RelativeContainer() {
         Column() {
           Text(`当前页面序号：${this.pageNo}`)
             .margin(20)
           Text(`当前页面点击次数：${this.pageClickCount}`)
             .margin(10)
           Text(`本次启动点击次数：${this.startupClickCount}`)
             .margin(10)
           Text(`总计点击次数：${this.totalClickCount}`)
             .margin(10)
           Button('Click!')
             .margin(10)
             .onClick(() => {
               // 点击计数
               this.pageClickCount++;
               this.startupClickCount++;
               this.totalClickCount++;
             })
           Button('New Page')
             .margin(10)
             .onClick(() => {
               this.router.pushUrl({ url: 'pages/Index' });
             })
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Center)
       }
     }
   }
   ```

## 总结

PersistentStorage需要在首页加载后进行初始化才能正确绑定UI状态，因此一定要在windowStage.loadContent之后进行初始化，否则无法正确获取已存储的数据，或者会导致将已存储的数据覆盖。
