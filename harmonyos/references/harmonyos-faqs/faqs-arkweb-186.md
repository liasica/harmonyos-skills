---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-186
title: H5网页中Cookie跨域场景及解决方案
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > H5网页中Cookie跨域场景及解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3a473a652ad73afae315c2c48f019d74adec0982e4828344d10aa327a63d3fc5
---

## 问题现象

H5网页中有哪些Cookie跨域场景？针对这些场景，又如何解决？

## 背景知识

* 什么是跨域：

  浏览器从一个域名的网页去请求另一个域名的资源时，域名、端口、协议任一不同即为跨域。

  以https://www.test.com/index.html网址为参考，跨域示例：

  | URL | 是否跨域 | 原因 |
  | --- | --- | --- |
  | https://www.test.com/index1.html | 否 | 协议、域名、端口号相同 |
  | http://www.test.com/index.html | 是 | http协议不同 |
  | https://www.test.com:8080/index.html | 是 | 端口号不同 |
  | https://api.test.com/index.html | 是 | 子域名不同 |
  | https://www.test001.com/index.html | 是 | 主域名不同 |
* 为什么Cookie默认不跨域共享：

  出于对安全及隐私保护，默认禁止跨域共享Cookie，防止CSRF（跨站请求伪造）攻击和用户被追踪。
* Cookie的定义属性：

  Cookie是存储在客户端（通常是浏览器）中的小型文本数据，用于在客户端和服务器之间传递信息。Cookie可以具有各种属性，这些属性控制着Cookie的行为和使用。以下是常见的Cookie属性及含义：

  | 属性 | 含义 |
  | --- | --- |
  | Name | Cookie的名称，是一个唯一的标识符，用于在服务器和客户端之间识别Cookie。 |
  | Value | Cookie的值，包含了实际的数据。这是Cookie存储的主要信息。 |
  | Domain | Cookie绑定的域名，属性值是服务器端的域名，指定了可以访问该Cookie的域名。  如：设置Domain=.example.com，那么这个Cookie将在example.com域名及所有子域名（如www.example.com、api.example.com等）中可见和访问。  需要注意的是Domain属性值不应该包含协议和端口号。 |
  | Path | 指定了可以访问Cookie的路径，属性默认值是'/'。  如：将Path设置为Path=/example，那么只有在路径以 "/example" 开头的请求中才会发送Cookie。 |
  | Expires | 指定Cookie的过期日期和时间。一旦过期，Cookie将被删除。 |
  | Max-Age | 指定了Cookie的最大存活时间，以秒为单位，Max-Age表示Cookie在指定的时间段内有效，如果设置为0，会话结束后会删除Cookie。 |
  | Secure | 设置为true，请求只会在通过https安全连接发送时才会携带Cookie。 |
  | SameSite | 控制Cookie是否会在跨站点请求中发送。可以设置为Strict、Lax或None。  Strict：表示只在同一站点请求中发送；  Lax：表示在部分跨站点请求中发送；  None：表示在所有请求中发送，需配合Secure=true一起使用。 |
  | HttpOnly | 如果设置为true，JavaScript将无法访问Cookie。这有助于防止跨站点脚本攻击（XSS）窃取Cookie数据。 |

## 解决方案

Web组件加载网页时，主要存在子域名跨域、第三方Cookie跨域2种场景。

