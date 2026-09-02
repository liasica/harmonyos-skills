---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-415
title: Navigation通过pushPathByName跳转页面为什么显示空白
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation通过pushPathByName跳转页面为什么显示空白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a5f11136a003a5d1dab2ad935a28bcca42a94ea7615dd2647db188575e4c57f8
---

**常见原因及解决措施**

**原因一：路由未正确配置**

未配置系统路由表，或未为Navigation组件设置navDestination属性；目标页面未在路由表中注册，或未在navDestination的builder方法中定义。

**解决措施**

检查并配置路由表，确保所有目标页面在路由表（如router配置）中正确定义。

在Navigation组件中显式设置navDestination属性，并在其builder方法中包含目标页面。

**原因二：模块类型错误**

在module.json5文件中，type类型设置为"feature"（应为"har"或"shared"），导致跳转失败。

**解决措施**

修改module.json5文件，将type改为"har"或"shared"，例如：

```ts
"module": {
  // "name": "your_module",
  // "type": "har", // or shared, avoid using feature,
  // ...
},
```

**原因三：****NavBar隐藏导致页面栈异常**

hideNavBar属性设置为true时，NavBar被隐藏，若页面栈为空，会显示白屏。

**解决措施**

确认Navigation组件的hideNavBar属性未设置为true，将其改为false以确保NavBar可见：

```ts
Navigation() {
  // page content
  // ...
}
.hideNavBar(false) // Ensure not hidden
```

**原因四：****跳转名称（Name）无效或为空**

pushPathByName传入的name参数为空、拼写错误或不存在于路由表中，跳转无效。

**解决措施**

检查跳转代码中的name值是否与路由表注册的名称完全一致。

使用有效名称，例如：

```ts
// Correct example: The name must match the routing table
this.pageStack.pushPathByName('PageDetail', 'param');
```

**原因五：调试环境不兼容**

使用Previewer调试时，不支持系统路由表跳转，可能导致白屏。

**解决措施**

改用模拟器或真机调试复杂页面跳转。

**原因六：子页面错误创建导航栈**

子页面自行创建NavPathStack实例（如new NavPathStack()），导致与父级Navigation路由栈冲突，页面无法渲染。

**解决措施**

子页面应直接使用父级传递的NavPathStack实例，避免重新创建。例如：

```ts
// Subpage code, avoid creating it yourself
@Component
struct ChildPage {
  // Error: Should not use new NavPathStack()
  // pageStack: NavPathStack = new NavPathStack();
  // Correct: Inject the parent stack through @Consume or parameters
  @Consume('pageStack') pageStack: NavPathStack;
  build() {
    // ...
  }
}
```

**pushPathByName方法的局限性及替代方案**

**局限性**

pushPathByName是同步方法，跳转至不存在的页面时不会抛出异常，直接显示空白页面。

**推荐替代方案**

改用pushDestinationByName（异步方法），可捕捉错误并重定向：

```ts
// Asynchronous jump using pushDestructionByName
this.pageStack.pushDestinationByName('TargetPage', 'param')
  .then(() => {
    hilog.info(0x000, 'testTag', 'pushDestinationByName success');
  })
  .catch((error: BusinessError) => {
    // Jump failed, redirected to custom page (such as Stay tuned page)
    this.pageStack.pushPathByName('ErrorPage', 'param');
    hilog.error(0x000, 'testTag', `pushDestinationByName failed, code=${error.code}, message=${error.message}`);
  })
```

优势：通过回调处理错误，避免白屏。
