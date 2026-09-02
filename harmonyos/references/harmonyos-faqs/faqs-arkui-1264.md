---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1264
title: List组件中加载多个Web组件只显示最后一个页面怎么解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > List组件中加载多个Web组件只显示最后一个页面怎么解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c6f08847b622070d4ef185207e962922b78457a8a67a647915cc3ef134a72ffa
---

## 问题现象

在一个List组件中，循环加载Web组件来显示富文本数据。在富文本数据数量未知的情况下，直接使用单个WebviewController只显示最后一个item的页面数据，需要解决办法。

## 背景知识

* 富文本在如今的互联网应用软件或者页面中十分常见，它能够为文字添加图片、链接、字体样式等，使得文字的阅读更加生动有趣。在常见的博客、社交媒体平台软件上都多有使用：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/gVeOtO40RhCNQSAqdLkjaA/zh-cn_image_0000002628596110.png "点击放大")
* 由于富文本内容通常需要跨平台去显示，所以大多数情况下开发者都会选择HTML来作为存储的格式，来减少重复开发的工作，所以HarmonyOS我们可以选择能够加载HTML文档的组件来展示富文本文档内容。在HarmonyOS目前能够解析HTML富文本显示的组件有[RichEditor](../harmonyos-guides/arkts-common-components-richeditor.md)、[RichText](../harmonyos-references/ts-basic-components-richtext.md)和[Web](../harmonyos-guides/web-component-overview.md)，这里主要聚焦纯显示的场景，一般就是从[RichText](../harmonyos-references/ts-basic-components-richtext.md)和[Web](../harmonyos-guides/web-component-overview.md)两个组件中选择，而由于[RichText](../harmonyos-references/ts-basic-components-richtext.md)可自定义程度较低、功能不够丰富而且比较消耗内存资源，在List这种重复使用RichText组件的场景下，会出现卡顿、滑动响应慢等现象。所以在List中循环展示富文本内容时，会选择[Web](../harmonyos-guides/web-component-overview.md)来进行展示。
* 除了HarmonyOS组件外，还可以自行开发组件通过直接解析HTML文档再调用Text等基础文本组件组装进行展示，可以高度自定义功能，但是需要投入大量开发资源，在此不展开说明。

## 解决方案

