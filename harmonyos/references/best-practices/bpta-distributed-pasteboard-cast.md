---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-distributed-pasteboard-cast
title: 跨设备剪贴板
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 跨设备剪贴板
category: best-practices
scraped_at: 2026-04-28T08:21:41+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:005d2fab9ad68e17a815976b0c6f57ed49755a712e3dabe55084e31a321fb161
---

剪贴板分为本地剪贴板和跨设备剪贴板，本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。

当用户拥有多台设备时，可以通过跨设备剪贴板的功能，在A设备的应用上复制一段文本，粘贴到B设备的应用中，高效地完成多设备间的内容共享。

当开发者正在开发一款浏览器类应用，或是备忘录、笔记、邮件等富文本编辑类应用时，均可接入跨设备剪贴板，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/YsxtzshkSfqKbckorIJiWA/zh-cn_image_0000002533352062.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=34007FC035323873D1EE97C5F074906EC0F04C95C4963299493730D27A4F0662 "点击放大")

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/mke0f-7STr2mP73UQR10Uw/zh-cn_image_0000002533512006.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=6A4809B2F41E3A0CD7E6D5B9151139DCE6BD0E86D9797C6C65A902727999AF6C "点击放大")

1. 用户在设备A复制数据。

2. 系统剪贴板服务将处理相关数据，并完成数据同步。此过程开发者不感知。

3. 用户在设备B粘贴来自设备A的数据。

## 约束与限制

| 设备版本 | 使用限制 |
| --- | --- |
| HarmonyOS NEXT Developer Preview0及以上 | * 双端设备需要打开跨设备剪贴板开关。 * 双端设备需要登录同一华为账号。 * 双端设备需要打开Wi-Fi和蓝牙开关。 * 双端设备在过程中需解锁、亮屏。 |

## 接口说明

在开发具体功能前，请先查阅[参考文档](../harmonyos-references/js-apis-pasteboard.md)，获取详细的接口说明。

| 接口 | 说明 |
| --- | --- |
| getSystemPasteboard(): SystemPasteboard | 获取系统剪贴板对象。 |
| createData(mimeType: string, value: ValueType): PasteData | 构建一个自定义类型的剪贴板内容对象。 |
| setData(data: PasteData): Promise<void> | 将数据写入系统剪贴板，使用Promise异步回调。 |
| getData(callback: AsyncCallback<PasteData>): void | 读取系统剪贴板内容，使用callback异步回调。  应用使用自定义控件后台访问剪贴板需要申请ohos.permission.READ\_PASTEBOARD。 |
| getRecordCount(): number | 获取剪贴板内容中条目的个数。 |
| getPrimaryMimeType(): string | 获取剪贴板内容中首个条目的数据类型。 |
| getPrimaryText(): string | 获取首个条目的纯文本内容。 |

## 开发示例

说明

跨设备复制的数据两分钟内有效。

* 设备A复制数据，写入到剪贴板服务。

  ```
  1. import pasteboard from '@ohos.pasteboard';
  2. import { BusinessError } from '@ohos.base';
  3. export async function setPasteDataTest(): Promise<void> {
  4. let text: string = 'hello world';
  5. let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, text);
  6. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  7. await systemPasteBoard.setData(pasteData).catch((err: BusinessError) => {
  8. console.error(`Failed to set pastedata. Code: ${err.code}, message: ${err.message}`);
  9. });
  10. }
  ```
* 设备B粘贴数据，读取剪贴板内容。

  ```
  1. import pasteboard from '@ohos.pasteboard';
  2. import { BusinessError } from '@ohos.base';
  3. // 设备B粘贴数据，读取剪贴板内容
  4. export async function getPasteDataTest(): Promise<void> {
  5. let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  6. systemPasteBoard.getData((err: BusinessError, data: pasteboard.PasteData) => {
  7. if (err) {
  8. console.error(`Failed to get pastedata. Code: ${err.code}, message: ${err.message}`);
  9. return;
  10. }
  11. // 对pastedata进行处理，获取类型，个数等
  12. let recordCount: number = data.getRecordCount(); // 获取剪贴板内record的个数
  13. let types: string = data.getPrimaryMimeType(); // 获取剪贴板内数据的类型
  14. let primaryText: string = data.getPrimaryText(); // 获取剪贴板内数据的内容
  15. });
  16. }
  ```
