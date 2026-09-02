---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-60
title: 文件夹下所有文件拷贝至另一个文件夹
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 文件夹下所有文件拷贝至另一个文件夹
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b335c65cf803eaa1f5af9beb70057965de1e05140927d6f0c1714f6a218c3dc4
---

## 问题现象

文件夹A和文件夹B存在同一个沙箱目录中，文件夹A包含子目录文件和普通文件。如何把文件夹A包含的所有文件拷贝至文件夹B？

## 背景知识

[fs.listFile()](../harmonyos-references/js-apis-file-fs.md#fileiolistfile)用于遍历文件夹下所有文件，包含目录文件，其返回值是文件名数组。[fs.copyFileSync()](../harmonyos-references/js-apis-file-fs.md#fileiocopyfilesync)复制普通文件，[fs.copyDirSync()](../harmonyos-references/js-apis-file-fs.md#fileiocopydirsync10)复制目录文件。二者使用有一定的区别：前者需要指定完整的路径作为目标路径，包含文件名；后者的目标路径不包含源目录文件名。

## 解决方案

先使用fs.listFile()遍历文件夹A下的所有文件，然后使用fs.statSync(srcPath).isDirectory()判断是否是目录文件。如果是目录文件，则使用fs.copyDirSync()拷贝；如果不是，则使用fs.copyFileSync()进行拷贝。示例代码如下：

```ts
import fs from '@ohos.file.fs';
import common from '@ohos.app.ability.common';

@Entry
@Component
struct Index {
  uiContext = this.getUIContext();

  build() {
    Column() {
      Button('1.在tempDir中创建文件/文件夹')
        .margin({ bottom: 20 })
        .onClick(() => {
          let context = this.uiContext?.getHostContext() as common.UIAbilityContext;
          let tempDir = context.tempDir;
          let filePath = tempDir + '/testFile.txt';
          let dirPath = tempDir + '/testDir';

          // 必须使用 try-catch 包裹同步的文件系统操作
          try {
            // 1. 创建并写入文件
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.writeSync(file.fd, 'Try to write str.');
            fs.closeSync(file); // 操作完成后务必关闭文件

            // 2. 创建文件夹 (先判断是否存在，避免抛出异常)
            if (!fs.accessSync(dirPath)) {
              fs.mkdirSync(dirPath);
              console.info('文件夹创建成功');
            } else {
              console.info('文件夹已存在，无需重复创建');
            }
          } catch (error) {
            // 捕获异常，防止应用闪退
            console.error(`文件操作失败. Code: ${error.code}, message: ${error.message}`);
          }
        });

      Button('2.拷贝至filesDir')
        .onClick(() => {
          let context = this.uiContext?.getHostContext() as common.UIAbilityContext;
          let tempDir = context.tempDir;
          let filesDir = context.filesDir;

          try {
            // 获取 tempDir 下的所有文件名/文件夹名
            let filenames = fs.listFileSync(tempDir);

            for (let i = 0; i < filenames.length; i++) {
              let fileName = filenames[i];
              let srcPath = tempDir + `/${fileName}`;

              if (fs.statSync(srcPath).isDirectory()) {
                // 拷贝文件夹时，目标路径只需要精确到“父目录”即可
                let dstPath = filesDir;
                fs.copyDirSync(srcPath, dstPath);
                console.info(`目录 ${fileName} 拷贝成功`);
              } else {
                // 拷贝文件时，目标路径必须是包含文件名的“完整路径”
                let dstPath = filesDir + `/${fileName}`;
                fs.copyFileSync(srcPath, dstPath);
                console.info(`文件 ${fileName} 拷贝成功`);
              }
            }
            console.info('所有拷贝操作执行完毕');
          } catch (error) {
            console.error(`拷贝操作出错. Code: ${error.code}, message: ${error.message}`);
          }
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
