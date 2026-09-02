---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-12
title: 如何分享用户目录文件
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 如何分享用户目录文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:49+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5f10581d2b3d25af36959f045495a9a6c8b4bf8202e1e8cb8a892a3447a169e7
---

## 问题现象

使用[选择器](../harmonyos-references/js-apis-file-picker.md)[保存用户文件](../harmonyos-guides/save-user-file.md)获得URI，通过URI写入文本内容生成文件。[系统分享](../harmonyos-guides/system-share-overview.md)分享此文件URI，无法拉起面板分享文件，应该如何正确分享用户目录下的文件？

## 背景知识

* [通过分享面板发起分享](../harmonyos-guides/share-mobilephone-app-share.md)：宿主应用构造分享数据、构造[ShareController](../harmonyos-references/share-system-share.md#sharecontroller)以及注册分享面板状态监听。
* [授权持久化](../harmonyos-guides/file-persistpermission.md)：应用通过Picker获取临时授权，临时授权在应用退出后或者设备重启后会清除。如果应用重启或者设备重启后需要直接访问之前已访问过的文件，则对文件进行持久化授权。

## 解决方案

无法拉起面板分享文件的原因是，应用通过Picker获取URI仅有临时授权，无法进行分享，需要对文件使用[fileShare.persistPermission](../harmonyos-references/js-apis-fileshare.md#filesharepersistpermission11)进行持久化授权。

步骤一：申请[ohos.permission.FILE\_ACCESS\_PERSIST](../harmonyos-guides/restricted-permissions.md#ohospermissionfile_access_persist)受限权限，参考步骤[申请受限开放权限](../harmonyos-guides/restricted-permissions.md)。

步骤二：使用fileShare.persistPermission获取授权持久化权限的URI，再通过ShareController拉起分享面板。

```ts
import { common } from '@kit.AbilityKit';
import { systemShare } from '@kit.ShareKit';
import { fileShare, picker } from '@kit.CoreFileKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {

  private async shareUserFile(): Promise<void> {
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    // 创建文件管理器选项实例
    const documentSelectOptions = new picker.DocumentSelectOptions();
    // 创建文件选择器实例。
    const documentViewPicker = new picker.DocumentViewPicker(context);
    // 用户选择目标文件夹，用户选择与文件类型相对应的文件夹，即可完成文件保存操作。保存成功后，返回保存文档的URI。
    let uri = (await documentViewPicker.select(documentSelectOptions))[0];

    if (canIUse('SystemCapability.FileManagement.AppFileService.FolderAuthorization')) {
      let policies: Array<fileShare.PolicyInfo> = [{
        uri: uri,
        operationMode: fileShare.OperationMode.READ_MODE,
      }];
      fileShare.persistPermission(policies).then(() => {
        console.info('persistPermission successfully');
        let data: systemShare.SharedData = new systemShare.SharedData({
          utd: uniformTypeDescriptor.UniformDataType.TEXT,
          uri: uri
        });
        // 构建ShareController
        let controller: systemShare.ShareController = new systemShare.ShareController(data);
        // 注册分享面板关闭监听
        controller.on('dismiss', () => {
          console.info('Share panel closed');
          // 分享结束，可处理其他业务。
        });
        console.info('Start  controller.show');
        controller.show(context, {
          previewMode: systemShare.SharePreviewMode.DETAIL,
          selectionMode: systemShare.SelectionMode.SINGLE
        });
      }).catch((err: BusinessError<Array<fileShare.PolicyErrorResult>>) => {
        console.error(`persistPermission failed with error message:  ${err.message} , error code: ${err.code}`);
      });
    }
  }

  build() {
    RelativeContainer() {
      Text('选择文件分享')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.shareUserFile();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
