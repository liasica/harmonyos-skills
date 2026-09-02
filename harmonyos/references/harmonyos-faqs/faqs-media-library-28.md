---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-28
title: 如何通过安全控件、弹窗授权实现媒体资源保存
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > 如何通过安全控件、弹窗授权实现媒体资源保存
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:6bcb3d289b986accb211b5df0c06955f8932e72f96abe264c5d67f8a4eef79bf
---

## 问题现象

当应用不符合ohos.permission.WRITE\_IMAGEVIDEO权限的使用场景时，如何在无权限的情况下保存图片和视频到相册？

## 背景知识

[ohos.permission.WRITE\_IMAGEVIDEO](../harmonyos-guides/restricted-permissions.md#ohospermissionwrite_imagevideo)是受限开放的权限，在不满足权限申请条件的情况下，应用可以通过安全控件或授权弹窗的方式，将指定的媒体资源保存到相册中。

* 安全控件（[SaveButton](../harmonyos-references/ts-security-components-savebutton.md#savebutton-1)）：安全控件的保存控件，用户通过点击该保存按钮，可以临时获取存储权限，而不需要权限弹窗授权确认。使用此控件需要UI样式合法，不合法会导致授权失败，可参考安全控件样式的[约束与限制](../harmonyos-guides/savebutton.md#约束与限制)。
* 授权弹窗（[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)）：通过调用接口拉起保存确认弹窗，基于弹窗授权的方式获取的目标媒体文件uri。用户同意保存后，返回已创建并授予保存权限的uri列表，该列表永久生效，应用可使用该uri写入图片/视频。如果用户拒绝保存，将返回空列表。

## 解决方案

* 方式一：安全控件[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)可以临时获取存储权限，而不需要权限弹窗授权确认，最终把图片保存到相册。参考代码：

  ```ts
  import photoAccessHelper from '@ohos.file.photoAccessHelper';
  import fs from '@ohos.file.fs';
  import { common } from '@kit.AbilityKit';
  import { UIContext } from '@kit.ArkUI';

  @Entry
  @Component
  struct saveButtonMethod {
    uiContext: UIContext = this.getUIContext();

    build() {
      Row() {
        Column() {
          SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.SAVE })
            .onClick(async (_event: ClickEvent, result: SaveButtonOnClickResult) => {
              if (result === SaveButtonOnClickResult.SUCCESS) {
                try {
                  let context: Context = this.uiContext.getHostContext() as common.UIAbilityContext;
                  let helper = photoAccessHelper.getPhotoAccessHelper(context);
                  // onClick触发后一分钟内通过createAsset接口创建图片文件，一分钟后createAsset权限收回。
                  let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg');
                  // 使用uri打开文件，可以持续写入内容，写入过程不受时间限制
                  let file = await fs.open(uri, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                  try {
                    context.resourceManager.getMediaContent($r('app.media.startIcon').id, 0)
                      .then(async value => {
                        let media = value.buffer;
                        // 写到媒体库文件中
                        await fs.write(file.fd, media);
                        await fs.close(file.fd);
                        this.uiContext.showAlertDialog({ message: '已保存至相册!' });
                      });
                  } catch (err) {
                    console.error(`error is ${err}`);
                  }
                } catch (error) {
                  console.error(`error is ${error}`);
                }
              } else {
                this.uiContext.showAlertDialog({ message: '设置权限失败' });
              }
            });
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```
* 方式二：调用showAssetsCreationDialog弹窗授权保存图片到相册。

  使用弹窗授权保存图片到相册，首先获取需要保存到媒体库的位于应用沙箱的图片/视频uri，然后调用showAssetsCreationDialog接口弹窗授权，通过[fs.copyFileSync](../harmonyos-references/js-apis-file-fs.md#fileiocopyfilesync)将图片保存到相册。示例代码如下：

  ```ts
  import { fileIo as fs, fileUri } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';
  import { photoAccessHelper } from '@kit.MediaLibraryKit';

  @Entry
  @Component
  struct showAssetsCreationDialogMethod {
    uiContext: UIContext = this.getUIContext();

    async saveFile() {

      // 拷贝资源文件到沙箱
      let mContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let array = mContext.resourceManager.getRawFileContentSync('test.jpg');
      let dirpath = (this.uiContext.getHostContext() as common.UIAbilityContext).tempDir + '/test.jpg';
      let dirUri = fileUri.getUriFromPath(dirpath);
      let dirFile = fs.openSync(dirpath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      fs.writeSync(dirFile.fd, array.buffer);
      fs.closeSync(dirFile);

      // 获取需要保存到媒体库的位于应用沙箱的图片/视频uri
      try {
        let srcFileUris: Array<string> = [dirUri];
        let photoCreationConfigs: Array<photoAccessHelper.PhotoCreationConfig> = [{
          fileNameExtension: 'jpg',
          photoType: photoAccessHelper.PhotoType.IMAGE,
        }];
        let context = this.uiContext.getHostContext() as common.UIAbilityContext;
        let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
        let desFileUris: Array<string> =
          await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
        console.info('showAssetsCreationDialog success, data is ' + desFileUris);
        if (desFileUris.length > 0) {
          try {
            let srcFile = fs.openSync(srcFileUris[0], fs.OpenMode.READ_ONLY);
            let desFile = fs.openSync(desFileUris[0], fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.copyFileSync(srcFile.fd, desFile.fd);
            fs.closeSync(srcFile);
            fs.closeSync(desFile);
          } catch (e) {
            console.error(e);
          }
        }
      } catch (err) {
        console.error('showAssetsCreationDialog',
          `showAssetsCreationDialog failed with error: ${err.code}, ${err.message}`);
      }
    }

    build() {
      RelativeContainer() {
        Row() {
          Button('弹窗保存')
            .margin({ top: '700lpx', left: '60lpx' })
            .onClick(() => {
              this.saveFile();
            });
        }.justifyContent(FlexAlign.Center).width('100%');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  **注意**：

  弹窗需显示应用名称，但无法直接获取。因此，调用showAssetsCreationDialog接口时，请确保[module.json5](../harmonyos-guides/module-configuration-file.md)文件中的abilities标签已配置label和icon项，label值即应用名称值。需要注意的是，图标不受abilities标签中的icon项影响，不支持修改。

## 常见FAQ

Q：为什么不设计showAssetsCreationDialog只进行一步操作就可以成功保存图片？

A：由于图片保存涉及到安全性能问题，所以要限制临时权限的赋予时间，这就导致showAssetsCreationDialog每次都会拉起相应弹窗去获取临时权限。

可以使用[createAssetWithShortTermPermission](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#createassetwithshorttermpermission12)，此API在用户“同意”后的5min之内，弹窗便不会再次弹出，createAssetWithShortTermPermission涉及到受限权限ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO，申请权限时可以详细描述一下具体使用场景，通过受限权限。

Q：使用photoAccessHelper.showAssetsCreationDialog将沙箱中的图片保存到系统相册，工程中的icon和label也没有显示，弹窗中间还有个矩形空白区域？

A：首先确认弹窗的图标为应用图标，请确保[module.json5](../harmonyos-guides/module-configuration-file.md)文件中的abilities标签已配置label和icon项，label值即应用名称值。不支持修改，是固定的。

Q：使用showAssetsCreationDialog保存图片时，图片预览有问题。

A：[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)方法中参数srcFileUris为需保存到媒体库中的图片文件对应的媒体库uri，需要使用[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)补全传入的路径，保存时即可正确预览图片。

Q：使用photoAccessHelper保存图片，配置PhotoCreationConfig的title属性无效，设置的title未在弹窗中显示。

A：[PhotoCreationConfig](../harmonyos-references/arkts-apis-photoaccesshelper-i.md#photocreationconfig12)中配置的title是设置的保存的图片的标题，可以在相册中查看保存的图片标题与设置的title是一致的。

Q：视频成功下载到应用中但是读取到的数据为18，与预期不符。

A：视频下载成功但与预期不符，可能是链接有问题，下载后可以用[video组件](../harmonyos-references/ts-media-components-video.md)进行播放测试。

Q：H5页面中无法使用安全控件，如何保存媒体文件至相册？

A：可以使用[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)将H5中保存的图片，保存到手机媒体库。

Q：如何下载网络图片并保存到相册？

A：开发者可以通过[ohos.request](../harmonyos-references/js-apis-request.md)下载图片文件，可参考[下载网络资源文件至应用文件目录](../harmonyos-guides/app-file-upload-download.md#下载网络资源文件至应用文件目录)。下载完成后使用弹窗授权的方式保存至图库。

Q：使用photoAccessHelper.showAssetsCreationDialog，弹窗不显示图片预览的原因。

A：当传入uri为沙箱路径时，可正常保存图片/视频，但无界面预览，如果需要预览正常，需要保证传入的是文件路径。

Q：用户需要保存图片、视频等用户文件到图库时，使用弹窗授权保存媒体库资源时创建的媒体库uri不存在。

A：使用[showAssetsCreationDialog](../harmonyos-references/arkts-apis-photoaccesshelper-photoaccesshelper.md#showassetscreationdialog12)申请弹窗授权保存图片到相册时，需要先获取到需保存到媒体库中的图片对应的应用沙箱目录的uri，然后使用弹窗授权把图片保存到相册。

Q：为什么使用了弹窗授权，应用上架时依然提示ohos.permission.WRITE\_IMAGEVIDEO权限申请不通过？

A：使用安全控件或者授权弹窗的方式进行资源保存时，应用无需申请ohos.permission.WRITE\_IMAGEVIDEO权限，同时需要将配置文件内静态权限列表中的ohos.permission.WRITE\_IMAGEVIDEO权限删除，否则再次上架时还会报错。

Q：如何截取视频中的某一帧图片并保存？

A：可以先[从视频中提取特定帧图片](faqs-media-30.md)，获取特定帧后使用弹窗授权的方式保存到相册。
