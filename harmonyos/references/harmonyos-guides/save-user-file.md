---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/save-user-file
title: 保存用户文件
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 选择与保存用户文件 > 保存用户文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c87a2856b668542b032d19704e10a4fcad3c23407c31a725abd0e14e8f0b254
---

在从网络下载文件到本地或将已有用户文件另存为新的文件路径等场景下，需要使用FilePicker提供的保存用户文件的能力。需关注以下关键点：

**权限说明**

* 通过Picker获取的URI默认只具备**临时读写权限**，临时授权在应用退出后台自动失效。
* 如果设置[autoCreateEmptyFile](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)参数为false，获取的URI除了具备**临时读写权限**外，还具备**临时创建和删除权限**。
* 获取持久化权限需要通过[FilePicker设置永久授权](file-persistpermission.md#通过picker获取临时授权并进行授权持久化)方式获取。
* 使用Picker对音频、图片、视频、文档类文件的保存操作**无需申请权限**。

**系统隔离说明**

* 通过Picker保存的文件存储在用户指定的目录。此类文件与图库管理的资源隔离，无法在图库中看到。
* 若开发者需要保存图片、视频资源到图库，可使用用户无感的[安全控件进行保存](photoaccesshelper-savebutton.md#使用安全控件保存媒体库资源)。

## 保存图片或视频类文件

[PhotoViewPicker](../harmonyos-references/js-apis-file-picker.md#photoviewpickerdeprecated)在后续版本不再演进，建议使用[Media Library Kit（媒体文件管理服务）中能力来保存媒体库资源](photoaccesshelper-savebutton.md)。

如果开发场景无法调用安全控件进行图片、视频保存，可使用相册管理模块[PhotoAccessHelper.showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)接口进行保存操作。

## 保存文档类文件

1. 模块导入。

   ```
   1. import { picker } from '@kit.CoreFileKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 根据实际业务需求配置[文件保存选项](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)。以下代码仅例举各选项的配置参考。

   ```
   1. // 创建文件管理器选项实例。
   2. const documentSaveOptions = new picker.DocumentSaveOptions();
   3. // 保存文件名（可选）。 默认为空。
   4. documentSaveOptions.newFileNames = ["DocumentViewPicker01.txt"];
   5. // 指定保存的文件或者目录的URI（可选）。
   6. documentSaveOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
   7. // 保存文件类型['后缀类型描述|后缀类型'],选择所有文件：'所有文件(*.*)|.*'（可选） ，如果选择项存在多个后缀（最多限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
   8. documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];
   9. // 保存文件时，由应用决定是否预置空文件。默认为true，Picker会预置空文件并且返回文件的URI数组。false不预置空文件，只会返回文件的URI数组。
   10. documentSaveOptions.autoCreateEmptyFile = false;
   ```
3. 创建文件选择器[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#constructor12)实例。调用[save()](../harmonyos-references/js-apis-file-picker.md#save)接口拉起FilePicker界面进行文件保存。

   ```
   1. let uris: string[] = [];
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. const documentViewPicker = new picker.DocumentViewPicker(context);
   4. documentViewPicker.save(documentSaveOptions).then((documentSaveResult: string[]) => {
   5. uris = documentSaveResult;
   6. console.info('documentViewPicker.save to file succeed and uris are:' + uris);
   7. // ···
   8. }).catch((err: BusinessError) => {
   9. console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
   10. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/SavingUserFiles/entry/src/main/ets/pages/Index.ets#L136-L149)

   注意

   * Picker会默认[预置空文件](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)并返回保存文件的URI数组，应用拿到URI后可使用[文件管理](../harmonyos-references/js-apis-file-fs.md)模块的接口进行文件读写操作。
   * 避免在Picker回调中直接操作URI。
   * 建议使用全局变量保存URI以供后续使用。
   * 可以通过[DOWNLOAD模式](save-user-file.md#download模式保存文件)直达下载目录。
4. 待界面从FilePicker返回后，使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口，通过URI打开这个文件得到文件描述符（fd）。

   ```
   1. if (uris.length > 0) {
   2. let uri: string = uris[0];
   3. // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   4. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   5. console.info('file fd: ' + file.fd);
   6. }
   ```
5. 通过（fd）使用[fileIo.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)接口对这个文件进行编辑修改，编辑修改完成后关闭（fd）。

   ```
   1. let writeLen: number = fileIo.writeSync(file.fd, 'hello, world');
   2. console.info('write data to file succeed and size is:' + writeLen);
   3. fileIo.closeSync(file);
   ```

## 保存音频类文件

1. 模块导入。

   ```
   1. import { picker } from '@kit.CoreFileKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 配置保存选项。

   ```
   1. const audioSaveOptions = new picker.AudioSaveOptions();
   2. // 保存文件名（可选）
   3. audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
   ```
3. 创建[音频选择器AudioViewPicker](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)实例。调用[save()](../harmonyos-references/js-apis-file-picker.md#save-5)接口拉起FilePicker界面进行文件保存。

   ```
   1. let uris: string[] = [];
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. const audioViewPicker = new picker.AudioViewPicker(context);
   4. audioViewPicker.save(audioSaveOptions).then((audioSelectResult: string[]) => {
   5. uris = audioSelectResult;
   6. console.info('audioViewPicker.save to file succeed and uri is:' + uris);
   7. // ···
   8. }).catch((err: BusinessError) => {
   9. console.error(`Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
   10. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/SavingUserFiles/entry/src/main/ets/pages/Index.ets#L218-L231)

   注意

   * Picker会默认[预置空文件](../harmonyos-references/js-apis-file-picker.md#documentsaveoptions)并返回保存文件的URI数组，应用拿到URI后可使用[文件管理](../harmonyos-references/js-apis-file-fs.md)模块的接口进行文件读写操作。
   * 避免在Picker回调中直接操作URI。
   * 建议使用全局变量保存URI以供后续使用。
   * 可以通过[DOWNLOAD模式](save-user-file.md#download模式保存文件)直达下载目录。
4. 待界面从FilePicker返回后，可以使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口，通过URI打开这个文件得到文件描述符（fd）。

   ```
   1. if (uris.length > 0) {
   2. let uri: string = uris[0];
   3. // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   4. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   5. console.info('file fd: ' + file.fd);
   6. }
   ```
5. 通过（fd）使用[fileIo.writeSync](../harmonyos-references/js-apis-file-fs.md#fileiowritesync)接口对这个文件进行编辑修改，编辑修改完成后关闭（fd）。

   ```
   1. let writeLen = fileIo.writeSync(file.fd, 'hello, world');
   2. console.info('write data to file succeed and size is:' + writeLen);
   3. fileIo.closeSync(file);
   ```

## DOWNLOAD模式保存文件

**模式特点**

* 自动创建在Download/包名/目录。
* 跳过文件选择界面直接保存。
* 返回的URI已具备持久化权限， 用户可在该URI下创建文件。

注意

DOWNLOAD模式创建的目录仅用于保存文件，目录之间无访问隔离，不建议保存应用敏感数据。

1. 模块导入。

   ```
   1. import { fileUri, picker } from '@kit.CoreFileKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 配置下载模式。

   ```
   1. const documentSaveOptions = new picker.DocumentSaveOptions();
   2. // 配置保存的模式为DOWNLOAD，若配置了DOWNLOAD模式，此时配置的其他documentSaveOptions参数将不会生效。
   3. documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
   ```
3. 保存到下载目录。

   ```
   1. let uri: string = '';
   2. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
   3. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   4. const documentViewPicker = new picker.DocumentViewPicker(context);
   5. const documentSaveOptions = new picker.DocumentSaveOptions();
   6. documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
   7. documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
   8. uri = documentSaveResult[0];
   9. console.info('documentViewPicker.save succeed and uri is:' + uri);
   10. const testFilePath = new fileUri.FileUri(uri + '/test.txt').path;
   11. const file = fileIo.openSync(testFilePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
   12. fileIo.writeSync(file.fd, 'Hello World!');
   13. fileIo.closeSync(file.fd);
   14. }).catch((err: BusinessError) => {
   15. console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
   16. })
   ```
