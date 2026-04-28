---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/filemanagerservice-arkts-filemanagerservice
title: fileManagerService
breadcrumb: API参考 > 应用服务 > File Manager Service Kit（文件管理服务） > ArkTS API > fileManagerService
category: harmonyos-references
scraped_at: 2026-04-28T08:16:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58dea81a65be73278ac36630bc967da11173d7e6ca997a7b2980addff6e5c25b
---

fileManagerService模块提供删除文件到回收站、获取文件图标及解析文件快捷方式的能力。

**起始版本：** 5.0.5(17)

## 导入模块

PhonePC/2in1Tablet

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
```

## fileManagerService.deleteToTrash

PhonePC/2in1Tablet

deleteToTrash(uri: string): Promise<string>

以异步方法删除文件到回收站，返回删除后路径。使用Promise异步回调。

注意

此接口参数uri的具体使用方式参见用户文件uri介绍中的[文档类URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri)。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 待删除文件的uri |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 文件删除到回收站后的uri。使用Promise异步回调。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 1014000001 | Operation not permitted. |
| 1014000002 | No such file or directory. |
| 1014000003 | No space left on device. |
| 1014000004 | System inner fail. |

**示例代码：**

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. async function deleteFile() {
5. // 以内置存储目录为例
6. // 示例代码targetUri表示Download目录下文件
7. // 开发者应根据自己实际获取的uri进行开发，并确保对该文件有读写权限
8. let targetUri: string = "file://docs/storage/Users/currentUser/Download/1.txt";
9. try {
10. let trashUri: string = await fileManagerService.deleteToTrash(targetUri);
11. console.info("trashUri: " + trashUri);
12. } catch (err) {
13. let error: BusinessError = err as BusinessError;
14. console.error("delete failed, errCode:" + error.code + ", errMessage:" + error.message);
15. }
16. }
```

## fileManagerService.getFileIconSync

PhonePC/2in1Tablet

getFileIconSync(fileType: string): string | Resource

根据文件类型获取文件图标。

**需要权限**：ohos.permission.GET\_FILE\_ICON

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
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

**示例代码：**

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { uniformTypeDescriptor } from '@kit.ArkData';

