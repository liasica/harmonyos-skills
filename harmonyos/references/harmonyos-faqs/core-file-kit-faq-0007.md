---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-faq-0007
title: 文件基础服务操作与读写常见问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 常见问题 > 文件基础服务操作与读写常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c4c615f16255eccba39f80a1ea79a6b5e9ef3dda44eec6c52e10e259fef0f1d0
---

**Q：常见文件操作API的参数涉及沙箱路径、文件句柄fd、文件uri，如何进行转换以及涉及常见转换场景有哪些？**

**A**：

1. 文件操作API的参数类型的常见参数类型转换、以及常见业务场景如下：

   针对上面背景知识描述，要想获取到标准规范的待处理文件参数，一般有安全沙箱目录，文件uri，文件fd三大类型的互联转换：

   | 序号 | 参数转换 | 常见业务场景 | 转换方式 |
   | --- | --- | --- | --- |
   | 1 | sandboxPath -> fd | 应用拷贝rawfile目录下文件至沙箱进行读写 | let file = fs.openSync(sandboxPath); let fd = file.fd; |
   | 2 | sandboxPath -> uri | 图片编辑场景下，获取图片uri后拉起图片编辑类应用 | let uri = fileUri.getUriFromPath(sandboxPath); |
   | 3 | fd -> sandboxPath | 文件管理器类应用需要根据某一个文件获取整个目录下同类或其他文件 | let file = fs.dup(fd); let sandboxPath = file.path; |
   | 4 | fd -> uri | 文件管理器类应用需要根据某一个文件获取整个目录下同类或其他文件 | let file = fs.dup(fd); fileUri.getUriFromPath(file.path); |
   | 5 | uri -> fd | 应用打开文件管理器操作文本文件进行读写 | let file = fs.openSync(uri); let fd = file.fd; |
   | 6 | uri -> sandboxPath | 应用打开文件管理器操作文本文件进行读写 | let file = fs.openSync(uri); let sandboxPath = file.path; |
