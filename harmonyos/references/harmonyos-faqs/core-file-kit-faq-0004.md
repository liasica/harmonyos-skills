---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-faq-0004
title: 沙箱文件访问、路径获取与操作常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 常见问题 > 沙箱文件访问、路径获取与操作常见问题
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:08+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:d012592581faedb2ee6767587c7e24dc00ae083a2994fa280306ef551ca9c921
---

**Q：出于安全考虑，对系统文件夹访问权限被收回，想要访问系统文件夹里的文件，必须使用[DocumentViewPicker](../harmonyos-references/js-apis-file-picker.md#documentviewpicker)打开可视化交互页面，那么开发过程中涉及到的对各类文件的操作，就要依靠沙箱来实现，应该怎样访问沙箱中的文件呢？**

**A：**沙箱目录/文件常见操作如下：

* 查看正在调试的设备的沙箱文件：
  + 通过IDE的可视化工具Device File Browser中查看设备文件目录，该工具可以在IDE中通过View -> Tool Windows -> Device File Browser打开，Device File Browser对应沙箱目录如下：/data/app/el2/100/base/{应用包名}/haps/entry/files。
  + 通过命令行的方式访问debug应用的沙箱目录，API 15前后的系统版本访问方式不同，参考：[命令行方式访问应用沙箱](../harmonyos-guides/ide-device-file-explorer.md#section48216711204)。
* 获取沙箱路径下的文件列表：fs.listFile列出文件夹下所有文件名，支持递归列出所有文件名（包含子目录下），支持文件过滤，代码示例请参考：[fs.listFile](../doccenter-references/api/js-apis-file-fs.md#fileiolistfile)。
* 读取沙箱路径下的文件：以读取json文件为例，首先通过[openSync](../harmonyos-references/js-apis-fileio.md#fileioopensync)打开沙箱文件路径，然后[fs.writeSync](../doccenter-references/api/js-apis-file-fs.md#fileiowritesync)将数据写入文件，最后通过[fs.readTextSync](../doccenter-references/api/js-apis-file-fs.md#fileioreadtextsync)直接读取文件的文本内容，代码示例如下：

  ```ts
  import { fileIo as fs } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';

  @Entry
  @Component
  struct ReadFilePage {
    build() {
      Column() {
        Text('读取文件测试')
          .padding(40)
          .onClick(()=>{
            let context = this.getUIContext().getHostContext() as common.Context;
            let pathDir = context.filesDir;
            let filePath = pathDir + '/test.json';
            let json:ESObject = {key:1};
            let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
            fs.writeSync(file.fd, JSON.stringify(json));
            let json2 = fs.readTextSync(filePath);
            console.info(`读取的json: : ${json2}`);
            fs.closeSync(file);
          })
      }
    }
  }
  ```

* 删除沙箱路径文件：
  + [fs.unlink](../doccenter-references/api/js-apis-file-fs.md#fileiounlink)：删除单个沙箱路径文件，使用promise异步回调。
  + [fs.rmdir](../doccenter-references/api/js-apis-file-fs.md#fileiormdir)：删除目录及其所有子目录和文件，使用promise异步回调。该接口支持删除单个文件，但不推荐使用此方法删除单个文件，推荐使用unlink接口删除单个文件。
* Native侧访问应用沙箱文件：[Native侧实现沙箱文件访问](../best-practices/bpta-file-native-side.md)有ArkTS侧获取沙箱路径传递给Native侧访问文件和Native侧直接拼接沙箱路径访问文件两种方案。

**Q：Image组件可以直接使用传入沙箱路径进行显示吗？**

**A：**Image组件不能直接传入应用沙箱路径，需要传入应用沙箱uri，拿到文件的沙箱路径后，通过调用@ohos.file.fileUri模块的[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)将沙箱路径转化为沙箱uri，传入之后即可正常显示。

**Q：使用listFiles并传入过滤器filter来获取指定后缀名的文件名时，如何排除目录名，仅保留文件名？**

**A：**[ListFileOptions](../harmonyos-references/js-apis-file-fs.md#listfileoptions11)中recursion为false时，返回当前目录下满足过滤要求的文件名及目录名，若不想返回目录名，可将recursion置为true，此时仅返回满足过滤要求的文件的相对路径（包含文件名）。

**Q：如何将用户文件复制到应用的沙箱目录？**

**A：**使用[fs.copy](../doccenter-references/api/js-apis-file-fs.md#fileiocopy11)拷贝文件到沙箱即可，该API使用promise异步回调。

**Q：native如何获取沙箱路径？**

**A：**目前支持通过ArkTS侧获取沙箱路径传递到Native侧，或者在Native侧直接拼接沙箱路径。详细实现方法可参考文章：[方案二：Native侧直接拼接沙箱路径访问文件](../harmonyos-guides/file-native-side.md#方案二native侧直接拼接沙箱路径访问文件)。

**Q：在应用开发中，经常需要创建文件或者文件夹进行文件读写操作，如何在应用沙箱内创建文件或者文件夹？**

**A：**创建文件或文件夹，一般步骤如下：

1. 使用fs.access判断文件/目录是否存在；
2. 使用fs.mkdir创建文件夹（当参数recursion指定为true时，可递归创建多文件夹）；
3. 使用fs.open(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ\_WRITE)创建文件并以读写模式打开；
4. 文件读写则使用fs.read、fs.write方法。

若在创建文件夹前未判断文件夹是否存在，当文件夹已存在时会报错[13900015](../harmonyos-references/errorcode-filemanagement.md#section13900015-文件存在)，表示需创建的文件已存在。因此创建文件夹前须先判断文件夹是否存在。

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
