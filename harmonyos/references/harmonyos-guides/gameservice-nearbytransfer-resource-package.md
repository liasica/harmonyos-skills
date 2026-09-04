---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-nearbytransfer-resource-package
title: 传输资源包
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏近场快传（可选） > 开发指导 > 传输资源包
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:08+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:d0d79cd0a1d1505d499cac8b25fa93c433ef22b490eb4e6013ea6b14d69a6e6f
---

从API版本26.0.0开始，资源包传输接入流程更新，开发者无需手动绑定设备，可直接通过碰一碰开启传输，并通过want参数内的信息确认设备为接收端或发送端。

游戏近场快传支持已安装游戏的玩家间传输游戏内资源包，节省玩家下载资源包所需的流量和时间。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/IS4fiGtKSp-WT4YVj3-9Eg/zh-cn_image_0000002712245164.png)

1. 发送端游戏调用以下接口注册监听。

   * 注册连接通知监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonconnectnotify)('connectNotify')
   * 注册收到包信息监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonreceivepackageinfo)('receivePackageInfo')
   * 注册传输通知监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferontransfernotify)('transferNotify')
   * 注册错误事件监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonerror)('error')
2. 发送端近场快传服务向游戏发送建链成功connectNotify事件回调。

   **说明** 

   仅发送端有建链成功connectNotify事件回调，接收端收到[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调即代表建链成功。
3. 发送端游戏调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)创建资源包传输任务。
4. 接收端设备拉起游戏，获取[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中的want参数，并确认want内parameters参数中的isGameNearbyReceiver参数值。若值为true，则确认当前设备为接收端。

   当游戏未打开时，请获取[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)回调；当游戏已打开时，请获取[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调。
5. 接收端游戏调用以下接口注册监听。

   * 注册连接通知监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonconnectnotify)('connectNotify')
   * 注册收到包信息监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonreceivepackageinfo)('receivePackageInfo')
   * 注册传输通知监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferontransfernotify)('transferNotify')
   * 注册错误事件监听接口：[on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonerror)('error')
6. 接收端游戏调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)创建资源包传输任务。
7. 接收端游戏调用[sendPackageInfo](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo)发送自身文件信息，如版本信息、包信息。
8. 发送端游戏收到receivePackageInfo事件回调。
9. 发送端游戏比较版本。如对比结果为不需要发送，则调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)销毁服务。
10. 如发送端游戏对比结果为需要发送，则调用[transferPackageData](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata)向接收端发送需要传输的资源包。
11. 接收端游戏和发送端游戏可在transferNotify回调中获取当前已传输的包体大小、包体总大小、传输速率、传输剩余时间等信息。传输完成后，接收端游戏可获取已接收资源包的存储目录，对传输完成的资源文件做处理。
12. 处理传输完成的资源文件后，可调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)销毁服务。

    **说明** 

    * destroy接口会清除已接收数据，请确保对已接收数据做好处理或转移后再调用该接口。
    * 每次调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口会自动清理自身历史数据。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-nearbytransfer.md)。

| 接口名 | 描述 |
| --- | --- |
| [create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)(createParameters: CreateParameters): Promise<CreateResult> | 创建游戏近场快传服务。 |
| [on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonconnectnotify)(type: 'connectNotify', callback: Callback<ConnectNotification>): void | 订阅连接通知事件。 |
| [off](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferoffconnectnotify)(type: 'connectNotify', callback?: Callback<ConnectNotification>): void | 取消订阅连接通知事件。 |
| [on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonreceivepackageinfo)(type: 'receivePackageInfo', callback: Callback<PackageInfo>): void | 订阅收到包信息事件。 |
| [off](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferoffreceivepackageinfo)(type: 'receivePackageInfo', callback?: Callback<PackageInfo>): void | 取消订阅收到包信息事件。 |
| [on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferontransfernotify)(type: 'transferNotify', callback: Callback<TransferNotification>): void | 订阅传输通知事件。 |
| [off](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferofftransfernotify)(type: 'transferNotify', callback?: Callback<TransferNotification>): void | 取消订阅传输通知事件。 |
| [on](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonerror)(type: 'error', callback: Callback<ReturnResult>): void | 订阅错误事件。 |
| [off](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferofferror)(type: 'error', callback?: Callback<ReturnResult>): void | 取消订阅错误事件。 |
| [sendPackageInfo](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo)(packageInfo: PackageInfo): Promise<void> | 接收端发送自身文件信息。 |
| [transferPackageData](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata)(packageData: PackageData): Promise<void> | 传输包数据。 |
| [destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)(): Promise<void> | 销毁游戏近场快传服务。 |