2. 文件操作API的参数类型的常见参数类型转换场景：
   * 应用读取rawfile目录下文件至沙箱进行读写：

     sandboxPath -> fd转换： 一般通过fs.openSync接口，打开沙箱路径sandboxPath，获取File对象，进而获取文件描述符fd。

     ```ts
     // 1、sandboxPath转化fd
                 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 let content = context.resourceManager.getRawFileContentSync('testPic.png');
                 // 获取沙箱文件sandboxPath：
                 let sandboxPath = context.filesDir + '/testPic.png';
                 // 通过fs.openSync接口获取File对象
                 let file = fs.openSync(sandboxPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                 fs.writeSync(file.fd, content.buffer);
                 fs.closeSync(file);
                 hilog.info(0x0000, TAG, `sandboxPath转化为fd 成功。`);
     ```
   * 图片编辑场景下，获取图片uri后拉起图片编辑类应用：

     sandboxPath -> uri： 通过fileUri.getUriFromPath接口将沙箱文件转换为文件uri。

     ```ts
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 let sandboxPath = context.filesDir + 'testPic';
                 // 2、sandboxPath转化uri
                 let uri = fileUri.getUriFromPath(sandboxPath);
                 let abilityStartCallback: common.AbilityStartCallback = {
                   onError: (code, name, message) => {
                     const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
                     hilog.error(0x0000, TAG, `startAbilityByType: ${tip}`);
                   },
                   onResult: (result) => {
                     // 获取到回调结果中编辑后的图片uri并做对应的处理
                     hilog.info(0x0000, TAG, `PhotoEditorCaller result: ${JSON.stringify(result)}`);
                   }
                 };
                 context.startAbilityByType('photoEditor', {
                   // 原始图片的uri,只支持传入一个uri
                   'ability.params.stream': [uri],
                   // 至少需要分享读权限给到图片编辑面板
                   'ability.want.params.uriPermissionFlag': wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION

                 } as Record<string, Object>, abilityStartCallback, (err) => {
                   if (err) {
                     hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
                   } else {
                     hilog.info(0x0000, TAG, 'startAbilityByType: success');
                   }
                 });
     ```
   * 文件管理器类应用需要根据某一个文件获取整个目录下同类或其他文件：

     fd -> sandboxPath： 根据fs.dup(fd)接口获取File对象，从而获取沙箱路径sandboxPath。

     fd -> uri： 有上述步骤获取到沙箱路径sandboxPath；再通过fileUri.getUriFromPath（sandboxPath）获取uri对象。

     ```ts
     let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 let filePath = context.filesDir + 'testPic';
                 let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
                 let fd: number = file.fd;
                 // 通过fs.dup接口将fd转换为sandboxPath
                 let sandboxPath = fs.dup(fd).path;
                 hilog.info(0x0000, TAG, `sandboxPath is ${sandboxPath}`);
                 // 再通过sandboxPath获取uri
                 let uri = fileUri.getUriFromPath(sandboxPath);
                 hilog.info(0x0000, TAG, `uri is ${uri}`);
                 fs.closeSync(file);
     ```
   * 应用打开文件管理器操作文本文件进行读写：

     uri -> fd转换： 一般通过fs.openSync接口，打开沙箱路径sandboxPath，获取File对象，进而获取文件描述符fd。

     uri -> sandboxPath转换： 需要使用fileUri.FileUri先获取fileUri对象，再通过FileUri.getFullDirectoryUri（fileUri）获取全目录json对象上的path属性，最后获得沙箱路径sandboxPath。

     ```ts
     let uris: Array<string> = [];
                 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 // 创建文件选择器实例
                 const documentSelectOptions = new picker.DocumentSelectOptions();
                 documentSelectOptions.maxSelectNumber = 1;
                 const documentViewPicker = new picker.DocumentViewPicker(context);
                 documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
                   // 文件选择成功后，返回被选中文档的uri结果集。
                   uris = documentSelectResult;
                   hilog.info(0x0000, TAG, `documentViewPicker.select to file succeed and uris are: ${uris}`);
                   let file = fs.openSync(uris[0], fs.OpenMode.READ_ONLY);
                   // 通过fs.openSync获取File对象，从而获得fd、sandboxPath
                   hilog.info(0x0000, TAG, `file fd: ${file.fd}`);
                   hilog.info(0x0000, TAG, `sandboxPath is ${file.path}`);
                 }).catch((err: BusinessError) => {
                   hilog.info(0x0000, TAG, `Invoke documentViewPicker.select failed, code is ${err.code},
                   message is ${err.message}`);
                 });
     ```

   完整示例代码如下：

   ```ts
   import { fileIo as fs, fileUri, picker } from '@kit.CoreFileKit';
   import { common, wantConstant } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const TAG: string = 'documentConvert';

   @Entry
   @Component
   struct Index {
     build() {
       Column({ space: 20 }) {
         Button('sandboxPath转化为fd')
           .onClick(() => {
             try {
               // 1、sandboxPath转化fd
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let content = context.resourceManager.getRawFileContentSync('testPic.png');
               // 获取沙箱文件sandboxPath：
               let sandboxPath = context.filesDir + '/testPic.png';
               // 通过fs.openSync接口获取File对象
               let file = fs.openSync(sandboxPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
               fs.writeSync(file.fd, content.buffer);
               fs.closeSync(file);
               hilog.info(0x0000, TAG, `sandboxPath转化为fd 成功。`);
               } catch (e) {
               let err = e as BusinessError;
               hilog.error(0x0000, TAG, `sandboxPath转化为fd 失败, code is ${err.code},message is ${err.message}`);
             }
           });

         Button('sandboxPath转化为uri')
           .onClick(() => {
             try {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let sandboxPath = context.filesDir + 'testPic';
               // 2、sandboxPath转化uri
               let uri = fileUri.getUriFromPath(sandboxPath);
               let abilityStartCallback: common.AbilityStartCallback = {
                 onError: (code, name, message) => {
                   const tip: string = `code:` + code + ` name:` + name + ` message:` + message;
                   hilog.error(0x0000, TAG, `startAbilityByType: ${tip}`);
                 },
                 onResult: (result) => {
                   // 获取到回调结果中编辑后的图片uri并做对应的处理
                   hilog.info(0x0000, TAG, `PhotoEditorCaller result: ${JSON.stringify(result)}`);
                 }
               };
               context.startAbilityByType('photoEditor', {
                 // 原始图片的uri,只支持传入一个uri
                 'ability.params.stream': [uri],
                 // 至少需要分享读权限给到图片编辑面板
                 'ability.want.params.uriPermissionFlag': wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION

               } as Record<string, Object>, abilityStartCallback, (err) => {
                 if (err) {
                   hilog.error(0x0000, TAG, `startAbilityByType: fail, err: ${JSON.stringify(err)}`);
                 } else {
                   hilog.info(0x0000, TAG, 'startAbilityByType: success');
                 }
               });
               } catch (e) {
               let err = e as BusinessError;
               hilog.error(0x0000, TAG, `sandboxPath转化为uri 失败, code is ${err.code},message is ${err.message}`);
             }
           });

         Button('fd转化sandboxPath以及fd转化uri')
           .onClick(() => {
             try {
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               let filePath = context.filesDir + 'testPic';
               let file = fs.openSync(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
               let fd: number = file.fd;
               // 通过fs.dup接口将fd转换为sandboxPath
               let sandboxPath = fs.dup(fd).path;
               hilog.info(0x0000, TAG, `sandboxPath is ${sandboxPath}`);
               // 再通过sandboxPath获取uri
               let uri = fileUri.getUriFromPath(sandboxPath);
               hilog.info(0x0000, TAG, `uri is ${uri}`);
               fs.closeSync(file);
               } catch (e) {
               let err = e as BusinessError;
               hilog.error(0x0000, TAG,
                 `fd转化sandboxPath以及fd转化uri 失败, code is ${err.code},message is ${err.message}`);
             }
           });

         Button('uri->fd转换、uri->sandboxPath转换')
           .onClick(() => {
             try {
               let uris: Array<string> = [];
               let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
               // 创建文件选择器实例
               const documentSelectOptions = new picker.DocumentSelectOptions();
               documentSelectOptions.maxSelectNumber = 1;
               const documentViewPicker = new picker.DocumentViewPicker(context);
               documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
                 // 文件选择成功后，返回被选中文档的uri结果集。
                 uris = documentSelectResult;
                 hilog.info(0x0000, TAG, `documentViewPicker.select to file succeed and uris are: ${uris}`);
                 let file = fs.openSync(uris[0], fs.OpenMode.READ_ONLY);
                 // 通过fs.openSync获取File对象，从而获得fd、sandboxPath
                 hilog.info(0x0000, TAG, `file fd: ${file.fd}`);
                 hilog.info(0x0000, TAG, `sandboxPath is ${file.path}`);
               }).catch((err: BusinessError) => {
                 hilog.info(0x0000, TAG, `Invoke documentViewPicker.select failed, code is ${err.code},
                 message is ${err.message}`);
               });
               } catch (e) {
               let err = e as BusinessError;
               hilog.error(0x0000, TAG,
                 `uri->fd转换、uri->sandboxPath转换 失败, code is ${err.code},message is ${err.message}`);
             }
           });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     };
   }
   ```