5. @Entry
6. @Component
7. struct Index {
8. @State fileIcon: string | Resource = '';

10. private getFileIconByFileExtension(filenameExtension: string): void {
11. try {
12. let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
13. this.fileIcon = fileManagerService.getFileIconSync(typeId);
14. } catch (error) {
15. let err: BusinessError = error as BusinessError;
16. console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
17. }
18. }

20. build() {
21. RelativeContainer() {
22. Column() {
23. Image(this.fileIcon)
24. .height(88)
25. .border({ width: 1, radius: 6 })
26. Button('Update FileIcon')
27. .onClick(() => {
28. // 以txt格式为例
29. this.getFileIconByFileExtension('.txt');
30. })
31. }
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }
```

## fileManagerService.getFileIcon

PhonePC/2in1Tablet

getFileIcon(fileType: string): Promise<string | Resource>

根据文件类型获取文件图标。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_FILE\_ICON

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本：** 5.0.5(17)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileType | string | 是 | 文件类型对应的UTD-ID，详见[图标格式说明](filemanagerservice-iconformat.md) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string | [Resource](ts-types.md#resource)> | 文件图标的Base64编码或资源对象。使用Promise异步回调。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 1014000004 | System inner fail. |

**示例代码：**

```
1. import { fileManagerService } from '@kit.FileManagerServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { uniformTypeDescriptor } from '@kit.ArkData';

5. @Entry
6. @Component
7. struct Index {
8. @State fileIcon: string | Resource = '';

10. private getFileIconByFileExtension(filenameExtension: string): void {
11. try {
12. console.info('getFileIconByFileExtension');
13. let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
14. fileManagerService.getFileIcon(typeId).then((retIcon: string | Resource) => {
15. this.fileIcon = retIcon;
16. });
17. } catch (error) {
18. let err: BusinessError = error as BusinessError;
19. console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
20. }
21. }

23. build() {
24. RelativeContainer() {
25. Column() {
26. Image(this.fileIcon)
27. .height(88)
28. .border({ width: 1, radius: 6 })
29. Button('Update FileIcon')
30. .onClick(() => {
31. // 以txt格式为例
32. this.getFileIconByFileExtension('.txt');
33. })
34. }
35. }
36. .height('100%')
37. .width('100%')
38. }
39. }
```

## fileManagerService.parseShortcut

PhonePC/2in1Tablet

parseShortcut(linkUri: string): Promise<string>

根据快捷方式文件的URI解析出对应原文件的URI。使用Promise异步回调。

**系统能力**：SystemCapability.FileManagement.FileManagerService.Core

**起始版本**：6.1.0(23)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| linkUri | string | 是 | 快捷方式文件的URI，调用方对该文件需要有读权限。具体使用方式参见用户文件URI介绍中的[文档类URI的使用方式](../harmonyos-guides/user-file-uri-intro.md#文档类uri)，快捷方式文件URI的后缀必须为“.hlink”。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 对应原文件的URI。使用Promise异步回调。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](filemanagerservice-arkts-errorcode.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1014000002 | No such file or directory. |
| 1014000005 | Invalid shortcut file. |

**示例代码**：

```
1. import fileManagerService from '@hms.filemanagement.fileManagerService';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State linkUri: string = '';
8. @State parseResult: string = '';
9. private scroller: Scroller = new Scroller();

11. build() {
12. Stack() {
13. Column() {
14. List({ scroller: this.scroller }) {
15. ListItem() {
16. Column() {
17. Text("解析快捷方式")
18. .fontSize('30fp')
19. .fontWeight(FontWeight.Bold)
20. .margin({ top: 20 })
21. .alignRules({
22. center: { anchor: '__container__', align: VerticalAlign.Center },
23. middle: { anchor: '__container__', align: HorizontalAlign.Center }
24. })
25. TextInput({
26. placeholder: '请输入要解析快捷方式URI（例如：file://docs/storage/Users/currentUser/Documents/1.jpg.hlink）'
27. })
28. .width('90%')
29. .margin({ top: 20 })
30. .alignRules({
31. center: { anchor: '__container__', align: VerticalAlign.Center },
32. middle: { anchor: '__container__', align: HorizontalAlign.Center }
33. })
34. .onChange((value: string) => {
35. this.linkUri = value;
36. })
37. Button("解析快捷方式", { type: ButtonType.Normal })
38. .backgroundColor(0x317aff)
39. .width('90%')
40. .height(40)
41. .margin({ top: 20 })
42. .onClick(async () => {
43. const linkUri: string = this.linkUri;
44. let targetUri: string = '';
45. try {
46. targetUri = await fileManagerService.parseShortcut(linkUri);
47. console.info('parseShortcut success, linkUri:' + linkUri + ', targetUri:' + targetUri);
48. this.parseResult = '解析快捷方式成功，目标原文件URI：' + targetUri;
49. } catch (err) {
50. let error: BusinessError = err as BusinessError;
51. console.error('parseShortcut failed, errCode:' + error.code + ', errMessage:' + error.message);
52. this.parseResult = 'errCode:' + error.code + ', errMessage:' + error.message;
53. }
54. })
55. Row() {
56. Text('解析结果：')
57. .textAlign(TextAlign.Start)
58. .margin({ top: 20 })
59. .fontSize('25fp')
60. Text(this.parseResult)
61. .textAlign(TextAlign.Start)
62. .margin({ top: 20 })
63. .fontSize('25fp')
64. }
65. }
66. }
67. .width('100%')
68. }
69. .height('100%')
70. .width('100%')
71. .padding({left: 10, right: 10})
72. }
73. }
74. .align(Alignment.BottomEnd)
75. }
76. }
```
