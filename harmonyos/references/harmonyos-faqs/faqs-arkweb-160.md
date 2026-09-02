---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-160
title: Web组件使用JavaScriptProxy注入JsBridge对象时，Jsb Permission Denied报错如何解决
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件使用JavaScriptProxy注入JsBridge对象时，Jsb Permission Denied报错如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e8764166a955967206da48aef1b690aef33a306730ec03f7a1c3668765bfe056
---

## 问题现象

Web组件用file协议加载位于Download目录下的html文件，用JavaScriptProxy注入JsBridge对象，但前端页面无法调用注入的JsBridge对象的方法，前端页面报错为Uncaught Error：Jsb Permission Denied。部分问题代码如下：

```screen
jsBridgePermission: JsBridgePermission = {
  javascriptProxyPermission: {
    urlPermissionList: [       // Object级权限，如果匹配，所有Method都授权
      {
        scheme: 'resource',    // 精确匹配，不能为空
        host: 'rawfile',       // 精确匹配，不能为空
        port: '',              // 精确匹配，为空不检查
        path: ''               // 前缀匹配，为空不检查
      },
      {
        scheme: 'file',   // 精确匹配，不能为空
        host: '',   // 精确匹配，不能为空
        port: '',          // 精确匹配，为空不检查
        path: ''           // 前缀匹配，为空不检查
      }
    ],
    methodList: [
      {
        methodName: 'test',
        urlPermissionList: [   // Method级权限
          {
            scheme: 'resource', // 精确匹配，不能为空
            host: 'rawfile',   // 精确匹配，不能为空
            port: '',          // 精确匹配，为空不检查
            path: ''           // 前缀匹配，为空不检查
          }
        ]
      }
    ]
  }
}
```

## 背景知识

* [前端页面调用应用侧函数](../harmonyos-guides/web-in-page-app-function-invoking.md)：开发者使用Web组件将应用侧代码注册到前端页面中，注册完成之后，前端页面中使用注册的对象名称就可以调用应用侧的函数，实现在前端页面中调用应用侧方法。
* [JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)：定义要注入的JavaScript对象。该方法有一个可选参数permission——JSON字符串，默认为空，通过该字符串配置JsBridge的权限管控，可以定义object、method一级的url白名单。

## 问题定位

根据问题现象及报错信息，可知是JsBridge权限相关问题。发现代码中配置了JavaScriptProxy的permission参数，考虑JsBridge使用受限是由于该参数对JsBridge权限进行了管控，排查该参数配置：

1. scheme（协议）和host（域名）参数是否为空，若为空则会报错。
2. 是否配置了调用失败的JsBridge方法的method级白名单。以file协议为例，使用file协议加载html，若只在object级配置了file协议的白名单、方法A的method级未配置file协议的白名单，将无法调用方法A；反过来也一样，若只在方法A的method级配置了file协议、object级中未配置file协议的白名单，也无法调用方法A。

## 分析结论

要使用JavaScriptProxy的permission对JsBridge方法的调用进行权限管控，JavaScriptProxy的permission参数配置需要遵循以下原则：

* scheme（协议）和host（域名）参数不可为空。
* 可以只配置object级的白名单，该白名单对所有JsBridge方法生效。
* 若JsBridge方法A设置了method级白名单，那么**方法A最终的白名单是object级白名单与其method级白名单的交集**。比如方法A的method级配置了scheme为file、host为docs的白名单，那么object级也必须设置scheme为file、host为docs的白名单；反过来也是如此，若object级配置了scheme为file、host为docs的白名单，而方法A需要在对应场景允许调用的话，方法A的method级也需要配置同样scheme和host的白名单。
* file协议的host为第一级目录名称，path（路径）可为空，不为空时需要注意object级和method级白名单的交集原则，object级和method级的path不能冲突（完全相同或method级path为object级path的子目录）。

## 修改建议