**Q：通过documentViewPicker.select选择文件，将用户选择的文件路径，即回调参数作为参数值，调用@ohos.file.fs的fs.statSync为什么报错，fs.openSync就没报错？**

**A**：documentViewPicker.select返回的是用户选择文件的uri数组，fs.openSync要求传入沙箱路径或者文件uri参数所以没报错；API22之前，fs.statSync要求传入沙箱路径或者文件fd值，参数类型不匹配，所以报错了，从API22开始，支持传入URI。

**Q：在对基础文件进行操作和管理的过程中，有时需要获取指定路径下文件的大小，以及指定路径文件夹的总大小，以及文件类型。这些信息应如何获取呢？**

**A**：获取指定路径下文件的大小。文件的fs.statSync可以同步获取文件的信息，以获取图片大小为例，使用PhotoViewPicker选择图片后把图片复制到沙箱mkdir创建好的文件夹下，通过fs.statSync就可以获取沙箱路径下的文件大小信息，请参考以下示例代码：

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

获取指定路径文件夹的总大小以及判断文件属于什么类型。获取文件夹总大小，可以通过遍历操作使用fs.statSync，计算文件夹下文件大小总和；当前没有获取文件类型的API，可以通过此方案间接获取：进行文件类型和传输数据类型的映射关系，截取文件后缀进行判断哪种类型。请参考以下示例代码：

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

**Q：怎么获取文件的创建时间？**

**A**：fs.stat返回结果创建时间用Atime代替，Ctime表示最近改变文件状态的时间。

**Q：链接文件信息怎么获取？**

**A**：使用[fs.lstat](../doccenter-references/api/js-apis-file-fs.md#fileiolstat)可以获取链接文件信息。

**Q：怎么设置修改文件的最后访问时间？**

**A**：使用[fs.utimes](../doccenter-references/api/js-apis-file-fs.md#fileioutimes11)更改文件上次修改该文件的时间，或使用标准posix接口futimes等。

**Q：使用fileIo.open以只读模式打开文件，然后使用fileIo.stat获取mode的值，发现该值与文档中的描述不一致。使用场景是API支持用户传入文件描述符(fd)，如何根据fd对应的模式来判断是否有对应的操作权限？例如，如果API涉及写入操作，则需要通过fileIo.stat获取mode，以判断是否支持写入。**

**A**：fileIo.stat取出的mode值为文件本身的权限值。十进制432的八进制表示为660，这是沙箱中的默认权限。开发者希望获取的是文件的打开方式，而打开方式是用户已知的内容。目前，系统不提供获取文件打开方式的接口。

1. 若要获取open的打开方式，但系统默认假定用户已知此信息。
2. mode是文件的权限信息，不涉及应用对文件的操作。

**Q：如何解决文件的中文乱码问题？**

**A**：读取文件内容的buffer数据后，通过TextDecoder对文件内容进行解码。

```ts
import { util } from '@kit.ArkTS';
import { fileIo } from '@kit.CoreFileKit';

// In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
let context = AppStorage.get("context") as UIContext;
// Create a file to write Chinese characters
let filePath = context.getHostContext()!.filesDir + "/test0.txt";
let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
// Write a paragraph of content to a file
let writeLen = fileIo.writeSync(file.fd, "Hello, world");
fileIo.closeSync(file);
console.info(`GarbledCnCharacters The length of str is: ${writeLen}`);
let stream = fileIo.createStreamSync(filePath, "r+");
let buffer = new ArrayBuffer(4096);
stream.readSync(buffer);
// Set the encoding format to "utf-8"
let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
// Retrieve the corresponding text after decoding the input
let readString = textDecoder.decodeToString(new Uint8Array(buffer), { stream: false });
console.info(`GarbledCnCharacters read content is:${readString}`);
```

参考链接：[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)。
