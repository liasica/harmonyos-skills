---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-145
title: 全局订阅网络状态变化，如何在具体页面控制业务
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 全局订阅网络状态变化，如何在具体页面控制业务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:086fe6a1edafc2b234b3a501d9d37ee1eecfa7ee016322b2b85b51fb6c27c775
---

## 问题现象

如何在应用全局订阅网络状态，在不同子页面根据网络变化处理业务。

## 背景知识

* [接收指定网络的状态变化通知](../harmonyos-guides/net-connection-manager.md#接收指定网络的状态变化通知)。
* 应用全局的UI状态存储：[AppStorage](../harmonyos-guides/arkts-appstorage.md)、[@StorageProp](../harmonyos-guides/arkts-appstorage.md#storageprop)。
* 应用状态管理装饰器：[@Watch](../harmonyos-guides/arkts-watch.md)。

## 解决方案

1. 在应用启动后，EntryAbility中注册监听网络状态变化，监听到网络状态后存储在AppStorage中。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       this.netWork.register();
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```

   注册监听网络状态变化的具体实现在NetWork工具类中。

   ```ts
   register(): void {
     // 订阅网络能力变化事件
     this.netConnect.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
       let netAvailable = data.netCap.networkCap?.includes(connection.NetCap.NET_CAPABILITY_INTERNET);
       AppStorage.setOrCreate('netAvailable', netAvailable);
     });

     // 订阅网络丢失事件
     this.netConnect.on('netLost', () => {
       AppStorage.setOrCreate('netAvailable', false);
     });

     // 初始化注册
     this.netConnect.register((error: BusinessError) => {
       if (error) {
         console.log('AppNetStatus', 'register net failed');
         return;
       }
       console.log('AppNetStatus', 'register net success');
     });
   }
   ```
2. 在具体的page页面中实时接收网络状态变化，控制业务。

   ```ts
   @Entry
   @Component
   struct Index {
     @StorageProp('netAvailable') @Watch('onNetStatusChange') netAvailable: boolean = true;
     @State message: string = '网络正常';
     @State color: ResourceColor = Color.Green;

     build() {
       Column() {
         Text(this.message)
           .fontSize(48)
           .fontColor(this.color)
       }
       .justifyContent(FlexAlign.Center)
       .width('100%')
       .height('100%')
     }

     onNetStatusChange() {
       if (this.netAvailable) { // 网络恢复时重连业务
         this.message = '网络正常';
         this.color = Color.Green;
       } else { // 显示离线状态UI
         this.message = '网络异常';
         this.color = Color.Red;
       }
     }
   }
   ```
3. 退出应用后在EntryAbility中注销监听网络状态变化。

   ```ts
   onWindowStageDestroy(): void {
     // Main window is destroyed, release UI related resources
     this.netWork.unregister();
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
   }
   ```
4. 需要添加权限。

   ```json
   "requestPermissions": [
     { "name": "ohos.permission.GET_NETWORK_INFO" }
   ],
   ```

完整示例参考如下：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import NetWork from '../NetWork';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  private netWork: NetWork = new NetWork();
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
      this.netWork.register();
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    this.netWork.unregister();
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

```ts
import { connection } from "@kit.NetworkKit";
import { BusinessError } from "@kit.BasicServicesKit";

export default class NetWork {
  private netConnect: connection.NetConnection = connection.createNetConnection();

  register(): void {
    // 订阅网络能力变化事件
    this.netConnect.on('netCapabilitiesChange', (data: connection.NetCapabilityInfo) => {
      let netAvailable = data.netCap.networkCap?.includes(connection.NetCap.NET_CAPABILITY_INTERNET);
      AppStorage.setOrCreate('netAvailable', netAvailable);
    });

    // 订阅网络丢失事件
    this.netConnect.on('netLost', () => {
      AppStorage.setOrCreate('netAvailable', false);
    });

    // 初始化注册
    this.netConnect.register((error: BusinessError) => {
      if (error) {
        console.log('AppNetStatus', 'register net failed');
        return;
      }
      console.log('AppNetStatus', 'register net success');
    });
  }

  unregister(): void {
    if (this.netConnect) {
      this.netConnect.unregister((error: BusinessError) => {
        if (error) {
          console.log('register net failed');
          return;
        }
        console.log('register net success');
      });
    }
  }
}
```

```ts
@Entry
@Component
struct Index {
  @StorageProp('netAvailable') @Watch('onNetStatusChange') netAvailable: boolean = true;
  @State message: string = '网络正常';
  @State color: ResourceColor = Color.Green;

  build() {
    Column() {
      Text(this.message)
        .fontSize(48)
        .fontColor(this.color)
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }

  onNetStatusChange() {
    if (this.netAvailable) { // 网络恢复时重连业务
      this.message = '网络正常';
      this.color = Color.Green;
    } else { // 显示离线状态UI
      this.message = '网络异常';
      this.color = Color.Red;
    }
  }
}
```
