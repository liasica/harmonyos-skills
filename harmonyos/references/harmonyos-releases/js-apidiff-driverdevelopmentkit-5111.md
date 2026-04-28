---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-driverdevelopmentkit-5111
title: Driver Development Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > API变更清单 > 5.1.1(19) Beta1引入的API > Driver Development Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:53+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e48667d61aefc6a6862a406e9a7347d2370dfa523cf460cbde4a8b617b3a7c3a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void;  差异内容：NA | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>;  差异内容：NA | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void;  差异内容：NA | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;  差异内容：NA | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void;  差异内容：NA | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| API废弃版本变更 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number): Promise<number>;  差异内容：NA | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number): Promise<number>;  差异内容：19 | api/@ohos.driver.deviceManager.d.ts |
| 新增API | NA | 类名：deviceManager；  API声明：function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;  差异内容：function bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>; | api/@ohos.driver.deviceManager.d.ts |
| 新增API | NA | 类名：deviceManager；  API声明：function unbindDriverWithDeviceId(deviceId: number): Promise<number>;  差异内容：function unbindDriverWithDeviceId(deviceId: number): Promise<number>; | api/@ohos.driver.deviceManager.d.ts |
