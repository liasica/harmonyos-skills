---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-6004
title: Connectivity Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta5引入的API > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:a27f5273323c5bffaffc570af990d351296ef22bc316660da21500a5f4d323ee
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：socket；  API声明：function getL2capPsm(serverSocket: number): number;  差异内容：function getL2capPsm(serverSocket: number): number; | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppType；  API声明：SPP\_L2CAP = 1  差异内容：SPP\_L2CAP = 1 | api/@ohos.bluetooth.socket.d.ts |
| 新增API | NA | 类名：SppType；  API声明：SPP\_L2CAP\_BLE = 2  差异内容：SPP\_L2CAP\_BLE = 2 | api/@ohos.bluetooth.socket.d.ts |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SppOptions；  API声明：psm?: number;  差异内容：psm?: number; | api/@ohos.bluetooth.socket.d.ts |
