---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-116
title: H5页面点击邮件链接后跳转空白页面
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > H5页面点击邮件链接后跳转空白页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb8f8ebb959ea1e2a597c0960a07dfd18faad2cbaae249232ebce60c15a4f7e4
---

## 问题现象

用户在查看隐私协议时，点击最下面的邮箱地址，跳转到空白页面。

## 背景知识

* mailto协议：一种用于在网页或应用中触发邮件客户端发送邮件的URI协议。通过它，用户可以直接点击链接或按钮，自动打开默认邮件客户端，并预填充收件人、主题、正文等信息，简化邮件发送流程。
* [onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)：当Web组件加载URL之前触发该回调，用于判断是否阻止此次访问。

## 问题定位

一般应用隐私协议都是通过H5页面加载的，跳转空白页面时，首先查看链接是否有效。搜索该应用的隐私协议发现，邮箱地址是一个a标签，且采用了mailto协议。

```ts
<!DOCTYPE html>
<html>
<body>
<div>
    <a href="mailto:xx.xx.xx" style="font-size: 40px;">xx.xx.xx</a>
</div>
</body>
</html>
```

而Web组件是不支持通过mailto协议拉起邮箱应用的，因此把该链接识别为了无效链接，所以跳转到空白页面。

## 分析结论

Web组件不支持通过mailto协议直接拉起邮箱应用，识别到无效链接，因此跳转空白页面。

## 修改建议

应用需要自己通过[onLoadIntercept](../harmonyos-references/arkts-basic-components-web-events.md#onloadintercept10)回调拦截“mailto”协议链接跳转，调用API拉起对应服务，相关介绍详见[跨应用跳转](../harmonyos-guides/web-redirection-and-browsing-history-mgmt.md#跨应用跳转)。

```ts
import { webview } from '@kit.ArkWeb';
import { common, Want } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private webviewController: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({
        src: $rawfile('testMail.html'),
        controller: this.webviewController
      })
        .geolocationAccess(false)
        .fileAccess(false)
        .size({
          width: '100%'
        })
        .onLoadIntercept((event) => {
          if (event) {
            let url: string = event.data.getRequestUrl();
            // 判断链接是否mailto
            if (url.indexOf('mailto:') === 0) {
              // 拉起邮件应用
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let want: Want = {
                // 以系统自带邮件为例，实际请自行替换
                bundleName: 'com.huawei.hmos.email',
                abilityName: 'EntryAbility',
                // uri里面通过mailto来配置收件人邮箱等参数。数据仅做示例，实际请替换为需要内容
                uri: 'mailto:123@***.com,456@***.com?subject=我是邮件标题&body=我是正文内容&&cc=cc@***.com&&bcc=bcc@***.com&&sceneType=2',
              };
              context.startAbility(want).then((data) => {
                console.info(`Success, ${data}`);
              }).catch(() => {
                console.error('error');
              });
              return true;
            }
          }
          return false;
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

详细方案介绍可参考：[拉起邮件类应用（mailto方式）](../harmonyos-guides/start-email-apps-by-mailto.md)。
