---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1064
title: 自定义字体的注册和使用
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义字体的注册和使用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f5476833c149a84c18145e7bcf13770bedd0fe4ab3779b5da995db782e99e398
---

## 问题现象

为了提升应用的用户体验和视觉吸引力，应用设计常常需要支持自定义字体即非系统字体，如何注册和使用自定义的字体？

## 背景知识

自定义字体是指开发者根据应用需求创建或选择的字体，通常用于实现特定的文字风格或满足独特的设计要求。当应用需要使用特定的文本样式和字符集时，可以注册并使用自定义字体进行文本渲染。

* [registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)：在字体管理中注册自定义字体。该接口为异步接口，不支持并发调用。
* [fontFamily](../harmonyos-references/ts-securitycomponent-attributes.md#fontfamily)：设置安全控件文字的字体。

实现流程：

1. 注册自定义字体：将字体文件（如ttf、otf文件等）从应用资源注册到系统中，使得应用能够使用这些字体进行文本渲染。注册过程通常指将字体文件通过字体管理接口注册到系统字体库中，以便在应用中进行调用。
2. 使用自定义字体：在应用中显式指定使用已注册的自定义字体进行文本渲染。开发者可以根据需要选择特定的文本样式（如常规、粗体、斜体等），并将其应用到UI元素、文本控件或其他文本展示区域，以确保符合设计要求并提供一致的视觉效果。

## 解决方案

1. 注册自定义字体。

   | 注册方法 | 资源文件加载方式 |
   | --- | --- |
   | registerFont | string |
   | registerFont | Resource |
   | registerFont | RawFile |
   | registerFont | 沙箱路径前加上file:// |

   **注意** 

   若项目entry模块下build-profile.json5文件有copyCodeResource字段，需改成true，否则familySrc不支持string和Resource。

   在工程中存放开发者自定义字体资源文件，通过registerFont接口在生命周期aboutToAppear中进行自定义字体注册。关键代码如下：

   ```ts
   aboutToAppear() {
     // 注册青鸟华光简美黑字体
     this.font.registerFont({
       familyName: 'QingNiaoHuaGuangJianMeiHei', // 注册的字体名称
       familySrc: '/font/QingNiaoHuaGuangJianMeiHei-2.ttf' // font文件夹与pages目录同级
     });

     // 注册字魂龙腾楷书字体
     this.font.registerFont({
       familyName: 'ZiHunLongTengKaiShu', // 注册的字体名称
       familySrc: '/font/ZiHunLongTengKaiShu(ShangYongXuShouQuan)-2.ttf' // font文件夹与pages目录同级
     });

     // 注册手写字体
     this.font.registerFont({
       familyName: $r('app.string.font_name'), // 注册的字体名称
       familySrc: $r('app.string.font_src')// font文件夹与pages目录同级
     });

     // 注册ExtraLight字体
     this.font.registerFont({
       familyName: 'SourceHanSerif-ExtraLight', // 注册的字体名称
       familySrc: $rawfile('font/SourceHanSerif-ExtraLight.otf') // resources/rawfile目录下
     });
   }
   ```

   其中方案二需要在resources/base/element/string.json中定义font\_name、font\_src。代码如下：

   ```json
   {
     "string": [
       {
         "name": "font_name",
         "value": "HandwrittenFont"
       },
       {
         "name": "font_src",
         "value": "/font/AiNiZaiHuangHunRiLuoShouXieTi-2.ttf"
       }
     ]
   }
   ```

   **说明** 

   应用若需全局使用自定义字体，请在EntryAbility.ets文件的onWindowStageCreate生命周期中，通过windowStage.loadContent回调注册。参考：[自定义字体无法全局使用如何处理](faqs-arkui-571.md)。
2. 在文本组件中通过fontFamily属性使用自定义字体，关键代码如下：

   ```ts
   Text('青鸟华光简美黑')
     .align(Alignment.Center)
     .fontSize(50)
     .fontColor(Color.Blue)
     .fontFamily('QingNiaoHuaGuangJianMeiHei') // 使用青鸟华光简美黑字体
   Text('字魂龙腾楷书')
     .align(Alignment.Center)
     .fontSize(50)
     .fontColor(Color.Blue)
     .fontFamily('ZiHunLongTengKaiShu') // 使用字魂龙腾楷书字体
   Text('手写字体')
     .align(Alignment.Center)
     .fontSize(30)
     .fontColor(Color.Blue)
     .fontFamily('HandwrittenFont') // 使用手写字体
   Text(this.message)
     .align(Alignment.Center)
     .fontSize(50)
     .fontColor(Color.Blue)
     .fontFamily('SourceHanSerif-ExtraLight') // 使用注册字体SourceHanSerif-ExtraLight
   ```

完整示例如下：

```ts
import { Font } from '@kit.ArkUI';

@Entry
@Component
struct FontExample {
  message: string = 'Hello World';
  private uiContext: UIContext = this.getUIContext();
  private font: Font = this.uiContext.getFont();
  aboutToAppear() {
    // 注册青鸟华光简美黑字体
    this.font.registerFont({
      familyName: 'QingNiaoHuaGuangJianMeiHei', // 注册的字体名称
      familySrc: '/font/QingNiaoHuaGuangJianMeiHei-2.ttf' // font文件夹与pages目录同级
    });

    // 注册字魂龙腾楷书字体
    this.font.registerFont({
      familyName: 'ZiHunLongTengKaiShu', // 注册的字体名称
      familySrc: '/font/ZiHunLongTengKaiShu(ShangYongXuShouQuan)-2.ttf' // font文件夹与pages目录同级
    });

    // 注册手写字体
    this.font.registerFont({
      familyName: $r('app.string.font_name'), // 注册的字体名称
      familySrc: $r('app.string.font_src')// font文件夹与pages目录同级
    });

    // 注册ExtraLight字体
    this.font.registerFont({
      familyName: 'SourceHanSerif-ExtraLight', // 注册的字体名称
      familySrc: $rawfile('font/SourceHanSerif-ExtraLight.otf') // resources/rawfile目录下
    });
  }
  build() {
    Column({ space: 10 }) {

      Text('青鸟华光简美黑')
        .align(Alignment.Center)
        .fontSize(50)
        .fontColor(Color.Blue)
        .fontFamily('QingNiaoHuaGuangJianMeiHei') // 使用青鸟华光简美黑字体
      Text('字魂龙腾楷书')
        .align(Alignment.Center)
        .fontSize(50)
        .fontColor(Color.Blue)
        .fontFamily('ZiHunLongTengKaiShu') // 使用字魂龙腾楷书字体
      Text('手写字体')
        .align(Alignment.Center)
        .fontSize(30)
        .fontColor(Color.Blue)
        .fontFamily('HandwrittenFont') // 使用手写字体
      Text(this.message)
        .align(Alignment.Center)
        .fontSize(50)
        .fontColor(Color.Blue)
        .fontFamily('SourceHanSerif-ExtraLight') // 使用注册字体SourceHanSerif-ExtraLight
      Text(this.message)
        .align(Alignment.Center)
        .fontSize(50)
        .fontColor(Color.Blue)
    }
    .width('100%')
    .margin({ top: 30 })
  }
}
```

**注意事项**：

通过downloadFile下载的字体文件，在调用registerFont注册自定义字体时，若直接使用下载时使用的沙箱路径，会出现设置失败的现象，解决上述问题需要在沙箱路径前加上file://来使用实时沙箱路径字体，示例如下：

```ts
import { BusinessError, request } from '@kit.BasicServicesKit';
import { zlib } from '@kit.BasicServicesKit';
import { Font } from '@kit.ArkUI';

function getFileNameFromUrl(url: string): string {
  const segments = url.split('/');
  let tmp = segments.pop() || '';
  if (tmp.indexOf('?') != -1) {
    return tmp.split('?')[0];
  }
  return tmp;
};

@Entry
@Component
struct Index {
  private url: string = 'xxxxxxxxxxxxxx';// 需替换成自己的下载网址https://ziyuan.guwendao.net/font/yyys.zip'
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.getUIContext().getHostContext();
  private font: Font = this.uiContext.getFont();
  message: string = 'Go Next Page';

  DownLoad() {
    let config: request.agent.Config = {
      action: request.agent.Action.DOWNLOAD,
      url: this.url,
      overwrite: true,
      method: 'GET',
      saveas: this.context?.filesDir + '/myFonts/' + getFileNameFromUrl(this.url),
      mode: request.agent.Mode.BACKGROUND,
      gauge: true,
      retry: false
    };
    request.agent.create(this.context, config).then((task: request.agent.Task) => {
      task.start((err: BusinessError) => {
        if (err) {
          console.error(`Failed to start the upload task, Code: ${err.code}  message: ${err.message}`);
          return;
        }
      });
      task.on('progress', async (progress) => {
        console.warn(`/Request download status ${progress.state}, downloaded ${progress.processed}`);
      });
      task.on('completed', async () => {
        console.warn(`/Request download completed`);
        // 解压字体文件
        let inFile = this.context?.filesDir + '/myFonts/' + getFileNameFromUrl(this.url);
        let outFileDir = this.context?.filesDir + '/myFonts';
        let options: zlib.Options = {
          level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION
        };
        try {
          zlib.decompressFile(inFile, outFileDir, options).then(() => {
            let uri = 'file:/' + this.context?.filesDir + '/myFonts/' + 'yyys.ttf';
            console.info('沙箱路径' + uri);
            this.url = uri;
          }).then(() => {
            // 注册字体
            this.font.registerFont({
              familyName: 'yyys',
              familySrc: this.url
            });
          }
          ).catch((errData: BusinessError) => {
            console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
          });
        } catch (errData) {
          let code = (errData as BusinessError).code;
          let message = (errData as BusinessError).message;
          console.error(`errData is errCode:${code}  message:${message}`);
        }
      });
    }).catch((err: BusinessError) => {
      console.error(`Failed to create a download task, Code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Column({ space: 30 }) {
      Button('点击下载使用字体')
        .onClick(() => {
          this.DownLoad();
        })
      Text(this.message)
        .id('Go Next Page')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .fontFamily('yyys')
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }
}
```

常见FAQ

Q：API18之后，如何在EntryAbility中怎么注册全局字体，直接使用font会提示警告？

A：font.registerFont从APIversion18开始废弃，建议使用[registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)。

Q：在注册自定义字体registerFont时，需传入参数familySrc仅支持string、Resource类型，如何将base64编码的字体注册为可供使用的自定义字体？

A：将base64编码的字体数据转换为字体文件，通过buffer.from的方法，将base64编码格式的字符串创建为新的Buffer对象，用fileIo.writeSync方法将转换好的Buffer对象写入文件。转换代码如下：

```ts
import { buffer } from '@kit.ArkTS'; 
import { fileIo } from '@kit.CoreFileKit'; 
import { common } from '@kit.AbilityKit'; 
import { fileUri } from "@kit.CoreFileKit"; 
import { hilog } from '@kit.PerformanceAnalysisKit'; 

