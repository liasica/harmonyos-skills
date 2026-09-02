---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-22
title: 弹窗点击允许后没有进行后续对应操作
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 弹窗点击允许后没有进行后续对应操作
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e19b349eecdc6aa698f049e9bbfb696bee612b10fab81f1a95b22fe6c31e00d5
---

## 问题现象

弹窗询问“检测到剪贴板有内容，是否允许查询商品？”，点击允许后没有自动进行商品搜索。

## 背景知识

[剪贴板](../harmonyos-references/js-apis-pasteboard.md)为开发者提供数据的复制粘贴能力。当需要使用复制粘贴等功能时，例如：复制文字内容到备忘录中粘贴，复制图库照片到文件管理粘贴，就可以通过剪贴板来完成。

* 判断系统剪贴板中是否有内容：[SystemPasteboard.hasData](../harmonyos-references/js-apis-pasteboard.md#hasdata9)。
* 判断系统剪贴板中是否有内容：[SystemPasteboard.getData](../harmonyos-references/js-apis-pasteboard.md#getdata9)。
* [自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。

## 问题定位

1. 应用外进行复制内容，打开应用，会弹出弹窗，确认弹窗允许按钮是否可以点击。
2. 复制不同内容进行区别定位，可发现复制口令内容可以成功跳转搜索，其他内容直接关闭申请授权弹窗。

## 分析结论

由于剪贴板权限申请前未进行内容识别，导致每次用户进入APP，只要剪贴板存有内容，就无差别弹框要求授权。

## 修改建议

* 场景一：

  在进入应用时，判断剪切板内容是普通文本复制还是口令复制。仅在确认为口令复制时，才会弹出窗口请求用户授权与查询商品。

  实现方案：

  1. 获取系统剪贴板对象。

     ```ts
     let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
     ```
  2. 定义要检测的模式数组。

     ```ts
     let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.NUMBER];
     ```
  3. 先将传入的patterns数组和检测得到的data数组分别进行排序（使用sort方法），然后将排序后的数组元素连接成字符串（使用join('')）再进行比较。其目的为看期望检测的所有模式是否都在剪贴板中被找到了，如果两个处理后的字符串相等，意味着所有期望的模式都在剪贴板里被检测到了，就会执行后续获取剪贴板数据的相关操作。只要符合这个格式的剪贴板内容都会触发后续操作。

     ```ts
     systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
       // 对数组排序并转换成字符串。且跟剪贴板中的数据比较，如果两个处理后的字符串相等，意味着所有期望的模式都在剪贴板里被检测到了。
       if (patterns.sort().join('') == data.sort().join('')) {
         console.info('All needed patterns detected, next get data');
         try {
           // 获取剪贴板内容
           let result = this.getPaste();
           console.info('Succeeded in getting PasteData.', result);
         } catch (err) {
           console.error(`Failed to get PasteData. Cause: ${err.message}`);
         }
         ;
       } else {
         console.info('Not all needed patterns detected, no need to get data.');
       }
     });
     ```
  4. 在进行权限申请之前，需要在module.json5中按需声明ohos.permission.READ\_PASTEBOARD权限以访问剪贴板。参考[向用户申请授权](../best-practices/bpta-permission-application.md#section1816918297167)。
  5. 当权限被授予时，尝试从系统剪贴板获取数据，如果成功则从pasteData中获取主要文本数据。如果权限未被授予，则根据this.permission\_state的状态来决定是否向用户请求权限或者进行其他处理。

     ```ts
     async getPaste(): Promise<string> {
       // 校验权限 没有授权的话去获取授权
       if (this.grantStatus != abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
         const permissions: Array<Permissions> = ['ohos.permission.READ_PASTEBOARD'];
         // 申请权限
         this.reqPermissionsFromUser(permissions);
       }

       // 校验是否获取授权
       if (this.grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
         try {
           // 获取系统剪贴板对象
           let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
           let pasteData = await systemPasteboard.getData();
           return pasteData.getPrimaryText();
         } catch (err) {
           return '';
         }
       }

       return '';
     }
     ```

  完整代码如下：

  ```ts
  import { BusinessError, pasteboard } from '@kit.BasicServicesKit';
  import { abilityAccessCtrl, PermissionRequestResult, Permissions } from '@kit.AbilityKit';

  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';
    grantStatus: abilityAccessCtrl.GrantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;

    aboutToAppear(): void {
      let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
      let patterns: Array<pasteboard.Pattern> = [pasteboard.Pattern.URL, pasteboard.Pattern.NUMBER];
      systemPasteboard.detectPatterns(patterns).then((data: Array<pasteboard.Pattern>) => {
        // 对数组排序并转换成字符串。且跟剪贴板中的数据比较，如果两个处理后的字符串相等，意味着所有期望的模式都在剪贴板里被检测到了。
        if (patterns.sort().join('') == data.sort().join('')) {
          console.info('All needed patterns detected, next get data');
          try {
            // 获取剪贴板内容
            let result = this.getPaste();
            console.info('Succeeded in getting PasteData.', result);
          } catch (err) {
            console.error(`Failed to get PasteData. Cause: ${err.message}`);
          }
          ;
        } else {
          console.info('Not all needed patterns detected, no need to get data.');
        }
      });
    }

    reqPermissionsFromUser(permissions: Array<Permissions>): void {
      let context: Context = this.getUIContext().getHostContext() as Context;
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
      atManager.requestPermissionsFromUser(context, permissions).then((data: PermissionRequestResult) => {
        let grantStatus: Array<number> = data.authResults;
        let length: number = grantStatus.length;
        for (let i = 0; i < length; i++) {
          if (grantStatus[i] === 0) {
            // 用户授权，可以继续访问目标操作
            this.grantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED;
          } else {
            // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限
            this.grantStatus = abilityAccessCtrl.GrantStatus.PERMISSION_DENIED;
            this.getUIContext().getPromptAction().showToast({ message: '用户拒绝授权' });
            return;
          }
        }
        // 授权成功
      }).catch((err: BusinessError) => {
        console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
      });
    }

    async getPaste(): Promise<string> {
      // 校验权限 没有授权的话去获取授权
      if (this.grantStatus != abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        const permissions: Array<Permissions> = ['ohos.permission.READ_PASTEBOARD'];
        // 申请权限
        this.reqPermissionsFromUser(permissions);
      }

      // 校验是否获取授权
      if (this.grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
        try {
          // 获取系统剪贴板对象
          let systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
          let pasteData = await systemPasteboard.getData();
          return pasteData.getPrimaryText();
        } catch (err) {
          return '';
        }
      }

      return '';
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.message = 'Welcome';
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 场景二：

  在进入应用时，剪切板内容是复制的图库图片如何获取并展示。

  实现方案：

  1. [粘贴控件](../harmonyos-guides/pastebutton.md)：粘贴控件是一种特殊的系统安全控件，它允许应用在用户的授权下无提示地读取剪贴板数据。

     示例代码如下：

     ```ts
     import { common } from '@kit.AbilityKit';
     import { image } from '@kit.ImageKit';
     import { pasteboard } from '@kit.BasicServicesKit';
     import { fileIo as fs } from '@kit.CoreFileKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Entry
     @Component
     struct ImageClipboardAbility {
       @State pastePixelMap: image.PixelMap | null = null; // 粘贴后的图片
       @State savePastePath: string = '';

       build() {
         Column({ space: 20 }) {
           Text('剪贴板图片读写示例')
             .fontSize(24)
             .margin(20);

           Image(this.pastePixelMap ? this.pastePixelMap : $r('app.media.startIcon'))
             .width(150);
           PasteButton()
             .padding({
               top: 12,
               bottom: 12,
               left: 24,
               right: 24
             })
             .onClick((event: ClickEvent, result: PasteButtonOnClickResult) => {
               console.info(`event：${event}`);
               if (PasteButtonOnClickResult.SUCCESS === result) {
                 pasteboard.getSystemPasteboard().getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
                   if (err) {
                     console.error(`Failed to get paste data. Code is ${err.code}, message is ${err.message}`);
                     return;
                   }
                   let type: string = pasteData.getPrimaryMimeType();
                   let uri: string = pasteData.getPrimaryUri();
                   console.info(`gettype:${type}`);
                   console.info(`geturi:${uri}`);
                   try {
                     const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                     let file1 = fs.openSync(uri);
                     const dateStr = (new Date().getTime()).toString();
                     // 临时文件目录
                     let newPath = context.cacheDir + `/${dateStr + file1.name}`;
                     this.savePastePath = newPath;
                     let file2 = fs.openSync(newPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);

                     fs.copyFileSync(file1.fd, file2.fd);
                     fs.closeSync(file1);
                     fs.closeSync(file2);
                   } catch (e) {
                     console.error(e);
                   }

                   const imageSourceObj: image.ImageSource = image.createImageSource(this.savePastePath);
                   try {
                     imageSourceObj.createPixelMap().then((pixelMap: image.PixelMap) => {
                       console.info('Succeeded in creating pixelMap object through image decoding parameters.');
                       this.pastePixelMap = pixelMap;
                     }).catch((error: BusinessError) => {
                       console.error(`Failed to create pixelMap object through image decoding parameters, error.code ${error.code}, error.message ${error.message}`);
                     });
                   } catch (e) {
                     console.error(e);
                   }
                 });
               }
             });
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)
         .padding(20);
       }
     }
     ```
  2. [getData](../harmonyos-references/js-apis-pasteboard.md#getdata9)：允许应用读取剪贴板，需配置"ohos.permission.READ\_PASTEBOARD"。具体权限配置可参考[声明权限](../harmonyos-guides/declare-permissions.md)。

     示例代码如下：

     ```ts
     import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';
     import { image } from '@kit.ImageKit';
     import { pasteboard } from '@kit.BasicServicesKit';
     import { fileIo as fs } from '@kit.CoreFileKit';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Entry
     @Component
     struct ImageClipboardAbility {
       @State pixelMap: image.PixelMap | null = null; // 粘贴后的图片
       @State savePath: string = '';
       permissions: Array<Permissions> = ['ohos.permission.READ_PASTEBOARD'];

       reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
         let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
         // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
         atManager.requestPermissionsFromUser(context, permissions).then((data) => {
           let grantStatus: Array<number> = data.authResults;
           let length: number = grantStatus.length;
           for (let i = 0; i < length; i++) {
             if (grantStatus[i] === 0) {
               // 用户授权，可以继续访问目标操作。
             } else {
               // 用户拒绝授权，提示用户必须授权才能访问当前页面的功能，并引导用户到系统设置中打开相应的权限。
               return;
             }
           }
           // 授权成功。
         }).catch((err: BusinessError) => {
           console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
         });
       }

       aboutToAppear() {
         const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
         this.reqPermissionsFromUser(this.permissions, context);
       }

       onPasteImage() {
         const systemPasteboard: pasteboard.SystemPasteboard = pasteboard.getSystemPasteboard();
         systemPasteboard.getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
           if (err) {
             console.error('Failed to get PasteData. Cause: ' + err.message);
             return;
           }
           let type: string = pasteData.getPrimaryMimeType();
           let uri: string = pasteData.getPrimaryUri();
           console.info(`gettype:${type}`);
           console.info(`geturi:${uri}`);

           try {
             const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
             let file1 = fs.openSync(uri);
             const dateStr = (new Date().getTime()).toString();
             // 临时文件目录
             let newPath = context.cacheDir + `/${dateStr + file1.name}`;
             this.savePath = newPath;
             let file2 = fs.openSync(newPath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);

             fs.copyFileSync(file1.fd, file2.fd);
             fs.closeSync(file1);
             fs.closeSync(file2);
           } catch (e) {
             console.error(e);
           }

           const imageSourceObj: image.ImageSource = image.createImageSource(this.savePath);
           try {
             imageSourceObj.createPixelMap().then((pixelMap: image.PixelMap) => {
               console.info('Succeeded in creating pixelMap object through image decoding parameters.');
               this.pixelMap = pixelMap;
             }).catch((error: BusinessError) => {
               console.error(`Failed to create pixelMap object through image decoding parameters, error.code ${error.code}, error.message ${error.message}`);
             });
           } catch (e) {
             console.error(e);
           }
         });
       }

       build() {
         Column({ space: 20 }) {
           Text('剪贴板图片读写示例')
             .fontSize(24)
             .margin(20);
           Image(this.pixelMap ? this.pixelMap : $r('app.media.startIcon'))
             .width(150);
           Button('粘贴').onClick(() => {
             this.onPasteImage();
           });
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)
         .padding(20);
       }
     }
     ```
