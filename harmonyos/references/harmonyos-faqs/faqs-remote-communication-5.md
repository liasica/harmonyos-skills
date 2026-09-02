---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-5
title: 如何解决创建rcp请求基类对象失败的问题
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > 如何解决创建rcp请求基类对象失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:447ee823612bb7dd7f2b190e70ba2d0c87a65195552de83860b440d1d58cafac
---

## 问题现象

创建rcp请求对象时失败，导致所有网络请求失败。错误码：1007900994，报错信息：Sessions number reached limit。相关代码如下：

```ts
class RcpClass {
  cache:ResponseCache = new ResponseCache();
  session = rcp.createSession({
    interceptors: [new ResponseCachingInterceptor(this.cache)]
  });
  url?: string;
  content?: rcp.RequestContent;
  constructor(url:string,content: rcp.RequestContent) {
    this.url = url;
    this.content = content;
  }
  async post(){
    return await this.session.post(this.url,this.content);
  }
  // 继续封装其他方法get、fetch、put等
}
```

## 背景知识

* 使用[rcp.createSession()](../harmonyos-references/remote-communication-rcp.md#createsession)方法创建session会话，该方法自API18版本开始单个子线程最多可以同时创建1024个session实例。
* 使用[session.close()](../harmonyos-references/remote-communication-rcp.md#close)方法可以关闭会话，释放与此会话关联的资源。
* [ArkTS API错误码](../harmonyos-references/errorcode-remote-communication.md)：可通过错误码自查表查找错误原因。

## 问题定位

* 检查session使用后是否及时关闭会话，释放资源。
* 根据错误码[1007900994](../harmonyos-references/errorcode-remote-communication.md#section1007900994-会话数达到限制)，查看对应的报错原因：session创建数量过多导致，自5.1.0(18)版本开始单个子线程最多可创建1024个session实例。

## 分析结论

根据报错信息分析得出：同时创建多个session对象，未及时关闭不用的session对象，导致session资源超限。因此在再次创建新的session对象时，抛出session数量超过限制的错误。

## 修改建议

应用在通过创建的session实例访问完网络请求后，应及时关闭session，保证资源合理利用。

方案一：使用全局session对象，实现同一session实例的复用性。

参考代码如下：

```ts
import { rcp } from "@kit.RemoteCommunicationKit";

// 单例模式实现全局session
export class SessionManager {
  static session: rcp.Session;

  static creatSession(): rcp.Session {
    if (!SessionManager.session) {
      SessionManager.session = rcp.createSession();
    }
    return SessionManager.session;
  }
}

async function testInterceptor(url: string) {
  const session = SessionManager.creatSession();
  console.error(`Response url is: ${url}, Session id: ${session.id}.`);
  session.get(url).then((response) => {
    console.error(`Response is: ${response}`);
  });
}
// 单例模式实现全局session

@Entry
@Component
struct Index {
  private message: string = 'Hello World';
  private url: string[] = ['url1.xxx', 'url2.xxx'];  // 请根据实际业务情况传url。
  private urlIndex = 0;

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('Test Session')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          testInterceptor(this.url[this.urlIndex]);
          this.urlIndex = 1 - this.urlIndex;
        });
    }
    .height('100%')
    .width('100%');
  }
}
```

方案二：使用session.close()方法及时关闭使用完的session。

参考示例可见[Session.close()](../harmonyos-references/remote-communication-rcp.md#close)小节示例。

## 常见FAQ

Q：不想使用全局session是否有其他方法？

A：rcp.createSession()自5.1.0(18)版本开始变更为单个子线程最多可创建1024个session实例，或者开发者从业务上优化下并发数。

Q：rcp.createSession创建实例个数的限制是针对模块的限制，还是一个APP的限制？

A：rcp会话的限制是针对一个APP的限制，同一APP自API18版本开始，单个子线程最多可以同时创建1024个session实例。

Q：在使用rcp进行网络请求时，什么时候是与后台服务建立起的连接，是创建session的时候吗？还是其他调用方法的时候？

A：创建session不会直接与后台服务建立网络连接，实际建立网络连接发生在发起具体HTTP请求时（如调用get、post等方法）。

Q：在创建session时使用了单例，整个应用可以使用同一个session吗？

A：session具有复用性，可以使用全局创建的session单例，一个session可以发起多个请求，若session不再使用，调用close方法关闭session，以释放资源。自5.1.0(18)版本开始变更为单个子线程最多可创建1024个session实例。

Q：taskpool的子线程释放掉后session对象会被释放并且次数对应会减少吗？如果session创建用全局变量存着，在同一个子线程中运行完成一个任务后，在运行其它任务的时候全局变量的session可以被再次使用吗？

A：使用taskpool任务，如果task任务中不关闭session，即使task任务执行完成也不会session标记数量也不会减少，建议使用worker方式管理。session具有复用性，因此可以在完成一个任务后再次使用。

## 总结

* 优先使用全局session，增加资源复用。
* session使用完成后，及时调用session.close()关闭session，避免资源超限。
