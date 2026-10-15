---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-distributed-pasteboard-cast
title: 跨设备剪贴板
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 跨设备剪贴板
category: best-practices
scraped_at: 2026-10-16T07:06:42+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:38784eb0723d78ee516f373da954ab7defdb128d31744c2c3825c8c4d4d90f9a
---

剪贴板分为本地剪贴板和跨设备剪贴板，本地剪贴板提供设备内的内容复制粘贴，跨设备剪贴板提供跨设备的内容复制粘贴。

当用户拥有多台设备时，可以通过跨设备剪贴板的功能，在A设备的应用上复制一段文本，粘贴到B设备的应用中，高效地完成多设备间的内容共享。

当开发者正在开发一款浏览器类应用，或是备忘录、笔记、邮件等富文本编辑类应用时，均可接入跨设备剪贴板，提升用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Psny_oDvSyCmVWdmfbCksA/zh-cn_image_0000002757092113.gif "点击放大")

## 运作机制

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/L-6yyh-OTZmWY-GEzQ7fWA/zh-cn_image_0000002563685436.png "点击放大")

1. 用户在设备A复制数据。

2. 系统剪贴板服务将处理相关数据，并完成数据同步。此过程开发者不感知。

3. 用户在设备B粘贴来自设备A的数据。

## 约束与限制

| 设备版本 | 使用限制 |
| --- | --- |
| HarmonyOS NEXT Developer Preview 0及以上 | * 双端设备需要打开跨设备剪贴板开关。 * 双端设备需要登录同一华为账号。 * 双端设备需要打开Wi-Fi和蓝牙开关。 * 双端设备在过程中需解锁、亮屏。 |

## 接口说明

在开发具体功能前，请先查阅参考文档[@ohos.pasteboard (剪贴板)](../harmonyos-references/js-apis-pasteboard.md)，获取详细的接口说明。

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

**说明** 

跨设备复制的数据两分钟内有效。

* 设备A复制数据，写入到剪贴板服务。

  ```screen
  let pasteData: pasteboard.PasteData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_URI, 'PageABuilder');
  let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
  await systemPasteboard.setData(pasteData);
  ```
* 设备B粘贴数据，读取剪贴板内容。

  ```screen
  PasteButton()
  // ...
    .onClick(async (_event: ClickEvent, result: PasteButtonOnClickResult) => {
      if (result === PasteButtonOnClickResult.SUCCESS) {
        try {
          // ...
          let systemPasteBoard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
          let gettedData = await systemPasteBoard.getData();
          if (gettedData.getRecordCount() <= 0) {
            return;
          }

          let isPastedSuccess: boolean = false;
          for (let i = 0; i < gettedData.getRecordCount(); i++) {
            let record = gettedData.getRecord(i);
            let targetTypes: string[] = [
              pasteboard.MIMETYPE_TEXT_HTML,
              pasteboard.MIMETYPE_TEXT_PLAIN,
              pasteboard.MIMETYPE_PIXELMAP
            ];
            let tmpTypes: string[] = record.getValidTypes(targetTypes);
            for (let j = 0; j < tmpTypes.length; j++) {
              switch (tmpTypes[j]) {
                case pasteboard.MIMETYPE_TEXT_HTML: {
                  let htmlRecord = await record.getData(pasteboard.MIMETYPE_TEXT_HTML);
                  htmlRecord = htmlRecord as string;
                  this.handlerPasteHtmlData(htmlRecord);
                  isPastedSuccess = true;
                  break;
                }
                case pasteboard.MIMETYPE_TEXT_PLAIN: {
                  let textRecord = await record.getData(pasteboard.MIMETYPE_TEXT_PLAIN);
                  textRecord = textRecord as string;
                  let styledString = new StyledString(textRecord);
                  this.pasteTextController.setStyledString(styledString);
                  isPastedSuccess = true;
                  break;
                }
                case pasteboard.MIMETYPE_PIXELMAP: {
                  let pixelMapRecord = await record.getData(pasteboard.MIMETYPE_PIXELMAP);
                  pixelMapRecord = pixelMapRecord as PixelMap;
                  this.pastePixelMapController.deleteSpans();
                  this.pastePixelMapController.addImageSpan(pixelMapRecord, {
                    imageStyle: {
                      size: ['57px', '57px']
                    }
                  });
                  isPastedSuccess = true;
                  break;
                }
                default:
                  break;
              }
            }
          }
          // ...
        } catch {
          (err: BusinessError) => {
            hilog.error(0x0000, '[PasteBoard]', `getData error.code: ${err.code}, message: ${err.message}`);
          }
        }
      }
    })
  ```
