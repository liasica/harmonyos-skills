---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-21
title: 更换头像时头像资源加载异常
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 更换头像时头像资源加载异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e18612f20bf0cba017632649572c14748857f7e1bff6302fb48c45495b13cfe2
---

## 问题现象

点击头像更换，提示头像资源加载异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/wo4V0tVGTQOgtGz4ZXK3_w/zh-cn_image_0000002658852669.png "点击放大")

## 背景知识

* rawfile目录是项目的资源目录。支持创建多层子目录，文件夹允许放置各种类型的资源文件。需要注意的是：rawfile目录下的资源文件会直接打包进入应用包体内，不经过编译，所以不会被赋予资源文件Id，需要通过指定文件路径和文件名来进行访问。
* HarmonyOS侧提供了[@ohos.zlib](../harmonyos-references/js-apis-zlib.md)的能力，其中[zlib.compressFile](../harmonyos-references/js-apis-zlib.md#zlibcompressfile9)方法可以将指定文件/指定文件夹压缩，并将压缩后文件输出至指定路径。

## 问题定位

排查配置信息是否正确，是否获取到资源包。通过两段日志分析，在应用启动时获取config信息失败。在更换头像页面中获取头像资源时，判断zip资源不存在。

```screen
[network_security_config.cpp:322]Get json failed.
[network_security_config.cpp:68]GetConfig failed
```

```screen
[zip_file.cpp(IsDirExist:376)]file not dir
[zip_file.cpp(IsDirExist:376)]file not dir
[zip_file.cpp(IsDirExist:376)]file not dir
```

## 分析结论

* 应用启动时获取配置信息失败，资源zip包更新失败。
* 本地没有工程自带资源作为备用。

## 修改建议

在工程rawfile目录中存放少量头像资源包，在动态更新资源包失败的情况下使用本地资源，避免报错。复制rawfile目录的zip并解压到沙箱目录，参考如下步骤：

1. 通过[getRawFd()](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)获取rawfile/apps.zip所在hap包的descriptor信息。
2. 使用buffer将rawfile/apps.zip文件内容复制到沙箱临时文件路径。
3. 使用[zlib.decompressFile()](../harmonyos-references/js-apis-zlib.md#zlibdecompressfile9)解压zip文件至沙箱通用文件路径。

示例代码如下：

```screen
import fs from '@ohos.file.fs';
import zlib from '@ohos.zlib';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  build() {
    Row() {
      Column() {
        Button('复制zip到沙箱，并解压zip', { type: ButtonType.Normal, stateEffect: true })
          .borderRadius(8)
          .backgroundColor(0x317aff)
          .width(90)
          .height(40)
          .onClick(() => {
            /**
             * 通过fd来进行拷贝，避免文件过大的内存占用问题
             * data.fd是hap包的fd，data.offset表示目标文件在hap包中的偏移，data.length表示目标文件的长度
             */
            this.context.resourceManager.getRawFd('apps.zip', (err, data) => {
              if (!err) {
                let sandboxPath = this.context.filesDir;
                console.log('沙箱路径：' + sandboxPath);
                let filePath = this.context.tempDir + '/bfapps.zip';
                console.log('压缩文件路径：' + filePath);
                let dest: fs.File | null = null;
                try {
                  dest = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
                  let bufsize = 4096;
                  if (data.length <= bufsize) {
                    bufsize = data.length;
                  }
                  let buf = new ArrayBuffer(bufsize);
                  let off = 0, len = 0, readedLen = 0;
                  /**
                   * 通过buffer将rawfile文件内容copy到沙箱路径
                   */
                  len = fs.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize });
                  while (len) {
                    readedLen += len;
                    fs.writeSync(dest.fd, buf, { offset: off, length: len });
                    off = off + len;
                    if ((data.length - readedLen) < bufsize) {
                      bufsize = data.length - readedLen;
                    }
                    len = fs.readSync(data.fd, buf, { offset: data.offset + off, length: bufsize });
                  }
                  // 对沙箱路径下的压缩文件进行解压
                  zlib.decompressFile(filePath, sandboxPath);
                  this.context.resourceManager.closeRawFd('apps.zip');
                }catch (e) {
                  console.error('fs.openSync failed error is : ', JSON.stringify(e));
                } finally {
                  if (dest !== null) {
                    fs.closeSync(dest);
                  }
                }
              }
            });
          })
          .width('100%')
      }
      .height('100%')
    }
  }
}
```