// 获取应用上下文和沙箱文件目录
let context = this.getUIContext() as common.UIAbilityContext; 
let filesDir = context.filesDir; 

/**
 * 将Base64编码的字体文件写入沙箱文件系统
 * @param data Base64 字符串（含数据类型前缀，如"data:font/ttf;base64,"）
 * @returns 返回文件的沙箱路径URI
 */
export async function writeFontFile(data: string): Promise<string> { 
  let uri = ''; 
  try { 
    // 构造文件路径（目标文件名改为字体格式，如font.ttf）
    let filePath = filesDir + "/font.ttf"; 
    // 获取文件URI
    uri = fileUri.getUriFromPath(filePath); 
    // 以读写模式打开文件（若文件不存在则创建）
    let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE); 
    // 正则表达式去除Base64数据前缀（如"data:font/ttf;base64,"）
    const reg = new RegExp("data:font/\\w+;base64,"); 
    const base64 = data.replace(reg, "");
    // 将Base64字符串转换为字节数组
    const dataBuffer = buffer.from(base64, 'base64'); 
    // 将字节数组写入文件
    let writeLen = fileIo.writeSync(file.fd, dataBuffer.buffer); 
    // 关闭文件
    fileIo.closeSync(file); 
  } 
  catch (error) { 
    hilog.error(0xA0c0d0, 'Error', error.code); 
  } 
  return uri; 
}
```
