---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-driverdevelopmentkit-b035
title: Driver Development Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > API变更清单 > HarmonyOS NEXT Developer Beta3引入的API > Driver Development Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:29+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:1fbb45731128a390b373b92b5da1621c6229fbb30a0a6fe48c818c3fb0dcd818
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 错误码变更 | 类名：deviceManager；  API声明：function queryDevices(busType?: number): Array<Readonly<Device>>;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function queryDevices(busType?: number): Array<Readonly<Device>>;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{  deviceId: number;  remote: rpc.IRemoteObject;  }>): void;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{  deviceId: number;  remote: rpc.IRemoteObject;  }>;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number, callback: AsyncCallback<number>): void;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
| 错误码变更 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number): Promise<number>;  差异内容：22900001,401 | 类名：deviceManager；  API声明：function unbindDevice(deviceId: number): Promise<number>;  差异内容：201,22900001,401 | api/@ohos.driver.deviceManager.d.ts |