* **场景一：**

  **子域名跨域**：从子域名a的网页请求子域名b的资源，即为子域名跨域。

  举例：主域名：.test.com，子域名a：a.test.com，子域名b：b.test.com。此场景子域名a网页设置Cookie，没有设置Domain属性或Domain属性值不为主域名时，请求子域名b的资源时不会携带子域名a的Cookie值。

  解决方案为：设置Cookie时，设置Domain=主域名。Cookie值与属性在ArkTS、H5网页、服务端任意一侧设置均可。

  ArkTS侧示例代码：

  ```screen
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct Page1 {
    private controller: WebviewController = new webview.WebviewController();
    // url使用时请替换为真实地址，此示例***.test.com为子域名，test.com为主域名
    url: string = 'https://***.test.com';

    build() {
      Column() {
        Web({ src: this.url, controller: this.controller })
          .fileAccess(false)
          .geolocationAccess(false)
          .onControllerAttached(() => {
            try {
              // 为了子域名跨域时可以正常访问Cookie，需要将Domain属性值设置为主域名
              webview.WebCookieManager.configCookieSync(this.url, 'cookie_key=cookie_value;Domain=.test.com');
            } catch (error) {
              console.error(`excute configCookieSync failed. error is ${error}`);
            }
          });
      };
    }
  }
  ```

  H5侧示例代码：

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
      <title>Hello World</title>
      <script type="text/javascript">
          window.onload = function() {
              // 使用时，Domain的值请替换为真实主域名
              document.cookie = "cookie_key=cookie_value; Domain=.test.com";
          };
      </script>
  </head>
  <body>
  <h1>Hello World!</h1>
  </body>
  </html>
  ```
* **场景二：**

  **第三方Cookie跨域**：从域名a的网页请求域名b的资源，并且使用域名b的Cookie，即为第三方Cookie跨域。

  举例：上述场景一、场景二均是访问域名a的网页，并在域名a下设置Cookie，然后调用子域名或其他主域名请求。对于将H5网页预置在应用本地resfile目录时，访问网页时，url为file://\*\*\*，服务端请求为http|https请求，并且需要将Cookie设置在服务端请求域名下，此时就涉及第三方域名Cookie管控。

  解决方案为：Web组件设置[putAcceptThirdPartyCookieEnabled](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#putacceptthirdpartycookieenabled)为true，设置WebCookieManager实例允许发送和接收第三方Cookie。

  示例代码：

  ```ts
  import { webview } from '@kit.ArkWeb';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct Page2 {
    controller: webview.WebviewController = new webview.WebviewController();
    uiContext: UIContext = this.getUIContext();

    aboutToAppear(): void {
      // 设置WebCookieManager实例拥有发送和接收第三方cookie的权限
      webview.WebCookieManager.putAcceptThirdPartyCookieEnabled(true);
    }

    build() {
      Stack() {
        Column() {
          Web({ src: '', controller: this.controller })
            .fileAccess(false)
            .geolocationAccess(false)
            .onControllerAttached(() => {
              try {
                // 设置允许可以跨域访问的路径列表
                this.controller.setPathAllowingUniversalAccess([
                  this.uiContext.getHostContext()!.resourceDir
                ]);
                // 访问本地资源页面
                this.controller.loadUrl('file://' + this.uiContext.getHostContext()!.resourceDir + '/index.html');
              } catch (error) {
                console.error(
                  `loadUrl errorCode: ${(error as BusinessError).code},  message: ${(error as BusinessError).message}`);
              }

              try {
                // 为服务端请求设置Cookie，使用时请替换为真实地址
                webview.WebCookieManager.configCookieSync('www.example.com',
                  'cookie_key=cookie_value;Domain=.example.com;SameSite=None;Secure=true;HttpOnly');
              } catch (error) {
                console.error(`excute configCookieSync failed. error is ${error}`);
              }
            });
        };
      };
    }
  }
  ```

  index.html示例代码：

  ```html
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  </head>
  <body>

  <button onclick="sendRequest()">发送请求</button>

  <script>
      function sendRequest() {
        // 使用时请替换成真实网址
        fetch('https://www.example.com', {
          method: 'GET',
          credentials: 'include' // 设置无论是否跨域，始终在请求中携带凭据
        })
        .then(res => res.json())
        .then(data => console.info('成功:', data))
        .catch(err => console.error('失败:', err));
      }
  </script>

  </body>
  </html>
  ```

## 常见FAQ

Q：Cookie设置Secure属性时，通过官网指导[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)时，Application-Cookie内无法显示Cookie？

A：设置Secure属性时，若是http协议DevTools不会显示Cookie，改成https协议访问即可。

Q：WebCookieManager的putAcceptThirdPartyCookieEnabled和putAcceptCookieEnabled有什么区别？

A：[putAcceptThirdPartyCookieEnabled](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#putacceptthirdpartycookieenabled)控制是否发送与接收第三方Cookie，而[putAcceptCookieEnabled](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#putacceptcookieenabled)控制是否发送与接收同域Cookie，浏览器通常会默认禁止第三方Cookie，而允许同域Cookie。

因此，需要使用三方Cookie则将putAcceptThirdPartyCookieEnabled设置为true，需要使用同域Cookie则将putAcceptCookieEnabled设置为true。

Q：WebCookieManager的putAcceptThirdPartyCookieEnabled和putAcceptCookieEnabled都设置为true，有什么安全风险？

A：如果设置两者为true，意味着浏览器或应用将接受第三方Cookie和所有Cookie。这种设置可能会增加以下安全风险：

* 隐私泄露：第三方Cookie可以用于跨站点跟踪，如果接受第三方Cookie，那么用户的浏览行为和数据可能被第三方网站追踪和收集。
* Cookie滥用：如果接受所有Cookie，包括那些来自不可信的源，可能会导致Cookie被用于恶意目的，如进行针对性的广告投放或甚至身份盗窃。
* 安全漏洞：Cookie可以携带会话信息或其他敏感数据，如果这些数据落入错误之手，可能会导致严重的安全问题。因此，从安全角度考虑，建议谨慎使用这些设置，根据使用范围设置对应的API为true，并确保有适当的安全措施，如：最小权限，数据加密传输等来保护用户的数据和隐私。

Q：跨域报错The value of the "Access Control-Allow-Origin" header in the response must not be the wildcard '\*' when the request's credentials mode is "include"是什么原因？

A：Access-Control-Allow-Origin不能为通配符“\*”，必须指定具体的前端源，确保权限可控。

Q：[configCookieSync](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync11)设置token=123; Domain=www.example.com后，[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)时，查看设置的token Cookie，Domain显示为.www.example.com？

A：设置Domain时会在域名前加上(.)是chromium默认行为，是符合预期的。