以file协议加载Download目录下的html文件场景为例，要允许注入的JsBridge的方法A被调用，可参考如下修改建议：

* 不需要对JsBridge进行权限管控时，不配置JavaScriptProxy的permission参数即可。
* 只需要对JsBridge的所有方法统一权限管控时，只配置JavaScriptProxy的permission参数的object级白名单即可，配置项如下（使用对象形式方便修改和展示，实际使用时需将对象转换为JSON字符串格式）：

  ```screen
  jsBridgePermission: JsBridgePermission = {
    javascriptProxyPermission: {
      urlPermissionList: [ // Object级权限，如果匹配，所有Method都授权
        {
          scheme: 'resource', // 精确匹配，不能为空
          host: 'rawfile', // 精确匹配，不能为空
          port: '', // 精确匹配，为空不检查
          path: ''               // 前缀匹配，为空不检查
        },
        {
          scheme: 'file', // 精确匹配，不能为空
          host: 'docs', // 精确匹配，不能为空
          port: '', // 精确匹配，为空不检查
          path: '/storage/Users/currentUser/Download/'           // file协议加载HTML时，所有JsBridge方法只允许Download目录下的HTML调用
        },
      ]
    }
  };
  ```

* 需要针对JsBridge的某些方法进行权限管控时，应同时在object级和该方法的method级配置相同scheme、host、port的白名单，且path不能冲突（完全相同或method级path为object级path的子目录）。配置项如下（使用对象形式方便修改和展示，实际使用时需将对象转换为JSON字符串格式）：

  ```screen
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { fileIo, picker } from '@kit.CoreFileKit';
  import { common } from '@kit.AbilityKit';
  import { JSON } from '@kit.ArkTS';

  class TestClass {
    constructor() {
    }

    test(param: string): string {
      return `${param}->Hello, I am ets!`;
    }
  }

  interface JsBridgePermission {
    javascriptProxyPermission: JavascriptProxyPermission;
  }

  interface JavascriptProxyPermission {
    urlPermissionList: UrlPermission[];
    methodList?: MethodPermission[];
  }

  interface MethodPermission {
    urlPermissionList: UrlPermission[];
    methodName: string;
  }

  interface UrlPermission {
    scheme: string;
    host: string;
    port: string;
    path: string;
  }

  @Entry
  @Component
  struct Index {
    webviewController: webview.WebviewController = new webview.WebviewController();
    // 声明需要注册的对象
    testObj: TestClass = new TestClass();
    jsBridgePermission: JsBridgePermission = {
      javascriptProxyPermission: {
        urlPermissionList: [ // Object级权限，如果匹配，所有Method都授权
          {
            scheme: 'resource', // 精确匹配，不能为空
            host: 'rawfile', // 精确匹配，不能为空
            port: '', // 精确匹配，为空不检查
            path: ''               // 前缀匹配，为空不检查
          },
          {
            scheme: 'file', // 精确匹配，不能为空
            host: 'docs', // 精确匹配，不能为空
            port: '', // 精确匹配，为空不检查
            path: '/storage/Users/currentUser/'           // file协议加载HTML时，所有JsBridge方法只允许docs/storage/Users/currentUser/目录下的HTML调用
          }
        ],
        methodList: [
          {
            methodName: 'test',
            urlPermissionList: [ // Method级权限
              {
                scheme: 'resource', // 精确匹配，不能为空
                host: 'rawfile', // 精确匹配，不能为空
                port: '', // 精确匹配，为空不检查
                path: ''           // 前缀匹配，为空不检查
              },
              {
                scheme: 'file', // 精确匹配，不能为空
                host: 'docs', // 精确匹配，不能为空
                port: '', // 精确匹配，为空不检查
                path: '/storage/Users/currentUser/Download/'           // file协议加载HTML时，test方法只允许Download目录下的HTML调用
              }
            ]
          }
        ]
      }
    };

    build() {
      Column({ space: 20 }) {
        Button('将index.html下载到Download目录')
          .type(ButtonType.ROUNDED_RECTANGLE)
          .onClick(async () => {
            try {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let documentSaveOptions = new picker.DocumentSaveOptions();
              documentSaveOptions.newFileNames = ['index.html'];
              let documentPicker = new picker.DocumentViewPicker(context);
              documentPicker.save(documentSaveOptions).then((documentSelectResult: Array<string>) => {
                console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' +
                JSON.stringify(documentSelectResult));
                let path = documentSelectResult[0];
                let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE);
                let data = context.resourceManager.getRawFileContentSync('index.html');
                fileIo.writeSync(file.fd, data.buffer);
                fileIo.closeSync(file);
                console.info(`文件写入成功`);
              }).catch((err: BusinessError) => {
                console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
              });
            } catch (err) {
              console.error(`Failed to getRdbStore. code: ${err.code}, message: ${err.message}`);
            }
          });

        Button('选择Download下index.html')
          .onClick(() => {
            this.choseHtml();
          });
        Web({ src: '', controller: this.webviewController })
          .javaScriptProxy({
            object: this.testObj,
            name: 'testObjName',
            methodList: ['test'],
            controller: this.webviewController,
            asyncMethodList: [],
            permission: JSON.stringify(this.jsBridgePermission)
          })
          .fileAccess(true)
          .javaScriptAccess(true)
          .geolocationAccess(false)
          .domStorageAccess(true);
      };
    }

    choseHtml() {
      const documentSelectOptions = new picker.DocumentSelectOptions();
      documentSelectOptions.maxSelectNumber = 1;
      documentSelectOptions.fileSuffixFilters = ['文档|.html'];
      let uris: Array<string> = [];
      let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const documentViewPicker = new picker.DocumentViewPicker(context);
      documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
        uris = documentSelectResult;
        console.info(uris[0]); // file://docs/storage/Users/currentUser/Download/index.html
        try {
          this.webviewController.loadUrl(uris[0]);
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      }).catch((err: BusinessError) => {
        console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }
  ```

