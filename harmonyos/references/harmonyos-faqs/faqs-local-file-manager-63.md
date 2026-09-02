---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-63
title: 获取文件大小和文件类型
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 获取文件大小和文件类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3cfb144cd766653c8c90785d7e855a519ff4536fd49afb4ac31c3bae438bf333
---

## 问题现象

在对基础文件进行操作和管理的过程中，有时需要获取指定路径下文件的大小，以及指定路径文件夹的总大小，以及文件类型。这些信息应如何获取呢？

## 背景知识

* 文件管理[fs.mkdir](../harmonyos-references/js-apis-file-fs.md#fileiomkdir)可以创建目录，需要传入待创建的[应用沙箱目录与应用沙箱路径](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)。使用[fs.statSync](../harmonyos-references/js-apis-file-fs.md#fileiostatsync)和[fs.stat](../harmonyos-references/js-apis-file-fs.md#fileiostat)可以同步和异步获取文件的信息，可以获取到文件大小、文件路径等信息。
* 获取文件信息时传入的路径必须是沙箱下的有效路径，如果文件不在沙箱内，需要先[copyFileSync](../harmonyos-references/js-apis-file-fs.md#fileiocopyfilesync)复制文件到沙箱再获取文件信息。
* [应用及文件系统空间统计](../harmonyos-guides/app-fs-space-statistics.md)应用自身占用的空间大小和具体的文件大小是不同的，需要注意区分。

## 解决方案

* 获取指定路径下文件的大小。文件的fs.statSync可以同步获取文件的信息，以获取图片大小为例，使用PhotoViewPicker选择图片后把图片复制到沙箱mkdir创建好的文件夹下，通过fs.statSync就可以获取沙箱路径下的文件大小信息。

  ```ts
  import fs from '@ohos.file.fs';
  import photoAccessHelper from '@ohos.file.photoAccessHelper';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  async function getPicture(context: common.UIAbilityContext) {
    let pathDir = context.filesDir;
    let stat = fs.statSync(pathDir + '/picture.jpg');
    console.info('get file info succeed, the size of file is ' + stat.size);
  }

  async function picture(context: common.UIAbilityContext) {
    let dirPath = context.filesDir;
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
    photoSelectOptions.maxSelectNumber = 1;
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(photoSelectOptions).then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      let photouri: Array<string> = photoSelectResult.photoUris;
      let file = fs.openSync(photouri[0], fs.OpenMode.READ_ONLY);
      let file2 = fs.openSync(dirPath + '/picture.jpg', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
      fs.copyFileSync(file.fd, file2.fd);
      fs.closeSync(file);
      fs.closeSync(file2);
    });
  }

  @Entry
  @Component
  export struct GetFileSize {
    aboutToAppear(): void {
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      let pathDir = context.filesDir;
      let dirPath = pathDir + '/mediaFile';
      fs.mkdir(dirPath).then(() => {
        console.info('mkdir succeed');
      }).catch((err: BusinessError) => {
        console.error('mkdir failed with error message: ' + err.message + ', error code: ' + err.code);
      });

    }

    build() {
      Column() {
        Button('选择并保存').onClick(() => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

          picture(context);
        });
        Button('获取沙箱路径下图片大小')
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            getPicture(context);
          });
      };
    }
  }
  ```
* 获取指定路径文件夹的总大小以及判断文件属于什么类型。获取文件夹总大小，可以通过遍历操作使用fs.statSync，计算文件夹下文件大小总和；当前没有获取文件类型的API，可以通过此方案间接获取：进行文件类型和传输数据类型的映射关系，截取文件后缀进行判断哪种类型。

  ```ts
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct ReadFilePage {
    build() {
      Column() {
        Text('获取文件夹大小')
          .padding(40)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let pathDir = context.filesDir;
            let size = this.getFileSize(pathDir);    // 此处路径仅为示例，请更换为真实的路径
            console.info(`文件夹的总大小: ${size}`);
          });
        Text('判断文件类型')
          .padding(40)
          .onClick(()=>{
            let type = this.getPathExtension('xxx.JPG');
            console.info(`文件类型: ${type}`);
          });

      }
    }
    getFileSize(path:string):Number{
      let size = 0;
      class ListFileOption {
        // true为获取该文件夹下所有文件
        public recursion: boolean = true;
        // 获取文件的数量，为0时获取所有文件
        public listNum: number = 0;
      };
      let option = new ListFileOption();
      let filenames = fs.listFileSync(path, option);

      for(let i = 0;i < filenames.length;i++){
        size += fs.statSync(path+filenames[i]).size;
      }
      return size;
    }

    getPathExtension(url:string):string {
      const lastDotIndex = url.lastIndexOf('.');
      if (lastDotIndex < 0) {
        return '';
      }
      return url.slice(lastDotIndex + 1);
    };
  }
  ```

## 常见FAQ

Q：怎么获取文件的创建时间？

A：fs.stat返回结果创建时间用Atime代替，Ctime表示最近改变文件状态的时间。

Q：链接文件信息怎么获取？

A：使用[fs.lstat](../harmonyos-references/js-apis-file-fs.md#fileiolstat)可以获取链接文件信息。

Q：怎么设置修改文件的最后访问时间？

A：使用[fs.utimes](../harmonyos-references/js-apis-file-fs.md#fileioutimes11)更改文件上次修改该文件的时间，或使用标准posix接口[futimes](https://man7.org/linux/man-pages/man3/futimes.3.html)等。
