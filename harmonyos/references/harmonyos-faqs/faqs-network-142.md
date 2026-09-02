---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-142
title: 如何设置网络代理
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 如何设置网络代理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:bf7664d5a76e9c580c06283658d299f3f2774b8201013bdc8be1e318713e45e1
---

## 问题现象

* 场景一：如何为网络请求添加代理配置。
* 场景二：rcp请求通过代理访问部分域名时报错，错误码为1007900056，提示"Failure when receiving data from the peer"。使用curl通过同一代理可以正常访问目标域名，但rcp请求无法通过。

## 背景知识

* [connection.setAppHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectionsetapphttpproxy11)：设置应用级Http代理配置信息。
* [connection.getDefaultHttpProxy](../harmonyos-references/js-apis-net-connection.md#connectiongetdefaulthttpproxy10)：获取网络的默认代理配置信息。
* [ProxyConfiguration](../harmonyos-references/remote-communication-rcp.md#proxyconfiguration)：ProxyConfiguration接口允许开发者为会话中的HTTP请求配置代理设置，从而提供在系统、自定义或无代理之间进行选择的灵活性。
* [WebProxy](../harmonyos-references/remote-communication-rcp.md#webproxy)：自定义代理配置，允许指定代理URL、排除列表和安全配置，支持通过createTunnel控制代理隧道创建时机。
* [HttpProxy](../harmonyos-references/js-apis-net-connection.md#httpproxy10)：网络代理配置信息。

## 解决方案

* 场景一：

  权限声明，module.json5中配置权限声明：

  使用权限：ohos.permission.INTERNET。

  + 方案一：

    使用connection.setAppHttpProxy接口设置应用级别代理配置信息，会覆盖系统设置的代理配置信息。配置后应用内网络请求如果没有额外配置代理信息，默认执行该方法配置的代理信息。取消代理配置时，使用connection.setAppHttpProxy把host设置为空字符串，port设置为0。

    ```ts
    async setProxyStatus(host: string, port: number) {
        this.isLoading = true;
        try {
          connection.setAppHttpProxy({
            host: host,
            port: port,
            exclusionList: ['XXX']
          } as connection.HttpProxy);
          this.checkProxyStatus();
        } catch (err) {
          this.proxyEnabled = false;
          this.proxyInfo = `设置失败：${JSON.stringify(err)}`;
        } finally {
          this.isLoading = false;
        }
      }
    ```

    connection.getDefaultHttpProxy接口获取网络的默认代理配置信息，如果设置了全局代理，则返回全局代理配置信息。可以通过获取到的信息中host是否为空，port是否大于0，判断应用当前是否开启了网络代理。

    ```ts
    async checkProxyStatus() {
        this.isLoading = true;
        this.proxyInfo = '检测中...';
        try {
          // 获取全局代理详细信息
          let proxyDetail = await connection.getDefaultHttpProxy();

          if (proxyDetail.host.length > 0 && proxyDetail.port > 0) {
            this.proxyEnabled = true;
            this.proxyInfo = `${proxyDetail.host}:${proxyDetail.port}`;
          } else {
            this.proxyEnabled = false;
            this.proxyInfo = `...`;
          }
        } catch (err) {
          this.proxyEnabled = false;
          this.proxyInfo = `检测失败：${JSON.stringify(err)}`;
        } finally {
          this.isLoading = false;
        }
      }
    ```
  + 方案二：

    为单次网络请求配置代理信息。

    httpRequest.request请求时，HttpRequestOptions中的usingProxy代理信息可以自定义设置，无代理或系统设置的代理配置。

    ```ts
    async testHttpProxyRequest() {
        this.isLoading = true;
        this.testResult = '请求中...';
        try {
          const httpRequest = http.createHttp();
          const response = await httpRequest.request(this.url,
            {
              usingProxy: {
                host: this.proxyUrl,
                port: this.proxyPort
              } as connection.HttpProxy
            }
          );
          if (response.responseCode === 200) {
            const result = JSON.stringify(response.result);
            this.testResult = `请求成功 .\n：${result}`;
          } else {
            this.testResult = `请求失败 .\n响应码：${response.responseCode}`;
          }
        } catch (err) {
          this.testResult = `请求异常 .\n错误信息：${JSON.stringify(err)}`;
        } finally {
          this.isLoading = false;
        }
      }
    ```

    rcp请求时，rcp.Configuration中的proxy代理信息允许开发者为会话中的HTTP请求配置代理设置，从而提供在系统、自定义或无代理之间进行选择的灵活性。

    ```ts
    async testRcpProxyRequest() {
        this.isLoading = true;
        this.testResult = '请求中...';
        try {
          const session = rcp.createSession();
          // 自定义proxy
          const configuration: rcp.Configuration = {
            proxy: {
              url: `${this.proxyUrl}:${this.proxyPort}`,
              createTunnel: 'always',
            }
          };
          const request = new rcp.Request(this.url, 'GET');
          request.configuration = configuration;

          session.fetch(request).then((response: rcp.Response) => {
            if (response.statusCode === 200) {
              this.testResult = `请求成功 .\n：${response}`;
            } else {
              this.testResult = `请求失败 .\n响应码：${response.statusCode}`;
            }
            session.close();
          }).catch((err: BusinessError) => {
            console.error(`The error code is ${err.code}, error message is ${JSON.stringify(err)}`);
            session.close();
          });
        } catch (err) {
          this.testResult = `请求异常 .\n错误信息：${JSON.stringify(err)}`;
        } finally {
          this.isLoading = false;
        }
      }
    ```

  完整代码：

  ```ts
  import { connection } from '@kit.NetworkKit';
  import http from '@ohos.net.http';
  import { webview } from '@kit.ArkWeb';
  import { rcp } from '@kit.RemoteCommunicationKit';

  @Entry
  @Component
  struct ProxyCheckPage {
    @State proxyEnabled: boolean = false; // 是否启用代理
    url: string = 'XXX.XXX.XXX'; // 需要替换为开发者需要的请求地址
    proxyUrl: string = 'XXX.XXX.XXX.XXX'; // 需要替换为开发者需要的代理地址
    proxyPort: number = 8888; // 需要替换为开发者需要的代理端口
    @State proxyInfo: string = '未检测'; // 代理信息文本
    @State testResult: string = '未测试'; // 测试请求结果
    @State isLoading: boolean = false; // 加载状态
    webviewController: webview.WebviewController = new webview.WebviewController();

    aboutToAppear(): void {
      this.checkProxyStatus();
    }

    @Styles
    fancy() {
      .width('80%')
      .height(50)
      .enabled(!this.isLoading)
      .margin({ bottom: 15 });
    }

    build() {
      Column() {
        // 检测代理按钮
        Button('一键检测代理状态')
          .fancy()
          .backgroundColor('#007DFF')
          .fontColor(Color.White)
          .onClick(() => this.checkProxyStatus());

        // 设置代理按钮
        Button('设置应用级代理')
          .fancy()
          .backgroundColor('#007DFF')
          .fontColor(Color.White)
          .onClick(() => this.setProxyStatus(this.proxyUrl, this.proxyPort));

        // 取消代理按钮
        Button('取消应用级代理')
          .fancy()
          .backgroundColor('#007DFF')
          .fontColor(Color.White)
          .onClick(() => this.setProxyStatus('', 0));

        Text(`代理启用状态：${this.proxyEnabled ? '已启用' : '未启用'}`)
          .fontSize(16)
          .margin({ bottom: 20 });

        // 代理详细信息展示
        Text('代理详细信息：')
          .fontSize(18)
          .fontWeight(FontWeight.Medium)
          .alignSelf(ItemAlign.Start)
          .margin({ left: 40, bottom: 10 });

        Text(this.proxyInfo)
          .fontSize(14)
          .width('80%')
          .backgroundColor('#F5F7FA')
          .padding(15)
          .borderRadius(8)
          .margin({ bottom: 20 })
          .textAlign(TextAlign.Start);

        // 测试请求按钮
        Button('发起测试请求验证代理')
          .fancy()
          .backgroundColor('#36CFC9')
          .fontColor(Color.White)
          .onClick(() => this.testProxyRequest());

        // http测试请求
        Button('http请求设置代理')
          .fancy()
          .backgroundColor('#36CFC9')
          .fontColor(Color.White)
          .onClick(() => this.testHttpProxyRequest());

        //rcp测试请求按钮
        Button('rcp测试请求设置代理')
          .fancy()
          .backgroundColor('#36CFC9')
          .fontColor(Color.White)
          .onClick(() => this.testRcpProxyRequest());

        Text('测试请求结果：')
          .fontSize(18)
          .fontWeight(FontWeight.Medium)
          .alignSelf(ItemAlign.Start)
          .margin({ left: 40, bottom: 10 });

        Text(this.testResult)
          .fontSize(14)
          .width('80%')
          .backgroundColor('#F5F7FA')
          .padding(15)
          .borderRadius(8)
          .textAlign(TextAlign.Start);
      }
      .width('100%')
      .height('100%')
      .padding(20)
      .backgroundColor(Color.White)
      .justifyContent(FlexAlign.Center);
    }

    async checkProxyStatus() {
      this.isLoading = true;
      this.proxyInfo = '检测中...';
      try {
        // 获取全局代理详细信息
        let proxyDetail = await connection.getDefaultHttpProxy();

        if (proxyDetail.host.length > 0 && proxyDetail.port > 0) {
          this.proxyEnabled = true;
          this.proxyInfo = `${proxyDetail.host}:${proxyDetail.port}`;
        } else {
          this.proxyEnabled = false;
          this.proxyInfo = `...`;
        }
      } catch (err) {
        this.proxyEnabled = false;
        this.proxyInfo = `检测失败：${JSON.stringify(err)}`;
      } finally {
        this.isLoading = false;
      }
    }

    async setProxyStatus(host: string, port: number) {
      this.isLoading = true;
      try {
        connection.setAppHttpProxy({
          host: host,
          port: port,
          exclusionList: ['XXX']
        } as connection.HttpProxy);
        this.checkProxyStatus();
      } catch (err) {
        this.proxyEnabled = false;
        this.proxyInfo = `设置失败：${JSON.stringify(err)}`;
      } finally {
        this.isLoading = false;
      }
    }

    async testProxyRequest() {
      this.isLoading = true;
      this.testResult = '请求中...';
      try {
        const httpRequest = http.createHttp();
        const response = await httpRequest.request(this.url);
        if (response.responseCode === 200) {
          const result = JSON.stringify(response.result);
          this.testResult = `请求成功 .\n：${result}`;
        } else {
          this.testResult = `请求失败 .\n响应码：${response.responseCode}`;
        }
      } catch (err) {
        this.testResult = `请求异常 .\n错误信息：${JSON.stringify(err)}`;
      } finally {
        this.isLoading = false;
      }
    }

    async testHttpProxyRequest() {
      this.isLoading = true;
      this.testResult = '请求中...';
      try {
        const httpRequest = http.createHttp();
        const response = await httpRequest.request(this.url,
          {
            usingProxy: {
              host: this.proxyUrl,
              port: this.proxyPort
            } as connection.HttpProxy
          }
        );
        if (response.responseCode === 200) {
          const result = JSON.stringify(response.result);
          this.testResult = `请求成功 .\n：${result}`;
        } else {
          this.testResult = `请求失败 .\n响应码：${response.responseCode}`;
        }
      } catch (err) {
        this.testResult = `请求异常 .\n错误信息：${JSON.stringify(err)}`;
      } finally {
        this.isLoading = false;
      }
    }
    async testRcpProxyRequest() {
      this.isLoading = true;
      this.testResult = '请求中...';
      try {
        const session = rcp.createSession();
        // 自定义proxy
        const configuration: rcp.Configuration = {
          proxy: {
            url: `${this.proxyUrl}:${this.proxyPort}`,
            createTunnel: 'always',
          }
        };
        const request = new rcp.Request(this.url, 'GET');
        request.configuration = configuration;

        session.fetch(request).then((response: rcp.Response) => {
          if (response.statusCode === 200) {
            this.testResult = `请求成功 .\n：${response}`;
          } else {
            this.testResult = `请求失败 .\n响应码：${response.statusCode}`;
          }
          session.close();
        }).catch((err: BusinessError) => {
          console.error(`The error code is ${err.code}, error message is ${JSON.stringify(err)}`);
          session.close();
        });
      } catch (err) {
        this.testResult = `请求异常 .\n错误信息：${JSON.stringify(err)}`;
      } finally {
        this.isLoading = false;
      }
    }
  }
  ```
* 场景二：

  代理认证应配置在proxy.security.serverAuthentication中，支持basic、ntlm、digest认证方式。目标站点的证书校验配置（requestConfiguration.security）与代理认证不要混在一起。

  remoteValidation设置为skip仅影响目标HTTPS证书校验，不会解决代理CONNECT或代理认证失败问题。若错误日志中tlsDur为0，说明尚未进入目标站TLS校验阶段，不应设置remoteValidation为skip。

  排查步骤如下：

  1. 确认代理支持HTTPS CONNECT到目标域名，使用curl加-v参数查看是否出现CONNECT ...:443并返回200 Connection established。
  2. 在rcp中显式设置createTunnel为always做对比测试，HTTPS默认应走隧道，但显式设置能排除实现或识别问题。
  3. 将代理认证放在proxy.security.serverAuthentication中，与目标站点的security配置分离。
  4. 去掉remoteValidation为skip的设置，除非能确认是证书链问题。
  5. 换一个普通HTTPS站点和同一代理测试，若普通站点可通但目标站点被重置，问题可能在代理出口或目标站限制，而非rcp配置。
  6. 先使用最小化session配置，仅保留proxy、timeout和必要header，等代理CONNECT成功后再恢复缓存、复用和其他配置。
