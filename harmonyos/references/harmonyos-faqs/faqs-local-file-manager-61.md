---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-61
title: 如何在应用沙箱内创建文件或者文件夹
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何在应用沙箱内创建文件或者文件夹
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:79bbc1ad0e1b2c0e3124704562507eb0477ee554605d0e4262910f1da55fb955
---

## 问题现象

在应用开发中，经常需要创建文件或者文件夹进行文件读写操作，如何在应用沙箱内创建文件或者文件夹？

## 解决方案

创建文件或文件夹，一般步骤如下：

1. 使用fs.access判断文件/目录是否存在；
2. 使用fs.mkdir创建文件夹（当参数recursion指定为true时，可递归创建多文件夹）；
3. 使用fs.open(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE)创建文件并以读写模式打开；
4. 文件读写则使用fs.read、fs.write方法。

代码示例如下：

```ts
import { fileIo as fs } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct FileDemo {
  @State path: string = '';

  aboutToAppear(): void {
    this.path = `${this.getUIContext().getHostContext()!.filesDir}/testDir`;
  }

  createFolder() {
    let isExist = fs.accessSync(this.path, fs.AccessModeType.EXIST);
    if (isExist) {
      this.getUIContext().getPromptAction().showToast({ message: '文件夹已存在', alignment: Alignment.Center, duration: 1500 });
      return;
    }
    fs.mkdir(this.path).then(() => {
      this.getUIContext().getPromptAction().showToast({ message: '成功新建文件夹', alignment: Alignment.Center, duration: 1500 });
      console.info('mkdir succeed');
    }).catch((err: BusinessError) => {
      this.getUIContext().getPromptAction().showToast({ message: `新建文件夹失败:${err.message}`, alignment: Alignment.Center, duration: 1500 });
      console.error(`mkdir faile.error message: ${err.message},  error code: ${err.code}`);
    });
  }

  async createFile() {
    try {
      let isExist = fs.accessSync(this.path, fs.AccessModeType.EXIST);
      if (!isExist) {
        await fs.mkdir(this.path);
      }
      // 获取应用沙箱路径
      const filePath = `${this.path}/example.txt`;
      const file = await fs.open(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
      const text = 'HelloWorld';
      await fs.write(file.fd, text);
      await fs.close(file.fd);
      console.info(`文件保存成功，路径：${filePath}`);
      this.getUIContext().getPromptAction().showToast({ message: '新建文本文件', alignment: Alignment.Center, duration: 1500 });
    } catch (err) {
      let error = err as BusinessError;
      console.error(`保存文件失败：error message: ${error.message},  error code: ${error.code}`);
      this.getUIContext().getPromptAction().showToast({ message: '新建文本文件失败', alignment: Alignment.Center, duration: 1500 });
    }
  }

  async readFile() {
    const filePath = `${this.path}/example.txt`;
    let isExist = fs.accessSync(filePath, fs.AccessModeType.EXIST);
    if (!isExist) {
      this.getUIContext().getPromptAction().showToast({ message: '文件不存在', alignment: Alignment.Center, duration: 1500 });
      return;
    }
    const file = await fs.open(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
    let arrayBuffer = new ArrayBuffer(4096);
    await fs.read(file.fd, arrayBuffer);
    this.getUIContext().getPromptAction().showToast({
      message: buffer.from(arrayBuffer).toString('utf-8'),
      alignment: Alignment.Center,
      duration: 1500
    });
  }

  build() {
    Row() {
      Column({ space: 10 }) {
        Button('新建文件夹')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.createFolder();
          })

        Button('新建文件')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.createFile();
          })

        Button('读取文件')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.readFile();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
