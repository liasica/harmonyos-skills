---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-67
title: 使用DOWNLOAD模式保存的文件如何访问
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 使用DOWNLOAD模式保存的文件如何访问
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:c16c1acd4440f53d1e4cfb7ab9f94ec2c22d40aeb9fe895fef7ed10c1554a13c
---

## 问题现象

应用使用DOWNLOAD模式保存文件后，如何访问这些文件？

## 背景知识

* [DOWNLOAD模式保存文件](../harmonyos-guides/save-user-file.md#download模式保存文件)：自动创建在Download/包名/目录。跳过文件选择界面直接保存。返回的URI已具备持久化权限，用户可在该URI下创建文件。
* DOWNLOAD模式保存的文件URI示例：'file://docs/storage/Users/currentUser/Download/<bundleName>/\*\*\*.mp3'。
* [bundleManager.getBundleInfoForSelfSync](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforselfsync10)：以同步方法根据给定的bundleFlags获取当前应用的BundleInfo。
* [fs.listFileSync](../harmonyos-references/js-apis-file-fs.md#fileiolistfilesync)：默认以同步方式列出当前目录下所有文件名和目录名。支持过滤。可通过配置options中recursion参数实现递归列出所有文件的相对路径，相对路径以“/”开头。

## 解决方案

使用DOWNLOAD模式保存的文件，其URI已具备持久化权限，应用可以通过系统预定义的用户文件目录直接使用[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)的能力进行访问。注意该方式应用只能访问到Download目录下的自己包名下的文件或文件夹。

完整示例参考如下：

```ts
import { fileIo as fs, fileUri, ListFileOptions } from '@kit.CoreFileKit';
import { bundleManager } from '@kit.AbilityKit';

@Entry
@Component
struct VisitDownloadDir {
  build() {
    Column({ space: 5 }) {
      Button('DOWNLOAD模式访问')
        .onClick(() => {
          // 获取bundleName
          let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
          bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
          let data = bundleManager.getBundleInfoForSelfSync(bundleFlags);
          console.info('getBundleInfoForSelfSync successfully: ', JSON.stringify(data));
          let bundleName = data.name;
          // 获取Download目录下应用包名对应的path
          let uri = 'file://docs/storage/Users/currentUser/Download/' + bundleName;
          let fileUriObject = new fileUri.FileUri(uri);
          let path = fileUriObject.path;
          // 递归遍历出目录下的文件,进行业务操作(保证目录下有文件)
          let listFileOption: ListFileOptions = {
            recursion: true,
          };
          let filenames = fs.listFileSync(path, listFileOption);
          for (let i = 0; i < filenames.length; i++) {
            let file: fs.File | null = null;
            try {
              file = fs.openSync(path + '/' + filenames[i], fs.OpenMode.READ_WRITE);
              console.info('file path is :', file.path);
            } catch (e) {
              console.error('fs.openSync failed error is : ', JSON.stringify(e));
            } finally {
              if (file !== null) {
                fs.closeSync(file);
              }
            }
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 总结

使用DOWNLOAD模式保存的文件，其URI已具备持久化权限，应用可以直接访问Download目录下的自己包名下的文件或文件夹。应用卸载重装后若包名未修改，应用也可直接访问卸载前存放在该目录下的文件或文件夹。若需要访问其他公共目录，请使用[FilePicker](../harmonyos-guides/select-user-file.md)、[授权持久化](../harmonyos-guides/file-persistpermission.md)、[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)。
