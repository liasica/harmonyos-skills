---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-17
title: Instrument Test单元测试如何获取本地文件路径
breadcrumb: FAQ > DevEco Studio > 应用测试 > Instrument Test单元测试如何获取本地文件路径
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2cb5f7829f0716123fe295e793be43e6fceceb817ea1d336cdd855913bf1c256
---

## 问题现象

使用ArkTS开发HarmonyOS APP时，需针对某个功能实现单元测试。单元测试类型为Instrument Test，测试的功能为HarmonyOS的RCP模块发起http请求的文件上传功能。测试这个功能需要向RCP传入一个本地文件路径。文件上传成功后，服务器会把上传文件的内容返回给客户端。所以需要一个正确的“本地文件路径”来完成测试。

1. 通过“本地文件路径”向RCP传入，完成文件上传。
2. 通过“本地文件路径”在客户端读取文件内容，然后与服务器返回的文件内容比对一致性。

## 背景知识

* 在[应用沙箱](../harmonyos-guides/app-sandbox-directory.md#应用沙箱目录与应用沙箱路径)保护机制下，应用无法获知除自身应用文件目录之外的其他应用或用户的数据目录位置及存在。应用内使用RCP模块进行文件上传时，需要将本地文件保存至沙箱目录。
* [hash.hash](../harmonyos-references/js-apis-file-hash.md#hashhash)：计算文件的hash值，如果两个文件的hash值相同，则两个文件内容一致。

## 解决方案

1. 选择rawfile目录下的文件保存至沙箱目录后，将文件的沙箱目录作为参数，传入rcp.createSession().uploadFromFile()用于上传文件，并获得服务器返回的文件内容Arraybuffer。

   ```ts
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { common } from "@kit.AbilityKit";
   import { rcp } from "@kit.RemoteCommunicationKit";
   import { BusinessError } from "@kit.BasicServicesKit";

   @Entry
   @Component
   struct Index {
     // 获取context
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

     build() {
       RelativeContainer() {
         Column() {
           Text("保存文件至沙箱")
             .id('save')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(async () => {
               saveFile(this.context);
             })

           Text("上传文件")
             .id('upload')
             .fontSize($r('app.float.page_text_font_size'))
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               uploadFileSync(this.context);
             })
         }

       }
       .height('100%')
       .width('100%')
     }
   }

   /**
    * 保存文件至沙箱目录
    * @param context 上下文
    */
   export async function saveFile(context: common.UIAbilityContext) {
     const fileName = 'test.txt';
     // 构建沙箱路径
     const sandboxPath = context.filesDir + '/' + fileName;
     let resource = context.resourceManager;
     try {
       // 从rawfile中读取原始文件
       const rawContent = resource.getRawFileContentSync(fileName);
       // 写入沙箱
       const file = fs.openSync(sandboxPath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
       fs.writeSync(file.fd, rawContent.buffer);
       fs.closeSync(file);
     } catch (error) {
       console.error(`保存文件失败: ${error.message}`);
     }
   }

   /**
    * 上传文件
    * @param context 上下文
    * @returns 返回上传文件后的ArrayBuffer
    */
   export async function uploadFileSync(context: common.UIAbilityContext): Promise<ArrayBuffer> {
     // 文件的沙箱目录
     const sandboxPath = context.filesDir + '/' + "test.txt";
     try {

       // 定义uploadFromFile
       let uploadFromFile: rcp.UploadFromFile = {
         fileOrPath: sandboxPath
       };
       const session = rcp.createSession();
       // 此处URL:XX.XX.XX需要更换为实际的URL
       session.uploadFromFile("XX.XX.XX", uploadFromFile).then((response) => {
         console.info(`Succeeded in getting the response ${response}`);
         // 由于是测试URL并不会返回文件内容且存在访问返回403的情况，此处需要自行处理逻辑。例：data=response.body
       }).catch((err: BusinessError) => {
         console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
       });
       // 此处构造上传文件成功后的ArrayBuffer
       return getArrayBuffer(sandboxPath);
     } catch (err) {
       console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
       // 此处构造上传文件成功后的ArrayBuffer
       return getArrayBuffer(sandboxPath);
     } finally {
       console.info(`Method uploadFileSync run finished.`);
     }
   }

   /**
    * 获取文件的ArrayBuffer
    * @param fileUri 文件路径
    * @returns ArrayBuffer
    */
   async function getArrayBuffer(fileUri: string): Promise<ArrayBuffer> {
     let data: ArrayBuffer = new ArrayBuffer(0);
     try {
       const file = fs.openSync(fileUri, fs.OpenMode.READ_ONLY);
       let photoSize = fs.statSync(file.fd).size;
       let arrayBuffer = new ArrayBuffer(photoSize);
       fs.readSync(file.fd, arrayBuffer);
       fs.closeSync(file);
       return arrayBuffer;
     } catch (err) {
       console.error(`err: err code is ${err.code}, err message is ${JSON.stringify(err)}`);
       return data;
     } finally {
       console.info(`Method getArrayBuffer run finished.`);
     }
   }
   ```
2. Instrument Test[创建ArkTS测试用例](../harmonyos-guides/ide-instrument-test.md#section36049271219)：在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击右键>Show Context Actions>Create Instrument Test或快捷键Alt+enter>Create Instrument Test创建测试类。
3. 编写测试方法并进行测试：

   ```ts
   import { describe, it, expect } from '@ohos/hypium';
   import { abilityDelegatorRegistry } from '@kit.TestKit';
   import { UIAbility } from '@kit.AbilityKit';
   import { fileIo as fs, hash } from '@kit.CoreFileKit';
   import { saveFile, uploadFileSync } from '../../../main/ets/pages/Index';

   const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

   export default function IndexTest() {
     describe('IndexTest', () => {

       it('assertEqual', 0, async () => {
         // 获取当前ability
         const ability: UIAbility = await delegator.getCurrentTopAbility();
         console.info("get top ability");
         // 定义本地文件保存到沙箱目录的位置
         let filePath = ability.context.filesDir + "/test.txt"
         // 保存本地文件至沙箱目录，此处从rawfile保存至沙箱
         await saveFile(ability.context)
         // 返回rcp流程上传后的结果arraybuffer
         let upLoadRes = await uploadFileSync(ability.context);
         // 在沙箱目录下创建新的文件用于文件内容比对
         let upLoadFilePath = ability.context.filesDir + "/uploadResult.txt";
         // 将ArrayBuffer写入至新的文件
         let file = fs.openSync(upLoadFilePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
         fs.writeSync(file.fd, upLoadRes);
         fs.closeSync(file);
         // 获取两个文件的hash值
         const localHash = await hash.hash(filePath, 'sha256');
         const resultHash = await hash.hash(upLoadFilePath, 'sha256');
         // hash值比对
         expect(localHash).assertEqual(resultHash)
       })
     })
   }
   ```

## 总结

* 文件内容比对主要有以下两种方法，由于哈希方案能更好的兼顾性能和可靠性，所以一般实际开发时推荐哈希方案：
  + 小文件（<10MB）：逐字节比较简单直接。
  + 大文件：优先使用哈希比较，效率更高（SHA256几乎无碰撞风险）。
* [基于RCP实现文件上传下载功能Demo](https://gitee.com/harmonyos_samples/RcpFileTransfer)：基于Remote Communication Kit远场通信服务，使用post、fetch、downloadToFile等方法实现相册的文件上传下载、文件分片下载、断点续传、后台文件上传下载功能。为开发者提供基于RCP上传下载各种场景的开发指导。
