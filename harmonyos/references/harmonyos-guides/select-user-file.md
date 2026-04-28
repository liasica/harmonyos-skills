---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/select-user-file
title: 选择用户文件
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 用户文件 > 选择与保存用户文件 > 选择用户文件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e4f77f46679ff07ce1a84696bb8d441aeb6925171024756abca17e260f544da
---

用户需要分享文件、保存图片、视频等用户文件时，开发者可以通过系统预置的[文件选择器（FilePicker）](../harmonyos-references/js-apis-file-picker.md)，实现该能力。通过Picker访问相关文件，将拉起对应的应用，引导用户完成界面操作，接口本身无需申请权限。Picker选择文件或文件夹获取到的URI只具有**临时读写权限**，获取持久化权限需要通过[FilePicker设置永久授权](file-persistpermission.md#通过picker获取临时授权并进行授权持久化)方式获取。

根据用户文件的常见类型，选择器（FilePicker）分别提供以下选项：

* [PhotoViewPicker](../harmonyos-references/js-apis-file-picker.md#photoviewpickerdeprecated)：适用于图片或视频类型文件的选择与保存（该接口在后续版本不再演进）。请使用PhotoAccessHelper的[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)来选择图片文件。请使用[安全控件保存媒体库资源](photoaccesshelper-savebutton.md)。
* [DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)：适用于文件类型文件的选择与保存。DocumentViewPicker对接的选择资源来自于FilePicker，负责文件类型的资源管理，文件类型不区分后缀，比如浏览器下载的图片、文档等，都属于文件类型。
* [AudioViewPicker](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)：适用于音频类型文件的选择与保存。AudioViewPicker目前对接的选择资源来自于AudioPicker。

## 选择图片或视频类文件

[PhotoViewPicker](../harmonyos-references/js-apis-file-picker.md#photoviewpickerdeprecated)在后续版本不再演进，请使用PhotoAccessHelper的[PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)来选择图片文件。

## 选择文档类文件

1. 导入选择器模块和文件管理模块。

   ```
   1. import  { picker } from '@kit.CoreFileKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 需根据实际业务需求配置[文档选择选项](../harmonyos-references/js-apis-file-picker.md#documentselectoptions)。以下代码仅例举各选项的配置参考。

   ```
   1. const documentSelectOptions = new picker.DocumentSelectOptions();
   2. // 选择文件最大个数（可选）。API version 20及之前的版本，单次文件选择的最大数量上限为500个，默认值也为500。目录选择功能仅对具备该系统能力的设备开放，且单次最多可选择1个目录。API version 21及之后的版本取消文件选择数量的限制。受系统能力限制，选择文件数量过大可能会出现功能异常或处理性能较差等情况，建议单次选择文件个数不超过1万个。API version 23及之后的版本取消目录选择数量的限制。
   3. documentSelectOptions.maxSelectNumber = 5;
   4. // 指定选择的文件或者目录的URI（可选）。
   5. documentSelectOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
   6. // 选择的文档类型，默认值是FILE(文件类型)。该参数在2in1设备中可正常使用，在其他设备中无效果。
   7. documentSelectOptions.selectMode = picker.DocumentSelectMode.FILE;
   8. // 选择文件的后缀类型['后缀类型描述|后缀类型']（可选，不传该参数，默认不过滤，即显示所有文件），若选择项存在多个后缀名，则每一个后缀名之间用英文逗号进行分隔（可选），后缀类型名不能超过100。此外2in1设备支持通配符方式['所有文件(*.*)|.*']（说明：从API version 17开始，手机支持该配置），表示为显示所有文件。
   9. documentSelectOptions.fileSuffixFilters = ['图片(.png, .jpg)|.png,.jpg', '文档|.txt', '视频|.mp4', '.pdf'];
   10. // 选择是否对指定文件或目录授权，true为授权，当为true时，defaultFilePathUri为必选参数，拉起文管授权界面；false为非授权(默认为false)，拉起常规文管界面（可选）。该参数在2in1设备中可正常使用，在其他设备中无效果。
   11. documentSelectOptions.authMode = false;
   12. // 批量授权模式，默认为false（非批量授权模式）。当multiAuthMode为true时为批量授权模式。当multiAuthMode为true时，只有multiUriArray参数生效，其他参数不生效。该参数在Phone设备中可正常使用，在其他设备中无效果。
   13. documentSelectOptions.multiAuthMode = false;
   14. // 需要传入批量授权的uri数组（仅支持文件，文件夹不生效）。配合multiAuthMode使用。当multiAuthMode为false时，配置该参数不生效。该参数在Phone设备中可正常使用，在其他设备中无效果。
   15. documentSelectOptions.multiUriArray = ["file://docs/storage/Users/currentUser/test", "file://docs/storage/Users/currentUser/2test"];
   16. // 开启聚合视图模式，支持拉起文件管理应用的聚合视图。默认为DEFAULT，表示该参数不生效，非聚合视图。当该参数置为非DEFAULT时，其他参数不生效。
   17. // 该参数在Phone设备中可正常使用，在其他设备中无效果。
   18. documentSelectOptions.mergeMode = picker.MergeTypeMode.DEFAULT;
   19. // 是否支持加密（仅支持文件，文件夹不生效），默认为false。该参数为true时，在Picker界面可以选择对文件进行加密。（说明：从API version 19开始支持该参数）。
   20. documentSelectOptions.isEncryptionSupported = false;
   ```
3. 创建文件选择器[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)实例。调用[select()](../harmonyos-references/js-apis-file-picker.md#select-3)接口拉起FilePicker应用界面进行文件选择。

   ```
   1. let uris: string[] = [];
   2. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   3. const documentViewPicker = new picker.DocumentViewPicker(context);
   4. documentViewPicker.select(documentSelectOptions).then((documentSelectResult: string[]) => {
   5. uris = documentSelectResult;
   6. console.info('documentViewPicker.select to file succeed and uris are:' + uris);
   7. // ...
   8. }).catch((err: BusinessError) => {
   9. console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
   10. });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/SelectingUserFiles/entry/src/main/ets/pages/Index.ets#L135-L150)

   注意

   1. 使用Picker获取的[select()](../harmonyos-references/js-apis-file-picker.md#select-3)返回的URI权限是临时只读权限，待退出应用后台后，获取的临时权限就会失效。
   2. 如果想要获取持久化权限，请参考[文件持久化授权访问](file-persistpermission.md#通过picker获取临时授权并进行授权持久化)。
   3. 开发者可以根据结果集中URI做进一步的处理。建议定义一个全局变量保存URI。
   4. 如有获取元数据需求，可以通过[文件管理](../harmonyos-references/js-apis-file-fs.md)和[文件URI](../harmonyos-references/js-apis-file-fileuri.md)根据URI获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。
4. 待界面从FilePicker返回后，使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口通过URI打开这个文件得到文件描述符（fd）。

   ```
   1. if (uris.length > 0) {
   2. let uri: string = uris[0];
   3. // 这里需要注意接口权限参数是fileIo.OpenMode.READ_ONLY。
   4. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
   5. console.info('file fd: ' + file.fd);
   6. }
   ```
5. 通过fd使用[fileIo.readSync](../harmonyos-references/js-apis-file-fs.md#fileioreadsync)接口读取这个文件内的数据。

   ```
   1. let buffer = new ArrayBuffer(4096);
   2. let readLen = fileIo.readSync(file.fd, buffer);
   3. console.info('readSync data to file succeed and buffer size is:' + readLen);
   4. // 读取完成后关闭fd。
   5. fileIo.closeSync(file);
   ```

## 选择音频类文件

1. 导入选择器模块和文件管理模块。

   ```
   1. import  { picker } from '@kit.CoreFileKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { common } from '@kit.AbilityKit';
   ```
2. 创建音频类型文件选择选项实例。

   说明

   目前AudioSelectOptions不支持参数配置，默认可以选择所有类型的用户文件。

   ```
   1. const audioSelectOptions = new picker.AudioSelectOptions();
   ```
3. 创建音频选择器[AudioViewPicker](../harmonyos-references/js-apis-file-picker.md#audioviewpicker)实例。调用[select()](../harmonyos-references/js-apis-file-picker.md#select-5)接口拉起AudioPicker应用界面进行文件选择。

   ```
   1. let uris: string[] = [];
   2. // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
   3. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   4. const audioViewPicker = new picker.AudioViewPicker(context);
   5. audioViewPicker.select(audioSelectOptions).then((audioSelectResult: Array<string>) => {
   6. // 文件选择成功后，返回被选中音频的URI结果集。
   7. uris = audioSelectResult;
   8. console.info('audioViewPicker.select to file succeed and uri is:' + uris);
   9. // ...
   10. }).catch((err: BusinessError) => {
   11. console.error(`Invoke audioViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
   12. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/UserFile/SelectingUserFiles/entry/src/main/ets/pages/Index.ets#L187-L196)

   注意

   1. 使用Picker获取的[select()](../harmonyos-references/js-apis-file-picker.md#select-3)返回的URI权限是临时只读权限，待退出应用后台后，获取的临时权限就会失效。
   2. 如果想要获取持久化权限，请参考[文件持久化授权访问](file-persistpermission.md#通过picker获取临时授权并进行授权持久化)。
   3. 开发者可以根据结果集中的URI做读取文件数据操作。建议定义一个全局变量保存URI。例如通过[文件管理](../harmonyos-references/js-apis-file-fs.md)模块的接口根据URI拿到音频资源的文件描述符（fd），再配合媒体服务实现音频播放的开发，具体请参考[音频播放开发指导](audio-playback-overview.md)。
4. 待界面从AudioPicker返回后，可以使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口通过URI打开这个文件得到文件描述符（fd）。

   ```
   1. if (uris.length > 0) {
   2. let uri: string = uris[0];
   3. // 这里需要注意接口权限参数是fileIo.OpenMode.READ_ONLY。
   4. let file = fileIo.openSync(uri, fileIo.OpenMode.READ_ONLY);
   5. console.info('file fd: ' + file.fd);
   6. }
   ```
5. 通过fd可以使用[fileIo.readSync](../harmonyos-references/js-apis-file-fs.md#readsync)接口读取这个文件内的数据。

   ```
   1. let buffer = new ArrayBuffer(4096);
   2. let readLen = fileIo.readSync(file.fd, buffer);
   3. console.info('readSync data to file succeed and buffer size is:' + readLen);
   4. // 读取完成后关闭fd。
   5. fileIo.closeSync(file);
   ```

## 示例代码

* [选择并查看文档与媒体文件](https://gitcode.com/HarmonyOS_Samples/picker)
