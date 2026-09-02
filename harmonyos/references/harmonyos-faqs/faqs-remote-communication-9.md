---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-9
title: rcp怎么在请求和拦截器中增加query参数
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp怎么在请求和拦截器中增加query参数
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:4a950e30a9e5c7df3493e841b162b57f813e41d9c4b1e2e52e5bbd119329ac0e
---

## 问题现象

rcp请求过程中，如何增加query参数，以及在请求拦截场景，如何在拦截器中增加query参数？

## 背景知识

* [拦截器](../harmonyos-guides/remote-communication-interceptconfig.md)：使用拦截器可以便捷地对HTTP的请求与响应进行修改，您可以创建拦截器链，按需定制一组拦截器对网络请求/响应进行修改。[Remote Communication Kit](../harmonyos-references/remote-communication-api.md)模块提供了拦截器能力，在[SessionConfiguration](../harmonyos-references/remote-communication-rcp.md#sessionconfiguration)中添加[Interceptor](../harmonyos-references/remote-communication-rcp.md#interceptor)参数，传入自定义的拦截器，即可在HTTP请求和响应的过程中添加拦截器功能。
* [addQueryValue](../harmonyos-references/js-apis-uri.md#addqueryvalue12)在当前URI对象上添加查询参数后返回新的URI对象，保持原有URI对象不变。

## 解决方案

在rcp请求时，使用[uri.URI](../harmonyos-references/js-apis-uri.md#uri)接口输入请求资源地址构建URI类，使用addQueryValue接口添加参数。在拦截场景中，新建一个自定义的拦截器，拦截器中使用addQueryValue接口添加参数，自定义拦截器传入SessionConfiguration中，在创建rcp会话时，作为入参传入，具体示例代码如下：

```screen
import uri from '@ohos.uri';
import { rcp } from '@kit.RemoteCommunicationKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { url } from '@kit.ArkTS';

// 模拟拦截器开关
export class InterceptorSwitch {
  isNeedInterceptor: boolean = true;

  public constructor(isNeedInterceptor: boolean) {
    this.isNeedInterceptor = isNeedInterceptor;
  }
}

// 定义RequestUrlChangeInterceptor拦截器
export class RequestUrlChangeInterceptor implements rcp.Interceptor {
  private readonly interceptorSwitch: InterceptorSwitch;

  constructor(interceptorSwitch: InterceptorSwitch) {
    this.interceptorSwitch = interceptorSwitch;
  }

  // 自定义请求处理逻辑
  async intercept(context: rcp.RequestContext, next: rcp.RequestHandler): Promise<rcp.Response> {
    if (this.interceptorSwitch.isNeedInterceptor) {
      console.info('[RequestUrlChangeInterceptor]: Network need Interceptor');
      console.info('[RequestUrlChangeInterceptor] href: ' + context.request.url.href);
      let uriBuilder = new uri.URI(context.request.url.href);
      let finalUrl = uriBuilder.addQueryValue('r', '0').toString();
      console.log('[RequestUrlChangeInterceptor] finalUrl: ' + finalUrl);
      context.request.url = url.URL.parseURL(finalUrl);
    } else {
      console.info('[RequestUrlChangeInterceptor]: Network do not need Interceptor');
    }
    return next.handle(context);
  }
}

@Entry
@Component
struct Index {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  savePath = this.context.filesDir;
  needInterceptor = new InterceptorSwitch(true);

  build() {
    RelativeContainer() {
      Button('RCP Add Query Value')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let downloadUrl: string = '';
          try {
            // 下载链接需根据自身业务自行配置
            downloadUrl = this.context.resourceManager.getStringSync($r('app.string.download_url').id);
          } catch (error) {
            console.error(`getStringSync failed, error code: ${error.code}, message: ${error.message}.`);
          }
          if (downloadUrl === '') {
            return;
          }

          let uriBuilder = new uri.URI(downloadUrl);
          let finalUrl = uriBuilder.addQueryValue('pid', 'ImgRaw');
          let finalUrlStr = finalUrl.toString();
          console.log('Hello World: ' + finalUrlStr);
          let downloadToFile: rcp.DownloadToFile = {
            kind: 'folder',
            path: this.savePath // 请根据自身业务选择合适的路径
          } as rcp.DownloadToFile;

          const sessionConfig: rcp.SessionConfiguration = {
            interceptors: [
              new RequestUrlChangeInterceptor(this.needInterceptor),
            ],
          };
          const session = rcp.createSession(sessionConfig);
          session.downloadToFile(finalUrlStr, downloadToFile).then((response) => {
            if (response) {
              console.info(`Succeeded in getting the url ${JSON.stringify(response.request.url)}`);
            }
          }).catch((err: BusinessError) => {
            console.error(`DownloadToFile failed, the error message is ${JSON.stringify(err)}`);
          });
        });
    }
    .height('100%')
    .width('100%');
  }
}
```