* **方案一**：由于每个Web组件需要对应一个WebviewController，可以考虑把List中每条item抽出来作为子组件，把Web组件放到这个子组件中，这样就能做到每个Web组件对应一个WebviewController了，然后就可以通过WebviewController单独加载每条富文本数据。

  ```screen
  import web_webview from '@ohos.web.webview';

  // 子组件
  @Component
  export struct RichTextItem {
    private src: string = '';
    controller: web_webview.WebviewController = new web_webview.WebviewController();

    build() {
      Column() {
        Web({ src: '', controller: this.controller })
          .width('100%')
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .geolocationAccess(false)
          .mixedMode(MixedMode.None)
          .fileAccess(true)
          .imageAccess(true)
          .cacheMode(CacheMode.None)
          .onlineImageAccess(true)
          .layoutMode(WebLayoutMode.FIT_CONTENT) // 使得web高度自适应
          .onControllerAttached(() => {
            this.controller.loadData(this.src, 'text/html', 'utf-8', ' ', ' ');
          })
          .onSslErrorEvent(event => {
            event.handler.handleConfirm();
          })
      }
    }
  }

  @Entry
  @Component
  struct ListWebViewSolutionOne {
    @State richTextList: Array<string> = [
      `
        <span style="font-size:12.5px;"><span style="color:#666666;line-height:1.5;"><span style="font-size:12.5px;"><span style="color:#666666;"></span></span></span><span style="color:#666666;line-height:1.5;">【超级0卡糖*·低负担·0咖啡】</span><br />
        <br />
        <span style="color:#0A59F7;line-height:1.5;">不含咖啡的友好小铁</span><br />
        <span style="color:#0A59F7;line-height:1.5;">陪伴午后的闲暇时光</span><br />
        <br />
        <span style="color:#999;line-height:1.5;">「超级0卡糖*」原创定制</span><br />
        <span style="color:#666666;line-height:1.5;">果味清爽沁甜</span><br />
        <br />
        <span style="color:#444;line-height:1.5;">感受青提风味在奶香和椰香中游走</span><br />
        <span style="color:#555;line-height:1.5;">轻盈地，过夏天</span><br />
        <br />
        <span style="color:#777;line-height:1.5;">*本品使用0卡青提风味饮料浓浆（含赤藓糖醇）</span><br />
        </span>
      `,
      `
      <div>
        <p>我是 P1</p>
        <span><font color="#0A59F7">我是span1</font></span>
        <span>我是span2</span>
        <p>我是 P2</p>
        <span><font color="#0A59F7">我是span3</font></span>
        <span>我是span4</span>
      </div>
      `,
      `
      <div><font color="gray">兑换说明</font><br>赠送15.0%；<br></div>
      <div><font color="#0A59F7">兑换说明</font><br><font color="blue">赠送30.0%；</font><br></div>
      <font color="gray">兑换说明</font><br><font color="blue">赠送60.0%；</font><br>
      <font color="#0A59F7">兑换说明</font><font color="blue">赠送125.0%；</font><br>
      `,
      `
      <span style=\"color:#999999;\">手机的实名人需与我的信息为</span> <span style=\"color:#0A59F7;\">同一人</span> <span style=\"color:#999999;\">，否则请更换账户或手机号码</span>
      `,
      `
      <span style='text-align:center;'>您好, 现在会员促销期间<font color='#0A59F7'>全场商品打6折</font>哟~错过时间会<font color='#0A59F7'>恢复原价</font>哈!</span>
      `,
      `<font color='#0A59F7'>宝宝</font><font color='#0A59F7'>不爱吃饭</font>别怕！有它轻松拿捏挑食<font color='#0A59F7'>宝宝</font>！我家<font color='#0A59F7'>宝宝</font>不知是随...#<font color='#0A59F7'>宝宝</font>营养补充#`,
      `
      <span style='text-align:center;'>您好, 现在会员促销期间<font color='#0A59F7'>打6折</font>哟~错过时间<font color='#0A59F7'>恢复原价</font>哈!</span>
      `,
      '<p>欢迎来到松山湖华为溪流背坡村</p><table><tbody><tr class="firstRow"><td width="204" valign="top"><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2019/xcun-0404.jpg?w=500" style="width:100%;"/></td><td width="204" ' +
        'valign="top"><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2019/xcun-0406.jpg?w=500" style="width:100%;"/></td></tr><tr><td width="204" valign="top"><br/></td><td width="204" valign="top"><br/></td></tr></tbody></table><p><br/></p>',
      '<p><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2017/headquarter-dr-center.jpg?w=1000"/></p>',
    ];
    controller: web_webview.WebviewController = new web_webview.WebviewController();

    build() {
      Column() {
        List({ space: 8 }) {
          ForEach(this.richTextList, (item: string) => {
            ListItem() {
              RichTextItem({ src: this.getHtmlText(item) })
            }
            .borderRadius(8)
            .backgroundColor(Color.White)
            .padding({
              top: 8,
              right: 12,
              bottom: 8,
              left: 12
            })
          }, (item: string) => item)
        }
        .scrollBar(BarState.Off)
      }
      .backgroundColor(Color.Gray)
      .padding(8)
    }

    // 使用完整的html片段加载
    getHtmlText(src: string) {
      let msg = `
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no"/>
        </head>
        <body>
        ${src}
        </body>
        </html>`;
      return msg;
    }
  }
  ```
* **方案二**：除了单独创建一个子组件实现外，还可以通过在合适的时机加载富文本进行展示，可以做到用一个WebviewController控制多个Web组件展示富文本。
  + 在Web的[onControllerAttached](../harmonyos-references/arkts-basic-components-web-events.md#oncontrollerattached10)事件中去进行WebviewController.loadData(...)加载动作，也可以展示富文本数据，单个controller会依次绑定到每个Web组件上然后加载富文本数据。
  + 但这种方式和官方建议的“同一页面的多个Web组件，必须绑定不同的WebviewController”相悖，可能会导致其他功能有异常，建议仅在纯显示不涉及编辑的场景中使用。

    ```screen
    import web_webview from '@ohos.web.webview';

    @Entry
    @Component
    struct ListWebViewSolutionTwo {
      @State richTextList: Array<string> = [
        `
          <span style="font-size:12.5px;"><span style="color:#666666;line-height:1.5;"><span style="font-size:12.5px;"><span style="color:#666666;"></span></span></span><span style="color:#666666;line-height:1.5;">【超级0卡糖*·低负担·0咖啡】</span><br />
          <br />
          <span style="color:#0A59F7;line-height:1.5;">不含咖啡的友好小铁</span><br />
          <span style="color:#0A59F7;line-height:1.5;">陪伴午后的闲暇时光</span><br />
          <br />
          <span style="color:#999;line-height:1.5;">「超级0卡糖*」原创定制</span><br />
          <span style="color:#666666;line-height:1.5;">果味清爽沁甜</span><br />
          <br />
          <span style="color:#444;line-height:1.5;">感受青提风味在奶香和椰香中游走</span><br />
          <span style="color:#555;line-height:1.5;">轻盈地，过夏天</span><br />
          <br />
          <span style="color:#777;line-height:1.5;">*本品使用0卡青提风味饮料浓浆（含赤藓糖醇）</span><br />
          </span>
        `,
        `
        <div>
          <p>我是 P1</p>
          <span><font color="#0A59F7">我是span1</font></span>
          <span>我是span2</span>
          <p>我是 P2</p>
          <span><font color="#0A59F7">我是span3</font></span>
          <span>我是span4</span>
        </div>
        `,
        `
        <div><font color="gray">兑换说明</font><br>赠送15.0%；<br></div>
        <div><font color="#0A59F7">兑换说明</font><br><font color="blue">赠送30.0%；</font><br></div>
        <font color="gray">兑换说明</font><br><font color="blue">赠送60.0%；</font><br>
        <font color="#0A59F7">兑换说明</font><font color="blue">赠送125.0%；</font><br>
        `,
        `
        <span style=\"color:#999999;\">手机的实名人需与我的信息为</span> <span style=\"color:#0A59F7;\">同一人</span> <span style=\"color:#999999;\">，否则请更换账户或手机号码</span>
        `,
        `
        <span style='text-align:center;'>您好, 现在会员促销期间<font color='#0A59F7'>全场商品打6折</font>哟~错过时间会<font color='#0A59F7'>恢复原价</font>哈!</span>
        `,
        `<font color='#0A59F7'>宝宝</font><font color='#0A59F7'>不爱吃饭</font>别怕！有它轻松拿捏挑食<font color='#0A59F7'>宝宝</font>！我家<font color='#0A59F7'>宝宝</font>不知是随...#<font color='#0A59F7'>宝宝</font>营养补充#`,
        `
        <span style='text-align:center;'>您好, 现在会员促销期间<font color='#0A59F7'>打6折</font>哟~错过时间<font color='#0A59F7'>恢复原价</font>哈!</span>
        `,
        '<p>欢迎来到松山湖华为溪流背坡村</p><table><tbody><tr class="firstRow"><td width="204" valign="top"><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2019/xcun-0404.jpg?w=500" style="width:100%;"/></td><td width="204" ' +
          'valign="top"><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2019/xcun-0406.jpg?w=500" style="width:100%;"/></td></tr><tr><td width="204" valign="top"><br/></td><td width="204" valign="top"><br/></td></tr></tbody></table><p><br/></p>',
        '<p><img src="https://www-file.huawei.com/-/media/corporate/images/press%20center/facilities%20around%20the%20world/2017/headquarter-dr-center.jpg?w=1000"/></p>',
      ];
      controller: web_webview.WebviewController = new web_webview.WebviewController();

      build() {
        Column() {
          List({ space: 8 }) {
            ForEach(this.richTextList, (item: string) => {
              ListItem() {
                Web({ src: '', controller: this.controller })
                  .width('100%')
                  .javaScriptAccess(true)
                  .domStorageAccess(true)
                  .mixedMode(MixedMode.None)
                  .geolocationAccess(false)
                  .fileAccess(true)
                  .imageAccess(true)
                  .cacheMode(CacheMode.None)
                  .onlineImageAccess(true)
                  .layoutMode(WebLayoutMode.FIT_CONTENT) // 使得web高度自适应
                  .onControllerAttached(() => {
                    this.controller.loadData(this.getHtmlText(item), 'text/html', 'utf-8', ' ', ' ');
                  })
                  .onSslErrorEvent(event => {
                    event.handler.handleConfirm();
                  })
              }
              .borderRadius(8)
              .backgroundColor(Color.White)
              .padding({
                top: 8,
                right: 12,
                bottom: 8,
                left: 12
              })
            }, (item: string) => item)
          }
          .scrollBar(BarState.Off)
        }
        .backgroundColor(Color.Gray)
        .padding(8)
      }

      // 使用完整的html片段加载
      getHtmlText(src: string) {
        let msg = `
          <!DOCTYPE html>
          <html>
          <head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0,minimum-scale=1.0,user-scalable=no"/>
          </head>
          <body>
          ${src}
          </body>
          </html>`;
        return msg;
      }
    }
    ```

    执行以上代码需要获取使用Internet网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)。

## 总结

当需要在长列表中用Web组件显示富文本内容时，可以通过两种方法来实现：

* 将长列表中的每个项作为一个子组件开发，在子组件中放置Web组件并绑定唯一的WebviewController，然后通过WebviewController去加载即可。优点是每个Web对应一个WebviewController，符合官方开发建议，可以通过controller控制单个Web的功能；缺点是当只需要显示富文本的场景时，多个WebviewController会占用内存。
* 不开发子组件，在列表项Web组件的onControllerAttached事件去加载富文本内容。优点是单个WebviewController即可完成多个Web组件的富文本显示；缺点是单个WebviewController去绑定多个Web组件不符合官方开发建议，不能再利用WebviewController去控制Web的功能。
