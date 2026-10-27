---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-faq-0006
title: DOWNLOAD模式保存文件访问常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 常见问题 > DOWNLOAD模式保存文件访问常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:7b987f324ad77a8236e6998c1b90f0d501f3f68a41948afdc940d4f4b8ee79f2
---

**Q：应用使用DOWNLOAD模式保存文件后，如何访问这些文件？**

**A**：使用DOWNLOAD模式保存的文件，其URI已具备持久化权限，应用可以通过系统预定义的用户文件目录直接使用[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)的能力进行访问。注意该方式应用只能访问到Download目录下的自己包名下的文件或文件夹。

示例代码如下：

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
