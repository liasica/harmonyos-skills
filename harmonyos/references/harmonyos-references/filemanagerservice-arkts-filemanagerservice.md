---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice
title: fileManagerService
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > ArkTS API > fileManagerService
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95aac0d490b3bf60a6c56640ef8f52b7f71ba3be39b38b02003d7eb65ee8bf46
---

fileManagerService模块提供删除文件到回收站、获取文件图标及解析文件快捷方式的能力。

**起始版本：** 5.0.5(17)

## 导入模块

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
```

## fileManagerService.deleteToTrash

deleteToTrash(uri: string): Promise<string>

以异步方法删除文件到回收站，返回删除后路径。使用Promise异步回调。

**注意** 

此接口参数uri的具体使用方式参见用户文件uri介绍中的[文档类URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri)。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待删除文件的uri |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回文件删除到回收站后的uri。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. |
| 1014000001 | Operation not permitted. |
| 1014000002 | No such file or directory. |
| 1014000003 | No space left on device. |
| 1014000004 | System inner fail. |

**示例代码：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function deleteFile() {
  // 以内置存储目录为例
  // 示例代码targetUri表示Download目录下文件
  // 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
  let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
  try {
    let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
    console.info("trashUri: " + trashUri);
  } catch (err) {
    let error: BusinessError = err as BusinessError;
    console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
  }
}
```

## fileManagerService.getFileIconSync

getFileIconSync(fileType: string): string | Resource

根据文件类型获取文件图标。

**需要权限**：ohos.permission.GET\_FILE\_ICON

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileType | string | 是 | 文件类型对应的UTD-ID，详见[图标格式说明](filemanagerservice-iconformat.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | [Resource](ts-types.md#resource) | 文件图标的Base64编码或资源对象 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-universal.md#section201-权限校验失败) | Permission denied. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

**示例代码：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      // 1、根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 2、调用getFileIconSync方法，根据UTD-ID获取对应的文件图标
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

## fileManagerService.getFileIcon

getFileIcon(fileType: string): Promise<string | Resource>

根据文件类型获取文件图标。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_FILE\_ICON

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileType | string | 是 | 文件类型对应的UTD-ID，详见[图标格式说明](filemanagerservice-iconformat.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string | [Resource](ts-types.md#resource)> | Promise对象，返回文件图标的Base64编码或资源对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](errorcode-universal.md#section201-权限校验失败) | Permission denied. |
| [401](errorcode-universal.md#section401-参数检查失败) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

**示例代码：**

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      console.info('getFileIconByFileExtension');
      // 1、根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 2、调用getFileIcon方法，根据UTD-ID获取对应的文件图标
      fileManagerService.getFileIcon(typeId).then((retIcon: string | Resource) => {
        this.fileIcon = retIcon;
      });
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

## fileManagerService.parseShortcut

parseShortcut(linkUri: string): Promise<string>

根据快捷方式文件的URI解析出对应原文件的URI。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本**：6.1.0(23)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| linkUri | string | 是 | 快捷方式文件的URI，调用方对该文件需要有读权限。具体使用方式参见用户文件URI介绍中的[文档类URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri)，快捷方式文件URI的后缀必须为“.hlink”。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回对应原文件的URI。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1014000002 | No such file or directory. |
| 1014000005 | Invalid shortcut file. |

**示例代码**：

```typescript
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State linkUri: string = '';
  @State parseResult: string = '';
  private scroller: Scroller = new Scroller();

  build() {
    Stack() {
      Column() {
        List({ scroller: this.scroller }) {
          ListItem() {
            Column() {
              Text("解析快捷方式")
                .fontSize('30fp')
                .fontWeight(FontWeight.Bold)
                .margin({ top: 20 })
                .alignRules({
                  center: { anchor: '__container__', align: VerticalAlign.Center },
                  middle: { anchor: '__container__', align: HorizontalAlign.Center }
                })
              TextInput({
                placeholder: '请输入要解析快捷方式URI（例如：file://docs/storage/Users/currentUser/Documents/1.jpg.hlink）'
              })
                .width('90%')
                .margin({ top: 20 })
                .alignRules({
                  center: { anchor: '__container__', align: VerticalAlign.Center },
                  middle: { anchor: '__container__', align: HorizontalAlign.Center }
                })
                .onChange((value: string) => {
                  this.linkUri = value;
                })
              Button("解析快捷方式", { type: ButtonType.Normal })
                .backgroundColor(0x317aff)
                .width('90%')
                .height(40)
                .margin({ top: 20 })
                .onClick(async () => {
                  const linkUri: string = this.linkUri;
                  let targetUri: string = '';
                  try {
                    targetUri = await fileManagerService.parseShortcut(linkUri);
                    console.info('parseShortcut success, linkUri:' + linkUri + ', targetUri:' + targetUri);
                    this.parseResult = '解析快捷方式成功，目标原文件URI：' + targetUri;
                  } catch (err) {
                    let error: BusinessError = err as BusinessError;
                    console.error('parseShortcut failed, errCode:' + error.code + ', errMessage:' + error.message);
                    this.parseResult = 'errCode:' + error.code + ', errMessage:' + error.message;
                  }
                })
              Row() {
                Text('解析结果：')
                  .textAlign(TextAlign.Start)
                  .margin({ top: 20 })
                  .fontSize('25fp')
                Text(this.parseResult)
                  .textAlign(TextAlign.Start)
                  .margin({ top: 20 })
                  .fontSize('25fp')
              }
            }
          }
          .width('100%')
        }
        .height('100%')
        .width('100%')
        .padding({left: 10, right: 10})
      }
    }
    .align(Alignment.BottomEnd)
  }
}
```