## 接入步骤

### 导入模块

导入Game Service Kit及公共模块。

```typescript
import { abilityAccessCtrl, AbilityConstant, UIAbility, common } from "@kit.AbilityKit";
import { hilog } from '@kit.PerformanceAnalysisKit';
import { gameNearbyTransfer } from '@kit.GameServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 申请权限

申请ohos.permission.DISTRIBUTED\_DATASYNC权限用于设备发现，详情可参考[向用户申请授权](request-user-authorization.md)。

```typescript
let atManager = abilityAccessCtrl.createAtManager();
let uiAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
try {
  atManager.requestPermissionsFromUser(uiAbilityContext, ['ohos.permission.DISTRIBUTED_DATASYNC']).then((data) => {
    if (data.authResults[0] === 0) {
      // 用户授权，可以继续访问目标操作。
      hilog.info(0x0000, 'nearby', `ohos.permission.DISTRIBUTED_DATASYNC is granted by user.`);
    } else {
      // 用户拒绝授权，提示用户必须授权才能访问当前功能，并引导用户到系统设置中打开相应的权限。
      return;
    }
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'nearby', `Failed to request permissions from user, code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'nearby', `request permissions from user exception. Code: ${err.code}, message: ${err.message}`);
}
```

### 发送端注册相关回调

导入相关模块后，发送端需先注册各回调事件。

```typescript
// 注册监听
public registerCallback() {
  try {
    gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
    gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
    gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
    gameNearbyTransfer.on('error', errorCallBack);
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, 'nearby', `registerCallback error. Code: ${err.code}, message: ${err.message}`);
  }
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // 发送端收到连接回调，并调用create接口
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // 接收包信息回调，发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要传输资源包数据。
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // 传输回调，处理传输进度信息
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  // 异常信息回调，处理相关异常信息
}
```

### 发送端创建游戏近场快传服务

收到建链成功回调后，发送端调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口创建游戏近场快传服务。

```typescript
function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  if (callback.connectState == gameNearbyTransfer.ConnectState.CONNECTED) {
    // 发送端收到连接回调，并去调用create接口
    let uiAbilityContext = AppStorage.get<common.UIAbilityContext>('context')!;
    let initParam: gameNearbyTransfer.CreateParameters = {
      abilityName: uiAbilityContext.abilityInfo.name,
      context: uiAbilityContext,
      moduleName: uiAbilityContext.abilityInfo.moduleName,
      needShowSystemUI: false,
    };

    try {
      gameNearbyTransfer.create(initParam).then((createResult) => {
        hilog.info(0x0000, 'nearby', `create success localDeviceName ${createResult.localDeviceName}`);
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'nearby', `create failed. Code: ${err.code}, message: ${err.message}`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'nearby', `create exception. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

### 接收端获取want参数并发送自身文件信息

接收端拉起游戏，获取[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)或[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)回调中的want参数，并注册各回调事件，调用[create](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfercreate)接口创建游戏近场快传服务。近场快传服务创建完成后，调用[sendPackageInfo](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfersendpackageinfo)接口发送自身文件信息，如版本信息、包信息。

```typescript
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.startTransfer(want);
}

onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.startTransfer(want);
}

async startTransfer(want: Want) {
  const records = want.parameters;
  if (records) {
    const isGameNearbyReceiver = records.isGameNearbyReceiver as boolean;
    if (isGameNearbyReceiver) {
      // 注册回调并创建快传服务
      try {
        gameNearbyTransfer.on('connectNotify', connectNotifyCallBack);
        gameNearbyTransfer.on('receivePackageInfo', receivePackageInfoCallBack);
        gameNearbyTransfer.on('transferNotify', transferNotifyCallBack);
        gameNearbyTransfer.on('error', errorCallBack);
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, 'nearby', `registerCallback error. Code: ${err.code}, message: ${err.message}`);
      }
      let uiAbilityContext = this.context;
      AppStorage.setOrCreate('context', uiAbilityContext);
      let initParam: gameNearbyTransfer.CreateParameters = {
        abilityName: uiAbilityContext.abilityInfo.name,
        context: uiAbilityContext,
        moduleName: uiAbilityContext.abilityInfo.moduleName,
        needShowSystemUI: false,
      };

      try {
        await gameNearbyTransfer.create(initParam);
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, 'nearby', `create exception. Code: ${err.code}, message: ${err.message}`);
      }
      // 发送资源包信息给发送端
      let packageInfo: gameNearbyTransfer.PackageInfo = {
        name: 'com.huawei.xxxx',
        files: [],
        version: '1.1.0',
        extraData: 'extraData'
      };
      let fileInfo: gameNearbyTransfer.FileInfo = {
        path: '/xxx/xxxx/files/data.zip', // 沙箱路径
        hash: 'fileHash' // 可选
      };
      packageInfo.files?.push(fileInfo);
      try {
        gameNearbyTransfer.sendPackageInfo(packageInfo).then(() => {
          hilog.info(0x0000, 'nearby', `sendPackageInfo success`);
        }).catch((err: BusinessError) => {
          hilog.error(0x0000, 'nearby', `sendPackageInfo failed. Code: ${err.code}, message: ${err.message}`);
        });
      } catch (error) {
        let err = error as BusinessError;
        hilog.error(0x0000, 'nearby', `sendPackageInfo exception. Code: ${err.code}, message: ${err.message}`);
      }
    }
  }
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // 连接状态回调，收到连接断开回调时，可调用destroy
  hilog.info(0x0000, 'nearby', `connectNotify. State: ${callback.connectState}`);
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // 接收包信息回调，发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要传输资源包数据。
  hilog.info(0x0000, 'nearby', `get package info. version: ${callback.version}`);
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // 传输回调，处理传输进度信息
  hilog.info(0x0000, 'nearby', `get transfer state: ${callback.transferState}`);
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  // 异常信息回调，处理相关异常信息
  hilog.error(0x0000, 'nearby', `Error info. Code: ${callback.code}, message: ${callback.message}`);
}
```

### 发送端对比后传输资源包

发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要调用[transferPackageData](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransfertransferpackagedata)接口发送资源包数据。如果不需要发送资源包数据，则直接调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)接口销毁服务。

```typescript
function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  const version = callback.version;
  hilog.error(0x0000, 'nearby', `remote version: ${version}`);
  // 比较版本，决定是否需要发送资源包，也可以比较文件hash
  let packageInfoResult: gameNearbyTransfer.PackageInfoResult = {
    packageInfoResultCode: gameNearbyTransfer.PackageInfoResultCode.PACKAGE_AVAILABLE_COMPARED
  };
  if (packageInfoResult.packageInfoResultCode === gameNearbyTransfer.PackageInfoResultCode.PACKAGE_UNAVAILABLE_COMPARED) {
    // 如果不需要发送，需要调用destroy接口
    return;
  }
  let packageData: gameNearbyTransfer.PackageData = {
    name: 'com.huawei.gamenearbydemo',
    version: '1.0.0',
    files: [{
      srcPath: '/data/xxxx/a.zip',
      destPath: 'xxxx/a.zip'
    }] // srcPath是需要发送文件的路径，详情请参见沙箱路径。destPath为接收文件的路径，完整路径是fileStoragePath+destPath。
  };
  try {
    // 发送资源包
    gameNearbyTransfer.transferPackageData(packageData).then(() => {
      // 发送成功
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'nearby', `transferPackageData error Code: ${err.code}, message: ${err.message}`);
    });
  } catch (err) {
    let error = err as BusinessError;
    hilog.error(0x0000, 'nearby', `transferPackageData exception Code: ${error.code}, message: ${error.message}`);
  }
}
```

### 处理资源包传输进度信息

发送端和接收端在传输回调中处理传输进度信息，若传输异常，则需要调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)接口释放并清理资源。

```typescript
function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  if (callback.transferState === gameNearbyTransfer.TransferState.SEND_START ||
    callback.transferState === gameNearbyTransfer.TransferState.RECEIVE_START) {
    // 开始传输，按需处理
  }
  if (callback.transferState === gameNearbyTransfer.TransferState.SEND_PROCESS) {
    // 处理发送进度，如显示进度条和速率
  }
  if (callback.transferState === gameNearbyTransfer.TransferState.SEND_FINISH) {
    // 发送完成
  }
  if (callback.transferState === gameNearbyTransfer.TransferState.RECEIVE_PROCESS) {
    // 处理接收进度，如显示进度条和速率
  }
  if (callback.transferState === gameNearbyTransfer.TransferState.RECEIVE_FINISH) {
    // 接收完成，获取到资源包存储的沙箱路径
    let fileStoragePath = callback.fileStoragePath;
    if (fileStoragePath) {
      hilog.info(0x0000, 'nearby', `get transfer path: ${fileStoragePath}`);
      // 对fileStoragePath下的文件做处理，处理完成后调用destroy释放并清理资源
    }
  }
  if (callback.transferState === gameNearbyTransfer.TransferState.SEND_ERROR ||
    callback.transferState === gameNearbyTransfer.TransferState.RECEIVE_ERROR) {
    // 传输异常，需要调用destroy释放并清理资源
  }
}
```

### 处理已接收资源包后销毁服务

对已接收数据做好处理或转移后，调用[destroy](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferdestroy)接口销毁服务。若服务销毁后再次使用近场快传服务，需重新从[发送端注册相关回调](gameservice-nearbytransfer-resource-package.md#发送端注册相关回调)开始进行相关操作。

```typescript
public destroy() {
  // 取消回调注册
  this.unregisterCallback();
  // 销毁服务
  try {
    gameNearbyTransfer.destroy().then(() => {
      hilog.info(0x0000, 'nearby', `destroy success`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'nearby', `destroy failed. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, 'nearby', `destroy exception. Code: ${err.code}, message: ${err.message}`);
  }
}
public unregisterCallback() {
  try {
    gameNearbyTransfer.off('connectNotify', connectNotifyCallBack);
    gameNearbyTransfer.off('receivePackageInfo', receivePackageInfoCallBack);
    gameNearbyTransfer.off('transferNotify', transferNotifyCallBack);
    gameNearbyTransfer.off('error', errorCallBack);
  } catch (error) {
    let err = error as BusinessError;
    hilog.error(0x0000, 'nearby', `unregisterCallback error. Code: ${err.code}, message: ${err.message}`);
  }
}

function connectNotifyCallBack(callback: gameNearbyTransfer.ConnectNotification) {
  // 连接状态回调，接收端在此处调用sendPackageInfo接口发送自身文件信息，如版本信息、包信息
}

function receivePackageInfoCallBack(callback: gameNearbyTransfer.PackageInfo) {
  // 接收包信息回调，发送端收到接收端发送的版本信息后进行对比，根据对比结果决定是否需要传输资源包数据
}

function transferNotifyCallBack(callback: gameNearbyTransfer.TransferNotification) {
  // 传输回调，处理传输进度信息
}

function errorCallBack(callback: gameNearbyTransfer.ReturnResult) {
  // 异常信息回调，处理相关异常信息
}
```