完整示例参考如下：

ArkTS示例代码：

```screen
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, picker } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { JSON } from '@kit.ArkTS';

class TestClass {
  constructor() {
  }

  test(param: string): string {
    return `${param}->Hello, I am ets!`;
  }
}

interface JsBridgePermission {
  javascriptProxyPermission: JavascriptProxyPermission;
}

interface JavascriptProxyPermission {
  urlPermissionList: UrlPermission[];
  methodList?: MethodPermission[];
}

interface MethodPermission {
  urlPermissionList: UrlPermission[];
  methodName: string;
}

interface UrlPermission {
  scheme: string;
  host: string;
  port: string;
  path: string;
}

@Entry
@Component
struct Index {
  webviewController: webview.WebviewController = new webview.WebviewController();
  // 声明需要注册的对象
  testObj: TestClass = new TestClass();
  jsBridgePermission: JsBridgePermission = {
    javascriptProxyPermission: {
      urlPermissionList: [ // Object级权限，如果匹配，所有Method都授权
        {
          scheme: 'resource', // 精确匹配，不能为空
          host: 'rawfile', // 精确匹配，不能为空
          port: '', // 精确匹配，为空不检查
          path: ''               // 前缀匹配，为空不检查
        },
        {
          scheme: 'file', // 精确匹配，不能为空
          host: 'docs', // 精确匹配，不能为空
          port: '', // 精确匹配，为空不检查
          path: '/storage/Users/currentUser/'           // file协议加载HTML时，所有JsBridge方法只允许docs/storage/Users/currentUser/目录下的HTML调用
        }
      ],
      methodList: [
        {
          methodName: 'test',
          urlPermissionList: [ // Method级权限
            {
              scheme: 'resource', // 精确匹配，不能为空
              host: 'rawfile', // 精确匹配，不能为空
              port: '', // 精确匹配，为空不检查
              path: ''           // 前缀匹配，为空不检查
            },
            {
              scheme: 'file', // 精确匹配，不能为空
              host: 'docs', // 精确匹配，不能为空
              port: '', // 精确匹配，为空不检查
              path: '/storage/Users/currentUser/Download/'           // file协议加载HTML时，test方法只允许Download目录下的HTML调用
            }
          ]
        }
      ]
    }
  };

  build() {
    Column({ space: 20 }) {
      Button('将index.html下载到Download目录')
        .type(ButtonType.ROUNDED_RECTANGLE)
        .onClick(async () => {
          try {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let documentSaveOptions = new picker.DocumentSaveOptions();
            documentSaveOptions.newFileNames = ['index.html'];
            let documentPicker = new picker.DocumentViewPicker(context);
            documentPicker.save(documentSaveOptions).then((documentSelectResult: Array<string>) => {
              console.info('DocumentViewPicker.select successfully, documentSelectResult uri: ' +
              JSON.stringify(documentSelectResult));
              let path = documentSelectResult[0];
              let file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE);
              let data = context.resourceManager.getRawFileContentSync('index.html');
              fileIo.writeSync(file.fd, data.buffer);
              fileIo.closeSync(file);
              console.info(`文件写入成功`);
            }).catch((err: BusinessError) => {
              console.error(`DocumentViewPicker.select failed with err, code is: ${err.code}, message is: ${err.message}`);
            });
          } catch (err) {
            console.error(`Failed to getRdbStore. code: ${err.code}, message: ${err.message}`);
          }
        });

      Button('选择Download下index.html')
        .onClick(() => {
          this.choseHtml();
        });
      Web({ src: '', controller: this.webviewController })
        .javaScriptProxy({
          object: this.testObj,
          name: 'testObjName',
          methodList: ['test'],
          controller: this.webviewController,
          asyncMethodList: [],
          permission: JSON.stringify(this.jsBridgePermission)
        })
        .fileAccess(true)
        .javaScriptAccess(true)
        .geolocationAccess(false)
        .domStorageAccess(true);
    };
  }

  choseHtml() {
    const documentSelectOptions = new picker.DocumentSelectOptions();
    documentSelectOptions.maxSelectNumber = 1;
    documentSelectOptions.fileSuffixFilters = ['文档|.html'];
    let uris: Array<string> = [];
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    const documentViewPicker = new picker.DocumentViewPicker(context);
    documentViewPicker.select(documentSelectOptions).then((documentSelectResult: Array<string>) => {
      uris = documentSelectResult;
      console.info(uris[0]); // file://docs/storage/Users/currentUser/Download/index.html
      try {
        this.webviewController.loadUrl(uris[0]);
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Invoke documentViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

html示例代码：

```screen
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no"/>
    <style>
        button {
          width: 200px;
          height: 60px;
          font-size: 20px;
        }
        #demo {
          font-size: 24px;
          font-weight: 700;
        }
    </style>
</head>
<body>
<button class="inline-style-button" type="button" onclick="callArkTSMethod()">
    CallArkTS Method
</button>
<p id="demo"></p>
<script>
    function callArkTSMethod() {
      let str = testObjName.test("Hi, I am H5.");
      document.getElementById("demo").innerHTML = str;
    }
</script>
</body>
</html>
```

## 总结

要允许注入的JsBridge的方法A被调用，可参考如下修改建议：

* 不需要对JsBridge进行权限管控时，不配置JavaScriptProxy的permission参数即可。
* 只需要对JsBridge的所有方法统一权限管控时，只配置JavaScriptProxy的permission参数的object级白名单即可。
* 需要针对JsBridge的某些方法进行权限管控时，应同时在object级和该方法的method级配置相同scheme、host、port的白名单，且path不能冲突（完全相同或method级path为object级path的子目录）。
