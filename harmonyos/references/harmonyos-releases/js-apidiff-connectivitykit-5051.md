---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-connectivitykit-5051
title: Connectivity Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > API变更清单 > Connectivity Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:76f840056ad38f046ca42947f255a6b433003c46d249dd0687c3f4bb362d576c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：socket；  API声明：function getDeviceId(clientSocket: number): string;  差异内容：function getDeviceId(clientSocket: number): string; | api/@ohos.bluetooth.socket.d.ts |
| 删除API | 类名：opp；  API声明：function createOppServerProfile(): OppServerProfile;  差异内容：function createOppServerProfile(): OppServerProfile; | NA | api/@ohos.bluetooth.opp.d.ts |
| 起始版本有变化 | 类名：global；  API声明：declare namespace opp  差异内容：15 | 类名：global；  API声明：declare namespace opp  差异内容：16 | api/@ohos.bluetooth.opp.d.ts |
| 起始版本有变化 | 类名：opp；  API声明：interface OppServerProfile  差异内容：15 | 类名：opp；  API声明：interface OppServerProfile  差异内容：16 | api/@ohos.bluetooth.opp.d.ts |
